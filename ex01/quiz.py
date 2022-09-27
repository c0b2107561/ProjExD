import random
import datetime

def shutudai(qa_lst):
    qa = random.choice(qa_lst)
    print("問題:"+qa['q'])
    return qa['a']

def kaito(ans_lst):
    ans = int(input('答えるんだ！:'))
    if ans==ans_lst:
        print('正解！！')
    else:
        print(f"出直してこい")

if __name__ == "__main__":
    qa_lst={
        {'q':'サザエの旦那の名前は？','a':['マスオ','ますお']},
        {'q':'カツオの妹の名前は？','a':['ワカメ','わかめ']},
        {'q':'タラオはカツオから見てどんな関係？','a':['甥','おい','甥っ子','おいっこ']}
}
ans_lst =shutudai(qa_lst)
kaito(ans_lst)