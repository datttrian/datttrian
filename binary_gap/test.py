import pytest
from main import solution


@pytest.mark.parametrize(
    ["input_int", "expected_output"],
    [
        [9, 2],
        [529, 4],
        [20, 1],
        [15, 0],
        [32, 0],
        [6, 0],
        [328, 2],
        [11, 1],
        [19, 2],
        [42, 1],
        [1162, 3],
        [5, 1],
        [51712, 2],
        [561892, 3],
        [66561, 9],
        [6291457, 20],
        [74901729, 4],
        [805306369, 27],
        [1376796946, 5],
        [1073741825, 29],
        [1610612737, 28],
    ],
)
def test_solution(input_int: int, expected_output: int) -> bool:
    """Test the solution function.

    This function tests the solution function with various input lists
    and expected outputs to verify that it correctly identifies the
    smallest positive integer missing from the list.

    Parameters:
    - input_int (int): The input list of integers to test.
    - expected_output (int): The expected output for the given input list.

    """
    assert solution(input_int) == expected_output
    return True


if __name__ == "__main__":
    print(
        "Solution: ",
        solution(
            int(input("Input an array A of N integers: ")),
        ),
    )
