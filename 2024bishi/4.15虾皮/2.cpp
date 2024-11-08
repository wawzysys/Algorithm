#include <bits/stdc++.h>

using namespace std;

struct node
{
    int data;
    node *l, *r;
};

node* Build(int len, int a[], int b[])  //建树（模板）
{
    node *root = new node;
    if (len == 0)
        return NULL;

    int i;
    root->data = a[0];
    for (i = 0; i < len; i ++)
        if (b[i] == a[0])
            break;

    root->l = Build(i, a + 1, b);
    root->r = Build(len - i - 1, a + i + 1, b + i + 1);

    return root;
}

void f(node *tree)
{
    queue<node*> q;
    if (tree)
    {
        cout << tree->data;
        q.push(tree);
    }

    while (!q.empty())
    {
        node *root = q.front();
        q.pop();

        if (root->r)   //本来是先root-<l，这里交换一下位置
        {
            cout << ' ' << root->r->data;
            q.push(root->r);
        }
        if (root->l)
        {
            cout << ' ' << root->l->data;
            q.push(root->l);
        }
    }
}

int main()
{
    int n;
    int a[111], b[111];
    cin >> n;

    for (int i = 0; i < n; i ++)
        cin >> a[i];
    for (int i = 0; i < n; i ++)
        cin >> b[i];

    node *tree = new node;
    tree = Build(n, b, a);

    f(tree);    
    return 0;
}
