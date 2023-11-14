# TODO решите задачу
import json


def task() -> float:
    with open('input.json','r') as file:
        data = json.load(file)
    value = 0
    for dict_ in data:
        value += dict_["score"] * dict_["weight"]
    value = round(value, 3)
    return value
print(task())
