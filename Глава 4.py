# "Разделяй и влавствуй"


def sum(list):
    if not list:
        return 0
    return list[0] + sum(list[1:])


def count(list):
    if not list:
        return 0
    return 1 + count(list[1:])


def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max


arr = [1, 4, 6, 3]
print(sum(arr))
print(count(arr))
print(max(arr))
