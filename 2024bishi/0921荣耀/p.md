在计算机中容量单位一般使用B，KB、MB、GB来表示，它们之间的关系如下
1KB=1024B
1MB =1024KB
1GB-1024MB
程序输入一个整数，单位为B，请将该容量转换为最合适单位输出，结果四舍五入保留两位小数。
各单位取值范围:
B[0,1024)
KB、MB: [1.1024)
GB:[1,~)

如:1048576B=1024KB=1MB，数值1包含在MB单位的可取值范围内，因此输出为1.00MB
输入描述
非空整数，取值范围[0.2^31-1]
输出描述
容量大小(带单位)
示例1：
输入：
1048576
输出：
1.00MB