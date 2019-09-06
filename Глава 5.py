# Поиск по хэш-таблице

voted = {}


def check_voter(name):
    if voted.get(name):
        print("Выгнать его!")
    else:
        voted[name] = True
        print("Дать ему проголосовать")


check_voter("Tom")
check_voter("Ivan")
check_voter("Tom")
print(voted)
