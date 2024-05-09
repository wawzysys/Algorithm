#include <iostream>
#include <cmath>
#include <cstdint>

uint64_t findMinimumN(uint64_t m) {
    if (m == 0) return 0; // 处理 m 为 0 的特殊情况

    uint64_t n = static_cast<uint64_t>(std::ceil(std::log2(static_cast<double>(m))));
    return n;
}

int main() {
    uint64_t m = (uint64_t)pow(2, 64) - 1; // m 的最大值
    uint64_t n = findMinimumN(m);
    
    std::cout << "满足条件 2^n >= m 的最小非负整数 n 为: " << n << std::endl;
    
    return 0;
}
