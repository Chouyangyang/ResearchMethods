import pandas as pd

# 读取两个CSV文件
#Read two csv files
df1 = pd.read_csv('../Data/Training set values.csv')
df2 = pd.read_csv('../Data/Training set labels.csv')

# 使用merge函数将两个DataFrame按照'id'列进行合并
#Use the merge function to merge two DataFrames based on the 'id' column
merged_df = pd.merge(df1, df2, on='id')

# 将合并后的DataFrame保存为CSV文件
#Save the merged DataFrame as a CSV file
merged_df.to_csv('../Data/TrainingSet.csv', index=False)