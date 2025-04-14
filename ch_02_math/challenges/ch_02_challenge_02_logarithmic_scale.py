import math


def log_scale(data, base):
    logarithms = []

    for number in data:
        if number <= 0:
            raise ValueError("All numbers must be positive.")
        
        logarithm = math.log(number, base)
        logarithms.append(logarithm)
    return logarithms    


# Tests

test_cases = [
    ([1, 10, 100, 1000], 10, [0.0, 1.0, 2.0, 3.0]),
    ([1, 2, 4, 8], 2, [0.0, 1.0, 2.0, 3.0]),
    ([2, 4, 8, 16], 2, [1.0, 2.0, 3.0, 4.0]),
    ([3, 9, 27, 81], 3, [1.0, 2.0, 3.0, 4.0]),
    ([5, 25, 125, 625], 5, [1.0, 2.0, 3.0, 4.0]),
    ([10, 100, 1000, 10000], 10, [1.0, 2.0, 3.0, 4.0]),
    ([20, 400, 8000, 160000], 20, [1.0, 2.0, 3.0, 4.0]),
]

def test(data, base, expected_output, test_function):
    try:
        print("--------------------------------------------------------------------------------")
        print(f"Inputs:")
        print(f" * data: {data}")
        print(f" * base: {base}")
        print(f"Expecting: {expected_output}")
        print("--------------------------------------------------------------------------------")

        scaled_data = log_scale(data, base)
        
        for i in range(0, len(scaled_data)):
            scaled_data[i] = round(scaled_data[i], 2)
            
        print(f"Actual: {scaled_data}")

        if scaled_data == expected_output:
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
    main(log_scale)
