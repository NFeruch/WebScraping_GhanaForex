# coding: utf-8

from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import datetime as dt
import os
import time
import http.client
http.client._MAXHEADERS = 1000

session = HTMLSession()

currencies = {
    'USD': 'US Dollar',
    'GBP': 'British Pound Sterling',
    'EUR': 'Euro',
    'CAD': 'Canadian Dollar',
    'YEN': 'Japanese Yen',
    'ZAR': 'South African Rand',
    'XOF': 'West African COF franc',
    'CNY': 'Chinese Yuan',
    'CHF': 'Swiss Franc',
    'CNH': 'Chinese Yuan Renminbi',
    'JPY': 'Japanese Yen',
    'AUD': 'Australian Dollar',
    'BWP': 'Botswanan Pula',
    'DKK': 'Danish Krone',
    'HKD': 'Hong Kong Dollar',
    'INR': 'Indian Rupee',
    'KES': 'Kenyan Shilling',
    'LSL': 'Lesotho Loti',
    'MUR': 'Mauritian Rupee',
    'MWK': 'Malawian Kwacha',
    'NAD': 'Namibian Dollar',
    'NGN': 'Nigerian Naira',
    'NOK': 'Norwegian Krone',
    'NZD': 'New Zealand Dollar',
    'SEK': 'Swedish Krona',
    'SGD': 'Singapore Dollar',
    'SZL': 'Swazi Lilangeni',
    'UGX': 'Ugandan Shilling',
    'ZMW': 'Zambian Kwacha',
    'CFA': 'West African CFA franc'
}

# # 17) Fidelity Bank Ghana
print('Fidelity Bank Ghana')
DRIVER_PATH = r'C:\Users\user\Desktop\chromedriver.exe'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.fidelitybank.com.gh")
response = driver.page_source
driver.quit()

soup = BeautifulSoup(response, 'lxml')
# print(soup.prettify())

