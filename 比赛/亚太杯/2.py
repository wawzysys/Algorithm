import matplotlib.pyplot as plt
from matplotlib import rcParams
import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
# 设置字体为 SimHei（黑体）以支持中文
plt.rcParams['font.sans-serif'] = ['Times New Roman']
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False    # 解决负号
from translate import Translator

translation_map = {
    "美国": "United States",
    "中国": "China",
    "英国": "United Kingdom",
    "巴西": "Brazil",
    "德国": "Germany",
    "法国": "France",
    "日本": "Japan",
    "土耳其": "Turkey",
    "意大利": "Italy",
    "加拿大": "Canada",
    "澳大利亚": "Australia",
    "墨西哥": "Mexico",
    "西班牙": "Spain",
    "俄罗斯": "Russia",
    "印度": "India"
}
data = pd.read_excel('2023年世界各国宠物食品市场收入.xlsx')

# 数据
countries = data['国家'].values
revenues = data['收入 (百万美元)'].values

# 将数据保存为DataFrame
data = pd.DataFrame({"国家": countries, "收入 (百万美元)": revenues})

# 绘制图表
plt.figure(figsize=(12, 8))

# 添加翻译列
data["Country"] = data["国家"].map(translation_map)
print(data['国家'])
print(data['Country'])


plt.barh(data["Country"], data["收入 (百万美元)"], color="blue", alpha=0.7)
# 添加标题和标签
plt.title("Pet Food Market Revenue by World in 2023 (USD Million)", fontsize=14)
plt.xlabel("Revenue (US$ million)", fontsize=20)
plt.ylabel("country", fontsize=20)
plt.gca().invert_yaxis()  # 翻转y轴以符合图表顺序
plt.tick_params(labelsize=13)

# 显示图表
plt.tight_layout()
#plt.savefig('2023年世界各国宠物食品市场收入 (单位：百万美元).png',dpi=500)

plt.show()

import pandas as pd
import plotly.express as px
import pycountry

# 读取数据
data = pd.read_excel('2023年世界各国宠物食品市场收入.xlsx')

# 打印原始列名
print("Original Columns:", data.columns.tolist())

# 添加翻译列（假设已有 translation_map 字典）
translation_map = {
    '中国': 'China',
    '美国': 'United States',
    '德国': 'Germany',
    '土耳其': 'Turkey',
    '俄罗斯': 'Russia',
    '英国': 'United Kingdom',
    '巴西': 'Brazil',
    '法国': 'France',
    '日本': 'Japan',
    '意大利': 'Italy',
    '加拿大': 'Canada',
    '澳大利亚': 'Australia',
    '墨西哥': 'Mexico',
    '西班牙': 'Spain',
    '印度': 'India'
    # 其他国家的映射...
}

# 映射中文国家名称到英文
data["Country"] = data["国家"].map(translation_map)

# 重命名收入列为英文
data = data.rename(columns={'收入 (百万美元)': 'Revenue (Million USD)'})

# 打印重命名后的列名
print("Columns after renaming:", data.columns.tolist())

# 打印数据框架前几行以确认
print(data.head())

# 定义手动 ISO 代码映射
manual_iso_map = {
    'Turkey': 'TUR',
    'Russia': 'RUS',
    # 其他需要手动添加的国家...
}

# 获取 ISO Alpha-3 代码的函数
def get_iso3(country_name):
    try:
        return pycountry.countries.lookup(country_name).alpha_3
    except:
        # 如果 pycountry 找不到，尝试手动映射
        return manual_iso_map.get(country_name, None)

# 应用函数获取 ISO 代码
data['ISO_Code'] = data['Country'].apply(get_iso3)

# 检查是否有缺失的 ISO 代码
missing_iso = data[data['ISO_Code'].isnull()]['Country'].unique()
if len(missing_iso) > 0:
    print(f"Unable to find ISO codes for the following countries: {missing_iso}")
print(data.head())

