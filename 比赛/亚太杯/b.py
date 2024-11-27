import matplotlib.pyplot as plt
from matplotlib import rcParams
import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False
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

countries = data['国家'].values
revenues = data['收入 (百万美元)'].values

data = pd.DataFrame({"国家": countries, "收入 (百万美元)": revenues})

plt.figure(figsize=(12, 8))

data["Country"] = data["国家"].map(translation_map)
print(data['国家'])
print(data['Country'])


plt.barh(data["Country"], data["收入 (百万美元)"], color="blue", alpha=0.7)
plt.title("Pet Food Market Revenue by World in 2023 (USD Million)", fontsize=14)
plt.xlabel("Revenue (US$ million)", fontsize=20)
plt.ylabel("country", fontsize=20)
plt.gca().invert_yaxis()
plt.tick_params(labelsize=13)

plt.tight_layout()

plt.show()

import pandas as pd
import plotly.express as px
import pycountry

data = pd.read_excel('2023年世界各国宠物食品市场收入.xlsx')

print("Original Columns:", data.columns.tolist())

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
}

data["Country"] = data["国家"].map(translation_map)

data = data.rename(columns={'收入 (百万美元)': 'Revenue (Million USD)'})

print("Columns after renaming:", data.columns.tolist())

print(data.head())

manual_iso_map = {
    'Turkey': 'TUR',
    'Russia': 'RUS',
}

def get_iso3(country_name):
    try:
        return pycountry.countries.lookup(country_name).alpha_3
    except:
        return manual_iso_map.get(country_name, None)

data['ISO_Code'] = data['Country'].apply(get_iso3)

missing_iso = data[data['ISO_Code'].isnull()]['Country'].unique()
if len(missing_iso) > 0:
    print(f"Unable to find ISO codes for the following countries: {missing_iso}")
print(data.head())

fig = px.choropleth(
    data_frame=data,
    locations="ISO_Code",
    color="Revenue (Million USD)",
    hover_name="Country",
    color_continuous_scale=px.colors.sequential.Plasma,
    title="<b>2023 Pet Food Market Revenue by Country (Million USD)</b>",
    labels={'Revenue (Million USD)': 'Revenue (Million USD)'}
)

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

fig.show(renderer="browser")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.DataFrame({
    '国家': ['美国', '中国', '英国', '巴西', '德国', '法国', '日本', '土耳其',
            '意大利', '加拿大', '澳大利亚', '墨西哥', '西班牙', '俄罗斯', '印度'],
    '收入 (百万美元)': [57384.64, 7419.96, 7224.56, 6287.95, 5724.1,
                      4998.58, 4619.43, 4176.62, 3833.27, 3735.68,
                      2952.06, 2506.59, 2022.42, 1940.34, 1847.64]
})

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

data = data.rename(columns={'收入 (百万美元)': 'Revenue (Million USD)'})

total_revenue = data['Revenue (Million USD)'].sum()
data['Revenue Share (%)'] = (data['Revenue (Million USD)'] / total_revenue) * 100

data_sorted = data.sort_values(by='Revenue (Million USD)', ascending=False)

custom_colors = [
    '#FF9999',
    '#66B3FF',
    '#99FF99',
    '#FFCC99',
    '#C2C2F0',
    '#FFB3E6',
    '#C4E17F',
    '#F0E68C',
    '#ADD8E6',
    '#FFD700',
    '#FFA07A',
    '#20B2AA',
    '#9370DB',
    '#FF6347',
    '#40E0D0'
]
plt.rcParams['font.family'] = 'Times New Roman'
fig, axes = plt.subplots(1, 2, figsize=(20, 10))

axes[0].pie(
    data['Revenue Share (%)'],
    labels=data['Country'],
    autopct='%1.1f%%',
    startangle=140,
    colors=custom_colors[:len(data)],
    wedgeprops={'edgecolor': 'white'}
)
axes[0].set_title('Revenue Share by Country', fontweight='bold', fontsize=20)

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

