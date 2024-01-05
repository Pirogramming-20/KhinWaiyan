def brGame(player, num):
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
        print(f"{player} : {num}")
        if num >= 31:
            return num
    return num

num = 0
playerList = ["playerA", "playerB"]
curr_player = 0

while num < 31:
    num = brGame(playerList[curr_player], num)
    if num >= 31:
        print(f"{playerList[(curr_player + 1) % 2]} win!")
        break
    curr_player = (curr_player + 1) % 2