# 创建 Choropleth Map
fig = px.choropleth(
    data_frame=data,
    locations="ISO_Code",
    color="Revenue (Million USD)",
    hover_name="Country",
    color_continuous_scale=px.colors.sequential.Plasma,
    title="<b>2023 Pet Food Market Revenue by Country (Million USD)</b>",
    labels={'Revenue (Million USD)': 'Revenue (Million USD)'}
)

# 更新布局以优化显示
fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=True,
        projection_type='equirectangular'
    ),
    coloraxis_colorbar=dict(
        title="Revenue (Million USD)"
    )
)

# 显示图表，指定渲染器为浏览器以避免 nbformat 问题
fig.show(renderer="browser")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 创建数据框
data = pd.DataFrame({
    '国家': ['美国', '中国', '英国', '巴西', '德国', '法国', '日本', '土耳其',
            '意大利', '加拿大', '澳大利亚', '墨西哥', '西班牙', '俄罗斯', '印度'],
    '收入 (百万美元)': [57384.64, 7419.96, 7224.56, 6287.95, 5724.1,
                      4998.58, 4619.43, 4176.62, 3833.27, 3735.68,
                      2952.06, 2506.59, 2022.42, 1940.34, 1847.64]
})

# 添加翻译列
translation_map = {
    '美国': 'United States',
    '中国': 'China',
    '英国': 'United Kingdom',
    '巴西': 'Brazil',
    '德国': 'Germany',
    '法国': 'France',
    '日本': 'Japan',
    '土耳其': 'Turkey',
    '意大利': 'Italy',
    '加拿大': 'Canada',
    '澳大利亚': 'Australia',
    '墨西哥': 'Mexico',
    '西班牙': 'Spain',
    '俄罗斯': 'Russia',
    '印度': 'India'
}

data["Country"] = data["国家"].map(translation_map)

# 重命名收入列为英文
data = data.rename(columns={'收入 (百万美元)': 'Revenue (Million USD)'})

# 计算总收入和收入份额
total_revenue = data['Revenue (Million USD)'].sum()
data['Revenue Share (%)'] = (data['Revenue (Million USD)'] / total_revenue) * 100

# 按收入排序
data_sorted = data.sort_values(by='Revenue (Million USD)', ascending=False)

# 定义自定义颜色列表
custom_colors = [
    '#FF9999',  # 美国 - 浅红色
    '#66B3FF',  # 中国 - 浅蓝色
    '#99FF99',  # 英国 - 浅绿色
    '#FFCC99',  # 巴西 - 浅橙色
    '#C2C2F0',  # 德国 - 浅紫色
    '#FFB3E6',  # 法国 - 浅粉色
    '#C4E17F',  # 日本 - 浅黄绿色
    '#F0E68C',  # 土耳其 - 卡其色
    '#ADD8E6',  # 意大利 - 浅蓝色
    '#FFD700',  # 加拿大 - 金色
    '#FFA07A',  # 澳大利亚 - 浅珊瑚色
    '#20B2AA',  # 墨西哥 - 浅海蓝色
    '#9370DB',  # 西班牙 - 紫罗兰色
    '#FF6347',  # 俄罗斯 - 番茄色
    '#40E0D0'   # 印度 - 绿宝石色
]
# 设置全局字体为 Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
# 创建图表
fig, axes = plt.subplots(1, 2, figsize=(20, 10))

# 饼状图: 收入份额
axes[0].pie(
    data['Revenue Share (%)'],
    labels=data['Country'],
    autopct='%1.1f%%',
    startangle=140,
    colors=custom_colors[:len(data)],  # 使用自定义颜色
    wedgeprops={'edgecolor': 'white'}
)
axes[0].set_title('Revenue Share by Country', fontweight='bold', fontsize=20)

