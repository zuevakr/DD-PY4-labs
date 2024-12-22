# TODO решите задачу
import json

def task() -> float:
    total_product = 0

    file_path = "D:\PyCharm\Course Python английский\Работа с источниками данных\Лабораторная работа\Найти сумму произведений из списка словарей\input.json"
    with open(file_path) as f:
        data = json.load(f)

    for entry in data:
        score = entry.get('score', 0)
        weight = entry.get('weight', 0)

        if score and weight:
            product = score * weight
            total_product += product

    return round(total_product, 3)

result = task()
print(f'{result}')
