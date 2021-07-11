"""
This is a simple two-player Rock-Paper-Scissors game. (Hint: Ask for player
plays (using input), compare them, print out a message of congratulations
to the winner, and ask if the players want to start a new game)
Remember the rules:
●	Rock beats scissors
●	Scissors beats paper
●	Paper beats rock
"""

class Rock_paper_scissors:

    def __init__(self, name_user1, name_user2):
        self.name_user1 = name_user1
        self.name_user2 = name_user2
        self.input_set = ["r", "p", "s"]
        self.input_set_opp = ["s", "r", "p"]
        self.user1_score = 0
        self.user2_score = 0

    def score(self, user_1, user_2):
        cond_1 = (user_1 == self.input_set[0] and user_2 == self.input_set_opp[0])
        cond_2 = (user_1 == self.input_set[1] and user_2 == self.input_set_opp[1])
        cond_3 = (user_1 == self.input_set[2] and user_2 == self.input_set_opp[2])
        cond_4 = (user_1 == user_2)
        if cond_1 or cond_2 or cond_3:
            self.user1_score += 1
            print(self.name_user1, "wins !!!")
        elif cond_4:
            print("OOPS it was a tie!!!")
        else:
            self.user2_score += 1
            print(self.name_user2, "wins !!!")

    def score_dis(self):
        print("\n Final Score Board: ")
        print(self.name_user1, ":", self.user1_score)
        print(self.name_user2, ":", self.user2_score)
        if self.user1_score > self.user2_score:
            print(self.name_user1, "is the CHAMPION !!!")
        elif self.user2_score > self.user1_score:
            print(self.name_user2, "is the CHAMPION !!!")
        else:
            print("OOPS the match was a tie !!! Better Luck next time for both!!!")

# Main Loop:
def user_details():
    name_user1 = input("User1 Please enter your name: ")
    name_user2 = input("User2 Please enter your name: ")
    game_start = Rock_paper_scissors(name_user1, name_user2)
    return game_start

game = user_details()

def user_input():
    user1_input = input("Input User1(r, p, s): ")
    user2_input = input("Input user2(r, p, s): ")
    input_set = ["r", "p", "s"]
    if user1_input in input_set and user2_input in input_set:
        game.score(user1_input, user2_input)
    else:
        print("Invalid Input, Please try again!!")
        pass

while True:
    user_input()
    Ans = input("Do you want to continue? (y/n): ")
    if Ans == "n":
        game.score_dis()
        break


