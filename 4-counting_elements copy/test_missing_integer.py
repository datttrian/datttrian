import pytest


def solution(A: list) -> int:  # pylint: disable=C0103
    """Find the smallest positive integer that does not occur in a sequence.

    :param A: list[int] A non-empty list of integers.
    :return: [int] The smallest positive integer that is missing.

    Sort the array and walk through it until we find the missing item.
    I wonder if this is a mistake: allowing us to sort the array first?

    """
    missing = 1
    for elem in sorted(A):
        if elem == missing:
            missing += 1
        if elem > missing:
            break
    return missing


@pytest.mark.parametrize(
    ["input_list", "expected_output"],
    [
        [[1, 3, 6, 4, 1, 2], 5],
        [[1, 2, 3], 4],
        [[-1, -3], 1],
        [[0, 1, 2, 3], 4],
        [[-2, -4, -3], 1],
        [[], 1],
    ],
)
def test_solution(input_list: list, expected_output: int) -> bool:
    """Test the solution function.

    This function tests the solution function with various input lists
    and expected outputs to verify that it correctly identifies the
    smallest positive integer missing from the list.

    Parameters:
    - input_list (list of int): The input list of integers to test.
    - expected_output (int): The expected output for the given input list.

    """
    assert solution(input_list) == expected_output
    return True


if __name__ == "__main__":
    print(
        "Solution: ",
        solution(
            list(map(int, input("Input an array A of N integers: ").split())),
        ),
    )
