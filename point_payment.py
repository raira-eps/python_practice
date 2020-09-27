card, count = map(int, input().split())
ilist = [int(input()) for i in range(count)]
point = 0
#print(count)
#print(ilist)
for n in ilist:
    s = int(n)
    if point >= s:
        point -= s
    elif point < s:
        card = card - s
        point += s / 10
        point = int(point)

    print(str(card) +" "+ str(point))