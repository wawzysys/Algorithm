import pandas as pd
df1 = pd.read_excel(f'2019 - 2023 年中国宠物食品产量及出口额预测结果.xlsx')
df2 = pd.read_excel(f'各国的食品与市场规模的预测结果.xlsx')
df3 = pd.read_excel(f'国外宠物数量变化预测结果.xlsx')

df1 = df1[df1.columns[1:]]
df2 = df2[df2.columns[1:]]
df3.columns = ['年份', 'America_Cat', 'America_Dog', 'France_Cat', 'France_Dog',
       'Germany_Cat', 'Germany_Dog']

df = pd.merge(df1,df2,on='年份')
df = pd.merge(df,df3,on='年份')
# print(df)
print(f"Current column count: {len(df.columns)}, columns: {df.columns}")

new_columns = ['Year', 'China_Food_Production', 'China_Export_Value', 
               'US_Food', 'Western_Europe_Food', 'Japan_Food', 
               'China_Food_Demand', 'Western_Europe_Market', 'Japan_Market', 
               'US_Market', 'China_Market', 'America_Cat', 'America_Dog', 
               'France_Cat', 'France_Dog', 'Germany_Cat', 'Germany_Dog']

df.columns = new_columns
print(df.head())
df

import pandas as pd

# 读取数据
tax = pd.read_excel('欧美对外经济政策.xlsx')

# 筛选欧盟和美国的数据，并重置索引
tax1 = tax[tax.地区 == '欧盟'].reset_index(drop=True)
tax2 = tax[tax.地区 == '美国'].reset_index(drop=True)

# 提取年份
year = tax1['年份'].values

# 去掉不必要的列（假设第 2 列之后是指标数据）
tax1 = tax1[tax1.columns[2:]]
tax2 = tax2[tax2.columns[2:]]

# 修改列名为英文
tax1.columns = ['EU_' + col for col in tax1.columns]
tax2.columns = ['US_' + col for col in tax2.columns]

# 合并数据并添加年份列
t = pd.concat([tax1, tax2], axis=1)
t['Year'] = year
# 检查结果
print(t.head())
# 修改 df 的列名为英文
df.columns = [
    'Year', 'China_Food_Production', 'China_Export_Value', 'US_Food',
    'Western_Europe_Food', 'Japan_Food', 'China_Food_Demand',
    'Western_Europe_Market', 'Japan_Market', 'US_Market', 'China_Market',
    'America_Cat', 'America_Dog', 'France_Cat', 'France_Dog', 'Germany_Cat',
    'Germany_Dog'
]

# 修改 t 的列名为英文
t.columns = [
    'EU_FDI_Inflow_MillionUSD', 'EU_Policy_InterestRate_Percentage',
    'EU_Trade_Balance_MillionUSD', 'EU_Export_Total_MillionUSD',
    'EU_Import_Total_MillionUSD', 'US_FDI_Inflow_MillionUSD',
    'US_Policy_InterestRate_Percentage', 'US_Trade_Balance_MillionUSD',
    'US_Export_Total_MillionUSD', 'US_Import_Total_MillionUSD', 'Year'
]

# 使用英文列名合并数据框
df = pd.merge(df, t, on='Year')

# 检查结果
print(df.head())
from scipy.stats import pearsonr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
from sklearn.preprocessing import MinMaxScaler
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
import warnings
warnings.filterwarnings("ignore")

# 设置字体为 Times New Roman
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['axes.unicode_minus'] = False

def correlation_matrix_with_p_values(X):
    cols = X.columns
    # 初始化显示矩阵，用来存储格式化的 (p值)相关系数
    display_matrix = np.empty((len(cols), len(cols)), dtype=object)
    display_matrix_values = np.empty((len(cols), len(cols)), dtype=object)
    
    # 计算相关系数和p值
    for i in range(len(cols)):
        for j in range(len(cols)):
            # 计算相关系数和p值
            corr, pval = pearsonr(X[cols[i]].dropna(), X[cols[j]].dropna())
            # 格式化结果为 (p值)相关系数
            display_matrix[i, j] = f"{corr:.3f}"
            display_matrix_values[i, j] = round(corr,3)
    
    # 将矩阵转为 DataFrame
    display_df = pd.DataFrame(display_matrix, index=cols, columns=cols)
    display_df_values = pd.DataFrame(display_matrix_values, index=cols, columns=cols)
    
    # 画热力图（使用蓝色系配色）
    plt.figure(figsize=(15, 12))
    sns.heatmap(display_df_values.astype('float'), 
                annot=display_df, 
                fmt='', 
                cmap='Blues',  # 改为Blues配色
                cbar=False)
    plt.title('Correlation Matrix')
    plt.show()

# 使用函数
X = df
correlation_matrix_with_p_values(X)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 设置字体和样式
sns.set(style="whitegrid")
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.unicode_minus"] = False  # 解决坐标轴负号显示问题

# 忽略警告
import warnings
warnings.filterwarnings("ignore")

