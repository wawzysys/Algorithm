import java.io.*;
import java.util.*;

// 80%^
public class Main {
    // Segment Tree class to handle range maximum queries and point updates
    static class SegmentTree {
        int size;
        char[] tree;

        // Initialize the segment tree with the given data
        public SegmentTree(char[] data) {
            // Find the next power of 2 greater than or equal to data length
            size = 1;
            while (size < data.length)
                size <<= 1;
            tree = new char[2 * size];
            Arrays.fill(tree, 'a'); // Initialize with the smallest character

            // Insert the data into the leaves of the tree
            for (int i = 0; i < data.length; i++) {
                tree[size + i] = data[i];
            }

            // Build the tree by computing the maximum character for each internal node
            for (int i = size - 1; i >= 1; i--) {
                tree[i] = maxChar(tree[2 * i], tree[2 * i + 1]);
            }
        }

        // Update the character at position pos to value
        public void update(int pos, char value) {
            pos += size;
            tree[pos] = value;
            pos >>= 1;
            while (pos >= 1) {
                char left = tree[2 * pos];
                char right = tree[2 * pos + 1];
                char parent = maxChar(left, right);
                if (tree[pos] == parent)
                    break; // No change, can stop
                tree[pos] = parent;
                pos >>= 1;
            }
        }

        // Query the maximum character in the range [l, r] (0-based indices)
        public char queryMax(int l, int r) {
            l += size;
            r += size;
            char res = 'a';
            while (l <= r) {
                if ((l & 1) == 1) {
                    res = maxChar(res, tree[l]);
                    l++;
                }
                if ((r & 1) == 0) {
                    res = maxChar(res, tree[r]);
                    r--;
                }
                l >>= 1;
                r >>= 1;
            }
            return res;
        }

        // Helper method to determine the maximum of two characters
        private char maxChar(char a, char b) {
            return a > b ? a : b;
        }
    }

    public static void main(String[] args) throws IOException {
        // Use BufferedReader for fast input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // Use BufferedWriter or StringBuilder for fast output
        StringBuilder sb = new StringBuilder();
        String line;
        // Read number of test cases
        line = br.readLine();
        if (line == null || line.isEmpty())
            return;
        int T = Integer.parseInt(line.trim());
        for (int testCase = 0; testCase < T; testCase++) {
            // Read n and q
            while ((line = br.readLine()) != null && line.trim().isEmpty()) {
                // Skip empty lines
            }
            if (line == null)
                break;
            String[] nq = line.trim().split("\\s+");
            int n = Integer.parseInt(nq[0]);
            int q = Integer.parseInt(nq[1]);

            // Read string s
            while ((line = br.readLine()) != null && line.trim().isEmpty()) {
                // Skip empty lines
            }
            if (line == null)
                break;
            String sStr = line.trim();
            if (sStr.length() != n) {
                // If string length doesn't match n, adjust accordingly
                while (sStr.length() < n) {
                    String nextPart = br.readLine();
                    if (nextPart == null)
                        break;
                    sStr += nextPart.trim();
                }
            }
            char[] s = sStr.toCharArray();

            // Initialize character position lists
            TreeSet<Integer>[] charPos = new TreeSet[26];
            for (int i = 0; i < 26; i++) {
                charPos[i] = new TreeSet<>();
            }
            for (int i = 0; i < n; i++) {
                char c = s[i];
                charPos[c - 'a'].add(i);
            }

            // Initialize the Segment Tree
            SegmentTree st = new SegmentTree(s);

            // Process q operations
            for (int opIdx = 0; opIdx < q; opIdx++) {
                while ((line = br.readLine()) != null && line.trim().isEmpty()) {
                    // Skip empty lines
                }
                if (line == null)
                    break;
                String[] parts = line.trim().split("\\s+");
                int op = Integer.parseInt(parts[0]);
                if (op == 1) {
                    // Operation 1: Update
                    int i = Integer.parseInt(parts[1]) - 1; // Convert to 0-based index
                    char p = parts[2].charAt(0);
                    char oldChar = s[i];
                    if (oldChar != p) {
                        // Remove from old character's TreeSet
                        charPos[oldChar - 'a'].remove(i);
                        // Add to new character's TreeSet
                        charPos[p - 'a'].add(i);
                        // Update the string
                        s[i] = p;
                        // Update the Segment Tree
                        st.update(i, p);
                    }
                } else if (op == 2) {
                    // Operation 2: Query
                    int l = Integer.parseInt(parts[1]) - 1; // Convert to 0-based index
                    int r = Integer.parseInt(parts[2]) - 1;
                    // Query the maximum character in [l, r]
                    char maxChar = st.queryMax(l, r);
                    int maxCharIdx = maxChar - 'a';
                    TreeSet<Integer> positions = charPos[maxCharIdx];
                    // Find all positions of maxChar within [l, r]
                    NavigableSet<Integer> relevantPositions = positions.subSet(l, true, r, true);
                    if (relevantPositions.isEmpty()) {
                        // No maximum character found in the interval, which shouldn't happen
                        sb.append("0\n");
                        continue;
                    }
                    // Convert NavigableSet to list for easier traversal
                    List<Integer> posList = new ArrayList<>(relevantPositions);
                    // Calculate maximum distance
                    int maxDist = 0;
                    // Distance from l to first position
                    maxDist = Math.max(maxDist, posList.get(0) - l);
                    // Distance from last position to r
                    maxDist = Math.max(maxDist, r - posList.get(posList.size() - 1));
                    // Distance between consecutive positions
                    for (int i = 1; i < posList.size(); i++) {
                        int dist = (posList.get(i) - posList.get(i - 1)) / 2;
                        maxDist = Math.max(maxDist, dist);
                    }
                    sb.append(maxDist).append("\n");
                }
            }
        }
        // Print all outputs at once
        System.out.print(sb.toString());
    }
}
