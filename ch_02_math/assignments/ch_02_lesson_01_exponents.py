def get_estimated_spread(audiences_followers):
    pass


# Tests

test_cases = [
    ([7, 4, 3, 100, 765, 2344, 1, 2, 32], 5056),
    ([12, 12, 12], 45),
    ([10, 200, 3000, 5000, 4], 11333),
    ([], 0),
    ([1, 1, 1], 4),
    ([100], 100),
    ([50, 60, 70, 80, 90], 483),
    ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 872),
    ([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100], 1912),
]

def test(input, expected_output, test_function):
    try:
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
    except Exception as e:
        print("Fail")
        print(e)
        return False


def main(test_function):
    passed = 0
    failed = 0

    for test_case in test_cases:
        correct = test(*test_case, test_function)

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
    main(get_estimated_spread)
