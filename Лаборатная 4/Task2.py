import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as file:
        str_list = [str_ for str_ in csv.DictReader(file)]

    with open(OUTPUT_FILENAME, "w") as file:
        json.dump(str_list, file, indent=4)





if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
