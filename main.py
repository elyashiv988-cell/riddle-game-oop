from game import*
from player import*
from ridlle_repository import *
import json

def get_path():
    with open("data.json", "r") as file:
        raw_data = json.load(file)
        return raw_data




riddles=RiddleRepository(get_path())

game=RiddleGame(Player(input("Enter your name: ")),riddles.load_riddles(),[])
game.print_summary(game.start())

