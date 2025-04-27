def get_menu_option():
  '''
  Should print a menu with the following options:
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI

  The function should return a number between 1-4.
  If the user will enter invalid data (for example 5), than a message will appear
  asking to input a new value.
  '''
  options = [
        "1. Human vs Human",
        "2. Random AI vs Random AI",
        "3. Human vs Random AI",
        "4. Human vs Unbeatable AI"
    ]

  while True:
        print("\nSelect a game mode:")
        for option in options:
            print(option)

        choice = input("Enter your choice (1-4): ").strip()

        if choice in {'1', '2', '3', '4'}:
            return int(choice)
        else:
            print("Invalid option. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print("If the user selected 1, it should print 1")
    print(option) 