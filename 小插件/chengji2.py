import pandas as pd

# 定义要读取的文件路径列表
file_paths = [
    r'E:\0Code\Algorithm\xjtu\S3265.xlsx',
    r'E:\0Code\Algorithm\xjtu\S3266.xlsx'
    # r'E:\0Code\Algorithm\xjtu\S3261.xlsx',
    # r'E:\0Code\Algorithm\xjtu\S3262.xlsx'
]


all_data = pd.DataFrame()


for file_path in file_paths:
    excel_data = pd.ExcelFile(file_path)
    df = excel_data.parse('Sheet1')  # 假设所有文件的数据在'Sheet1'中
    all_data = pd.concat([all_data, df], ignore_index=True)

# 计算加权平均分（与之前相同的处理逻辑）
filtered_df = all_data[all_data['课程类别'] != '选修课']
weighted_avg_df = filtered_df.groupby(['学号', '姓名']).apply(
    lambda x: (x['成绩'] * x['课程学分']).sum() / x['课程学分'].sum()
).reset_index(name='加权平均分')

# 保留四位小数
weighted_avg_df['加权平均分'] = weighted_avg_df['加权平均分'].round(4)
print(weighted_avg_df[['学号', '姓名', '加权平均分']])

# 保存结果到一个新的Excel文件
output_file_path = r'E:\0Code\Algorithm\xjtu\combined_results4.xlsx'
weighted_avg_df.to_excel(output_file_path, index=False)

print(f"Weighted average results have been saved to {output_file_path}")
