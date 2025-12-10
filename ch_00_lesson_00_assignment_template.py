"""
Original solution:

"""

def ASSIGNMENT_FUNCTION(input):
    return input


# Test

def test(input, expected_output, test_function):
    try:
        print("\n\n--------------------------------------------------------------------------------")
        print(f"Inputs:")

        print(f" * input: {input}")

        print(f"Expected: {expected_output}")
        print("--------------------------------------------------------------------------------")

        result = test_function(input)

        print(f"Expected: {expected_output}")
        print(f"Actual: {result}")

        if result == expected_output:
            print(">>> PASS")
            return True
        else:
            print(">>> FAIL")
            return False
    except Exception as e:
        print()
        print(">>> FAIL")
        print(e)
        return False



# Runner

test_cases = [
]

def main(test_function):
    passed = 0
    failed = 0

    for test_case in test_cases:
        correct = test(*test_case, test_function)
        if correct:
            passed += 1
        else:
            failed += 1

    print()
    print()

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")

    print(f"\n{passed} passed, {failed} failed\n")


if __name__ == "__main__":
    main(ASSIGNMENT_FUNCTION)
