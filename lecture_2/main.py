# Current year constant - used for age calculation
CURRENT_YEAR = 2025

# Set of commands that will stop the hobby collection loop
# Using a set for O(1) lookup time
STOP_COMMANDS = {"stop", "exit", "quit", "done", "end"}

# Immutable tuple of life stage strings
# Using tuple instead of list for better performance and safety
LIFE_STAGES = ("Child", "Teenager", "Adult")


def life_stage(age: int) -> str:
    """
    Determine life stage based on age efficiently.
    
    Args:
        age (int): The age to evaluate
        
    Returns:
        str: The corresponding life stage string
    """
    # Age 0-12: Child
    if age <= 12:
        return LIFE_STAGES[0]
    # Age 13-19: Teenager  
    elif age <= 19:
        return LIFE_STAGES[1]
    # Age 20+: Adult
    return LIFE_STAGES[2]


class Profile:
    """
    Profile class with slots for memory efficiency.
    
    Using __slots__ reduces memory usage by preventing the creation of __dict__
    and provides faster attribute access.
    """

    # Define fixed attributes to save memory
    __slots__ = ('name', 'birth_year', 'current_age', 'life_stage', 'hobbies')

    def __init__(self, user_dict: dict):
        """
        Initialize Profile instance from dictionary.
        
        Args:
            user_dict (dict): Dictionary containing profile data with keys:
                - name: Full name
                - birth_year: Year of birth  
                - current_age: Calculated age
                - life_stage: Life stage category
                - hobbies: List of hobbies
        """
        # Assign dictionary values to instance attributes
        self.name = user_dict["name"]
        self.birth_year = user_dict["birth_year"]
        self.current_age = user_dict["current_age"]
        self.life_stage = user_dict["life_stage"]
        self.hobbies = user_dict["hobbies"]

    def __str__(self) -> str:
        """
        String representation of Profile for printing.
        
        Returns:
            str: Formatted profile summary string
        """
        # Build output efficiently using list joining
        lines = [
            f"---\nProfile Summary:\nName: {self.name}\nAge: {self.current_age}\nLife Stage: {self.life_stage}\n"
        ]
        
        # Handle hobbies display based on whether any exist
        if not self.hobbies:
            lines.append("You didn't mention any hobbies.\n")
        else:
            # Show count and list of hobbies
            lines.append(f"Favorite Hobbies ({len(self.hobbies)}):\n")
            # Use generator expression for memory efficiency
            lines.extend(f"- {hobby}\n" for hobby in self.hobbies)
        
        lines.append("---")
        # Join all lines into final string
        return "".join(lines)


def get_user_hobbies() -> list[str]:
    """
    Collect hobbies from user input efficiently.
    
    Returns:
        list[str]: List of hobby strings entered by user
    """
    # Initialize empty list for hobbies
    hobbies: list[str] = []
    
    # Cache method lookups for better performance in loop
    append = hobbies.append  # Reference to append method
    lower = str.lower        # Reference to lower method

    # Continuous loop until user enters stop command
    while True:
        # Get user input and clean it
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ").strip()
        
        # Skip empty input
        if not hobby:
            continue
            
        # Check if user wants to stop (case-insensitive)
        if lower(hobby) in STOP_COMMANDS:
            break
            
        # Add valid hobby to list
        append(hobby)

    return hobbies


# Main execution block - runs only when script is executed directly
if __name__ == "__main__":
    # Collect basic user information
    name_input = input("Enter full name: ").strip()
    birth_year_input = int(input("Enter birth year: "))
    
    # Calculate current age
    current_age_input = CURRENT_YEAR - birth_year_input

    # Collect hobbies from user
    hobbies_list = get_user_hobbies()

    # Create dictionary with all user data
    # This structure makes it easy to serialize or extend later
    user_dict = {
        "name": name_input,
        "birth_year": birth_year_input, 
        "current_age": current_age_input,
        "life_stage": life_stage(current_age_input),  # Determine life stage
        "hobbies": hobbies_list
    }

    # Create Profile object and display it
    profile_obj = Profile(user_dict)
    print(profile_obj)