# 柱状图: 各国收入
axes[1].bar(
    data_sorted['Country'],
    data_sorted['Revenue (Million USD)'],
    color='indianred'
)
axes[1].set_title('Revenue by Country (Million USD)', fontweight='bold', fontsize=20)
axes[1].set_xlabel('Country', fontsize=20)
axes[1].set_ylabel('Revenue (Million USD)', fontsize=20)
axes[1].tick_params(axis='x', rotation=45, labelsize=20)
axes[1].tick_params(axis='y', labelsize=15)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()
df = pd.read_excel('2017-2022 各国市场规模和食品规模.xlsx')
plt.figure(figsize=(10, 6))

plt.plot(df['年份'], df.美国食品, label='美国食品',marker="*", linestyle='-',markerfacecolor='r',alpha=0.8,linewidth=5,markersize=20)
plt.plot(df['年份'], df.西欧食品, label='西欧食品',marker="*", linestyle='-',markerfacecolor='r',alpha=0.8,linewidth=5,markersize=20)
plt.plot(df['年份'], df.日本食品, label='日本食品',marker="*", linestyle='-',markerfacecolor='r',alpha=0.8,linewidth=5,markersize=20)
plt.plot(df['年份'], df.中国食品, label='中国食品',marker="*", linestyle='-',markerfacecolor='r',alpha=0.8,linewidth=5,markersize=20)

plt.xticks(rotation=0)

plt.title("2017 - 2022年各地区宠物食品平均价格", fontsize=14)
plt.xlabel("年份", fontsize=20)
plt.ylabel("食品价格（十亿人民币）", fontsize=20)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.xticks(df['年份'])
plt.tick_params(labelsize=13)
plt.legend(fontsize=15)
#plt.savefig('问题2\\2017 - 2022年各地区宠物食品平均价格.png',dpi=500)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 数据准备
data = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022],
    'USA Food': [200.6, 209.2, 222.4, 231.4, 244.2, 287.0],
    'Western Europe Food': [136.4, 141.8, 144.0, 152.6, 155.7, 156.5],
    'Japan Food': [30.5, 30.9, 31.0, 31.3, 31.4, 31.7],
    'China Food': [41.3, 54.6, 68.4, 81.5, 92.1, 99.3],
}

df = pd.DataFrame(data)

# 分组柱状图
x = np.arange(len(df['Year']))  # 年份的位置
width = 0.2  # 每个柱子的宽度

plt.figure(figsize=(14, 8))
plt.bar(x - 1.5*width, df['USA Food'], width, label='USA Food', color='#FF5733')
plt.bar(x - 0.5*width, df['Western Europe Food'], width, label='Western Europe Food', color='#33FF57')
plt.bar(x + 0.5*width, df['Japan Food'], width, label='Japan Food', color='#3357FF')
plt.bar(x + 1.5*width, df['China Food'], width, label='China Food', color='#FFC300')

plt.xlabel('Year', fontsize=16, family='Times New Roman')
plt.ylabel('Food Prices (Billion CNY)', fontsize=16, family='Times New Roman')
plt.title('2017-2022 Average Pet Food Prices by Region', fontsize=18, fontweight='bold', family='Times New Roman')
plt.xticks(x, df['Year'], fontsize=12, family='Times New Roman')
plt.legend(fontsize=14, loc='upper left', frameon=True, prop={'family': 'Times New Roman'})
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


df = pd.read_excel('2017-2022 各国市场规模和食品规模.xlsx')
plt.figure(figsize=(10, 6))

plt.plot(df['年份'], df.美国市场, label='美国市场',marker="*", linestyle='-',markerfacecolor='r',alpha=0.8,linewidth=5,markersize=20)
plt.plot(df['年份'], df.西欧市场, label='西欧市场',marker="*", linestyle='-',markerfacecolor='r',alpha=0.8,linewidth=5,markersize=20)
plt.plot(df['年份'], df.日本市场, label='日本市场',marker="*", linestyle='-',markerfacecolor='r',alpha=0.8,linewidth=5,markersize=20)
plt.plot(df['年份'], df.中国市场, label='中国市场',marker="*", linestyle='-',markerfacecolor='r',alpha=0.8,linewidth=5,markersize=20)

plt.xticks(rotation=0)

