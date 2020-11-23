# -*- coding: utf-8 -*-
from __future__ import print_function
import httplib2
import os


# from apiclient import discovery       #[CLS]: 假如有問題,執行: pip install --upgrade google-api-python-client
from googleapiclient import discovery   #[CLS]: 再不行用這一行(所以變位置了?)

from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = ur"C:\\APN\\USERS\\clouds\\Google 雲端硬碟\\MyPrivy\\憑證\\Google-API\\hello-world-google-api\\client_id(hello-world-google-api-client).json"
# CLIENT_SECRET_FILE = ur"C:\\APN\\USERS\\clouds\\Google 雲端硬碟\\MyPrivy\\憑證\\Google-API\\invest-sim-google-api\\client_secret_invest-sim.json"
APPLICATION_NAME = 'Google Sheets API Python Quickstart' 



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
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)    #[CLS]: 認證快取存在這裏 C:\Users\cloud\.credentials\sheets.googleapis.com-python-quickstart.json
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)   #[CLS]: 使用認證資料，想要建立SCOPS描述的要求
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)                #[CLS]: 實際跑起browser做認證動作
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()                     #[CLS]: 打開網頁取得googles授權
    http = credentials.authorize(httplib2.Http())       #[CLS]: 利用認證資訊的http,接下來都用這個http動作
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,            #[CLS]: 得到sheets api service物件，對這個可以做sheets api
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'  #[CLS]: spreadsheets 檔案 id
    rangeName = 'Class Data!A2:E'                                   #[CLS]: worksheet name (& range)
    result = service.spreadsheets().values().get(                   #[CLS]: 一次抓完全部資料，results是dictionary
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))


if __name__ == '__main__':
    main()