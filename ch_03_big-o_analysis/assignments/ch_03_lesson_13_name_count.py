import time

"""
Original solution:
"""

def count_names(list_of_lists, target_name):
    target_name_counts = []

    for names in list_of_lists:
        target_name_instances = [name for name in names if name == target_name]
        target_name_counts.append(len(target_name_instances))

    return sum(target_name_counts)



# Test
def test(input1, input2, expected_output, test_function):
    try:
        print("\n\n--------------------------------------------------------------------------------")
        print(f"Inputs:")

        print(f" * list of lists: {input1}")
        print(f" * target name: {input2}")

        print(f"Expected: {expected_output}")
        print("--------------------------------------------------------------------------------")

        result = test_function(input1, input2)

        print(f"Expected: {expected_output}")
        print(f"Actual: {result}")

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
    (
        [
            ["George", "Eva", "George"], 
            ["Diane", "George", "Eva", "Frank"]
        ], 
        "George", 
        3
    ),
    (
        [
            ["Amy", "Bob", "Candy"],
            ["Diane", "George", "Eva", "Frank"],
            ["Diane", "George"],
            ["George", "name", "George"],
        ],
        "George",
        4,
    ),
    (
        [
            ["Alex", "name", "Chloe"],
            ["Eric", "name", "Fred"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["George"],
        ],
        "Hector",
        3,
    ),
    (
        [
            ["Alex", "name", "Chloe"],
            ["Eric", "name", "Fred"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["George"],
        ],
        "George",
        1,
    ),
    (
        [["Alex", "name", "Chloe"], ["Eric", "name", "Fred"], ["Hector", "name"]],
        "Alex",
        1,
    ),
    ([], "George", 0),
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
    main(count_names)
