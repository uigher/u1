import pandas as pd
 
# 文件名
filename = "test.xlsx"
# 表格数量
T_sheets = 5
 
df = []
for i in range(1, T_sheets+1):
    sheet_data = pd.read_excel(filename, sheet_name=i, header=None)
    df.append(sheet_data)
 
# 合并表格
output = "merged.xlsx"
df = pd.concat(df)
df.to_excel(output)