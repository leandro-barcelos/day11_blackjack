import random
import sys
from os import system, name


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class BlackJack:
    def __init__(self):
        self.CARDS = [
            'A', 'A', 'A', 'A',
            2, 2, 2, 2,
            3, 3, 3, 3,
            4, 4, 4, 4,
            5, 5, 5, 5,
            6, 6, 6, 6,
            7, 7, 7, 7,
            8, 8, 8, 8,
            9, 9, 9, 9,
            10, 10, 10, 10,
            'Q', 'Q', 'Q', 'Q',
            'J', 'J', 'J', 'J',
            'K', 'K', 'K', 'K'
        ]

        self.LOGO = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      `------'                           |__/
      """
        self.player_hand = []
        self.player_score = 0
        self.comp_hand = [self.CARDS[random.randint(0, 51)]]
        self.comp_score = 0

    def want_play(self):
        self.player_hand = []
        self.player_score = 0
        self.comp_hand = [self.CARDS[random.randint(0, 51)]]
        self.comp_score = 0
        check_play = input("Do you want to play a game of black jack? y/n ")
        if check_play != "y":
            sys.exit()

    def not_used(self):
        self.comp_score = self.comp_score

    def first_hand(self):
        for i in range(0, 2):
            self.player_hand.append(self.CARDS[random.randint(0, 51)])

    def calc_score(self, hand):
        self.not_used()
        score = 0
        for card in hand:
            if card == 'A':
                score += 1
            elif type(card) == str:
                score += 10
            else:
                score += card
        return score

    def hit(self):
        self.player_hand.append(self.CARDS[random.randint(0, 51)])
        self.player_score = self.calc_score(self.player_hand)
        print(f"Your cards: {self.player_hand}, current score: {self.player_score}\nComputer's"
              f" first card: {self.comp_hand[0]}")
        if self.player_score == 21:
            self.win()

    def check_over(self):
        if self.player_score > 21:
            self.lose()
        elif self.comp_score > 21:
            self.win()

    def pass_(self):
        self.comp_hand.append(self.CARDS[random.randint(0, 51)])
        score = self.calc_score(self.comp_hand)
        while score <= self.player_score:
            self.comp_hand.append(self.CARDS[random.randint(0, 51)])
            score = self.calc_score(self.comp_hand)

    def win(self):
        print("You win 🤩")
        self.bj_game()

    def lose(self):
        print("You lose 😤")
        self.bj_game()

    def bj_game(self):
        self.want_play()
        clear()
        print(self.LOGO)
        self.first_hand()
        self.player_score = self.calc_score(self.player_hand)
        self.comp_score = self.calc_score(self.comp_hand)
        print(f"Your cards: {self.player_hand}, current score: {self.player_score}\n"
              f"Computer's first card: {self.comp_hand[0]}, score: {self.comp_score}")
        win_loss = True

        while win_loss:
            action = input("Type 'y' to get another card, type 'n' to pass: ")
            if action == 'y':
                self.hit()
                self.check_over()
            elif action == 'n':
                self.pass_()
                self.comp_score = self.calc_score(self.comp_hand)
                print(f"Your cards: {self.player_hand}, score: {self.player_score}\n"
                      f"Computer's final cards: {self.comp_hand}, score: {self.comp_score}")
                self.check_over()
                if self.player_score > self.comp_score:
                    self.win()
                elif self.player_score == self.comp_score:
                    print("Tie")
                    self.bj_game()
                else:
                    self.lose()
            else:
                print("Invalid input!!")
                continue


game = BlackJack()
game.bj_game()
