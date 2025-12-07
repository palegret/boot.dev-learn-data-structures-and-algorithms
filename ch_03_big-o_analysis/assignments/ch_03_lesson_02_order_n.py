def find_max(nums):
    if not nums:
        return None
        
    maximum = float("-inf")

    for num in nums:
        if num > maximum:
            maximum = num

    return maximum


# Test

def test(input1, expected_output, test_function):
    print("--------------------------------------------------------------------------------")
    print(f"Inputs:")
    print(f" * nums: {input1}")
    print(f"Expected: {expected_output}")
    print("--------------------------------------------------------------------------------")

    result = test_function(input1)

    print(f"Actual:   {result}")

    if result == expected_output:
        print("Pass")
        return True
    else:
        print("Fail")
        return False


# Runner

test_cases = [
    ([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 2343243), 
    ([12, 12, 12], 12),
    ([10, 200, 3000, 5000, 4], 5000),
    ([0], 0),
    ([-1, -2, -3], -1),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10),
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
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")

    print(f"{passed} passed, {failed} failed")


if __name__ == "__main__":
    main(find_max)
