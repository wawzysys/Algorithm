# E:\0Code\Algorithm\bishi\wangyi\2_1.py 2024-08-17 by 777
import sys

sys.setrecursionlimit(100000)
input = lambda: sys.stdin.readline().strip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))


def find_violations(master_relationships, romantic_relationships):
    master_to_disciples = {}
    disciple_to_master = {}

    for i in range(0, len(master_relationships), 2):
        master = master_relationships[i]
        disciple = master_relationships[i + 1]
        if master not in master_to_disciples:
            master_to_disciples[master] = []
        master_to_disciples[master].append(disciple)
        disciple_to_master[disciple] = master
    romantic_pairs = []
    for i in range(0, len(romantic_relationships), 2):
        romantic_pairs.append(
            (romantic_relationships[i], romantic_relationships[i + 1]))

    def find_generational_link(person, generations):
        links = set()
        queue = [(person, 0)]
        while queue:
            current, gen = queue.pop(0)
            if gen < generations:
                if current in disciple_to_master:
                    master = disciple_to_master[current]
                    links.add(master)
                    queue.append((master, gen + 1))
        return links

    violations = set()
    for p1, p2 in romantic_pairs:

        links_p1 = find_generational_link(p1, 3)
        links_p2 = find_generational_link(p2, 3)

        if p1 in links_p2 or p2 in links_p1:
            violations.add(p1)
            violations.add(p2)
    return sorted(list(violations))


m = sint()
master_relationships = lint()
n = sint()
romantic_relationships = lint()
violations = find_violations(master_relationships, romantic_relationships)
print(*violations)
