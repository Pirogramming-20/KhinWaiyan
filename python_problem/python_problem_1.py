num = 0
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