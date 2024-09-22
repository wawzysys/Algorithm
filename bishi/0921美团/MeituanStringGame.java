import java.io.*;
import java.util.*;

// 0%
public class MeituanStringGame {
    static class SegmentTree {
        int n;
        char[] data;
        char[] tree;

        public SegmentTree(char[] data) {
            this.n = data.length;
            this.data = data;
            this.tree = new char[4 * n];
            build(1, 0, n - 1);
        }

        void build(int node, int l, int r) {
            if (l == r) {
                tree[node] = data[l];
            } else {
                int mid = (l + r) / 2;
                build(2 * node, l, mid);
                build(2 * node + 1, mid + 1, r);
                tree[node] = (char) Math.max(tree[2 * node], tree[2 * node + 1]);
            }
        }

        void update(int node, int l, int r, int idx, char val) {
            if (l == r) {
                tree[node] = val;
                data[idx] = val;
            } else {
                int mid = (l + r) / 2;
                if (idx <= mid) {
                    update(2 * node, l, mid, idx, val);
                } else {
                    update(2 * node + 1, mid + 1, r, idx, val);
                }
                tree[node] = (char) Math.max(tree[2 * node], tree[2 * node + 1]);
            }
        }

        char query(int node, int l, int r, int ql, int qr) {
            if (ql > r || qr < l)
                return 'a' - 1;
            if (ql <= l && r <= qr)
                return tree[node];
            int mid = (l + r) / 2;
            char left = query(2 * node, l, mid, ql, qr);
            char right = query(2 * node + 1, mid + 1, r, ql, qr);
            return (char) Math.max(left, right);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            String[] parts = br.readLine().split(" ");
            int n = Integer.parseInt(parts[0]);
            int q = Integer.parseInt(parts[1]);
            char[] s = br.readLine().toCharArray();

            SegmentTree segTree = new SegmentTree(s);

            TreeSet<Integer>[] charPositions = new TreeSet[26];
            for (int i = 0; i < 26; i++) {
                charPositions[i] = new TreeSet<>();
            }
            for (int i = 0; i < n; i++) {
                charPositions[s[i] - 'a'].add(i);
            }

            for (int i = 0; i < q; i++) {
                String line = br.readLine();
                parts = line.split(" ");
                int op = Integer.parseInt(parts[0]);
                if (op == 1) {
                    int idx = Integer.parseInt(parts[1]) - 1;
                    char p = parts[2].charAt(0);
                    char oldChar = s[idx];
                    charPositions[oldChar - 'a'].remove(idx);
                    charPositions[p - 'a'].add(idx);
                    segTree.update(1, 0, n - 1, idx, p);
                } else if (op == 2) {
                    int l = Integer.parseInt(parts[1]) - 1;
                    int r = Integer.parseInt(parts[2]) - 1;
                    char c = segTree.query(1, 0, n - 1, l, r);
                    int cIndex = c - 'a';
                    Integer minPos = charPositions[cIndex].ceiling(l);
                    Integer maxPos = charPositions[cIndex].floor(r);
                    int maxDistance = 0;
                    if (minPos != null) {
                        maxDistance = Math.max(minPos - l, r - maxPos);
                    }
                    int units = 0;
                    int dist = maxDistance + 1;
                    while ((1 << units) < dist) {
                        units++;
                    }
                    out.println(units);
                }
            }
        }
        out.flush();
        out.close();
    }
}
