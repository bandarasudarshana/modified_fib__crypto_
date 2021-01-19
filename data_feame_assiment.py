
import gspread
from oauth2client.service_account import ServiceAccountCredentials


import pandas as pd
import openpyxl

#read the data sets
xls_1 = pd.ExcelFile(r'C:\Users\Sudarshana Bandara\Downloads\Assignment.xlsx', engine='openpyxl')
df_Orders = pd.read_excel(xls_1, 'Orders')

xls_2 = pd.ExcelFile(r'C:\Users\Sudarshana Bandara\Downloads\Assignment.xlsx', engine='openpyxl')
df_Sales = pd.read_excel(xls_2, 'Sales')
df_Sales=df_Sales.head(34)
#cominne both data sets
frames_1 = [df_Sales, df_Orders]
data_set = pd.concat(frames_1,axis=1, join="inner")
df=data_set

# remove un named colunms
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df.loc[:,~df.columns.duplicated()]

#create new colunm
df['products'] = df[['Items','Quantity', 'Cost','Price']].apply(lambda x : '{}-{}-{}-{}'.format(x[0],x[1],x[2],x[3]), axis=1)

# #add nessary dat colunms to new data frame
data_set_final=pd.DataFrame()

data_set_final['Invoice No']= df['Invoice No']
data_set_final['Status']=df['Status']
data_set_final['Customer']=df['Customer']
data_set_final['Date']=df['Date']
data_set_final['products']=df['products']

# fill the missing values
data_set_final['Invoice No'] = data_set_final['Invoice No'].interpolate(method='slinear').interpolate(method='linear')
data_set_final['Customer'] = data_set_final['Customer'].interpolate(method='slinear').interpolate(method='linear')
data_set_final['Date'] = data_set_final['Date'].interpolate(method='slinear').interpolate(method='linear')



data_set_final













