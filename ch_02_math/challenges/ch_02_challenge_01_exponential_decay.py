def decayed_followers(intl_followers, fraction_lost_daily, days):
    if intl_followers <= 0:
        return 0
    
    if days <= 0:
        return intl_followers
    
    if fraction_lost_daily <= 0:
        return intl_followers
    
    if fraction_lost_daily >= 1:
        return 0
    
    retention_rate = 1 - fraction_lost_daily

    if retention_rate <= 0:
        return 0

    return round(intl_followers * (retention_rate ** days))


# Tests

test_cases = [
    (200, 0.5, 1, 100),
    (200, 0.5, 2, 50),
    (200, 0.05, 3, 171),
    (1000, 0.005, 2, 990),
    (1000, 0.05, 3, 857),
    (1200, 0.55, 8, 2),
    (1200, 0.09, 16, 265),
    (0, 0.5, 1, 0),
    (100, 0, 5, 100),
]

def test(input1, input2, input3, expected_output, test_function):
    try:
        print("--------------------------------------------------------------------------------")
        print(f"Inputs: {input}")
        print(f"Expecting: {expected_output}")
        print("--------------------------------------------------------------------------------")

        result = round(test_function(input1, input2, input3))
    
        if expected_output is not None:
            result = int(result)

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
    main(decayed_followers)
