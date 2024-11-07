import pandas as pd

file_path = r'E:\0Code\Algorithm\小插件\S3264.xlsx'
excel_data = pd.ExcelFile(file_path)


df = excel_data.parse('Sheet1')


filtered_df = df[df['课程类别'] != '选修课']


weighted_avg_df = filtered_df.groupby(['学号', '姓名']).apply(
    lambda x: (x['成绩'] * x['课程学分']).sum() / x['课程学分'].sum()
).reset_index(name='加权平均分')


weighted_avg_df['加权平均分'] = weighted_avg_df['加权平均分'].round(4)


print(weighted_avg_df[['学号', '姓名', '加权平均分']])
output_file_path = r'E:\0Code\Algorithm\小插件\S3264_chengji.xlsx'
weighted_avg_df.to_excel(output_file_path, index=False)

print(f"Weighted average results have been saved to {output_file_path}")
