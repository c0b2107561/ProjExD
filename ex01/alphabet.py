import random
import datetime

num_of_alpha= 26 #全数
num_of_all_chars = 10 #対象数
num_of_abs_chars = 2 #欠損数
num_of_challenge = 2 #チャレンジ数


def shutudai(alphabet):
    all_chars = random.sample(alphabet, num_of_all_chars)
    print("対象文字:",end="")
    for c in sorted(all_chars):
        print(c,end=" ")
    print()

    abs_chars = random.sample(all_chars, num_of_abs_chars)
    print("表示文字:",end="")
    for c in all_chars: 
        if c not in abs_chars:
            print(c, end=" ")
    print()
    print("デバッグ用欠損文字:", abs_chars)
    return abs_chars


def kaito(seikai):
    num=int(input("欠損文字はいくつあるでしょうか？:"))
    if num != num_of_abs_chars:
        print("不正解です")
    else:
        print("正解です。それでは、具体的に欠損文字一つずつ入力してください")
        for i in range(num):
            c=input(f"{i+1}つ目の文字を入力してください:")
            if c not in seikai:
                print("不正解です。またチャレンジしてください")
                return False
            else:
                seikai.remove(c)
        else: 
            print("パーフェクトです！")
            return True
    return False

if __name__ == "__main__":
    alphabet = [chr(i+65) for i in range(num_of_alpha)]
    #shutudai(alphabet)
    for _ in range(num_of_challenge):
        abs_chars = shutudai(alphabet)
        ret = kaito(abs_chars)
        if ret:
            break
        else:
            print("-"*20)
