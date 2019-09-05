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

# method - takes string input and floor integer then returns the index
# position of the first time that floor is reached
def position(input_string, floor_query):
    return 1



print(locate(file_opener()))
