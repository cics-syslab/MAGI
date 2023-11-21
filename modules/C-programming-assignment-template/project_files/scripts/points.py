import yaml

total_points = 0

with open("test_list.yml") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    tests = data["tests"]

    for test in tests:
        points = test["points"]
        total_points = total_points + points

print(f"Total points for this assignment are {total_points}")

# tests = yaml.load("test_list.yml", Loader=yaml.FullLoader)

# print(tests)

# total_points = 0

# for test in tests:
#     print(test["points"])
#     test_points = int(test["points"])
#     total_points = total_points + test_points

# print(f"Total points for this assignment is {total_points}")
