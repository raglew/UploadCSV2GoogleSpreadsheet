<H1> Upload CSV 2 Google Spreadsheet </H1>
Python 3 code designed to upload data from a CSV file to a Google Spreadsheet

<H3> Step 1: Prepare your CSV data </H3>

Use a text editor to make sure that all your CSV separators are commas.

<H3> Step 2: Turn on the Drive API </H3>

Use wizard at https://console.developers.google.com/start/api?id=drive to create or select a project in the Google Developers Console and automatically turn on the API. Click Continue, then Go to credentials.
At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button.
Select the Credentials tab, click the Create credentials button and select OAuth client ID.
Select the application type Other, enter the name "Drive API Quickstart", and click the Create button.
Click OK to dismiss the resulting dialog.
Click the file_download (Download JSON) button to the right of the client ID.
Move this file to your working directory and rename it client_secret.json.

<H3> Step 3: Install the Google Client Library </H3>

pip install --upgrade google-api-python-client

<H3> Step 4: Run python application </H3>

python3 csv2googsheet.py

You will be asked to enter the name of your CSV file. Make sure the file can be located in your working directory. You can use example.csv for testing purposes.

You will then need access to a browser and the internet to permit access to your Google Drive. Click Allow and return to your command line interface.

(If your browser is on a different machine then run the python application with the command line parameter below:

python3 csv2googsheet.py --noauth_local_webserver

You will be asked for a verification code. Use the provided link and to get the code.)

You will then be asked to enter a name for your Google Spreadsheet. If you use the example.csv file, you can enter Population as your title.

Good luck!
