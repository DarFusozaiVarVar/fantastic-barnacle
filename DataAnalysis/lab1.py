import pandas as pd 
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 10000)
pd.set_option('display.width', 1000)

sheets = pd.ExcelFile(f'DataAnalysis/data.xlsx').sheet_names
print(sheets)

t1 = pd.read_excel('DataAnalysis/data.xlsx', sheet_name=sheets[0], skiprows=[0])
print(t1)
#t2 = pd.read_excel('PQM - podatki za pilotni projekt (OCR12VM) - ENG.xlsx', 1, skiprows=lambda x: x in [2, 10])


#print(t2)

#tc = pd.merge(t1, t2, on='HeatNo', how='outer')

