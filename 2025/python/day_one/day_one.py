input = []


with open("day_one_input.txt") as f:
    input = f.read().splitlines()


def part_one(input: list[str]) -> int:
    dial_position = 50
    secret_code = 0
    for rotation in input:
        distance = int(rotation[1:])

        if rotation[0] == "L":
            dial_position = (dial_position - distance) % 100
        else:
            dial_position = (dial_position + distance) % 100
        if dial_position == 0:
            secret_code += 1

    return secret_code


def part_two(input: list[str]) -> int:
    dial_position = 50
    secret_code = 0
    for rotation in input:
        distance = int(rotation[1:])
        for _ in range(distance):
            if rotation[0] == "L":
                dial_position = (dial_position - 1) % 100
            else:
                dial_position = (dial_position + 1) % 100
            if dial_position == 0:
                secret_code += 1

    return secret_code


print(part_one(input))
print(part_two(input))
