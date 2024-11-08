#include <bits/stdc++.h>
using namespace std;
class A
{
    int a;

public:
    A() : a(0) { cout << "$"; }
    A(int x) : a(x) { cout << "*"; }
    A(A &p) : a(p.a) { cout << "#"; }
    ~A() { cout << "&"; }

    void show() { cout << a; }
};

int main()
{
    A *p1 = new A;
    A *p2 = new A(10);
    A *p3 = new A[3];

    p1->show();
    delete p1;

    p2->show();
    delete p2;

    p3->show();
    delete[] p3;

    return 0;
}
