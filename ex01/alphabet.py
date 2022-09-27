import random
import datetime
from xml.dom.minidom import parseString

num_of_alpha= 26
num_of_all_chars = 10
num_of_abs_chars = 2
num_of_challenge = 2


def shutudai(alphabet):
    all_chars = random.sample(alphabet, num_of_all_chars)
    print("対象文字:",end="")
    for c in sorted(all_chars):
        print(c,end=" ")
    print()
    abc_chars = random.sample(all_chars, num_of_abs_chars)
    print("表示文字:",end="")
    for c in all_chars: 
        if c not in all_chars:
            print(c,end=" ")
    print()
    print("デバッグ用欠損文字:", abc_chars)
    pass


def kaito():
    parseString

if __name__ == "__main__":
    alphabet = [chr(i+65) for i in range(num_of_alpha)]
    shutudai(alphabet)