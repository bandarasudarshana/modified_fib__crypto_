# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 23:51:55 2021

@author: Sudarshana Bandara
"""
import pandas as pd
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

json_key = json.load(open(r'C:\Users\Sudarshana Bandara\Downloads\test04-5ec8f896239f.json'))
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


credentials = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\Sudarshana Bandara\Downloads\test04-5ec8f896239f.json', scope)
gc = gspread.authorize(credentials)


wks = gc.open("Assignment")

ws_1 = wks.get_worksheet(1)
ws_1
ws_2 = wks.get_worksheet(0)
ws_2
dataframe_1 = pd.DataFrame(ws_1.get_all_records())
dataframe_2 = pd.DataFrame(ws_2.get_all_records())
