"""
Original solution:
def decayed_followers(intl_followers, fraction_lost_daily, days):
    res = intl_followers * (1 - fraction_lost_daily) ** days
    return res
"""

def decayed_followers(initial_followers, fraction_lost_daily, days):
    remaining_total = initial_followers * ((1 - fraction_lost_daily) ** days)
    return remaining_total


# Test

def test(input1, input2, input3, expected_output, test_function):
    try:
        print("--------------------------------------------------------------------------------")
        print(f"Inputs: {(input1, input2, input3)}")
        print(f"Expecting: {expected_output}")
        print(f"Inputs:")
        print(f" * initial_followers: {input1}")
        print(f" * fraction_lost_daily: {input2}")
        print(f" * days: {input3}")
        print(f"Expected: {expected_output}")
        print("--------------------------------------------------------------------------------")

        result = round(test_function(input1, input2, input3))

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


# Runner

test_cases = [
    (200, 0.5, 1, 100),
    (200, 0.4, 2, 72),
    (200, 0.05, 3, 171),
    (1000, 0.005, 2, 990),
    (1000, 0.05, 3, 857),
    (1200, 0.55, 8, 2),
    (1200, 0.09, 16, 265),
    (0, 0.5, 1, 0),
    (100, 0, 5, 100),
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

    if failed == 0:
        print("===================================== PASS =====================================")
    else:
        print("===================================== FAIL =====================================")

    print(f"{passed} passed, {failed} failed.")


if __name__ == "__main__":
    main(decayed_followers)