plt.title("2017 - 2022年各地区宠物市场规模", fontsize=14)
plt.xlabel("年份", fontsize=20)
plt.ylabel("市场规模（十亿人民币）", fontsize=20)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.xticks(df['年份'])
plt.tick_params(labelsize=13)
plt.legend(fontsize=15)
#plt.savefig('问题2\\2017 - 2022年各地区宠物市场规模 (单位：美元).png',dpi=500)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 确保所有图表使用一致的风格
sns.set(style="whitegrid")

# 创建市场数据的DataFrame
data_market = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022],
    'USA Market': [279.6, 500.7, 529.2, 547.2, 577.2, 675.0],
    'Western Europe Market': [255.0, 265.9, 270.9, 287.8, 294.8, 295.8],
    'Japan Market': [95.4, 96.7, 97.3, 98.5, 99.1, 100.2],
    'China Market': [134.0, 178.0, 221.2, 295.3, 494.2, 493.6],
}

# 创建DataFrame
df_market = pd.DataFrame(data_market)

# 验证数据结构
print("Data Preview:")
print(df_market)

# 定义每个区域的颜色
colors = {
    'USA Market': 'red',
    'Western Europe Market': 'purple',
    'Japan Market': 'green',
    'China Market': 'blue'
}

# 设置全局字体为Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# 初始化绘图
plt.figure(figsize=(14, 8))

# 绘制每个区域的市场数据
for region, color in colors.items():
    plt.plot(
        df_market['Year'],
        df_market[region],
        label=region.replace(' Market', ''),  # 标签简化为地区名
        marker='o',
        linestyle='-',
        color=color,
        linewidth=3,      # 加粗线条
        markersize=10     # 加粗标记
    )
    # 填充线条下方的区域
    plt.fill_between(
        df_market['Year'],
        df_market[region],
        color=color,
        alpha=0.3
    )

# 设置标题和轴标签
plt.title("2017-2022 Pet Market Size by Region", fontsize=18, fontweight='bold')
plt.xlabel("Year", fontsize=16)
plt.ylabel("Market Size (Billion CNY)", fontsize=16)

# 自定义网格和刻度
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.xticks(df_market['Year'], fontsize=12)
plt.yticks(fontsize=12)

# 添加图例
plt.legend(title='Region', fontsize=14, title_fontsize=14, loc='upper left')

# 加粗图表边框（spines）并设置为黑色
ax = plt.gca()  # 获取当前轴
for spine in ax.spines.values():
    spine.set_linewidth(2)  # 设置边框线宽为2
    spine.set_color('black')  # 设置边框颜色为黑色

# 优化布局以防止标签重叠
plt.tight_layout()

# 显示图表
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure consistent plotting style
sns.set(style="whitegrid")

# Creating mock data for the given scenario
data_market = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022],
    'USA Market': [279.6, 500.7, 529.2, 547.2, 577.2, 675.0],
    'Western Europe Market': [255.0, 265.9, 270.9, 287.8, 294.8, 295.8],
    'Japan Market': [95.4, 96.7, 97.3, 98.5, 99.1, 100.2],
    'China Market': [134.0, 178.0, 221.2, 295.3, 494.2, 493.6],
}

# Creating a DataFrame
df_market = pd.DataFrame(data_market)

# Verify the DataFrame structure
print("Data Preview:")
print(df_market)

# Define distinct colors for each region
colors = {
    'USA Market': 'red',
    'Western Europe Market': 'purple',
    'Japan Market': 'green',
    'China Market': 'orange'
}

# Set the overall font to Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'

# Initialize the plot
plt.figure(figsize=(14, 8))

# Plot each region's market data
for region, color in colors.items():
    plt.plot(
        df_market['Year'],
        df_market[region],
        label=region.replace(' Market', ''),
        marker='o',
        linestyle='-',
        color=color,
        linewidth=3,      # Thicker lines
        markersize=10     # Larger markers
    )
    # Fill the area under the line with the same color
    plt.fill_between(
        df_market['Year'],
        df_market[region],
        color=color,
        alpha=0.3
    )

