import time

"""
Original solution:
def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False
"""

def binary_search(target, arr):
    arr.sort()

    low = 0
    high = len(arr) - 1

    while low <= high:
        median = (low + high) // 2
        test_value = arr[median]

        if test_value == target:
            return True
        
        if test_value > target:
            high = median - 1
        else:
            low = median + 1

    return False



# Test

def test(target, arr, expected_output, test_function):
    try:
        print("\n\n--------------------------------------------------------------------------------")
        print(f"Inputs:")

        print(f" * target: {target}")
        print(f" * arr length: {len(arr)} items")

        print(f"Expected: {expected_output}")
        print("--------------------------------------------------------------------------------")

        start = time.time()
        result = test_function(target, arr)
        end = time.time()
        timeout = 0.05

        if (end - start) < timeout:
            print(f"binary_search completed in less than {timeout * 1000} milliseconds!")

            if result == expected_output:
                print(f"Actual: {result}")
                print(">>> PASS")
                return True
            else:
                print(f"Actual: {result}")
                print(">>> FAIL")
                return False
        else:
            print(f"binary_search took too long ({(end - start) * 1000} milliseconds). Speed it up!")
            print(f"Actual: {result}")
            print(">>> FAIL")
            return False
    except Exception as e:
        print()
        print(">>> FAIL")
        print(e)
        return False



# Runner

test_cases = [
    (10, [i for i in range(200)], True),
    (-1, [i for i in range(20000)], False),
    (15, [], False),
    (0, [0], True),
    (-1, [-2, -1], True),
    (105028, [i for i in range(2000000)], True),
    (2000001, [i for i in range(2000000)], False),
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
    main(binary_search)
