def file_opener():
    with open('directions.txt', 'r') as file:
        return file.read()

def locate(directions):
    floor = 0

    for char in directions:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

    return floor

def position(input_string, floor_query):
    if floor_query == 0:
        return 0

    floor = 0

    for idx, char in enumerate(input_string, start=1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == floor_query:
            return idx

print(position(file_opener(), -1))


# print(locate(file_opener()))
