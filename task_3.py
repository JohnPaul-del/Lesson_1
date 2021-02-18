percent1 = [0, 5, 6, 7, 8, 9]
percent2 = [2, 3, 4]

quest = input("Введите число: ")

if int(quest) <= 100:
    if int(quest) > 9 and int(quest[0]) == 1:
        print(quest, "процентов")
    elif int(quest) > 9 and int(quest[1]) in percent1:
        print(quest, "процентов")
    elif int(quest) == 1 or int(quest[1]) == 1:
        print(quest, "процент")
    elif int(quest[0]) or int(quest[1]) in percent2:
        print(quest, "процента")
else:
    print("Не больше 100")
