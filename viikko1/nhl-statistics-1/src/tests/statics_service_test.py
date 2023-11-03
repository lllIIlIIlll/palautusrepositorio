import unittest
from statistics_service import StatisticsService, SortBy
from statistics_service import sort_by_points
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStaticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_konstruktori_luo_statistics_servicen(self):
        players = self.stats._players
        self.assertEqual(len(players), 5)

    def test_sort_by_points(self):
        sorted_players = sorted(self.stats._players, reverse=True, key=sort_by_points)
        self.assertEqual(sorted_players[0].name, 'Gretzky')

    def test_search_player(self):
        search = self.stats.search('Gretzky')
        self.assertEqual(search.name, 'Gretzky')

    def test_search_player_fail(self):
        search = self.stats.search('jkjkjkj')
        self.assertEqual(search, None)

    def test_team(self):
        team = self.stats.team('PIT')
        self.assertEqual(team[0].name, 'Lemieux')

    def test_top_points(self):
        players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual([players[0].name, players[1].name, players[2].name], ['Gretzky', 'Lemieux', 'Yzerman'])

    def test_top_goals(self):
        players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual([players[0].name, players[1].name, players[2].name], ['Lemieux', 'Yzerman', 'Kurri'])

    def test_top_assists(self):
        players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual([players[0].name, players[1].name, players[2].name], ['Gretzky', 'Yzerman', 'Lemieux'])
   
