def parse_input(n, m, shots):
    players = []
    for idx, shot_str in enumerate(shots.split()):
        shots = list(map(int, shot_str))
        total_goals = sum(shots)
        longest_streak = 0
        current_streak = 0
        misses = []
        
        for i, shot in enumerate(shots):
            if shot == 1:
                current_streak += 1
            else:
                if current_streak > longest_streak:
                    longest_streak = current_streak
                current_streak = 0
                misses.append(-i)
        
        if current_streak > longest_streak:
            longest_streak = current_streak
        players.append((idx + 1, total_goals, longest_streak, misses))

    return players

def sort_players(players):
    players.sort(key=lambda x: (-x[1], -x[2], x[3], x[0]))
    return [player[0] for player in players]

def main():
    n, m = map(int, input().split())
    input_shots = input()

    players = parse_input(n, m, input_shots)
    sorted_players = sort_players(players)
    print(*sorted_players)

main()
