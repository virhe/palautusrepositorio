
class TennisGame:
    def __init__(self, player1_name: str, player2_name: str) -> None:
        self.player1_name: str = player1_name
        self.player2_name: str = player2_name
        self.player1_score: int = 0
        self.player2_score: int = 0

    def won_point(self, player_name: str) -> None:
        if player_name == "player1":
            self.player1_score = self.player1_score + 1

        else:
            self.player2_score = self.player2_score + 1

    def get_score(self) -> str: 
        score: str = ""
        temp_score: int = 0

        if self.player1_score == self.player2_score:
            match self.player1_score:
                case 0:
                    score = "Love-All"
                case 1:
                    score = "Fifteen-All"
                case 2:
                    score = "Thirty-All"
                case _:
                    score = "Deuce"

        elif self.player1_score >= 4 or self.player2_score >= 4:
            minus_result: int = self.player1_score - self.player2_score

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"

        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_score
                else:
                    score = score + "-"
                    temp_score = self.player2_score

                match temp_score:
                    case 0:
                        score = score + "Love"
                    case 1:
                        score = score + "Fifteen"
                    case 2:
                        score = score + "Thirty"
                    case 3:
                        score = score + "Forty"

        return score
