import time

def intro():
    print("Welcome to Hogwarts, where would you like to go?")
    time.sleep(2)
    print("You are a student at Hogwarts School of Witchcraft and Wizardry.")
    time.sleep(2)
    print("Your adventure begins now!")
    time.sleep(2)
    print("\n")

def choose_house():
    print("You are sorted into your house")
    time.sleep(2)
    print("Which house would you like to be sorted into?")
    time.sleep(1)
    print("1. Gryffindor")
    print("2. Hufflepuff")
    print("3. Ravenclaw")
    print("4. Slytherin")
    house_choice = input("Enter the number of your choice: ")
    if house_choice == "1":
        return "Gryffindor"
    elif house_choice == "2":
        return "Hufflepuff"
    elif house_choice == "3":
        return "Ravenclaw"
    elif house_choice == "4":
        return "Slytherin"
    else:
        print("Invalid choice. Please try again.")
        return choose_house()

def explore_house(house):
    print("You explore the main room of", house)
    time.sleep(2)
    print("You find a hidden passage...")
    time.sleep(2)
    print("Do you want to explore it?")
    time.sleep(1)
    explore_choice = input("Enter 'yes' or 'no': ").lower()
    if explore_choice == "yes":
        print("You find a secret room filled with treasures!")
    elif explore_choice == "no":
        print("You decide not to explore the passage. You continue on your way.")
    else:
        print("Invalid choice. Please try again.")
        return explore_house(house)
    
def main():
    intro()
    house = choose_house()
    print("You have been sorted into", house)
    time.sleep(2)
    explore_house(house)
    print("Congratulations! You have completed your first adventure at Hogwarts!")
if __name__ == "__main__":
    main()