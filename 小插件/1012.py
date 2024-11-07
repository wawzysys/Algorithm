from itertools import permutations

# Read input
n, m, q, t = map(int, input().split())
d = list(map(int, input().split()))

# Prepare player data
players = [{'id': 0, 'x': n}]  # Mi Xiaoyou with player ID 0
for i, x in enumerate(d, start=1):
    players.append({'id': i, 'x': x})

# Function to simulate ticket allocation
def simulate(permutation):
    tier1_tickets = m
    tier2_tickets = m
    mi_xiaoyou_got_ticket = False

    for player in permutation:
        x = player['x']
        player_id = player['id']

        if x >= t:
            # Try to allocate Tier 1 ticket
            if tier1_tickets > 0:
                tier1_tickets -= 1
                allocated = True
            # Else try to allocate Tier 2 ticket
            elif tier2_tickets > 0:
                tier2_tickets -= 1
                allocated = True
            else:
                allocated = False
        else:
            # Try to allocate Tier 2 ticket
            if tier2_tickets > 0:
                tier2_tickets -= 1
                allocated = True
            else:
                allocated = False

        # Check if Mi Xiaoyou got a ticket
        if player_id == 0 and allocated:
            mi_xiaoyou_got_ticket = True

    return mi_xiaoyou_got_ticket

MOD = 10**9 + 7
count = 0

# Limit q to prevent excessive computation
if q > 8:
    print("Brute-force method is not practical for q > 8.")
else:
    all_permutations = permutations(players)
    for perm in all_permutations:
        if simulate(perm):
            count += 1

    print(count % MOD)
