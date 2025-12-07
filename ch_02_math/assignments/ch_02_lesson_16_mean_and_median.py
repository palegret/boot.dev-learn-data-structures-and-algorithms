import math

"""
Original solution:
def average_followers(nums):
    if len(nums) == 0:
        return None
    sum = 0
    for num in nums:
        sum += num
    return sum / len(nums)
"""

def average_followers(nums):
    #return sum(nums) / len(nums) if nums else None
    if len(nums) == 0:
        return None
    sum = 0
    for num in nums:
        sum += num
    return sum / len(nums)


# Test

def test(input1, expected_output, test_function):
    try:
        print("--------------------------------------------------------------------------------")
        print(f"Inputs:")
        print(f" * nums: {input1}")
        print(f"Expected: {expected_output}")
        print("--------------------------------------------------------------------------------")

        result = test_function(input1)

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


# Runner

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
