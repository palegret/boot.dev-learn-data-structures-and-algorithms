import math


def num_possible_orders(num_posts):
    if not num_posts:
        raise ValueError("Number of posts is required.")
    elif num_posts < 0:
        raise ValueError("Number of posts cannot be less than zero.")
    elif num_posts == 0:
        return 1
    else:
        return math.factorial(num_posts)


def num_possible_orders_original(num_posts):
    product = 1

    for i in range(1, num_posts + 1):
        product *= i

    return product


# Tests

test_cases = [
    (2, 2), 
    (3, 6), 
    (5, 120),
    (1, 1),
    (6, 720),
    (7, 5040),
    (8, 40320),
    (9, 362880),
    (11, 39916800),
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
    main(num_possible_orders)
