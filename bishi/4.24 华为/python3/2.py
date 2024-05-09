class Player:
    def __init__(self, player_id):
        self.id = player_id
        self.total_goals = 0
        self.longest_streak = 0
        self.misses = []

    def update_stats(self, goals, streak, misses):
        self.total_goals = goals
        self.longest_streak = streak
        self.misses = misses

def parse_input(n, m, shots):
    players_dict = {}
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
        
        if idx + 1 in players_dict:
            players_dict[idx + 1].update_stats(total_goals, max(longest_streak, players_dict[idx + 1].longest_streak), misses)
        else:
            player = Player(idx + 1)
            player.update_stats(total_goals, longest_streak, misses)
            players_dict[idx + 1] = player

    return players_dict

def sort_players(players_dict):
    sorted_players = sorted(players_dict.items(), key=lambda x: (-x[1].total_goals, -x[1].longest_streak, x[1].misses, x[0]))
    return [player[0] for player in sorted_players]

def main():
    n, m = map(int, input().split())
    input_shots = input()

    players_dict = parse_input(n, m, input_shots)
    sorted_players = sort_players(players_dict)
    print(*sorted_players)







if __name__ == '__main__':
    #t=int(input())
    #for _ in range(t):
    #   solve()

    main()
