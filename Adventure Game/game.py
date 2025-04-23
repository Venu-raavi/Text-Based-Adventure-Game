# game.py
from story import intro_scene
from inventory import Inventory

def start_game():
    player_inventory = Inventory()
    intro_scene(player_inventory)
