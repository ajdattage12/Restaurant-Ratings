"""Restaurant rating lister."""


import os
import sys

with open(os.path.join(sys.path[0], "scores.txt"), "r") as f:
   print(f.read())

restaurant = {
    "Florean Fortescue's Ice Cream Parlour" : 4,
    "Jellied Eel Shop" : 3,
    "The Tavern" : 3,
    "Luchino Caffe" : 1,
    "The Porcupine" : 5,
    "Diagon Alley cafe" : 2,
    "The Bear & Staff" : 2,
    "Ministry Munchies" : 1,
    "Chip Shop" : 3,
    "Eternelle's Elixir of Refreshment" : 5,
    "Big Bean Shack" : 3,
    "The Club" : 2
}

name = restaurant.keys
rating = restaurant.values

print (f"{name} is rated at {rating}.")