def median_followers(nums):
    if not nums:
        return None
        
    sorted_nums = sorted(nums)
    nums_length = len(sorted_nums)
    
    if nums_length % 2 == 0:
        # Even: the median is the AVERAGE of the two middle elements
        middle_element_1 = sorted_nums[nums_length // 2 - 1]
        middle_element_2 = sorted_nums[nums_length // 2]
        median = (middle_element_1 + middle_element_2) / 2
    else:
        # Odd: the median IS the middle element
        median = sorted_nums[nums_length // 2]
        
    return median


# Tests

test_cases = [
    ([12, 12, 12], 12),
    ([10, 200, 3000, 5000, 4], 200),
    ([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 7),
    ([], None),
    ([0], 0),
    ([1000000], 1000000),
    ([5, 2, 3, 7, 6, 4], 4.5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
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
    main(median_followers)
