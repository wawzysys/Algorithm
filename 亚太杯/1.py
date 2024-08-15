import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.colors import LinearSegmentedColormap

# 设置中文字体
font_path = 'C:/Windows/Fonts/simhei.ttf'  # 使用 SimHei 字体
font = FontProperties(fname=font_path)

# 读取 Excel 文件
file_path = r"C:\Users\19160\Desktop\spearman.xlsx"
data = pd.read_excel(file_path, index_col=0)

# 绘制相关矩阵的热图
plt.figure(figsize=(10, 5), dpi=300)  
sns.heatmap(data, annot=True, fmt=".4f", cmap='coolwarm', linewidths=.5, cbar_kws={"shrink": .5}, annot_kws={"size": 6})
plt.title('Spearman Correlation Heatmap', fontsize=20, fontweight='bold', fontproperties=font)
plt.xticks(rotation=45, ha='right', fontsize=12, fontproperties=font)
plt.yticks(fontsize=12, fontproperties=font)
plt.tight_layout()
plt.savefig('spearman_correlation_heatmap.png', dpi=300)  
plt.show()
