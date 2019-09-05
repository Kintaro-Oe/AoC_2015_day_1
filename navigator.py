def locate(directions):
    # iterate over the string one char at a time.
    # if char = ( then floor += 1
    # if char =) then floor -= 1
    # floor can be any positive or negative number

    floor = 0

    for char in directions:
        if char == '(':
            floor += 1

    return floor
