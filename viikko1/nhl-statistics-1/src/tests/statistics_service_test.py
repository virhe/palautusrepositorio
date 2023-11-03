import unittest
from statistics_service import StatisticsService
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        self.assertEqual(self.stats.search('False'), None)
        self.assertEqual(str(self.stats.search('Semenko')), 'Semenko EDM 4 + 12 = 16')

    def test_team(self):
        self.assertEqual(self.stats.team('False'), [])

    def test_top_points(self):
        two_best = self.stats.top(2)
        first = two_best[0]
        second = two_best[1]

        self.assertEqual(str(first), 'Gretzky EDM 35 + 89 = 124')
        self.assertEqual(str(second), 'Lemieux PIT 45 + 54 = 99')
