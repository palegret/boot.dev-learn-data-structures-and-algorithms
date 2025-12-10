import random

"""
Original solution:
def get_avg_brand_followers(all_handles, brand_name):
    count = 0
    for handles in all_handles:
        for handle in handles:
            if brand_name in handle:
                count += 1
    return count / len(all_handles)
"""

def get_avg_brand_followers(all_handles, brand_name):
    brand_name_counts = []

    for audience in all_handles:
        brand_name_handles = [handle for handle in audience if brand_name in handle]
        brand_name_counts.append(len(brand_name_handles))

    average = sum(brand_name_counts) / len(brand_name_counts) if all_handles else 0
    return average

def get_all_handles(num, audience_size):
    all_handles = []
    for i in range(num):
        m = random.randrange(
            int(audience_size - audience_size * 1.2),
            int(audience_size + audience_size * 1.2),
        )
        handles = get_user_handles(m)
        all_handles.append(handles)
    return all_handles

def get_user_handles(num):
    handles = []
    for i in range(0, num):
        m = random.randrange(0, 6)
        if m == 0:
            handles.append(f"luxaraygirl{i}")
        elif m == 1:
            handles.append(f"theprimerog{i}")
        elif m == 2:
            handles.append(f"luxafanboi{i}")
        elif m == 3:
            handles.append(f"dashlord{i}")
        elif m == 4:
            handles.append(f"saintrex{i}")
        elif m == 5:
            handles.append(f"writergurl{i}")
    return handles



# Test

def test(num_handles, avg_aud_size, brand_name, expected_output, test_function):
    try:
        print("\n\n--------------------------------------------------------------------------------")
        print(f"Inputs:")

        print(f"Checking {num_handles} influencers with average audience sizes of {avg_aud_size}...")
        print(f" * brand_name: {brand_name}")

        print(f"Expected: {expected_output}")
        print("--------------------------------------------------------------------------------")

        all_handles = get_all_handles(num_handles, avg_aud_size)
        average = test_function(all_handles, brand_name)
        result = round(average, 2)

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
    (10, 1000, "luxa", 383.9),
    (20, 2000, "luxa", 593.25),
    (30, 3000, "luxa", 932.23),
    (40, 4000, "luxa", 1495.4),
    (80, 8000, "luxa", 2608.95),
    (160, 16000, "luxa", 5920.98),
]

def main(test_function):
    random.seed(1) # 👀

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
    main(get_avg_brand_followers)
