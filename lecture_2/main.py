def generate_profile(age):
    """Return life stage based on age."""
    if 0 <= age <= 12:
        return "Child"
    if 13 <= age <= 19:
        return "Teenager"
    return "Adult"


def main():
    # --- Get user data ---
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")
    birth_year = int(birth_year_str)

    current_age = 2025 - birth_year
    hobbies = []

    while True:
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ").strip()
        if hobby.lower() == "stop":
            break
        hobbies.append(hobby)

    # --- Process profile ---
    life_stage = generate_profile(current_age)
    user_profile = {
        "name": user_name,
        "age": current_age,
        "stage": life_stage,
        "hobbies": hobbies
    }

    # --- Output summary ---
    print("\n---")
    print("Profile Summary:")
    print(f"Name: {user_profile['name']}")
    print(f"Age: {user_profile['age']}")
    print(f"Life Stage: {user_profile['stage']}")

    if not hobbies:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies ({len(hobbies)}):")
        for hobby in hobbies:
            print(f"- {hobby}")
    print("---")


if __name__ == "__main__":
    main()