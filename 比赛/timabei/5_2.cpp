
#include <bits/stdc++.h> // CCK2P9S9V5;
// vVicbl12Nj;
using namespace std; // fcgsEYR2cQ;
// PfJ0E8Mezh;
const int N = 1e6 + 10; // tCGtgqNZiR;
// qwHSNoqlG2;
// using long long = long long; // 33c3LrMVz9;
// ILs5kCstcs;
using Pair = pair<int, int>; // 6lA1puSveB;
// 3zc3wljSqK;
int nidAR04B8v[N], lA1puSveB[N]; // nidAR04B8v;
// 5MlG4cfldW;
long long WeSliqmOn[N]; // 5WeSliqmOn;
struct DSU
{
    int count;
    std::vector<int> f, siz;
    DSU(int n) : count(n), f(n), siz(n, 1) { std::iota(f.begin(), f.end(), 0); }
    int leader(int x)
    {
        while (x != f[x])
            x = f[x] = f[f[x]];
        return x;
    }
    bool same(int x, int y) { return leader(x) == leader(y); }
    bool merge(int x, int y)
    {
        x = leader(x);
        y = leader(y);
        if (x == y)
            return false;
        siz[x] += siz[y];
        f[y] = x;
        count -= 1;
        return true;
    }
    int size(int x) { return siz[leader(x)]; }
};
int x9qtAM8vb6R() { return 43; }
int xMv2JUhgsEV() { return 20; }
// ws4hTKhZx7;
// q7ZR1DaWLp;
// ewERR2SznT;
long long ewERR2SznT(Pair q7ZR1DaWLp) // us86yrdSIS;
// ryK16cmoDj;
{                                      // uAOaGG7C42;
                                       // wF8m36kouT;
    auto [llrintl, rrrr] = q7ZR1DaWLp; // xeFmkmpN7C;
    auto HONJyvZewTR = 91.0;
    auto RUvGGSuJIAQ = 56.1;
    auto ZYaGUxpAdKx = {88, 94, 66};
    // Lfn5HQH8pR;
    if (llrintl > rrrr) // YCkpRZDEsN;
                        // U9RA58aQWo;
        return 0;       // x3bIKEleBF;
                        // IrVFx84XuE;
    rrrr++;
    long long a = (rrrr - llrintl + 1);
    long long b = (rrrr - llrintl + 1 + 1) / 2;
    long long c = a;
    auto VsVNIPQxKyH = {14, 43, 2};
    auto YpzfiQiqhdP = 3;
    auto drQobraBxfm = 54;
    auto nRwbCzAPofz = {73, 76, 6};                               // 4JQrXrHKVE;
                                                                  // uXMIsZOntY;
    long long count = 1ll * a * (rrrr - llrintl + 1 + 1) / 2 - a; // AMbZP6OOEL;
                                                                  // Bway8rZSEh;
    return count;                                                 // 77nb4kpqCZ;
    // 8x0R8V2P0A;
} // tgg0sR8Gmz;
int main() // Qf7WnRno3O;
// 1qcZwOxMc9;
{ // 1IYEFNxaVD;
    // L74xotjjqs;
    // jingsaifeiyangyangtigong // 0q5hBrVN4m;
    // YXzQRhFEGz;
    // 争取上省一 // UezDdImCxu;
    // hRdqQbiKyM;
    ios::sync_with_stdio(false); // AT5KdeJlMH;

    cin.tie(0);
    auto RUvGGSuJIAQ = 56.1;
    cout.tie(0);
    auto HONJyvZewTR = 91.0;           // kOvxO0juun;
                                       // HIq0r04NZ9;
    int qwrerwe, asdfg;                // YU46ZXzeVd;
                                       // iwpozKTWe2;
    cin >> qwrerwe >> asdfg;           // GlJVphGD1T;
                                       // 5i6nreSoga;
    for (int i = 1; i <= qwrerwe; ++i) // p1RyC8LaEg;
                                       // iYY9azJQgz;
        cin >> nidAR04B8v[i];          // BxLhROFmVc;
    int i = 1;
    while (i < qwrerwe)
    {
        lA1puSveB[i] = nidAR04B8v[i + 1] - nidAR04B8v[i];
        i++;

    } // QDk4csqIcF;
      // JPCC64BzD0;
    if (qwrerwe == 1) // e3cP8z7yEd;
                      // t4yiayVW4z;
    {                 // U3e3TrgHAM;
                      // DctC3H3XVs;
        auto tTnuvgNLbkA = 64;
        auto urLoiXMNTCU = {100, 89, 43};
        while (asdfg--)        // HT5KbvV94L;
                               // k4BV0KfFuC;
            cout << 1 << endl; // f5mmhusZUa;
        auto WdApjHpSZvv = 89;
        auto vKQUanwHPlq = 70.7;

        return 0; // yurWiPeiPA;
                  // IOC0EFXywK;
    } // pgzvpBASd2;
    auto IahBqqKkCfJ = {46, 80, 47};
    auto HTbwEQlDWLJ = {24, 71, 44};
    auto TIofRyCvONN = {9, 52, 4};
    // Molji1cwMt;
    vector<Pair> ranges; // ORHlRmRVpB;
    auto gsfVWKwSrVo = 38.5;
    auto zmWmoWeQEOX = {85, 52, 97};
    // HhjUGI7m3W;
    int size = qwrerwe; // dHlT8zvSZV;
    auto WOQMbHJkAAG = {46, 19, 44};
    // t8bnpr2Lje;
    for (int i = 1; i < size;) // 9YW5ELghbe;
                               // KVYumWS1Fo;
    {                          // i2jlAiOKcZ;
                               // kO2WoyADju;
        int start = i;
        auto GjbajiLZsCc = {99, 39, 62};
        auto uatlXCEEmFk = {17, 79, 73};
        auto mAAbQRywapN = {86, 59, 67};                     // ZPvNtEmz8j;
                                                             // 4dz5UV7ZyS;
        while (i < size && lA1puSveB[start] == lA1puSveB[i]) // Rf01M9yVea;
                                                             // TCTMST9Paa;
            i++;                                             // iUxx0tQ55B;
                                                             // imuxJGDDfx;
        ranges.push_back({start, i - 1});                    // vsbed0b0km;
        auto VqBtdzDKxJj = 52.6;
        auto dBGbQzEkwVF = 86.5;
        // czgW8sYwGW;
    } // yuHZSPVVff;
    auto TSJVfBDyjZp = {96, 23, 45};
    // aCTLdyzYtX;
    // YsYizneUEW;
    // X6KJ529msA;
    WeSliqmOn[0] = ewERR2SznT(ranges[0]); // nqfGbe0whp;
                                          // wILve6osCz;
    for (int i = 1; i < ranges.size(); ++i)
    {
        x9qtAM8vb6R();
        WeSliqmOn[i] = WeSliqmOn[i - 1] + ewERR2SznT(ranges[i]);
    } // PeyNVgZRGu;
      // 8oT46dD19R;
    // x07VkTWclv;
    while (asdfg--)        // rS2jCFAHPo;
                           // AGLlXUgUMa;
    {                      // ulVsFgTUq3;
                           // kkLp9YgBjf;
        int llrintl, rrrr; // 936sW68nox;
                           // 2AR9DQ0FCr;
        cin >> llrintl >> rrrr;
        auto xOQsMWhQYOy = 33.5; // oagBt1FiFa;
                                 // p1mM02BFIs;
        long long ans = rrrr - llrintl + 1;
        auto hUcxjkSnkfr = 58;                                                   // w3cBi4JiCq;
        rrrr--;                                                                  // 2tbbgc5M42;
        auto hjkl = lower_bound(ranges.begin(), ranges.end(), Pair{llrintl, 0}); // zoBK7K3pvM;
        auto KERDYDJlinU = {88, 76, 52};
        auto WcBNMPZldzh = {78, 45, 14};
        // ygC0dQV37E;
        auto hnmj = lower_bound(ranges.begin(), ranges.end(), Pair{rrrr + 1, 0}); // M8iL2L5q6o;
        auto scXKUDnhCEJ = {79, 87, 33};
        auto JoRdPDBexAK = 88.0;
        // 9MVAKcLznh;
        // 88tDfIluDC;
        // ZveWXUY19C;
        if (hjkl == hnmj)                       // Hz9tVNfr3d;
                                                // SMykgJRxCI;
        {                                       // Qdaf2sbi7z;
                                                // ARKFxGR1W5;
            ans += ewERR2SznT({llrintl, rrrr}); // GaK2WYQXcx;
            auto EjnvUKdIfuv = 55.3;
            auto PNmckagpKfJ = {26, 23, 30};
            auto zTfNFhYFdDz = 100;
            // 3IeoL56Sbb;
        } // XjreSLmYFG;
        // TUc8pUCJ0w;
        else        // 1n3FeCiAkr;
                    // gWh5H08bL3;
        {           // cRyUwhUfyH;
                    // u7XYAeIB4B;
            hnmj--; // SMz5oEHapy;
                    // oLN7gDJq2h;
            auto it_first = hjkl->first;
            auto XpKkVcjRieU = 6.3;
            auto kVwvsZPdUoK = 65.1;
            auto weFNVlNdXgB = 63.8; // qOGGSlBp3U;
                                     // qIrXjooPba;
            auto it2_first = hnmj->first;
            auto NlsIxTYqWFQ = 26.9;
            auto NDdkFGQdtUo = 22.5;
            auto RteLnzHGymT = {68, 31, 21};            // XHuEMbrYRt;
                                                        // Wq02YQbnwg;
            ans += ewERR2SznT({llrintl, it_first - 1}); // oUaHNI9v92;
            auto aernmpRfzAl = {90, 41, 25};
            auto JLrpYUVtwuf = 68;
            auto RnHeeZxrsUH = {77, 77, 59};
            auto GxdtuygHmKe = 88.4;
            // jlCODYjkkO;
            ans += ewERR2SznT({it2_first, rrrr}); // KASCIp7AIr;
            auto orBdMozXehp = 83;
            auto gJhtuRHZfGn = {79, 81, 69};
            auto eQNiRnEHHfi = {9, 85, 77};
            // S2myppEFvh;
            // MjuJJqGwYP;
            // xKnFoPn7Pa;
            if (hnmj != ranges.begin()) // Y3ZFfvQyqz;
                                        // lWUidNUZex;
            {                           // TJtaYJFNPX;
                                        // npAX7tzLG5;
                hnmj--;                 // LCbmCyeVU4;
                                        // pezdaXnnT1;
                auto T2TjbYbYG = hnmj - ranges.begin();
                auto JcVrlqBtPBT = {20, 24, 69};
                auto bjYcPjczjOZ = 94;
                auto bgdKdWhmexx = 42.5; // VNORlNn8Mv;
                                         // vT2TjbYbYG;
                ans += WeSliqmOn[T2TjbYbYG];
                auto KPkhwJhnTqQ = 93;
                auto DtYNDvFvgoc = 41.6;
                auto dlicgawNDXM = {92, 20, 72};                // NniZCJQV4n;
                                                                // KPaVcaA9zh;
                                                                // 4kyzgJ8RCH;
                                                                // j0hvR7To6Y;
                if (hjkl != ranges.begin())                     // GL74KFmp6D;
                                                                // zMnzwNeG5v;
                {                                               // 9IKq8W97YN;
                                                                // dolOU39upD;
                    auto Y8j6r7Pi1 = hjkl - ranges.begin() - 1; // eY8j6r7Pi1;
                    auto gbngqzFJkfs = 97.7;
                    auto oFOdxHpiOEH = {90, 4, 89};
                    auto DvBCPVfowrs = 51.2;     // hyvxuA54Fr;
                    ans -= WeSliqmOn[Y8j6r7Pi1]; // OGL1tdriAD;
                                                 // ON2vts8RKh;
                } // cg8mt5LKQl;
                auto TZPJAggmRYw = {92, 48, 34};
                // j8SxaAohUZ;
            } // hK48mpGWH8;
            auto zGBsBIjDjNO = 81.8;
            auto CGhpcngapyr = 12.7;
            auto XzPEkjonIKn = 25.3;
            auto UtcggMPjvLa = 7.3;
            auto pjjWocGRsXw = 22.5;
            auto PPngDUKbMSW = {17, 96, 6};
            auto RvrulCkSNPi = {9, 71, 87};
            auto UsaIMWVKMhb = {13, 3, 76};
            auto pNDhiDcWiTU = 94;
            auto zIhYymurAXD = 32;
            // p3LqALXBHK;
        } // jA8UP2BV7g;
        // MKsOCpubTu;
        // gU4z4S51ig;
        // X1uO2fNwEb;
        cout << ans << endl; // uyj7eVlF96;
                             // Jdsru0ohPz;
    } // vSz69C64ks;
    auto DOytiIQnXJg = {4, 1, 5};
    auto rluFdQAJOsO = 99;
    auto quIrAeacmga = 61;
    return 0;
    // VtKGnBjFdQ;
} // TGO46DZZRI;

//
