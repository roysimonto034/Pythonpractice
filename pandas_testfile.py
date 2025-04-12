''' This file is demonstrate pandas dataframework'''
import pandas as pd
fp=pd.read_csv(r'E:\Python_project\annual-enterprise-survey-2021-financial-year-provisional-csv.csv')
print(fp.columns)
i=1
for ip,row in fp.iterrows():
    while i<10:
        print(row)
        i+=1
    break
 
