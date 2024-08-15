
print(1048575 -  666939)
print(666939 * 0.8)
print(666939 * 0.2)
1. 加载数据并进行预处理，包括清理缺失值和异常值。
2. 划分数据为特征集和目标变量，然后分为训练集和测试集。
3. 初始化并配置随机森林模型，设置树的数量、最大深度等参数。
4. 在训练集上训练模型，然后在测试集上进行预测。
5. 评估模型性能并输出特征重要性。
# 导入所需的库
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 加载数据
data = pd.read_csv('train.csv')

# 数据预处理
def preprocess_data(data):
    # 删除包含缺失值的行
    data.dropna(inplace=True)
    
    # 计算四分位数和IQR
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    
    # 根据IQR过滤异常值
    data = data[~((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).any(axis=1)]
    
    return data

# 应用数据预处理
cleaned_data = preprocess_data(data)

# 分离特征和目标变量
features = cleaned_data.drop('FloodProbability', axis=1)
target = cleaned_data['FloodProbability']

# 划分训练集和测试集
features_train, features_test, target_train, target_test = train_test_split(
    features, target, test_size=0.2, random_state=42)

# 初始化随机森林模型
rf = RandomForestRegressor(n_estimators=500, max_depth=15, max_features='sqrt',
                           min_samples_split=10, min_samples_leaf=4, random_state=42)

# 训练模型
rf.fit(features_train, target_train)

# 进行预测
predictions = rf.predict(features_test)

# 评估模型
mse = mean_squared_error(target_test, predictions)
print("Mean Squared Error:", mse)

# 特征重要性
importances = rf.feature_importances_
print("Feature Importances:", importances)
