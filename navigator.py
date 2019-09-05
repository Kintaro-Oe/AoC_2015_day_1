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

print(locate(file_opener()))
