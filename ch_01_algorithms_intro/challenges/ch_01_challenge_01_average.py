def sum(nums):
    if not nums:
        return 0

    sum = 0
    
    for num in nums:
        sum += num

    return sum


def average_followers(nums):
    if not nums:
        return None
        
    total_followers = sum(nums)
    
    return total_followers / len(nums)


# Tests

test_cases = [
    ([1], 1),
    ([1, 2, 3, 4, 5, 6, 7], 4),
    ([12, 12, 12], 12),
    ([], None),
    ([0], 0),
    ([100, 200, 300, 400, 500], 300),
    ([5, 10, 200, 3000, 5000], 1643),
    ([12_345, 618_222, 58_832_221, 2_180_831_475, 8_663_863_102], 2_180_831_473),
]

def test(input, expected_output, test_function):
    try:
        print("--------------------------------------------------------------------------------")
        print(f"Inputs: {input}")
        print(f"Expecting: {expected_output}")
        print("--------------------------------------------------------------------------------")

        result = test_function(input)

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
    main(average_followers)
