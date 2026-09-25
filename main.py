"""
Практична робота №3
Практична атрибуція запозиченого коду.
"""


def insertion_sort(numbers):
    """
    Сортує список чисел за зростанням методом сортування вставками.

    Першоджерело:
    https://github.com/marvincolgin/data-structures-and-algorithms

    Автор оригінального коду: Vin Colgin.
    Ліцензія: MIT License.

    Зміни:
    Алгоритм адаптовано та переписано для цього навчального прикладу.
    Структура функції та документація змінені.
    """

    result = numbers.copy()

    for i in range(1, len(result)):
        current = result[i]
        position = i - 1

        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1

        result[position + 1] = current

    return result


if __name__ == "__main__":
    data = [7, 2, 9, 1, 5, 3]

    print("Початковий масив:", data)
    print("Відсортований масив:", insertion_sort(data))
