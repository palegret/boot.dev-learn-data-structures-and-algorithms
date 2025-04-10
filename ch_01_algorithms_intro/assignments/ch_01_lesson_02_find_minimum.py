def find_minimum(nums):
    if not nums:
        return None
        
    minimum = float("inf")

    for num in nums:
        if num < minimum:
            minimum = num

    return minimum


# Tests

test_cases = [
    ([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 1),
    ([12, 12, 12], 12),
    ([10, 200, 3000, 5000, 4], 4),
    ([1], 1),
    ([1, 2, 3, 4, 5], 1),
    ([5, 4, 3, 2, 1], 1),
    ([100, 200, 300, 400, 500], 100),
    ([500, 400, 300, 200, 100], 100),
    ([], None),
]


def test(input, expected_output, test_function):
    print("--------------------------------------------------------------------------------")
    print(f"Inputs: {input}")
    print(f"Expecting: {expected_output}")
    print("--------------------------------------------------------------------------------")

    result = test_function(input)

    print(f"Actual: {result}")

    if result == expected_output:
        print("Pass")
        return True
    else:
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0

    for test_case in test_cases:
        correct = test(*test_case, find_minimum)

        if correct:
            passed += 1
        else:
            failed += 1
        
    if failed == 0:
        print("===================================== PASS =====================================")
    else:
        print("===================================== FAIL =====================================")

    print(f"{passed} passed, {failed} failed.")


if __name__ == "__main__":
    main()
