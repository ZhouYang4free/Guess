import random

print("欢迎来到猜大小游戏！")
print("我已经想好了一个1到100之间的数字，请你猜猜是多少。")

secret_number = random.randint(1, 100)
guess = None
guess_count = 0


while guess != secret_number:
    guess_count += 1
    guess = input("请猜一个1到100之间的整数: ")
    guess = int(guess)

    if guess < secret_number:
        print("小了，再猜")
    elif guess > secret_number:
        print("大了，再来")
    else:
        print(f"牛逼啊，猜了{guess_count}次猜对了！")
