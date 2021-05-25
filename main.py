answer = input("Would you like to play? (yes/no): ")
if answer.lower().strip() == "yes":
    answer = input(
        "You reach a corssroad, would you like to go left or right: ").lower().strip()
    if answer == 'left':
        answer = input(
            "You see an old lady carrying a basket. Approach or avoid?: ").lower().strip()
        if answer == 'approach':
            print(
                "Awful choice. Were you not raised to avoid strangers? She fed you a poison apple. Death. RIP")
        else:
            print(
                "Good choice. Never speak to strangers, especially old ladies in the woods...")

            answer = input(
                "You found a pot of gold! Do you take a few coins, yes or no?: ").lower().strip()

            if answer == 'yes':
                print("Oops. the coins were cursed...You now have the plague. RIP")
            else:
                print("Boring but wise. The coins were cursed. You survived!")

    elif answer == 'right':
        print("Ah, you fell down a ditch. RIP")

    else:
        print(
            "Invalid choice. You went down an unknown path and was attacked by a bear. RIP")

else:
    print("Oh :(")