# Set title and labels with Times New Roman
plt.title("2017-2022 Pet Market Size by Region", fontsize=18, fontweight='bold')
plt.xlabel("Year", fontsize=16)
plt.ylabel("Market Size (Billion CNY)", fontsize=16)

# Customize grid and ticks
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.xticks(df_market['Year'], fontsize=12)
plt.yticks(fontsize=12)

# Add legend with Times New Roman font
plt.legend(title='Region', fontsize=14, title_fontsize=14, loc='upper left')

# Optimize layout to prevent overlap
plt.tight_layout()
# 加粗图表边框（spines）并设置为黑色
ax = plt.gca()  # 获取当前轴
for spine in ax.spines.values():
    spine.set_linewidth(2)  # 设置边框线宽为2
    spine.set_color('black')  # 设置边框颜色为黑色
# Display the plot
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

a1 = ['美国食品', '西欧食品', '日本食品', '中国食品']
a2 = ['美国市场', '西欧市场', '日本市场', '中国市场']

for i, ax in enumerate(axes.flat):

    sns.regplot(x=a1[i], y=a2[i], data=df, scatter_kws={'alpha': 0.7}, line_kws={'color': 'red'}, ax=ax)
    
    
    ax.set_title(f"{a1[i]}与{a2[i]}之间的关系")
    ax.set_xlabel("年份",fontsize=15)
    ax.set_ylabel("市场规模（十亿人民币）",fontsize=15)
    ax.tick_params(axis='both', which='major', labelsize=15)

plt.tight_layout()
#plt.savefig('各国的食品与市场规模之间的关系.png',dpi=500)

plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.gridspec import GridSpec

# 确保系统中安装了Times New Roman字体
# 如果未安装，可以选择其他类似的衬线字体

# 模拟的数据
data = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022],
    'USA Food': [200.6, 209.2, 222.4, 231.4, 244.2, 287.0],
    'Western Europe Food': [136.4, 141.8, 144.0, 152.6, 155.7, 156.5],
    'Japan Food': [30.5, 30.9, 31.0, 31.3, 31.4, 31.7],
    'China Food': [41.3, 54.6, 68.4, 81.5, 92.1, 99.3],
    'USA Market': [279.6, 500.7, 529.2, 547.2, 577.2, 675.0],
    'Western Europe Market': [255.0, 265.9, 270.9, 287.8, 294.8, 295.8],
    'Japan Market': [95.4, 96.7, 97.3, 98.5, 99.1, 100.2],
    'China Market': [134.0, 178.0, 221.2, 295.3, 494.2, 493.6],
}

df_market = pd.DataFrame(data)


correlations = {}
countries = ['USA', 'Western Europe', 'Japan', 'China']
for country in countries:
    food_col = f'{country} Food'
    market_col = f'{country} Market'
    corr = df_market[food_col].corr(df_market[market_col])
    correlations[country] = corr

corr_df = pd.DataFrame(list(correlations.items()), columns=['Country', 'Correlation'])
corr_df.set_index('Country', inplace=True)


food_columns = ['USA Food', 'Western Europe Food', 'Japan Food', 'China Food']
market_columns = ['USA Market', 'Western Europe Market', 'Japan Market', 'China Market']


plt.rcParams['font.family'] = 'Times New Roman'


fig = plt.figure(figsize=(20, 10))
gs = GridSpec(2, 3, width_ratios=[1.5, 1, 1], height_ratios=[1, 1], wspace=0.3, hspace=0.3)


ax_heatmap.set_title('Correlation Heatmap of Pet Food and Pet Market by Country', fontsize=16, fontweight='bold', pad=20)
ax_heatmap.set_xlabel('')
ax_heatmap.set_ylabel('')

plt.setp(ax_heatmap.get_xticklabels(), rotation=45, ha='right', fontsize=12)
plt.setp(ax_heatmap.get_yticklabels(), rotation=0, fontsize=12)


