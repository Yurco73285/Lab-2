from itertools import count

choice = input("""Виберіть що хочеш: 
1 - Кількість букв в тексті
2 - Сортувати за абеткою
Твій вибір  : """)

ttxDict = []

def countstr(leter):
    d = {}
    for w in leter:
        d[w] = leter.count(w)
    for k in sorted(d):
        print(k + ":" + str(d[k]))


while choice == "1":
    print("Ви обрали обрахувати кількість кожної букви у тексті ")
    ttx = input("""Введіть ваше речення  : 
        """).replace('%', '').replace('$', '').replace('@', '').replace('*', '').replace('.', '').replace('!',
                                                                                                          '').replace(
        '&', '').replace('#', '').replace('^','').replace(';', '').replace('(', '').replace(')', '').replace(' ','').replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','').strip()
    countstr(ttx)
    print("Програма виконана свою роботу! ")
    print("Щоб продовжити натисніть - 1")
    print("Для виходу натисніть  - 2")
    choice2 = input("Ваш вибір : ")
    if choice2 == "2":
        break
    if choice2 == "1":
        choice == "1"
    else:
        print("Я БАЧУ ТИ ХАЦКЕР")
while choice == "2":
    print("Ви обрали посортувати слова в словниковому порядку")
    ttx = input("""Введіть ваше речення  : 
    """).replace('%', '').replace('$', '').replace('@', '').replace('*', '').replace('.', '').replace('!', '').replace(
        '&', '').replace('#', '').replace(';', '').replace('(', '').replace(')', '').replace('№','').replace('^','').replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')
    ttx = ttx
    ttx = ttx.split()
    ttxDict = dict.fromkeys(ttx, 1)
    ttxDict = sorted(ttxDict)
    print(ttxDict)
    print("Програма виконана свою роботу!")
    print("Щоб продовжити натисніть - 1")
    print("Для виходу натисніть - 2")
    choice3 = input("Ваш вибір : ")
    if choice3 == "2":
        break
    if choice3 == "1":
        choice == "B"
    else:
        print("Я БАЧУ ТИ ЖОСТКИЙ!!! ")
