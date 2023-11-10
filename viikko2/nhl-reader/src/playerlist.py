import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        

    def get_players(self):
        response = requests.get(self.url).json()
        
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        top = [player for player in self.reader.get_players() if player.nationality == nationality]

        return top