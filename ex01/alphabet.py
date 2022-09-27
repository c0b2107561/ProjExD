import random
import time

num_of_alpha = 26 #全数
num_of_all = 10 #対象数
num_of_abs = 2 #欠損数
num_of_challenge = 2 #チャレンジ数


def shutudai(alphabet):
    all_taisyou = random.sample(alphabet, num_of_all)
    print("対象文字:",end="")
    for c in sorted(all_taisyou):
        print(c,end=" ")
    print()

    kesson = random.sample(all_taisyou, num_of_abs)
    print("表示文字:",end="")
    for c in all_taisyou: 
        if c not in kesson:
            print(c, end=" ")
    print() #デバッグ用に実行する場合は「print("デバッグ用欠損文字:", kesson)」を次行に入れる

    return kesson


def kaito(seikai):
    num=int(input("欠損文字はいくつあるでしょうか？:"))
    if num != num_of_abs:
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
        time_sta = time.time()
        time.sleep(1)
        kesson = shutudai(alphabet)
        ret = kaito(kesson)
        if ret:
            time_end = time.time()
            tim = time_end - time_sta
            print(tim)
            break
        else:
            print("-"*20)
