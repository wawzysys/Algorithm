def fun():
    def calc_risk(th, data):
        from collections import defaultdict
        tr = defaultdict(list)  
        pc = defaultdict(lambda: [0, 0])  
        roots = set() 
        for nd, pr, sev, cnt in data:
            sev, cnt = int(sev), int(cnt)
            if pr == "*":
                roots.add(nd)
            else:
                tr[pr].append(nd)
            pc[nd][sev] += cnt

        def sum_probs(n):
            sv, gn = pc[n]
            for c in tr[n]:
                csv, cgn = sum_probs(c)
                sv += csv
                gn += cgn
            pc[n] = [sv, gn]
            return sv, gn
        for r in roots:
            sum_probs(r)
        risk_count = 0
        for r in roots:
            di = 5 * pc[r][0] + 2 * pc[r][1]
            if di > th:
                risk_count += 1

        return risk_count
    m, n = map(int, input().split())
    data = []
    for _ in range(n):
        parts = input().split()
        parts[2], parts[3] = int(parts[2]), int(parts[3])
        data.append(parts)
    result = calc_risk(m, data)
    print(result)
if __name__ == '__main__':
    fun()