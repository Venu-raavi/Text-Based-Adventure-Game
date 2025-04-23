# locations.py
def beach_path(inventory):
    print("\nYou walk along the Beach and found a broken Compass.")
    inventory.add_item("Broken Compass")
    next_step = input("Head into the jungle or search the ship? (jungle/ship): ").strip().lower()
    if next_step == "jungle":
        jungle_path(inventory)
    elif next_step == "ship":
        print("\nYou find a rusty sword but trigger a trap. You're caught, Game Over!")
        inventory.add_item("Rusty Sword")
        ending(False)
    else:
        print("You walk aimlessly and get caught in a storm. GAME OVER!")
        ending(False)

def jungle_path(inventory):
    print("\nYou enter the dense jungle and hear Strange Noises in the distance.")
    print("You carefully went through the bushes and discover an ancient abandoned camp.")
    print("Inside, there's a small locked chest and a mysterious glowing herb.")
    choice = input("Do you take the 'Glowing Herb' or try to open the 'Chest'? (herb/chest): ").strip().lower()
    print("\n")
    if choice == "herb":
        print("You collect the glowing herb. It might have healing properties!")
        inventory.add_item("Glowing Herb")
    elif choice == "chest":
        print("You open the chest and find a rusty sword. Might get Helpful!")
        inventory.add_item("Rusty Sword")
    else:
        print("You hesitate too long, and a group of insects drives you away. LOST!")

    print("\nAs you move deeper into the jungle, a wild monkey suddenly drops from the trees and attacks!")
    if "Rusty Sword" in inventory.items:
        print("You swing the rusty sword and the monkey screeches, escaped into the jungle. That was close!")
    elif "Glowing Herb" in inventory.items:
        print("The monkey manages to scratch you before you escape. You use the glowing herb to heal and regain strength.")
        print("Narrowly escaped, you catch your breath and continue.")
    else:
        print("The monkey bites you fiercely, and without defense or aid, you're too wounded to go on.")
        ending(False)
        return

    print("\nYou push forward deeper into the jungle and got behind a waterfall.")
    direction = input("The path splits! \nDo you follow the direction of cave or the cliff ? (cave /cliff ): ").strip().lower()
    print("\n")
    if direction == "cave":
        if "Broken Compass" in inventory.items:
            print("The compass confirms the direction leads to a hidden cave.")
            cave_path(inventory)
        else:
            print("Without guidance, you circle around and fall into a pit trap.")
            ending(False)
    elif direction == "cliff":
        print("You took the direction of cliff but it ends at a sharp fall. There's no way forward.")
        print("Suddenly, rocks Behind your feet crumble and you fall. The adventure ends here.")
        ending(False)
    else:
        print("You hesitate too long and lose your foot on the slippery rocks. You fall into the river below.")
        ending(False)

def cave_path(inventory):
    print("\nYou discover a cave guarded by Riddles.")
    answer1 = input("Solve the first riddle: What comes down but never goes up? (answer): ").strip().lower()
    if answer1 == "rain":
        print("Correct! You move deeper into the cave.")
        answer2 = input("Second riddle: What goes up, but never comes down? (answer): ").strip().lower()
        print("\n")
        if answer2 == "age":
            print("Brilliant! You have passed all the cave's challenges.")
            print("ROCK SLIDES AWAY!")
            print("Inside, you find the legendary treasure of Captain BlackPearl!")
            inventory.add_item("Captain BlackPearl's Treasure")
            ending(True)
        else:
            print("Wrong answer! A trap is triggered and the cave collapses.")
            ending(False)
    


def ending(victory):
    if victory:
        print("\nYOU WON!")
        print("\nCongratulations! You've found the hidden treasure and become a legendary pirate!")
    else:
        print("\nBad Luck, your journey ends in misfortune. Better luck next time, pirate!")