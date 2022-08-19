dict1 = {"House": "Loger", "Horse": "Cheval", "Frog": "Grenouille"}
print(f"Ваш словарь: {dict1}")
while True:
    num1 = input("Choose one: / 1:(Добавление данных) 2:(Удаление данных) 3:(Поиск данных) 4:(Замена данных): ")
    if num1 == "1":
        a = input("Enter your new word: ")
        b = input("Enter translate:")
        dict1[a] = b
        print(f"This is your new word: {dict1}")
    if num1 == "2":
        a = input("Enter word that you want delete(remove): ")
        del dict1[a]
        print(f"Remaining words: {dict1}")
    if num1 == "3":
        a = input("Enter word that you want find: ")
        if a in dict1:
            print(f"This is your word: {a}")
        else:
            print("Sorry, but we couldn't find your word")
            break
    if num1 == "4":
        c = input("Enter new place for new word: ")
        d = input("Enter that word: ")
        dict1[c] = d
        print(f"It's what happend {dict1}")
