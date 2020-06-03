def gotta_catch_em_all(movement_string):
    
    # Receive and clean the movement input string. Helps security and efficiency:
    directions = [char for char in movement_string if char in "NSEW"]

    """ If the set of the input string has length of 1, it means all chars are equal.
    If all chars are equal, the number of caught Pokemon will equal the string's length + 1 (for the starting position)."""
    if len(set(directions)) == 1:
        return len(directions) + 1
        
    else:
        
        # The coordinate pair for Ash's current position (he begins at 0, 0):
        ash_x, ash_y = 0, 0

        """ The number of Caught Pokemons will equal the number of UNIQUE Passed Positions (that's why a set is used).
        The position (0, 0) is already registered because Ash always catches his 1st Pokemon at the beggining.
        I used tuples because the coordinates of each position should be ordered and immutable."""
        passed_positions = {(0, 0)}

        for char in directions:
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
        return len(passed_positions)


# ----- TESTS -----
# Empty Input:
assert(gotta_catch_em_all("")) == 1, "Should be 1."
# Poorly Formatted Input:
assert(gotta_catch_em_all("N daskl__?*+dSNsnjc  -  wjopfedWWsc6?5156S189145W=)(/&J%$#  AE  sd)")) == 6, "Should be 6."
# Back and Forth Input:
assert(gotta_catch_em_all("NSNSNSNSNSNSNSNSNSNSNSNSNSNSNSN")) == 2, "Should be 2."
# Linear Input:
assert(gotta_catch_em_all("W" * 9999)) == 10000, "Should be 10000."

while True:
    user_input = input("Insert directions for Ash: ")
    print(f"{gotta_catch_em_all(user_input)}\n")

