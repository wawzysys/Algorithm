#include <bits/stdc++.h>
using namespace std;

class B;

class A
{
public:
    A() { cout << "*"; }
    ~A() { cout << "#"; }
    shared_ptr<B> p1;
};

class B
{
public:
    B() { cout << "$"; }
    ~B() { cout << "&"; }
    shared_ptr<A> p2;
};

void f()
{
    shared_ptr<A> pa(new A());
    shared_ptr<B> pb(new B());

    cout << pa.use_count();

    shared_ptr<A> pc = pa;
    cout << pa.use_count();
    cout << pb.use_count();
}

int main()
{
    f();
    return 0;
}
