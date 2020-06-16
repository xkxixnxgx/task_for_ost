# Задача.
# Дан массив целых чисел array и целое число k.
# Нужно вывести все уникальные пары чисел из массива,
# сумма которых равна k.


def search_pairs(array, k):
    # подготавливаем исходные данные
    array = list(set(array))
    array.sort()
    list_result = []
    while len(array) > 0:
        # перебираем элементы массива и подбираем пару
        for i in array:
            j = k - i
            if j in array:
                tuple_result = (i, j)
                list_result.append((tuple_result))
            # удаляем использованные элементы из массива
                array.remove(i)
                array.remove(j)
            else:
                array.remove(i)
    # возвращаем список с результатом
    return list_result


# после запуска скрипта введите в первой строке массив array,
# элементы которого разделены пробелом
# во второй строке введите число k
if __name__ == '__main__':
    array = list(map(int, input().split()))
    k = int(input())
    print(search_pairs(array, k))