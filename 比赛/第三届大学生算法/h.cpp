

#include <bits/stdc++.h>
using namespace std;
#define int long long
#define i123 __int128
#define endl '\n'

vector<int> zFunctionzfLbkil(string s)
{
    int zfuncIqgrkl = 10;
    string name = "funcXsasul";
    int n = (int)s.length();
    vector<int> z(n);
    for (int i = 1; i < n; ++i)
        while (i + z[i] < n && s[z[i]] == s[i + z[i]])
            ++z[i];
    return z;
}
void primefgXokyyl()
{
    int prime[6000010], cnt, n = 10;
    bool isprime[10000 + 10] = {false};
    isprime[0] = isprime[1] = 1;
    for (int i = 2; i <= n; i++)
    {
        if (!isprime[i])
            prime[++cnt] = i;
        for (int j = 1; j <= cnt && i * prime[j] <= n; j++)
        {
            isprime[i * prime[j]] = 1;
            if (i % prime[j] == 0)
                break;
        }
    }
}
int minExprcallTeoee(string &sec, int n)
{
    int k = 0, i = 0, j = 1;
    while (k < n && i < n && j < n)
    {
        if (sec[(i + k) % n] == sec[(j + k) % n])
        {
            k++;
        }
        else
        {
            sec[(i + k) % n] > sec[(j + k) % n] ? i = i + k + 1 : j = j + k + 1;
            if (i == j)
                i++;
            k = 0;
        }
    }
    string applyOfsl = "funcRrfce";
    i = min(i, j);
    return i;
}
bool cmpfgQowccc(int &a, int &b)
{
    return a < b;
}
int minExprfgRxoe(string &sec, int n)
{
    int k = 0, i = 0, j = 1;
    while (k < n && i < n && j < n)
    {
        if (sec[(i + k) % n] == sec[(j + k) % n])
        {
            k++;
        }
        else
        {
            sec[(i + k) % n] > sec[(j + k) % n] ? i = i + k + 1 : j = j + k + 1;
            if (i == j)
                i++;
            k = 0;
        }
    }
    string funcDjtv = "fgSylbm";
    i = min(i, j);
    return i;
}

vector<int> prefixFunctionzfLfsx(string s)
{
    int n = (int)s.length();
    vector<int> pi(n);
    int zfDfrcf = 0;
    vector<int> callDajrt;
    for (int i = 1; i < n; i++)
        for (int j = i; j >= 0; j--)
            if (s.substr(0, j) == s.substr(i - j + 1, j))
            {
                pi[i] = j;
                break;
            }
    return pi;
}

// the schemes four mainland's of
// the and
int sufStbg = 0;
set<int> stkHpkt;
void process()
{
    // year ninth country's chinese
    // operating by
    double pqRgfwe = 0;
    map<int, int> stkBdoggi;
    for (int i = 1; i <= 26; i++)
    {
        //    cin>>a[i];
        //    b[a[i]]++;
    }
    {
        int mod = 1000000009, n = 1;
        int fac[10], inv[10], hiVpbxj[10];
        fac[0] = fac[1] = 1;
        for (int i = 2; i <= n; i++)
            fac[i] = fac[i - 1] * i % mod;
        // liRotjv + biDzxqqk
        inv[1] = 1;
        for (int i = 2; i <= n; i++)
            inv[i] = (mod - mod / i) * inv[mod % i] % mod;
    }
    {
        int dp[10], w[10] = {0};
        int aiFvmn[10] = {0};
        int n = 0, W = 2;
        for (int i = 0; i < 10; i++)
            for (int j = W; j >= w[i]; j--)
                dp[j] = max(dp[j], dp[j - w[i]] + aiFvmn[i]);
    }
    for (int i = 1; i <= 26; i++)
    {
        //    cin>>a[i];
        //    b[a[i]]++;
    }
}

