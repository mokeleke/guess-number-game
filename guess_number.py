import random

def guess_number_game():
    """猜数字游戏 - 1到100之间的数字，7次机会"""
    target = random.randint(1, 100)
    attempts = 7

    print("🎮 猜数字游戏开始了！")
    print(f"我已想好一个 1 到 100 之间的数字。")
    print(f"你有 {attempts} 次机会猜出它！\n")

    while attempts > 0:
        try:
            guess = int(input(f"第 {7 - attempts + 1} 次机会，请输入你的猜测 (1-100): "))

            if guess < 1 or guess > 100:
                print("⚠️ 请输入 1 到 100 之间的数字！")
                continue

            attempts -= 1

            if guess == target:
                print(f"\n🎉 恭喜你猜对了！数字就是 {target}！")
                print(f"你总共用了 {7 - attempts} 次机会。")
                return
            elif guess < target:
                remaining = attempts
                if remaining > 0:
                    print(f"⬆️ 太小了！再试一次。剩余机会: {remaining}")
                else:
                    print("⬆️ 太小了！")
            else:
                remaining = attempts
                if remaining > 0:
                    print(f"⬇️ 太大了！再试一次。剩余机会: {remaining}")
                else:
                    print("⬇️ 太大了！")

        except ValueError:
            print("❌ 请输入有效的数字！")

    print(f"\n😢 游戏结束！你用完了所有 {attempts} 次机会。")
    print(f"正确答案是: {target}")

if __name__ == "__main__":
    guess_number_game()
