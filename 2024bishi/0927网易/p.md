# 1
在《梦幻西游》的世界中，长安城作为三界的重要商业中心，每天都有无数的玩家在此进行交易。在长安城的集市上，玩家可以通过摆摊、出售从任务、活动中获得的珍贵道具或饮料，赚取丰厚的银两。小易是一名资深的玩家，擅长通过各种渠道获取游戏内的稀有道具。他发现，最近长安城的集市交易异常火爆，很多玩家都在高价收购各种稀有道具。
目前，小易一共有 n 种道具准备出售，对于第种道具，其成本为 ai，目前的售价为6。所以，小易每卖出一件这种道具的利润为 b- αi。
为了控制流量，每人每天至多可以售卖k个道具第;个道具每天最多出售 “个。小易的目标是获得最大的利润。你能帮他计算一下，在这两个条件的限制下最多可以赚取多少银两?

输入描述
第一行输入两个整数n,k(1 ≤n ≤ 10';1 ≤k≤ 10°)代表小易售卖的道具种类、售卖总数量限制。
第二行输入 几 个整数
a1, a2,...., an(1≤ai≤10^6)，第之个数字代表第i
第二行输入n个整数b1,b2,·..,bn(1 ≤ ai≤ bi≤ 10^6)第之个数字代表第之个道具的售价。
第三行输入 n 个整数C1,C2,·.·,cn(1 < Ci< 10^6)第i个数字代表第之个道具的售卖数量限制。
输入：
3 5
1 2 3
4 2 6
1 2 3
输出：
12

# 1

在《阴阳师》中，小纸人的可爱形象总是被人津津乐道。无论是每日上线时的签到亦或是勾玉领取，还是每逢节日时的礼物祝福，小纸人总是会按时出现在大家的庭院。
然而，这么多的小纸人在培训的时候可是十分费劲的呢。小易这天就在町中培训小纸人--小纸人被排成了nxm 的矩阵，每个人身上都有一个编号，第i行第j列的纸人编号为(i-1)xm+j。小易会随机从以下三种类别中选取一个要求纸人们执行:
类型一:将第x行的小纸人与第y行的小纸人交换;
类型二:将第x行的小纸人整体左移y格，即这一行上的每一个小纸人都向左移动y格，左边多出来的小纸人按照原顺序补到末尾，更具体的说，记原先每个纸人身上的编号为 a1,a2,...,ay,...,am ，左移 y格后变为 ay+1,···,am,a1,a2,...,ay 。
类型三:让此时位于第 x行第 y列的小纸人报出自己身上的编号。

输入描述
第一行输入三个整数n,m,q(1≤n,m≤10^6;1≤q≤10^5)代表学生矩阵的行数、列数、教练的微调次数。
此后q行，先输入一个整数t(1 <t≤ 3)表示代表操作类别，随后:
如果t=1，代表操作类型一，在同一行上输入两个整数 , y(1 ≤ x,y≤ n);
如果t=2，代表操作类型二，在同一行上输入两个整数x,y (1 ≤x ≤ n;1 ≤y≤ 10^9)
如果t=3，代表操作类型三，在同一行上输入两个整数x,y (1 ≤ x ≤ n;1 ≤ y<= m)

输出描述
对于每一次ti = 3，在一行上输出一个整数，代表此时第 x 行第 y 列的小纸人身上的编号。

示例 1
输入
2 3 4
1 1 2
3 1 3
2 1 4
3 1 3

输出
6
4


# 3
在《镇魔曲》的东方玄幻世界中，修行者通过历练与战斗，不断提升自身修为，解锁传说中的圣印力量。圣印系统是修行者们在50级后觉醒的特殊能力，通过修炼和积累修炼值，修行者能够激活圣印，获得超凡的能力加持。
小易是一位年轻的修行者，在经历多次战斗和任务后，他的修为已达到50级，圣印系统得以激活，初始时，他的修练值为S=0。这一天，他偶然发现了一个古老的修炼场，传闻这里隐藏着许多远古修行者留下的强大圣印，修行者可以通过与这些圣印互动，获得特殊的修炼效果。
每个圣印的激活都有特定的条件，只有当小易的修炼值满足某些要求时，圣印的力量才能被激活，助他提升修炼值。具体地，第之个圣印的激活条件由四个整数(Li,Ri,Ti,Di)描述。只有当小易的修炼值 S 满足Li<S< Ri时，圣印i才会开始激活，激活过程持续Ti个时间单位，激活完成后，小易的修炼值将增加 Di点。一个圣印至多激活一次。
然而，修炼场内充满了不确定性。在激活过程中小易的修炼值不会立即改变，只有当激活结束时，修炼值才会增加。如果小易的修炼值发生变化，其他正在激活的圣印可能不再满足条件，导致激活中断。但若小易能在同一时刻完成多个圣印的激活，他将同时获得这些圣印的加持，使得他的修炼值快速提升，开启新的境界。将同时获得所有仙人的传授结果。
你需要计算，在修炼结束后，小易的修炼值最终是多少

第一行输入一个整数n(1 ≤n ≤ 10^5)代表圣印的数量。
此后n 行，第i行输入四个整数Li, R¡,Ti,Di (O ≤ Li≤ R¡≤ 10^8; 1 ≤ Ti,Di ≤ 10^8代表第i之个圣印的激活条件。

输出描述
在一行上输出一个整数，代表小易的最终修炼值。

示例 1
输入
4
0 3 1 3 
0 2 3 5 
3 3 1 2 
3 3 1 3

输出
8

说明
第零个时刻，修炼值即为初始值S=0，此时第一、二个圣印同时激活。
第一个时刻，第一个圣印激活完毕，S=3;由于此时已经不满足第二个圣印的规则，所以激活中断;同时，由于满足规则，第三、四个圣印被激活。
第二个时刻，第三、四个圣印同时激活完毕天人合一，小易的修炼值上升至8。
用java