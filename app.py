def gotta_catch_em_all(input_string):

    # If no input is given:
    if not input_string:
        return 1

    # Receive and clean the input string. Helps security and efficiency:
    directions = "".join([char for char in input_string if char in "NSEO"])

    # If no valid directions are found in input string:
    if not directions:
        return 1
        
    """ If the set of the input string has length of 1, it means all chars are equal.
    If all chars are equal, the number of caught Pokemon will equal the string's length + 1 (for the starting position)."""
    if len(set(directions)) == 1:
        return len(directions) + 1
        
    else:

        # An "NSN" movement is net equal to "N". Same for remaining element pairs in "replacements". Helps efficiency:
        replacements = [["NSN", "N"], ["SNS", "S"], ["EOE", "E"], ["OEO", "O"]]

        # Implement a cycle to ensure replacements are possible. It will stop as soon as the directions stop getting smaller:
        previous_length = len(directions) + 1
        while previous_length != len(directions):
            previous_length = len(directions)

            # Iterate over "replacements" and replace optimized values where applicable:
            for i in range(len(replacements)):
                if replacements[i][0] in directions:
                    directions = directions.replace(replacements[i][0], replacements[i][1])
        
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
            elif char == "O":
                ash_x -=1
                
            # The "add" method will only add new entries to a set if said entry isn't already present. Helps efficiency:
            passed_positions.add((ash_x, ash_y))

        # Use Length function to count unique passed positions. Then deliver output:
        return len(passed_positions)


# ----- TESTS -----
# Empty Input:
assert(gotta_catch_em_all("")) == 1, "Should be 1."
# No Valid Directions:
assert(gotta_catch_em_all("kksvckbjnwjid9u43203pok -.çp5l+434e")) == 1, "Should be 1."
# Poorly Formatted Input:
assert(gotta_catch_em_all("N daskl__?*+dSNsnjc  -  wjopfedOOsc6?5156S189145O=)(/&J%$#  AE  sd)")) == 6, "Should be 6."
# Back and Forth Input:
assert(gotta_catch_em_all("NS" * 9999)) == 2, "Should be 2."
# Linear Input:
assert(gotta_catch_em_all("O" * 9999)) == 10000, "Should be 10000."


while True:
    user_input = input("Insert directions for Ash: ")
    print(f"{gotta_catch_em_all(user_input)}\n")
