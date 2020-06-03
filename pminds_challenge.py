while True:

    # Receive and clean a movement input string:
    movement_input = [char for char in input("Insert directions for Ash: ") if char in "NSWE"]

    # The coordinate pair for Ash's current position (he begins at 0, 0):
    ash_x, ash_y = 0, 0

    """ The number of Caught Pokemons will equal the number of UNIQUE Passed Positions (that's why a set is used).
    (0, 0) is already registered because Ash always catches his 1st Pokemon at his starting position.
    (I used tuples because the coordinates of each position should be ordered and immutable)."""
    passed_positions = {(0, 0)}

    for char in movement_input:
        if char == "N":
            ash_y += 1
        elif char == "S":
            ash_y -= 1
        elif char == "E":
            ash_x += 1
        elif char == "W":
            ash_x -=1
        # The "add" method will only add new entries to a set if said entry isn't already present. Helps efficiency:
        passed_positions.add((ash_x, ash_y))

    # Use Length function to count unique passed positions. Then deliver output:
    print(f"{len(passed_positions)}\n")