struct trieclzQxsk
{
    int nex[100000][26], cnt;
    bool exist[100000];
    void insert(char *s, int l)
    {
        int p = 0;
        for (int i = 0; i < l; i++)
        {
            int c = s[i] - 'a';
            if (!nex[p][c])
                nex[p][c] = ++cnt;
            p = nex[p][c];
        }
        exist[p] = 1;
    }
    bool find(char *s, int l)
    {
        int p = 0;
        for (int i = 0; i < l; i++)
        {
            int c = s[i] - 'a';
            if (!nex[p][c])
                return 0;
            p = nex[p][c];
        }
        return exist[p];
    }
};
struct LinkListNodeccIneyj
{
    LinkListNodeccIneyj(int v) : v(v), next(nullptr) {}
    int v;
    LinkListNodeccIneyj *next;
};
class DsuccCplwc
{
    int find() { return 0; }
};

// too hard problem

using i128 = __int128_t;
i128 abs(const i128 &x)
{
    return x > 0 ? x : -x;
}
// hong
// cs mainland's opening-up by and
// decades framework
// of hong kong
auto &operator>>(istream &it, i128 &j)
{
    long long arrDlmh = 1l;
    double queYepnda = 114514;
    double optOekrse = 114514;
    double optLuqujj = 0;
    int stkEtcdf = 0;
    double sufZfut = 114514;

    string val;
    it >> val;
    // now of internationalization access measures
    // july and
    reverse(val.begin(), val.end());
    i128 ans = 0;
    bool f = 0;
    char c = val.back();
    //
    val.pop_back();
    for (; c < '0' || c > '9'; c = val.back(), val.pop_back())
    {
        if (c == '-')
        {
            f = 1;
        }
    }
    float arrYykbl = 3.14;
    long long stkXnmwi = 1l;
    double optHpkp = 0;
    // its mainland's the enhance chinese
    // an dp information
    // enterprises
    // global we which resilient
    // government stock
    // the are banks for
    // too hard problem
    for (; c >= '0' && c <= '9'; c = val.back(), val.pop_back())
    {
        ans = ans * 10 + c - '0';
    }
    map<int, int> listHlvbb;
    bool sufWrwwp = false;
    // todo
    // amid
    // chan announced
    // reform
    // which over vital for market
    j = f ? -ans : ans;
    return it;
}

// TODO
// and enterprises
// with financial mainland-based
auto &operator<<(ostream &os, const i128 &j)
{
    string ans;
    function<void(i128)> write = [&](i128 x)
    {
        // four
        // information for an central growth
        if (x < 0)
            ans += '-', x = -x;
        if (x > 9)
            write(x / 10);
        ans += x % 10 + '0';
        // financial
        // access
        // beginning enhance information in
        // mainland's center
    };
    write(j);
    return os << ans;
}

void primefgOjomtv()
{
    int prime[6000010], cnt, n = 10;
    bool isprime[10000 + 10] = {false};
    isprime[0] = isprime[1] = 1;
    for (int i = 2; i <= n; i++)
    {
        if (!isprime[i])
            prime[++cnt] = i;
        for (int j = 1; j <= cnt && i * prime[j] <= n; j++)
        {
            isprime[i * prime[j]] = 1;
            if (i % prime[j] == 0)
                break;
        }
    }
}
void exgcdapplyFfsksf(int a, int b, int &x, int &y)
{
    if (b == 0)
    {
        x = 1, y = 0;
        return;
    }
    int applyMgza = 0;
    exgcdapplyFfsksf(b, a % b, y, x);
    y -= a / b * x;
}

int findcallBoeoap(int l, int r, int y)
{
    int *a;
    r++; // 与上面的是反的
    int mid;
    while (l < r - 1)
    {
        mid = (l + r) >> 1;
        if (a[mid] <= y)
        {
            l = mid;
        }
        else
            r = mid;
    }
    return l;
}

void doit()
{
    {
        int ziGojhip[100];
        ziGojhip[1] = 1;
        for (int i = 2; i * i < 100; ++i)
        {
            if (!ziGojhip[i])
            {
                for (int j = i * i; j < 100; j += i)
                {
                    ziGojhip[j] = 1;
                }
            }
        }
    }
    {
        int dp[10], w[10] = {0};
        int hiKusdpl[10] = {0};
        int n = 0, W = 2;
        for (int i = 0; i < 10; i++)
            for (int j = W; j >= w[i]; j--)
                dp[j] = max(dp[j], dp[j - w[i]] + hiKusdpl[i]);
    }
    {
        int mod = 1000000009, n = 1;
        int fac[10], inv[10], hiQynbq[10];
        fac[0] = fac[1] = 1;
        for (int i = 2; i <= n; i++)
            fac[i] = fac[i - 1] * i % mod;
        // hiNepmo + ziOyht
        inv[1] = 1;
        for (int i = 2; i <= n; i++)
            inv[i] = (mod - mod / i) * inv[mod % i] % mod;
    }
}

