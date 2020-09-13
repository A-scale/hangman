#ハングマンというゲームを作る。

#答えのリストを作る。
answer = ['happy', 'oppappy', 'great', 'nice', 'humberger']

import random

#変数hangman(word)を作る。
#wordは当てる単語。wrondプレイヤーが間違えた数。
#stagesは間違えるごとに描かれる絵のリスト。
#rlettersはwordを一文字ずつに分解したリスト。
#boardはwordの文字数だけ_で表示する変数。

def hangman(word):
    wrong = 0
    stages = ['',
              '_______',
              '|                  ',
              '|      |',
              '|       0',
              '|      /|＼',
              '|       /＼',
              ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('ハングマンへようこそ')

#ハングマンが描かれ終わるまでループする。
#msgは入力してもらった文字。一つ目のif文でその文字が合っているか判別する。
#二つ目のif文で勝敗判定を行う。
    while wrong < len(stages) - 1:
        print("\n")
        msg = input('一文字を予想してね：')
        
        if msg in rletters:
            cind = rletters.index(msg)
            board[cind] = msg
            rletters[cind] = '$'
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        
        if '_' not in board:
            print('\nあなたの勝ち')
            print(' '.join(board))
            win = True
            break

#負けた人へのメッセージ
    if wrong == len(stages) - 1:
        print('あーあ、吊られちゃった……\nバイバイ')

def hangman2():
    word = answer[random.randint(0, 5)]
    hangman(word)

hangman2()
