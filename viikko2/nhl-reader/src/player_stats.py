def sorted_by_points(player):
    return player.goals + player.assists

class PlayerStats:
    def __init__(self, players):
        self.players = players.players

    def top_scorers_by_nationality(self, nat):
        players_by_nationality = filter(lambda player: player.nationality == nat, self.players)
        return sorted(players_by_nationality, reverse=True, key = sorted_by_points)