import math


def get_influencer_score(num_followers, average_engagement_percentage):
    return average_engagement_percentage * math.log(num_followers, 2)


# Tests

test_cases = [
    (40000, 0.3, 5), 
    (43000, 0.1, 2), 
    (100000, 0.6, 10),
    (1, 1, 0),
    (200, 0.8, 6),
    (300000, 0.5, 9),
    (500000, 0.2, 4),
    (750000, 0.7, 14),
]

def test(input1, input2, expected_output, test_function):
    try:
        print("--------------------------------------------------------------------------------")
        print(f"Inputs: {input}")
        print(f"Expecting: {expected_output}")
        print("--------------------------------------------------------------------------------")

        result = round(test_function(input1, input2))

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
    main(get_influencer_score)