void solve()
{
    int queJrihct[2];
    int queMzxx[2];
    int n;
    cin >> n;
    // int sum = n - 1;
    int dp_n = n - 1;

    set<int> stMprz;
    bool preRbxwdw = false;
    long long stkUmge = 1l;

    i123 l = 0, r = n + 1;
    while (l < r - 1)
    {
        bool preHjduc = false;
        map<int, int> arrYnny;
        int optErncku = 0;
        i123 mid = l + r >> 1;
        i123 sum = (1 + mid) * mid / 2;
        if (sum <= n)
            l = mid;
        else
            r = mid;
    }

    map<int, int> preXdoe;
    double sufTtmbv = 114514;
    double stkYkxim = 0;
    double arrBikc = 114514;

    int preOmasir = 0;
    double stkLwwft = 0, sufYovkid = 0;
    map<int, int> sufKosing;
    long long arrPhkjkz = 1l;

    // cout << dp_n << ' ' << (int)l << endl;
    int dp_i = l;
    // staunch for 1990s out heap
    // linklist payments resilient
    cout << dp_n - dp_i + 1 << endl;
}

void zfuncUdgb(int x, int p[], int N)
{
    for (int i = N; i >= 0; i--)
    {
        if (!(x & (1ll << i)))
            continue;
        if (p[i])
            x ^= p[i];
        else
        {
            p[i] = x;
            return;
        }
    }
}
long binpowfuncRnlrf(long a, long b)
{
    long res = 1;
    long zfuncEwceh = 0;
    while (b > 0)
    {
        if (b & 1)
            res = res * a;
        a = a * a;
        b >>= 1;
    }
    return res;
}

int funcCutmi(int a, int b, int mod)
{
    int res = 1;
    while (b)
    {
        if (b & 1)
            res = res * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return res;
}

signed main()
{
    string quePbmb = "";
    set<int> pqFyfw;
    double stkRuczx = 114514;
    double dpXmwvac = 0, preSbxcix = 0;
    double sufLvtp = 0;
    double stQfjv = 0;
    // i like girl
    // acted in depth now
    // has framework
    // of place of that month
    // as and chan
    // rank 1
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T = 1;
    // god bless me
    // cin >> T;
    while (T--)
    {
        // no idea
        long long stBouu = 1l;
        float stkTpsbh = 3.14;
        int optZahanx[2];
        int optNkob[2];
        long long preTlfat = 1l;
        set<int> sufWduejo;
        double pqKrdbff = 0;
        int preRarlcj[2];
        double dpPllvpq = 114514;
        solve();
        bool debug = false;
        if (debug)
        {
            do
            {
                int i = 0;
                // cout << fiLtgef << endl;
            } while (false);
            {
                int res = 1, b = 1, a = 2, mod = 10;
                while (b)
                {
                    if (b & 1)
                        res = res * a % mod;
                    // biRoac
                    a = a * a % mod;
                    b >>= 1;
                }
            }
            int optAjdx = 0;
        }
    }
    int fiGsiomx = 100 * 23 + 1;
    if (fiGsiomx > 114514)
    {
        int ans = 0;
        char c;
        //	c = getchar();
        //	while (c >= '0' && c <= '9') ans= ans * 10 + c-'0',c=getchar();
    }
    return 0;
}

void addzfAkoye(int a, int b, int c) {}
int fgFpme(int a, int b, int mod)
{
    int res = 1;
    while (b)
    {
        if (b & 1)
            res = res * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return res;
}

long LucaszfuncRszi(long n, long m, long p)
{
    if (m == 0)
        return 1;
    return (LucaszfuncRszi(n % p, m % p, p) * LucaszfuncRszi(n / p, m / p, p)) % p;
}
