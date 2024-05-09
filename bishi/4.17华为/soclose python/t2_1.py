from collections import *
#反向建图 从叶子节点
def fun():
    def risk_eval(th, entries):
        import collections
        p_map = {}  
        p_count = defaultdict(lambda: [0, 0])  
        leaves = set()
        nodes = set()
        for n_id, p_id, sev, count in entries:
            sev, count = int(sev), int(count)
            if p_id != "*":
                p_map[n_id] = p_id
                nodes.add(p_id)
            nodes.add(n_id)
            p_count[n_id][sev] += count
            leaves.add(n_id)
        leaves -= {p_map[n] for n in nodes if n in p_map}
        def accumulate(node):
            while node in p_map:
                parent = p_map[node]
                p_count[parent][0] += p_count[node][0]
                p_count[parent][1] += p_count[node][1]
                node = parent
        for leaf in leaves:
            accumulate(leaf)
        risky = 0
        roots = [n for n in nodes if n not in p_map]
        for root in roots:
            risk_index = 5 * p_count[root][0] + 2 * p_count[root][1]
            if risk_index > th:
                risky += 1

        return risky

    th, num_entries = map(int, input().split())
    data = []
    for _ in range(num_entries):
        parts = input().split()
        parts[2], parts[3] = int(parts[2]), int(parts[3])
        data.append(parts)
    risky_services = risk_eval(th, data)
    print(risky_services)   
if __name__ == '__main__':
    fun()