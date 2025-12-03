dial_position = 50
secret_code = 0
input = []

with open("day_one_input.txt") as f:
    input = f.read().splitlines()

for rotation in input:
    distance = int(rotation[1:])

    if rotation[0] == "L":
        dial_position = (dial_position - distance) % 100
    else:
        dial_position = (dial_position + distance) % 100

    if dial_position == 0:
        secret_code += 1


print(dial_position)
print(secret_code)
