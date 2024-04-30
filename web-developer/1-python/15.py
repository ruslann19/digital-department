import json

def mean_age(json_string):
    people = json.loads(json_string)
    general_age = 0
    for person in people:
        general_age += person["age"]
    res = general_age / len(people)

    json_obj = {"mean_age": res}
    string = json.dumps(json_obj)
    return string

# json_string = """
# [
#     {
#         "name": "Петр",
#         "surname": "Петров",
#         "patronymic": "Васильевич",
#         "age": 23,
#         "occupation": "ойтишнек"
#     },
#     {
#         "name": "Василий",
#         "surname": "Васильев",
#         "patronymic": "Петрович",
#         "age": 24,
#         "occupation": "дворник"
#     }
# ]
# """

# print(mean_age(json_string))
