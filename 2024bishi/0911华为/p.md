每天早晨，环卫T人需要处理各个小区的生活垃圾，每个小区的生活垃圾由一队环卫工人负责运送到最近的垃圾回收站进行处理，求将所有小区垃圾送到垃圾回收站的最小距离和。假设小区和垃圾回收站都在都在一个m行n列的区域矩阵上，相邻点的距离为1，只能上下左右移动;其中0表示垃圾处理站，1表示小区，2表示空白区域，-1表示障碍区域不可通行。区域内如果没有小区或者没有垃圾回收站，则最小距离和返回0，无法到达垃圾回收站的小区公单独处理，不计入本次距离和中。计算所有小区垃圾送到垃圾回收站的最小距离和。
解答要求
时间限制: C/C++ 1000ms,其他语言:2000ms内存限制: C/C++ 256MB,其他语言:512MB
输入
第 行为两个数字m和n，表示区域矩阵的行数和列数，中间使用空格分隔，m和n的范围均为[1,300]
接下来的m 行表示一个m*n的区域矩阵数组，每行的元素间以空格分隔，其中元素取值仅为-1(障得域)、0(垃圾处理站)、1(小区)、2(空白区域)
输入:
4 4
1 2 -1 1
2 0 2 0
2 2 -1 2
1 2 1 1
输出:
11

输入:
2 3
0 -1 1
1 -1 2
输出
1

2、圣诞节礼盒
圣诞节到了，豆豆的妈妈准备了很多圣诞礼盒，礼盒大小不同，豆豆在玩堆盒子的游戏，妈妈问豆豆，
怎么堆盒子使得堆出的高度最高，每个礼盒的大小由长、宽、高表示，
堆盒子的时候要求下面的盒子长、宽、高都必须大于上面的盒子，不包含等于，
请你帮助豆豆一起堆出最高的一堆礼盒，高度为堆出的礼盒的所有高度的总和。


输入
输入的第一行是礼盒的个数N,接下来输入N行,每行表示每个礼盒的长宽、高,礼盒的数量不超过1000个,
每个盒子的长、宽、高取范围为1~10.
输出
输出一行，输出能堆出盒子的最高高度

输出
输出一行，输出能堆出盒子的最高高度
样例1
输入:
4
1 1 1
2 3 4
3 6 7
4 5 6
输出:12
解释:选择1、2、3,3个盒子堆出的高度最高,1+4+7=12
样例2
输入:
4
1 1 1
1 1 1
2 2 2
2 2 2
输出
3
解释:其中的一种选择方式为选择1和3两个盒子,堆出的高度最高为1+2=3