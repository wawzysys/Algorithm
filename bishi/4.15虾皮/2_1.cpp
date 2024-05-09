
class Solution {
    int n, a[10001], b[10001];
    struct node{
        int data;
        node *l, *r;
    };
    vector<int> ans;

    node* Build(int len, int a[], int b[]){
        node *root = new node;
        if(len == 0)
        return NULL;

        int i;
        root -> data = a[0];
        for(i= 0; i<len; i++)
            if(b[i]==a[0])
                break;
        
        root->l = Build(i, a+1, b);
        root->r = Build(len-i-1, a+i+1, b+i+1);

        return root;
    }

    void f(node *tree){
        queue<node*> q;
        if(tree){
            cout<<tree->data;
            // ans.push_back(tree->data)
            q.push(tree);
        }
        while (!q.empty()){
            node *root = q.front();
            q.pop();
            if(root->l){
                ans.push_back(root->l->data);
                q.push(root->l);
            }
            if(root->r){
                ans.push_back(root->r->data);
                q.push(root->r);
            }
        }
    }


public:
    /**
     * Note: 类名、方法名、参数名已经指定，请勿修改
     *
     * 
     * 层序打印二叉树
     * @param pre int整型 vector 前序遍历数组
     * @param mid int整型 vector 中序遍历数组
     * @return int整型vector
     */
    vector<int> levelPrintTree(vector<int>& pre, vector<int>& mid) {
        // write code here
        n = pre.size();
        ans.clear();
        for(int i=0; i<n; i++){
            b[i] = pre[i];
        }
        for(int i=0; i<n; i++){
            a[i] = mid[i];
        }
        node *tree = new node;
        tree = Build(n, b, a);
        f(tree);
        return ans;
    }
};