tbl = soup.find('table', {'class': 'table forex-rates'})
df = pd.read_html(str(tbl))[0]
df = df.rename(columns={
    'buying': 'Exchange Rate Cash Buy',
    'selling': 'Exchange Rate Cash Sell',
    'currency': 'Currency Code'
})
df['Date'] = pd.to_datetime('today').normalize()
df['Currency'] = df['Currency Code'].apply(lambda x: currencies[x])
df['Exchange Rate Transfer_Buy'] = np.nan
df['Exchange Rate Transfer_Sell'] = np.nan
df['DateTime for Pull'] = dt.datetime.now()
df['Bank Name Link'] = 'https://www.fidelitybank.com.gh'
df['Bank Name'] = 'Fidelity Bank Ghana'
df = df[['Date', 'Currency', 'Currency Code', 'Exchange Rate Transfer_Buy', 'Exchange Rate Transfer_Sell', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell', 'DateTime for Pull', 'Bank Name Link', 'Bank Name']]

df.to_csv('ghana_forex.csv', mode='a', header=not os.path.exists('ghana_forex.csv'), index=False)



# # 21) Prudential Bank Limited
print('Prudential Bank Limited')
URL = 'https://www.prudentialbank.com.gh/pbl-rates.html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response =  session.get(URL, headers=headers)
response.html.render(wait=2, timeout=100)
soup = BeautifulSoup(response.html.html, 'lxml')
# print(soup.prettify())

tbl = soup.find('table', {'class': 'table'})
df = pd.read_html(str(tbl))[0].replace('-', np.nan)

df = df.rename(columns={
    'Bank Buy (GH¢)': 'Exchange Rate Cash Buy',
    'Bank Sell (GH¢)': 'Exchange Rate Cash Sell',
    'Currency': 'Currency Code'
})
df['Date'] = pd.to_datetime('today').normalize()
df['Currency Code'] = df['Currency Code'].str[:3]
df['Currency'] = df['Currency Code'].apply(lambda x: currencies[x])
df['Exchange Rate Transfer_Buy'] = np.nan
df['Exchange Rate Transfer_Sell'] = np.nan
df['DateTime for Pull'] = dt.datetime.now()
df['Bank Name Link'] = 'https://www.prudentialbank.com.gh/pbl-rates.html'
df['Bank Name'] = 'Prudential Bank Limited'
df = df[['Date', 'Currency', 'Currency Code', 'Exchange Rate Transfer_Buy', 'Exchange Rate Transfer_Sell', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell', 'DateTime for Pull', 'Bank Name Link', 'Bank Name']]

df.to_csv('ghana_forex.csv', mode='a', header=not os.path.exists('ghana_forex.csv'), index=False)



# # 22) Republic Bank Ghana Limited
print('Republic Bank Ghana Limited')
URL = 'https://republicghana.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = session.get(URL, headers=headers)
response.html.render(wait=2, timeout=100)
soup = BeautifulSoup(response.html.html, 'lxml')
# print(soup.prettify())

tbl = soup.find('table', {'class': 'tablepress tablepress-id-2 dataTable no-footer'})
df = pd.read_html(str(tbl))[0].replace('-', np.nan)

df = df.rename(columns={
    'Buy': 'Exchange Rate Cash Buy',
    'Sell': 'Exchange Rate Cash Sell',
    'Exchange Rates': 'Currency Code'
})
df['Date'] = pd.to_datetime('today').normalize()
df['Currency Code'] = df['Currency Code'].str.replace(')', '').str[-3:]
df['Currency'] = df['Currency Code'].apply(lambda x: currencies[x])
df['Exchange Rate Transfer_Buy'] = np.nan
df['Exchange Rate Transfer_Sell'] = np.nan
df['DateTime for Pull'] = dt.datetime.now()
df['Bank Name Link'] = 'https://republicghana.com/'
df['Bank Name'] = 'Republic Bank Ghana Limited'
df = df[['Date', 'Currency', 'Currency Code', 'Exchange Rate Transfer_Buy', 'Exchange Rate Transfer_Sell', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell', 'DateTime for Pull', 'Bank Name Link', 'Bank Name']]

df.to_csv('ghana_forex.csv', mode='a', header=not os.path.exists('ghana_forex.csv'), index=False)



# # 24) Stanbic Bank Ghana Limited
# print('Stanbic Bank Ghana Limited')
# ## Moved to PDF
# URL = 'https://www.stanbicbank.com.gh/gh/personal/about-us/news/daily-market-update'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# response = await asession.get(URL, headers=headers)
# await response.html.arender(wait=2, timeout=100)
# soup = BeautifulSoup(response.html.html, 'lxml')
# print(soup.prettify())

# tbl = soup.find('table', {'border': '1'})
# df = pd.read_html(str(tbl))[0]
# df.columns = df.iloc[0, :]
# df = df.iloc[1:, :]

# df = df.rename(columns={
#     'Buying': 'Exchange Rate Cash Buy', 
#     'Selling': 'Exchange Rate Cash Sell',
#     'Currency Pair': 'Currency Code'
# })
# df['Date'] = pd.to_datetime('today').normalize()
# df['Currency Code'] = df['Currency Code'].str[:3]
# df['Currency'] = df['Currency Code'].apply(lambda x: currencies[x])
# df['DateTime for Pull'] = dt.datetime.now()
# df['Bank Name Link'] = 'https://www.stanbicbank.com.gh/gh/personal/about-us/news/daily-market-update'
# df['Bank Name'] = 'Stanbic Bank Ghana Limited'
# df = df[['Date', 'Currency', 'Currency Code', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell', 'DateTime for Pull', 'Bank Name Link', 'Bank Name']]

# df.to_csv('ghana_forex.csv', mode='a', header=not os.path.exists('ghana_forex.csv'), index=False)



# # 23) Société Générale Ghana Limited
print('Société Générale Ghana Limited')
URL = 'https://societegenerale.com.gh/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = session.get(URL, headers=headers)
response.html.render(wait=2, timeout=100)
soup = BeautifulSoup(response.html.html, 'lxml')
# print(soup.prettify())

df = []
for l, p, s in zip(
    soup.find_all('div', {'class': 'label_col'}),
    soup.find_all('input', {'class': 'purchase_rate_input gcw_input3632784697'}),
    soup.find_all('input', {'class': 'sale_rate_input gcw_input3632784697'})
):
    df.append([l.text[:3], float(p['value']), float(s['value'])])
df = pd.DataFrame(df, columns=['Currency Code', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell'])

df['Date'] = pd.to_datetime('today').normalize()
df['Currency Code'] = df['Currency Code'].str[:3]
df['Currency'] = df['Currency Code'].apply(lambda x: currencies[x])
df['Exchange Rate Transfer_Buy'] = np.nan
df['Exchange Rate Transfer_Sell'] = np.nan
df['DateTime for Pull'] = dt.datetime.now()
df['Bank Name Link'] = 'https://societegenerale.com.gh'
df['Bank Name'] = 'Société Générale Ghana Limited'
df = df[['Date', 'Currency', 'Currency Code', 'Exchange Rate Transfer_Buy', 'Exchange Rate Transfer_Sell', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell', 'DateTime for Pull', 'Bank Name Link', 'Bank Name']]

df.to_csv('ghana_forex.csv', mode='a', header=not os.path.exists('ghana_forex.csv'), index=False)



# # 18) First National Bank Ghana
print('First National Bank Ghana')
DRIVER_PATH = r'C:\Users\user\Desktop\chromedriver.exe'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://www.firstnationalbank.com.gh/rates-pricing/foreignExchangeRates.html')
response = driver.page_source
driver.quit()

soup = BeautifulSoup(response, 'lxml')
# print(soup.prettify())

tbl = soup.find('div', {'id': 'forexRatesTable'}).findChildren(recursive=False)[4]
df = pd.read_html(str(tbl))[0]

df = df.rename(columns={
    'Bank Buying Notes': 'Exchange Rate Cash Buy',
    'Bank Selling Rate': 'Exchange Rate Cash Sell',
    'Code': 'Currency Code',
    'Bank Buying TT': 'Exchange Rate Transfer_Buy'
}).drop(columns=['Description'])
df['Date'] = pd.to_datetime('today').normalize()
df['Currency Code'] = df['Currency Code'].str[:3]
df['Currency'] = df['Currency Code'].apply(lambda x: currencies[x])
df['Exchange Rate Transfer_Sell'] = np.nan
df['DateTime for Pull'] = dt.datetime.now()
df['Bank Name Link'] = 'https://www.firstnationalbank.com.gh/rates-pricing/foreignExchangeRates.html'
df['Bank Name'] = 'First National Bank Ghana'
df = df[['Date', 'Currency', 'Currency Code', 'Exchange Rate Transfer_Buy', 'Exchange Rate Transfer_Sell', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell', 'DateTime for Pull', 'Bank Name Link', 'Bank Name']]

df.to_csv('ghana_forex.csv', mode='a', header=not os.path.exists('ghana_forex.csv'), index=False)

tbl = soup.find('div', {'id': 'forexRatesTable'}).findChildren(recursive=False)[6]
df_1 = pd.read_html(str(tbl))[0]

df_1 = df_1.rename(columns={
    'Bank Buying Notes': 'Exchange Rate Cash Buy',
    'Bank Selling Rate': 'Exchange Rate Cash Sell',
    'Code': 'Currency Code',
    'Bank Buying TT': 'Exchange Rate Transfer_Buy'
}).drop(columns=['Description'])
df_1['Date'] = pd.to_datetime('today').normalize()
df_1['Currency Code'] = df_1['Currency Code'].str[:3]
df_1['Currency'] = df_1['Currency Code'].apply(lambda x: currencies[x])
df['Exchange Rate Transfer_Sell'] = np.nan
df_1['DateTime for Pull'] = dt.datetime.now()
df_1['Bank Name Link'] = 'https://www.firstnationalbank.com.gh/rates-pricing/foreignExchangeRates.html'
df_1['Bank Name'] = 'First National Bank Ghana'
df = df[['Date', 'Currency', 'Currency Code', 'Exchange Rate Transfer_Buy', 'Exchange Rate Transfer_Sell', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell', 'DateTime for Pull', 'Bank Name Link', 'Bank Name']]

df = pd.concat([df, df_1]).reset_index(drop=True)
df.to_csv('ghana_forex.csv', mode='a', header=not os.path.exists('ghana_forex.csv'), index=False)



# # 16) Consolidated Bank Ghana
print('Consolidated Bank Ghana')
DRIVER_PATH = r'C:\Users\user\Desktop\chromedriver.exe'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://cbg.com.gh/rates.html")
time.sleep(5)
response = driver.page_source
driver.quit()

soup = BeautifulSoup(response, 'lxml')
# print(soup.prettify())

tbl = soup.find('div', {'id': 'response'}).find('table')
df = pd.read_html(str(tbl))[0].replace('-', np.nan)

df = df.rename(columns={
    'Cash': 'Exchange Rate Cash Buy',
    'Unnamed: 2': 'Exchange Rate Cash Sell',
    'Daily Exchange rate': 'Currency Code',
    'Cross Rates': 'Currency Code',
    'Transfer': 'Exchange Rate Transfer_Buy',
    'Unnamed: 4': 'Exchange Rate Transfer_Sell'
})
df = df.iloc[1:, :]
df['Date'] = pd.to_datetime('today').normalize()
df['Currency Code'] = df['Currency Code'].str[:3]
df['Currency'] = df['Currency Code'].apply(lambda x: currencies[x])
df['DateTime for Pull'] = dt.datetime.now()
df['Bank Name Link'] = 'https://cbg.com.gh/rates.html'
df['Bank Name'] = 'Consolidated Bank Ghana'
df = df[['Date', 'Currency', 'Currency Code', 'Exchange Rate Transfer_Buy', 'Exchange Rate Transfer_Sell', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell', 'DateTime for Pull', 'Bank Name Link', 'Bank Name']]

df.to_csv('ghana_forex.csv', mode='a', header=not os.path.exists('ghana_forex.csv'), index=False)



# # 15) CalBank Limited
print('CalBank Limited')
URL = 'https://calbank.net/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = session.get(URL, headers=headers)
response.html.render(wait=2, timeout=100)
soup = BeautifulSoup(response.html.html, 'lxml')
# print(soup.prettify())

try:
    df = []
    for i in soup.find('div', {'class': 'dce-acf-repeater'}).find_all('div', {'class': 'elementor-row'}):
        df.append(i.text.strip().replace('           ', ',').replace('\n', '').split(','))
    df = pd.DataFrame(df, columns=['Currency Code', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell'])
except:
    df = []
    for i in soup.find('div', {'class': 'dce-acf-repeater'}).find_all('div', {'class': 'elementor-row'}):
        df.append(i.text.strip().replace('           ', ',').replace('\n', '').split(' '))
    df = pd.DataFrame(df, columns=['Currency Code', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell'])

df['Date'] = pd.to_datetime('today').normalize()
df['Currency Code'] = df['Currency Code'].str[:3]
df['Currency'] = df['Currency Code'].apply(lambda x: currencies[x])
df['Exchange Rate Transfer_Buy'] = np.nan
df['Exchange Rate Transfer_Sell'] = np.nan
df['DateTime for Pull'] = dt.datetime.now()
df['Bank Name Link'] = 'https://calbank.net/'
df['Bank Name'] = 'CalBank Limited'
df = df[['Date', 'Currency', 'Currency Code', 'Exchange Rate Transfer_Buy', 'Exchange Rate Transfer_Sell', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell', 'DateTime for Pull', 'Bank Name Link', 'Bank Name']]

df.to_csv('ghana_forex.csv', mode='a', header=not os.path.exists('ghana_forex.csv'), index=False)



# # 26) Bank of Ghana
# ## Unscrapable
# print('Bank of Ghana')
# URL = 'https://www.bog.gov.gh/treasury-and-the-markets/historical-interbank-fx-rates/'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# response = await asession.get(URL, headers=headers, verify=False)
# await response.html.arender(wait=2, timeout=100)
# soup = BeautifulSoup(response.html.html, 'lxml')
# print(soup.prettify())

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# DRIVER_PATH = r'C:\Users\user\Desktop\chromedriver.exe'
# options = Options()
# # options.headless = True
# # options.add_argument("--window-size=1920,1200")

# driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
# driver.get("https://www.bog.gov.gh/treasury-and-the-markets/historical-interbank-fx-rates/")
# WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "responsiveExpander")))
# response = driver.page_source
# driver.quit()

# soup = BeautifulSoup(response, 'lxml')
# print(soup.prettify())



# # 14) Agricultural Development Bank
print('Agricultural Development Bank')
URL = 'https://www.agricbank.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = session.get(URL, headers=headers)
response.html.render(wait=2, timeout=100)
soup = BeautifulSoup(response.html.html, 'lxml')
# print(soup.prettify())

tbl = soup.find('table', {'class': 'full'})
df = pd.read_html(str(tbl))[0]
df.columns = df.columns.droplevel(0)
df = df.drop('Currency', axis=1)
df.columns = ['Currency Code', 'Exchange Rate Transfer_Buy', 'Exchange Rate Transfer_Sell', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell']

df['Date'] = pd.to_datetime('today').normalize()
df['Currency Code'] = df['Currency Code'].str[:3]
df['Currency'] = df['Currency Code'].apply(lambda x: currencies[x])
df['DateTime for Pull'] = dt.datetime.now()
df['Bank Name Link'] = 'https://www.agricbank.com/'
df['Bank Name'] = 'Agricultural Development Bank'
df = df[['Date', 'Currency', 'Currency Code', 'Exchange Rate Transfer_Buy', 'Exchange Rate Transfer_Sell', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell', 'DateTime for Pull', 'Bank Name Link', 'Bank Name']]

df.to_csv('ghana_forex.csv', mode='a', header=not os.path.exists('ghana_forex.csv'), index=False)



# # 19) Ghana Commercial Bank
print('Ghana Commercial Bank')
time.sleep(10)
for _ in range(2):
    URL = 'https://www.gcbbank.com.gh/87-exchange/447-foreign-exchange'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = session.get(URL, headers=headers)
    response.html.render(wait=2, timeout=100)
    soup = BeautifulSoup(response.html.html, 'lxml')
    # print(soup.prettify())

tbl = soup.find('table', {'class': 'table__subRows'})
df = pd.read_html(str(tbl))[0]
df.columns = df.iloc[0, :]
df = df.iloc[1:, :]

df = df.rename(columns={
    'Buying': 'Exchange Rate Cash Buy',
    'Selling': 'Exchange Rate Cash Sell',
    'Currency': 'Currency Code'
})
df['Date'] = pd.to_datetime('today').normalize()
df['Currency'] = df['Currency Code'].apply(lambda x: currencies[x])
df['Exchange Rate Transfer_Buy'] = np.nan
df['Exchange Rate Transfer_Sell'] = np.nan
df['DateTime for Pull'] = dt.datetime.now()
df['Bank Name Link'] = 'https://www.gcbbank.com.gh/87-exchange/447-foreign-exchange'
df['Bank Name'] = 'Ghana Commercial Bank'
df = df[['Date', 'Currency', 'Currency Code', 'Exchange Rate Transfer_Buy', 'Exchange Rate Transfer_Sell', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell', 'DateTime for Pull', 'Bank Name Link', 'Bank Name']]

df.to_csv('ghana_forex.csv', mode='a', header=not os.path.exists('ghana_forex.csv'), index=False)



# # 20) National Investment Bank Limited
time.sleep(10)
print('National Investment Bank Limited')
DRIVER_PATH = r'C:\Users\user\Desktop\chromedriver.exe'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get('https://www.nib-ghana.com/foreign-exchange/')
time.sleep(5)
response = driver.page_source
driver.quit()

soup = BeautifulSoup(response, 'lxml')
# print(soup.prettify())

tbl = soup.find('table', {'data-ninja_table_instance': 'ninja_table_instance_0'})
df = pd.read_html(str(tbl))[0].iloc[:-1, :]
df.columns = df.columns.droplevel(0)
df_t = df[df['CASH'] == 'NO'].rename(columns={
    'BUYING': 'Exchange Rate Transfer_Buy',
    'SELLING': 'Exchange Rate Transfer_Sell'
}).drop(columns=['CASH', 'TRANSFER/REMITTANCES'])

df_c = df[df['CASH'] == 'YES'].rename(columns={
    'BUYING': 'Exchange Rate Cash Buy',
    'SELLING': 'Exchange Rate Cash Sell'
}).drop(columns=['CASH', 'TRANSFER/REMITTANCES'])
df = df_t.merge(df_c, on='CURRENCY TO CEDI', how='outer').drop(columns=['Date_x', 'Date_y']).rename({'Date_y': 'Date'}).replace({'EURO': 'Euro', 'USD': 'US Dollar', 'GBP': 'British Pound Sterling'})
df['CURRENCY TO CEDI'] = df['CURRENCY TO CEDI'].apply(lambda x: {v: k for k, v in currencies.items()}[x])
df = df.rename(columns={'CURRENCY TO CEDI': 'Currency Code'})

df['Date'] = pd.to_datetime('today').normalize()
df['Currency'] = df['Currency Code'].apply(lambda x: currencies[x])
df['DateTime for Pull'] = dt.datetime.now()
df['Bank Name Link'] = 'https://www.nib-ghana.com/foreign-exchange/'
df['Bank Name'] = 'National Investment Bank Limited'
df = df[['Date', 'Currency', 'Currency Code', 'Exchange Rate Transfer_Buy', 'Exchange Rate Transfer_Sell', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell', 'DateTime for Pull', 'Bank Name Link', 'Bank Name']]

df.to_csv('ghana_forex.csv', mode='a', header=not os.path.exists('ghana_forex.csv'), index=False)



# # 25 Standard Chartered Bank Ghana Limited
print('Standard Chartered Bank Ghana Limited')
URL = 'https://www.african-markets.com/en/stock-markets/gse/listed-companies/company?code=SCB'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = session.get(URL, headers=headers)
response.html.render(wait=2, timeout=100)
soup = BeautifulSoup(response.html.html, 'lxml')
# print(soup.prettify())

tbl = soup.find('table', {'class': 'tabtable-rs_7f98zx7q'})
df = pd.read_html(str(tbl))[0]
df = df.drop([0, 2, 4], axis=1)
df = df.rename(columns={
    1: 'Currency Code',
    3: 'Exchange Rate Cash Buy'
})
df['Date'] = pd.to_datetime('today').normalize()
df['Exchange Rate Cash Buy'] = (df['Exchange Rate Cash Buy'].str[:4]).astype(float)
df['Currency Code'] = df['Currency Code'].str[2:]
df['Currency'] = df['Currency Code'].apply(lambda x: currencies[x])
df['Exchange Rate Cash Sell'] = np.nan
df['Exchange Rate Transfer_Buy'] = np.nan
df['Exchange Rate Transfer_Sell'] = np.nan
df['DateTime for Pull'] = dt.datetime.now()
df['Bank Name Link'] = 'https://www.african-markets.com/en/stock-markets/gse/listed-companies/company?code=SCB'
df['Bank Name'] = 'Standard Chartered Bank Ghana Limited'
df = df[['Date', 'Currency', 'Currency Code', 'Exchange Rate Transfer_Buy', 'Exchange Rate Transfer_Sell', 'Exchange Rate Cash Buy', 'Exchange Rate Cash Sell', 'DateTime for Pull', 'Bank Name Link', 'Bank Name']]

df.to_csv('ghana_forex.csv', mode='a', header=not os.path.exists('ghana_forex.csv'), index=False)
