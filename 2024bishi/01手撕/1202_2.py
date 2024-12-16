import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

# 数据预处理
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# 加载数据
train_loader = DataLoader(
    datasets.MNIST('./data', train=True, download=True, transform=transform),
    batch_size=64, shuffle=True)
test_loader = DataLoader(
    datasets.MNIST('./data', train=False, transform=transform),
    batch_size=64, shuffle=False)

# 定义网络
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Sequential(
            nn.Flatten(),  # 将28x28的图片展平为784维向量
            nn.Linear(28*28, 128),  # 第一个全连接层，784->128
            nn.ReLU(),  # 激活函数
            nn.Linear(128, 10)  # 输出层，128->10（10个数字类别）
        )
    
    def forward(self, x):
        return self.fc(x)

# 训练模型
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # 检查是否有GPU
model = Net().to(device)  # 创建模型并移到适当设备（GPU/CPU）
criterion = nn.CrossEntropyLoss()  # 损失函数
optimizer = torch.optim.Adam(model.parameters())  # 优化器

losses = []
for epoch in range(5):  # 训练5轮
    model.train()  # 设置为训练模式
    for data, target in train_loader:  # 遍历训练数据
        data, target = data.to(device), target.to(device)  # 数据移到设备上
        optimizer.zero_grad()  # 清空梯度
        output = model(data)  # 前向传播
        loss = criterion(output, target)  # 计算损失
        loss.backward()  # 反向传播
        optimizer.step()  # 更新参数
        losses.append(loss.item())  # 记录损失值
    
    # 测试
    model.eval()
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            pred = output.argmax(dim=1)
            correct += pred.eq(target).sum().item()
    
    print(f'Epoch {epoch}: Accuracy = {correct/len(test_loader.dataset):.4f}')

# 绘制损失曲线
plt.plot(losses)
plt.title('Training Loss')
plt.xlabel('Batch')
plt.ylabel('Loss')
plt.show()