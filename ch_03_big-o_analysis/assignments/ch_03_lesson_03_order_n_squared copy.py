def does_name_exist(first_names, last_names, full_name):
    for first_name in first_names:
        for last_name in last_names:
            if (f"{first_name} {last_name}" == full_name):
                return True

    return False

def get_first_names(num):
    names = []
    for i in range(num):
        m = i % 3
        if m == 0:
            names.append(f"bob{i}")
        elif m == 1:
            names.append(f"maria{i}")
        elif m == 2:
            names.append(f"sally{i}")
    return names


def get_last_names(num):
    names = []
    for i in range(num):
        m = i % 3
        if m == 0:
            names.append(f"gonzalez{i}")
        elif m == 1:
            names.append(f"smith{i}")
        elif m == 2:
            names.append(f"wagner{i}")
    return names



# Test

def test(num_fnames, num_lnames, check_name, expected_output, test_function):
    try:
        print("\n\n--------------------------------------------------------------------------------")
        print(f"Inputs:")

        print(f" * num first_names: {num_fnames}")
        print(f" * num last_names: {num_lnames}")
        print(f" * looking for name: {check_name}")

        print(f"Expected: {expected_output}")
        print("--------------------------------------------------------------------------------")

        fnames = get_first_names(num_fnames)
        lnames = get_last_names(num_lnames)
        result = test_function(fnames, lnames, check_name)

        print(f"Actual: {result}")
        print()

        if result == expected_output:
            print(">>> PASS")
            return True
        else:
            print(">>> FAIL")
            return False
    except Exception as e:
        print()
        print(">>> FAIL")
        print(e)
        return False



# Runner

test_cases = [
    (100, 100, "bob0 gonzalez0", True),
    (500, 500, "maria1 smith1", True),
    (1000, 1000, "bob500 smith1", False),
    (2000, 2000, "bob1999 wagner1998", False),
    (3000, 3000, "sally2999 smith2998", True),
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
    main(does_name_exist)
