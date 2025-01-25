import random

adjectives = ["Swift", "Mighty", "Bold", "Cheerful", "Luminous", 
              "Witty", "Fiery", "Gentle", "Zany", "Epic"]
nouns = ["Falcon", "Knight", "Hawk", "Sorcerer", "Panther", 
         "Comet", "Rogue", "Viper", "Wolf", "Gladiator"]

def generate_username(add_numbers=True, add_special_chars=True):
    username = random.choice(adjectives) + random.choice(nouns)
    if add_numbers:
        username += str(random.randint(1, 999))
    if add_special_chars:
        username += random.choice(["!", "@", "#", "$"])
    return username

def save_to_file(usernames, filename="usernames.txt"):
    try:
        with open(filename, "a") as file:
            file.write("\n".join(usernames) + "\n")
        print(f"Usernames saved to {filename}.")
    except IOError as e:
        print(f"Error saving to file: {e}")

def get_valid_input(prompt, valid_options):
    while True:
        response = input(prompt).strip().lower()
        if response in valid_options:
            return response
        print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    print("Welcome to the Random Username Generator!")
    usernames = []
    while True:
        print("\nMenu:")
        print("1. Generate Username")
        print("2. Save Usernames to File")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_numbers = get_valid_input("Do you want to include numbers? (yes/no): ", ["yes", "no"]) == "yes"
            add_special_chars = get_valid_input("Do you want to include special characters? (yes/no): ", ["yes", "no"]) == "yes"
            username = generate_username(add_numbers, add_special_chars)
            print(f"Generated Username: {username}")
            usernames.append(username)
        elif choice == "2":
            if usernames:
                save_to_file(usernames)
            else:
                print("No usernames to save. Generate some first!")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
