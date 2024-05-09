#include <iostream>
#include <vector>
using namespace std;

vector<unsigned long long> powersOfTwo;

// 预处理2的n次方
void preprocessPowersOfTwo() {
    unsigned long long powerOfTwo = 1;
    for (int i = 0; i <= 64; ++i) {  // 修改为64
        powersOfTwo.push_back(powerOfTwo);
        powerOfTwo *= 2;
    }
}

// 二分查找
unsigned long long findMinimumN(unsigned long long m) {  // 修改为unsigned long long
    unsigned long long low = 0, high = powersOfTwo.size() - 1;
    while (low <= high) {
        unsigned long long mid = (low + high) >> 1;
        if (powersOfTwo[mid] >= m) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return low; // 返回最小 n
}

int main() {
    preprocessPowersOfTwo();
    unsigned long long m;  // 修改为unsigned long long
    int k;
    cin >> k;
    for(int i = 0; i < k; i ++ ){
        cin >>m;
        cout << findMinimumN(m) << endl;
    }
    return 0;
}