for i in range(4):
    row = i // 2
    col = i % 2
    ax = fig.add_subplot(gs[row, col + 1])
    sns.regplot(
        x=food_columns[i],
        y=market_columns[i],
        data=df_market,
        scatter_kws={'alpha': 0.7},
        line_kws={'color': 'purple'},
        ax=ax
    )
    ax.set_title(f"Relationship between {food_columns[i]} and {market_columns[i]}", fontsize=12, family='Times New Roman')
    ax.set_xlabel("Food Size (Billion CNY)", fontsize=12, family='Times New Roman')
    ax.set_ylabel("Market Size (Billion CNY)", fontsize=12, family='Times New Roman')
    ax.tick_params(axis='both', which='major', labelsize=10)


plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.gridspec import GridSpec




data = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022],
    'USA Market': [279.6, 500.7, 529.2, 547.2, 577.2, 675.0],
    'Western Europe Market': [255.0, 265.9, 270.9, 287.8, 294.8, 295.8],
    'Japan Market': [95.4, 96.7, 97.3, 98.5, 99.1, 100.2],
    'China Market': [134.0, 178.0, 221.2, 295.3, 494.2, 493.6],
}

df_market = pd.DataFrame(data)


df_market['USA Food'] = [200.6, 209.2, 222.4, 231.4, 244.2, 287.0]
df_market['Western Europe Food'] = [136.4, 141.8, 144.0, 152.6, 155.7, 156.5]
df_market['Japan Food'] = [30.5, 30.9, 31.0, 31.3, 31.4, 31.7]
df_market['China Food'] = [41.3, 54.6, 68.4, 81.5, 92.1, 99.3]


print(df_market)


corr_matrix = df_market.drop('Year', axis=1).corr()


plt.rcParams['font.family'] = 'Times New Roman'  # 设置全局字体为Times New Roman
sns.set(style="white")  # 使用白色背景


gs = GridSpec(2, 3, width_ratios=[1.5, 1, 1], height_ratios=[1, 1], wspace=0.3, hspace=0.3)


ax_heatmap = fig.add_subplot(gs[:, 0])

)
ax_heatmap.set_title('Correlation Heatmap of Pet Food and Pet Market by Country', fontsize=16, fontweight='bold', pad=20)
ax_heatmap.set_xlabel('')
ax_heatmap.set_ylabel('')

plt.setp(ax_heatmap.get_xticklabels(), rotation=45, ha='right', fontsize=12)
plt.setp(ax_heatmap.get_yticklabels(), rotation=0, fontsize=12)


countries = ['USA', 'Western Europe', 'Japan', 'China']
food_columns = ['USA Food', 'Western Europe Food', 'Japan Food', 'China Food']
market_columns = ['USA Market', 'Western Europe Market', 'Japan Market', 'China Market']

for i in range(4):
    row = i // 2
    col = i % 2
    ax = fig.add_subplot(gs[row, col + 1])
    sns.regplot(
        x=food_columns[i],
        y=market_columns[i],
        data=df_market,
        scatter_kws={'alpha': 0.7},
        line_kws={'color': 'red'},
        ax=ax
    )
    ax.set_title(f"Relationship between {food_columns[i]} and {market_columns[i]}", fontsize=14, family='Times New Roman')
    ax.set_xlabel("Pet Food Size (Billion CNY)", fontsize=12, family='Times New Roman')
    ax.set_ylabel("Market Size (Billion CNY)", fontsize=12, family='Times New Roman')
    ax.tick_params(axis='both', which='major', labelsize=10)

plt.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


data = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022],
    'USA Market': [279.6, 500.7, 529.2, 547.2, 577.2, 675.0],
    'Western Europe Market': [255.0, 265.9, 270.9, 287.8, 294.8, 295.8],
    'Japan Market': [95.4, 96.7, 97.3, 98.5, 99.1, 100.2],
    'China Market': [134.0, 178.0, 221.2, 295.3, 494.2, 493.6],
}

df_market = pd.DataFrame(data)


