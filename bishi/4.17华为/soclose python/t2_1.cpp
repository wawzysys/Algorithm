#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <string>
using namespace std;
int risk_eval(int threshold, vector<vector<string>>& entries) {
    unordered_map<string, string> parent_map;
    unordered_map<string, vector<int>> severity_count;
    unordered_set<string> leaves;
    unordered_set<string> nodes;
    for (auto& entry : entries) {
        string node_id = entry[0];
        string parent_id = entry[1];
        int severity = stoi(entry[2]);
        int count = stoi(entry[3]);
        nodes.insert(node_id);
        severity_count[node_id].resize(2);
        severity_count[node_id][severity] += count;
        if (parent_id != "*") {
            parent_map[node_id] = parent_id;
            nodes.insert(parent_id);
        }

        leaves.insert(node_id);
    }

    for (auto& node : nodes) {
        if (parent_map.find(node) != parent_map.end()) {
            leaves.erase(parent_map[node]);
        }
    }
    for (auto& leaf : leaves) {
        string node = leaf;
        while (parent_map.find(node) != parent_map.end()) {
            string parent = parent_map[node];
            severity_count[parent][0] += severity_count[node][0];
            severity_count[parent][1] += severity_count[node][1];
            node = parent;
        }
    }
    int risky = 0;
    for (auto& node : nodes) {
        if (parent_map.find(node) == parent_map.end()) {  
            int risk_index = 5 * severity_count[node][0] + 2 * severity_count[node][1];
            if (risk_index > threshold) {
                risky++;
            }
        }
    }
    return risky;
}

int main() {
    int threshold, num_entries;
    cin >> threshold >> num_entries;
    vector<vector<string>> data(num_entries, vector<string>(4));

    for (int i = 0; i < num_entries; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> data[i][j];
        }
    }
    cout << risk_eval(threshold, data) << endl;
    return 0;
}
