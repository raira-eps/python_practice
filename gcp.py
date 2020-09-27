#じゃんけんの回数と指の合計本数入力を受け取る→int型に変換
n,f = [int(x) for x in input().split()]
#相手の出す手の入力
hand = input()
#相手がGを出す回数
g = hand.count("G")
#相手がCを出す回数
c = hand.count("C")
#相手がPを出す回数
p = n - g - c

#Pを出せる最大の回数
M_p = f

#最大の勝利数
M_win = 0

#Pの回数
for i in range(M_p + 1):
    #Cの回数
    for j in range(n+1-i):
        #合計の数がℲと等しいとき
        if 5*i + 2*j == f:
            win = min(g,i) + min(p,i) + min (c,n-i-j)
            M_win = max(M_win, win)

print(M_win)