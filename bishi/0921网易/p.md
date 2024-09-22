# 网易游戏雷火2024年秋招游戏研发工程师笔试
场景中有n只小怪，所有小怪均匀随机分布。玩家可以使用技能来同时对至多 m 只小怪各发射一支箭矢(每只小怪只能被选取一次)。
伤害系数 k=角度最相近的两支箭矢的角度差，当不足两支箭时，k=180;实际发射的箭矢数量为 a;
每支箭矢的伤害 d = 1/2m + 1/2a - (180 - k) / 360ma
给定 n,m，以及小怪的角度和玩家的坐标，求技能总伤害最大时的 k,a;总伤害等于每支箭矢的伤害乘以实际发射的箭矢数量。
如果存在多种情况的技能伤害相同，输出箭矢最多的结果

输入描述
第一行两个整数;n,m。(1<=n,m <= le4)
接下来n行，每行一个浮点数Gi，表示第i只小怪的角度，保证角度均匀随机。(0<ai < 360)
输出描述：
共两行，分别表示技能最大伤害时的k和a
k保留5位小数，计算过程请使用double浮点数

示例1：
输入：
10 5
30
35
45
90
130
259
260
289
300
352
输出:
41.00000
5


示例2：
输入：
1 1
302.58910
输出:
180.000000
1

说明:选取第35 90 259 300 352度的小怪，k取41时有最大值。
总伤害(1/10+1/10-(180-41)/(360*5*5))*5=0.92278


```cpp
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>

using namespace std;

bool check(int a, double k, const vector<double>& v, int n) {
  for(int i=0; i < n; i++) {
    int count =1;
    double last = v[i];
    for(int j=i+1; j < n; j++) {
      if(abs(v[j] - last) >= k && abs(last - v[j]) >= k) {
        count++;
        last = v[j];
        if(count == a) break;
      }
    }
    if(count ==a) {
      double diff = 360.0 - (last - v[i]);
      if(diff >=k) {
        return true;
      }
    }
  }
  return false;
}

int main(){
  int n, m;
  cin >> n >> m;
  vector<double> angles(n);
  for(int i=0; i<n; i++) cin >> angles[i];
  sort(angles.begin(), angles.end());

  int max_a = min(n, m);
  double best_D = -1.0;
  double best_k = 0.0;
  int best_a = 1;

  for(int a=1; a<=max_a; a++) {
    double k;
    if(a == 1){
      k = 180.0;
    }
    else{
      double low = 1;
      double high = 180;
      double ans = 0;
      while(low < high - 1e-5) {
        double mid = low + (high - low) / 2;
        if(check(a, mid, angles, n)){
          ans = mid;
          low = mid;
        }
        else{
          high = mid;
        }
      }
      k = (double)ans;
    }
    double D = ((double)a)/(2.0 * m) + 0.5 - (180.0 - k)/(360.0 * m);
    if(D > best_D + 1e-12){
      best_D = D;
      best_a = a;
      best_k = k;
    } else if(abs(D - best_D) <=1e-12 && a > best_a){
      best_a = a;
      best_k = k;
    }
  }
  best_k += 1e-9;
  best_k = floor(best_k * 100000.0 + 0.5) / 100000.0;

  printf("%.5lf\n", best_k);
  cout << best_a << "\n";
}
```