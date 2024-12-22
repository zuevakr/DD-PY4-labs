# TODO импортировать необходимые молули

import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    json_string = json.dumps(data, indent=4)  # TODO Сериализовать в файл с отступами равными 4

    with open(OUTPUT_FILENAME, 'w') as output_file:
        output_file.write(json_string)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
