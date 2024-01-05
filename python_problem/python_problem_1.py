import random

def brGame(player, num):
    if player == "computer":
        user_input = random.randint(1, 3)
        for i in range(user_input):
            num += 1
            print(f"{player} {num}")
            if num >= 31:
                break
    else:
        while True:
            user_input = input(f"{player}, 부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")
            try:
                user_input = int(user_input)
            except ValueError:
                print("정수를 입력하세요.")
                continue
            if user_input in [1, 2, 3]:
                break
            else:
                print("1,2,3 중 하나를 입력하세요")

        for i in range(user_input):
            num += 1
            print(f"{player} {num}")
            if num >= 31:
                break
    return num

num = 0
playerList = ["computer", "player"]
curr_player = 0

while num < 31:
    num = brGame(playerList[curr_player], num)
    if num >= 31:
        winner = playerList[(curr_player + 1) % 2]
        print(f"{winner} win!")
        break
    curr_player = (curr_player + 1) % 2
