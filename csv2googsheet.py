#!/usr/bin/env python
# coding: utf-8


"""
Title: Upload CSV data to a Google Spreadsheet
Author: raglew

"""

from __future__ import print_function
import httplib2
import os, sys, time

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-csv2googsheet.json

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'CSV 2 Google Spreadsheet'


def get_csv_data(csvfilename):
        """
        Open csv file
        Return CSV data
        Note: this code assumes that the CSV separator is a comma
        """
        try:
            csv_file = open(csvfilename, encoding='ISO-8859-1')
        except:
            print('%s not found. Try again!' % csvfilename)
            sys.exit()

        rows = []

        for line in csv_file:
            row = line.strip().split(',')             # CSV separator assumed to be a comma
            rows.append(row)
            data = {'values': rows}

        csv_file.close()
        return data

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-csv2googsheet.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():

    """
    Upload CSV data to Google Spreadsheet
    """

    # Get CSV data
    csv_filename = input('Please enter your CSV filename: ')
    csv_data = get_csv_data(csv_filename)

    # Google authorization
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())

    # Create service object
    service = discovery.build('sheets', 'v4', http=http)

    # Spreadsheet title
    spreadsheet_title = input('Please enter your spreadsheet title: ')
    spreadsheet_title_data = {'properties': {'title': '%s [%s]' % (spreadsheet_title, time.ctime())}}

    # Create google spreadsheet using spreadsheet title
    result = service.spreadsheets().create(body=spreadsheet_title_data).execute()

    # Get google spreadsheet id and indicate that spreadsheet has been created
    SHEET_ID = result['spreadsheetId']
    print('Created "%s"' % result['properties']['title'])

    # Update google spreadsheet with CSV data
    service.spreadsheets().values().update(spreadsheetId=SHEET_ID,
    range='A1', body=csv_data, valueInputOption='RAW').execute()

    # Indicate that spreadsheet has been updated
    print('Wrote data to Sheet:')
    rows = service.spreadsheets().values().get(spreadsheetId=SHEET_ID, range='Sheet1').execute().get('values', [])
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
