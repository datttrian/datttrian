def solution(N: int) -> int:  # pylint: disable=C0103
    """Determines the maximal 'binary gap' in an integer.

    :param N: [int] A positive integer (between 1 and maxint).
    :return: [int] The length of the longest sequence of zeros
    in the binary representation of the integer.

    Convert the int to a string of 0/1 chars.
    Loop through the chars in the string.
    When we see a zero, start the gap counter.
    When we see a one, compare with the biggest gap, and save the bigger;
    reset the gap counter.
    When we run out of characters, return the biggest gap.
    """
    # Convert the number to a string containing '0' and '1' chars.
    binary_string = str(bin(N))[2:]

    gap = max_gap = 0
    for char in binary_string:
        if char == "0":
            gap += 1
        else:
            max_gap = max(gap, max_gap)
            gap = 0

    return max_gap


if __name__ == "__main__":
    print(
        "Solution: ",
        solution(
            int(input("Input an array A of N integers: ")),
        ),
    )
