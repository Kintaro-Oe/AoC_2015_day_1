def locate(directions):
    floor = 0

    for char in directions:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

    return floor
