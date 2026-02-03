# def rock_paper_scissors(p1):

#     if p1=="rock":
#         return "paper"
#     elif p1=="paper":
#         return "scissors"
#     elif p1=="scissors":
#         return "rock"
#     else:
#         return "invalid"


# p1 = input().strip()


# result = rock_paper_scissors(p1)
# print(result)




import json
# json_str = '''[
#   {"id": 1, "name": "A"},
#   {"id": 2, "name": "B"}
# ]'''


# users = json.loads(json_str)

# for user in users:
#     print(user["name"])



data = {"id": 1, "active": True}
json_str = json.dumps(data)

print(json_str)