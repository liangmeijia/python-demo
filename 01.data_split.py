from distutils.log import fatal

import pandas as pd
from openpyxl import load_workbook

# 读取文件的路径
file_path1 = 'D:/lmj/data/cloud-data/b5dc39c7-5ffb-4e1b-842e-33b909b6b7bb-1.xlsx'
file_path2 = 'D:/lmj/data/cloud-data/b5dc39c7-5ffb-4e1b-842e-33b909b6b7bb-2.csv'
csv_path = 'D:/lmj/data/cloud-data/b5dc39c7-5ffb-4e1b-842e-33b909b6b7bb-1-3.csv'
df = pd.read_excel(file_path1,sheet_name='Sheet3')
df.to_csv(csv_path,index=False)