df_market['USA Food'] = [200.6, 209.2, 222.4, 231.4, 244.2, 287.0]
df_market['Western Europe Food'] = [136.4, 141.8, 144.0, 152.6, 155.7, 156.5]
df_market['Japan Food'] = [30.5, 30.9, 31.0, 31.3, 31.4, 31.7]
df_market['China Food'] = [41.3, 54.6, 68.4, 81.5, 92.1, 99.3]

print(df_market)


corr_matrix = df_market.drop('Year', axis=1).corr()


plt.rcParams['font.family'] = 'Times New Roman' 
sns.set(style="white")  


plt.figure(figsize=(12, 10))


heatmap = sns.heatmap(
    corr_matrix,
    annot=True,              
    fmt=".2f",              
    cmap='coolwarm',          
    linewidths=.5,            
    cbar_kws={"shrink": .8},   
    annot_kws={"size": 12}    
)


plt.title('Correlation Heatmap of Pet Food and Pet Market by Country', fontsize=16, fontweight='bold', pad=20)


plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(rotation=0, fontsize=12)


plt.tight_layout()


plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022],
    'Western Europe Pet Market (Billion CNY)': [255, 265.9, 270.9, 287.8, 294.8, 295.8],
    'Western Europe Pet Food (Billion CNY)': [136.4, 141.8, 144.0, 152.6, 155.7, 156.5],
    'Japan Pet Market (Billion CNY)': [95.4, 96.7, 97.3, 98.5, 99.1, 100.2],
    'Japan Pet Food (Billion CNY)': [30.5, 30.9, 31.0, 31.3, 31.4, 31.7],
    'USA Pet Market (Billion CNY)': [279.6, 500.7, 529.2, 547.2, 577.2, 675.0],
    'USA Pet Food (Billion CNY)': [200.6, 209.2, 222.4, 231.4, 244.2, 287.0]
}

df_pet = pd.DataFrame(data)


sns.set(style="whitegrid")
plt.rcParams['font.family'] = 'Times New Roman'


fig, axes = plt.subplots(1, 3, figsize=(24, 8), sharey=True)


regions = {
    'Western Europe': {
        'Market': 'Western Europe Pet Market (Billion CNY)',
        'Food': 'Western Europe Pet Food (Billion CNY)'
    },
    'Japan': {
        'Market': 'Japan Pet Market (Billion CNY)',
        'Food': 'Japan Pet Food (Billion CNY)'
    },
    'USA': {
        'Market': 'USA Pet Market (Billion CNY)',
        'Food': 'USA Pet Food (Billion CNY)'
    }
}

colors = {'Market': 'red', 'Food': 'purple'}

# 绘图循环
for ax, (region, cols) in zip(axes, regions.items()):
    sns.lineplot(
        data=df_pet,
        x='Year',
        y=cols['Market'],
        marker='o',
        label='Pet Market',
        color=colors['Market'],
        ax=ax
    )
    sns.lineplot(
        data=df_pet,
        x='Year',
        y=cols['Food'],
        marker='s',
        label='Pet Food',
        color=colors['Food'],
        ax=ax
    )
    ax.fill_between(df_pet['Year'], df_pet[cols['Market']], color=colors['Market'], alpha=0.3)
    ax.fill_between(df_pet['Year'], df_pet[cols['Food']], color=colors['Food'], alpha=0.3)

    ax.set_title(f'{region} Pet Market and Pet Food Trends (2017-2022)', fontsize=16, fontweight='bold')
    ax.set_xlabel('Year', fontsize=14)
    if ax == axes[0]:
        ax.set_ylabel('Amount (Billion CNY)', fontsize=14)
    ax.tick_params(axis='both', labelsize=12)
    ax.legend(title='Category', fontsize=12)
    # 加粗图表边框（spines）并设置为黑色
    for spine in ax.spines.values():
        spine.set_linewidth(2)  # 设置边框线宽为2
        spine.set_color('black')  # 设置边框颜色为黑色

plt.tight_layout()
plt.show()
