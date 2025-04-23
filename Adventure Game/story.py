# story.py
from locations import beach_path, jungle_path, cave_path, ending

def intro_scene(inventory):
    print("\nWelcome to 'TREASURE HUNT on PIRATE ISLAND!'")
    print("You are a young pirate seeking the Legendary Treasure of Captain BlackPearl.")
    print("You land on the Island with only a map and your Intelligence.\n")
    
    beach_path(inventory)