class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1
    
    def get_even_score(self):
        if self.m_score1 == 0:
            return "Love-All"
        elif self.m_score1 == 1:
            return "Fifteen-All"
        elif self.m_score1 == 2:
            return "Thirty-All"
        else:
            return "Deuce"

    def get_advantage(self):
        minus_result = self.m_score1 - self. m_score2
        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def count_score(self):
        result = self.count_player_score(1)
        return result + self.count_player_score(2)

    def count_player_score(self, player):
        if player == 1:
            return self.score_counter(self.m_score1) + "-"
        else:
            return self.score_counter(self.m_score2)

    def score_counter(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"
    
    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.get_even_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.get_advantage()
        else:
            return self.count_score()

