import pandas as pd
import os

# 指定CSV文件所在的目录
directory = 'D:/资料/四川电信/项目/云业务数据分析'
csv_path = 'D:/资料/四川电信/项目/云业务数据分析/result.csv'
# 获取该目录中的所有文件名
csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
# 初始化一个空的列表来存储所有的DataFrame
dataframes = []
# 循环读取每个CSV文件
for file in csv_files:
    file_path = os.path.join(directory, file)
    df = pd.read_csv(file_path, dtype={'客户电话': str,'合同ID': str,'合同编号': str,'合同名称': str,'合同起始时间': str,'合同终止时间': str})
    dataframes.append(df)
# 使用pd.concat()函数将所有DataFrame合并成一个
combined_df = pd.concat(dataframes, ignore_index=True)
# print(combined_df.head())
# print(combined_df.info()) # [294942 * 165]
# 检查是否有缺失值
# print(combined_df.isnull().sum())
#数据筛选
result_df = combined_df.loc[((combined_df['来源渠道'] == '省公司')|(combined_df['来源渠道'] == '云公司')|(combined_df['来源渠道'] == '云省份'))
                            &(combined_df['资源状态'] == '正常')
                            &(combined_df['公网ip'].notna())
                            &(combined_df['公网ip'].str.strip() != '')
                            &(combined_df['公网ip'] !='无')
                            &(combined_df['市场部一级产品名称'] != '云安全')]
print(result_df.head())
print(result_df.info())
result_df.to_csv(csv_path,index=False)