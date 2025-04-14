def get_follower_prediction(follower_count, influencer_type, num_months):
    r = 2

    if influencer_type == "fitness":
        r = 4
    elif influencer_type == "cosmetic":
        r = 3

    return follower_count * (r ** num_months)


# Tests

test_cases = [
    (10, "fitness", 1, 40),
    (10, "fitness", 2, 160),
    (12, "cosmetic", 4, 972),
    (15, "business", 4, 240),
    (10, "fitness", 5, 10240),
    (10, "fitness", 6, 40960),
    (10, "fitness", 7, 163840),
    (10, "fitness", 8, 655360),
    (10, "tech", 9, 5120),
]

def test(input1, input2, input3, expected_output, test_function):
    try:
        print("--------------------------------------------------------------------------------")
        print(f"Inputs: {input}")
        print(f"Expecting: {expected_output}")
        print("--------------------------------------------------------------------------------")

        result = test_function(input1, input2, input3)

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
    main(get_follower_prediction)