# 回归绘图函数
def function(data, column, name, ax):
    # 回归方程构建
    slope, intercept, r_value, p_value, std_err = linregress(data[column], data['China_Export_Value'])
    
    # 绘图
    sns.regplot(
        x=column,
        y='China_Export_Value',
        data=data,
        ax=ax,
        line_kws={'label': f"y={slope:.3f}x+{intercept:.3f}\nR2={r_value**2:.3f}", 'color': 'purple'},
        scatter_kws={'color': 'purple'}
    )
    ax.set_title(f'China Export Value vs {name}', fontsize=14)
    ax.set_xlabel(f'{name}', fontsize=12)
    ax.set_ylabel('China Export Value', fontsize=12)
    ax.legend(loc='upper right', fontsize=10)

# 列名列表
columns = [
    'China_Food_Production', 'US_Food', 'Western_Europe_Food', 'Japan_Food',
    'China_Food_Demand', 'Western_Europe_Market', 'Japan_Market',
    'US_Market', 'China_Market', 'America_Cat', 'America_Dog', 'France_Cat',
    'France_Dog', 'Germany_Cat', 'Germany_Dog', 'EU_FDI_Inflow_MillionUSD',
    'EU_Policy_InterestRate_Percentage', 'EU_Trade_Balance_MillionUSD',
    'EU_Export_Total_MillionUSD', 'EU_Import_Total_MillionUSD',
    'US_FDI_Inflow_MillionUSD', 'US_Policy_InterestRate_Percentage',
    'US_Trade_Balance_MillionUSD', 'US_Export_Total_MillionUSD',
    'US_Import_Total_MillionUSD'
]

# 限制输出为 3 行
n_rows = 3
n_cols = 4
max_plots = n_rows * n_cols

# 设置网格布局
fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(20, n_rows * 5))
axes = axes.flatten()

# 绘制每个图
for i, c in enumerate(columns[:max_plots]):  # 限制绘制的图数量
    function(df, c, c, axes[i])

# 移除多余的子图框
for j in range(len(columns[:max_plots]), len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 设置风格
plt.style.use('seaborn')
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['axes.unicode_minus'] = False

# 创建模拟数据
np.random.seed(42)

# 1. 预测误差随时间的变化
time_periods = np.array([3, 6, 12, 18, 24, 30, 36])
error_rates = np.array([2.1, 3.5, 5.0, 6.8, 8.0, 10.5, 12.0])

# 2. 敏感性分析数据
policy_changes = np.array([-20, -15, -10, -5, 0, 5, 10, 15, 20])
tariff_impact = -0.42 * policy_changes + np.random.normal(0, 1, 9)
tech_barrier_impact = -0.35 * policy_changes + np.random.normal(0, 1, 9)
exchange_impact = -0.28 * policy_changes + np.random.normal(0, 1, 9)

# 3. 风险分布数据
risk_data = np.random.normal(0, 3, 1000)

# 创建图形
fig = plt.figure(figsize=(15, 12))

# 1. 预测误差图
ax1 = plt.subplot(221)
ax1.plot(time_periods, error_rates, 'o-', color='navy', linewidth=2)
ax1.set_xlabel('Forecast Period (Months)', fontsize=10)
ax1.set_ylabel('Prediction Error (%)', fontsize=10)
ax1.set_title('Prediction Error Over Time', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)

# 2. 政策敏感性分析
ax2 = plt.subplot(222)
ax2.plot(policy_changes, tariff_impact, 'o-', label='Tariff Impact', color='navy')
ax2.plot(policy_changes, tech_barrier_impact, 's-', label='Technical Barrier Impact', color='darkred')
ax2.plot(policy_changes, exchange_impact, '^-', label='Exchange Rate Impact', color='darkgreen')
ax2.set_xlabel('Policy Change (%)', fontsize=10)
ax2.set_ylabel('Export Value Change (%)', fontsize=10)
ax2.set_title('Policy Sensitivity Analysis', fontsize=12)
ax2.legend(fontsize=8)
ax2.grid(True, linestyle='--', alpha=0.7)

# 3. 风险分布
ax3 = plt.subplot(223)
sns.histplot(risk_data, bins=30, color='navy', alpha=0.6, ax=ax3)
ax3.axvline(np.percentile(risk_data, 95), color='red', linestyle='--', label='95% VaR')
ax3.set_xlabel('Return (%)', fontsize=10)
ax3.set_ylabel('Frequency', fontsize=10)
ax3.set_title('Risk Distribution', fontsize=12)
ax3.legend(fontsize=8)

# 4. 复苏周期分析
recovery_periods = [1, 2, 3, 3.5, 4, 5, 6]
recovery_prob = [0.05, 0.15, 0.25, 0.35, 0.15, 0.03, 0.02]
ax4 = plt.subplot(224)
bars = ax4.bar(recovery_periods, recovery_prob, color='navy', alpha=0.6)
ax4.set_xlabel('Recovery Period (Quarters)', fontsize=10)
ax4.set_ylabel('Probability', fontsize=10)
ax4.set_title('Recovery Period Distribution', fontsize=12)

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}',
             ha='center', va='bottom')

plt.tight_layout()
plt.show()