plt.tight_layout()

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
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022],
    'USA Food': [200.6, 209.2, 222.4, 231.4, 244.2, 287.0],
    'Western Europe Food': [136.4, 141.8, 144.0, 152.6, 155.7, 156.5],
    'Japan Food': [30.5, 30.9, 31.0, 31.3, 31.4, 31.7],
    'China Food': [41.3, 54.6, 68.4, 81.5, 92.1, 99.3],
}

df = pd.DataFrame(data)

x = np.arange(len(df['Year']))
width = 0.2

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
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

data_market = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022],
    'USA Market': [279.6, 500.7, 529.2, 547.2, 577.2, 675.0],
    'Western Europe Market': [255.0, 265.9, 270.9, 287.8, 294.8, 295.8],
    'Japan Market': [95.4, 96.7, 97.3, 98.5, 99.1, 100.2],
    'China Market': [134.0, 178.0, 221.2, 295.3, 494.2, 493.6],
}

df_market = pd.DataFrame(data_market)

print("Data Preview:")
print(df_market)

colors = {
    'USA Market': 'red',
    'Western Europe Market': 'purple',
    'Japan Market': 'green',
    'China Market': 'blue'
}

plt.rcParams['font.family'] = 'Times New Roman'

plt.figure(figsize=(14, 8))

for region, color in colors.items():
    plt.plot(
        df_market['Year'],
        df_market[region],
        label=region.replace(' Market', ''),
        marker='o',
        linestyle='-',
        color=color,
        linewidth=3,
        markersize=10
    )
    plt.fill_between(
        df_market['Year'],
        df_market[region],
        color=color,
        alpha=0.3
    )

plt.title("2017-2022 Pet Market Size by Region", fontsize=18, fontweight='bold')
plt.xlabel("Year", fontsize=16)
plt.ylabel("Market Size (Billion CNY)", fontsize=16)

plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.xticks(df_market['Year'], fontsize=12)
plt.yticks(fontsize=12)

plt.legend(title='Region', fontsize=14, title_fontsize=14, loc='upper left')

ax = plt.gca()
for spine in ax.spines.values():
    spine.set_linewidth(2)
    spine.set_color('black')

plt.tight_layout()

plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

data_market = {
    'Year': [2017, 2018, 2019, 2020, 2021, 2022],
    'USA Market': [279.6, 500.7, 529.2, 547.2, 577.2, 675.0],
    'Western Europe Market': [255.0, 265.9, 270.9, 287.8, 294.8, 295.8],
    'Japan Market': [95.4, 96.7, 97.3, 98.5, 99.1, 100.2],
    'China Market': [134.0, 178.0, 221.2, 295.3, 494.2, 493.6],
}

df_market = pd.DataFrame(data_market)

print("Data Preview:")
print(df_market)

colors = {
    'USA Market': 'red',
    'Western Europe Market': 'purple',
    'Japan Market': 'green',
    'China Market': 'orange'
}

plt.rcParams['font.family'] = 'Times New Roman'

plt.figure(figsize=(14, 8))

for region, color in colors.items():
    plt.plot(
        df_market['Year'],
        df_market[region],
        label=region.replace(' Market', ''),
        marker='o',
        linestyle='-',
        color=color,
        linewidth=3,
        markersize=10
    )
    plt.fill_between(
        df_market['Year'],
        df_market[region],
        color=color,
        alpha=0.3
    )

plt.title("2017-2022 Pet Market Size by Region", fontsize=18, fontweight='bold')
plt.xlabel("Year", fontsize=16)
plt.ylabel("Market Size (Billion CNY)", fontsize=16)

plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.xticks(df_market['Year'], fontsize=12)
plt.yticks(fontsize=12)

plt.legend(title='Region', fontsize=14, title_fontsize=14, loc='upper left')

plt.tight_layout()
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_linewidth(2)
    spine.set_color('black')
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

plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.gridspec import GridSpec


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


plt.rcParams['font.family'] = 'Times New Roman'
sns.set(style="white")


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
    for spine in ax.spines.values():
        spine.set_linewidth(2)
        spine.set_color('black')

plt.tight_layout()
plt.show()
