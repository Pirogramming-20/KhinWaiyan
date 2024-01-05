num = 0
player_names = ["playerA", "playerB"]
current_player = 0

while num < 31:

    while True:
        user_input = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")
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
        print(f"{player_names[current_player]} : {num}")
        if num >= 31:
            break
    current_player = (current_player + 1) % 2