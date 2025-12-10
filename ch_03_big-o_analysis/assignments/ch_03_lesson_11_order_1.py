import time

"""
Original solution:
def find_last_name(names_dict, first_name):
    try:
        return names_dict[first_name]
    except KeyError:
        return None
"""

def find_last_name(names_dict, first_name):
    try:
        return names_dict[first_name]
    except KeyError:
        return None
    except Exception as e:
        print(f"Error encountered: {e}")     

def get_name_dict(first_name, last_name, num):
    names = {}
    for i in range(num):
        names[f"{first_name}{i}"] = f"{last_name}{i}"
    return names



# Test

def test(complexity, first_name, last_name, expected_output, test_function):
    try:
        print("\n\n--------------------------------------------------------------------------------")
        print(f"Inputs:")

        print(f" * first_name: {first_name}")
        print(f"Expected:  {expected_output} & completed in less than 50 milliseconds")

        print(f"Expected: {expected_output}")
        print("--------------------------------------------------------------------------------")

        if last_name == "Error":
            first_name_key = first_name
        else:
            first_name_key = f"{first_name}{complexity - 1}"

        names_dict = get_name_dict(first_name, last_name, complexity)
        start = time.time()
        result = test_function(names_dict, first_name_key)
        end = time.time()
        timeout = 0.05

        if (end - start) < timeout:
            print(f"find_last_name completed in less than {timeout * 1000} milliseconds!")

            if result == expected_output:
                print(f"Actual: {result}")
                print(">>> PASS")
                return True
            else:
                print(f"Actual: {result}")
                print(">>> FAIL")
                return False
        else:
            print(f"find_last_name took too long ({(end - start) * 1000} milliseconds). Speed it up!")
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
    (1000000, "John", "Doe", "Doe999999"),
    (1500000, "Lane", "Wagner", "Wagner1499999"),
    (2000000, "Key", "Error", None),
    (2500000, "Chad", "Energy", "Energy2499999"),
    (3000000, "Tiffany", "Johnson", "Johnson2999999"),
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
    main(find_last_name)
