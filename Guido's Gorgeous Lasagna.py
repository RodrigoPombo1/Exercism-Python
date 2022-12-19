"""Functions used in preparing Guido's gorgeous lasagna.
 
Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""
# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40
# TODO: consider defining the 'PREPARATION_TIME' constant
PREPARATION_TIME = 2 # per layer
#       equal to the time it takes to prepare a single layer
# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
 
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.
 
    :param number_of_layers: int - number of layers.
    :return: int - total preparation time of all the layers.
 
    Function that takes the number of layers and returns how much time it will take to prepare all the layers.
    """
    return PREPARATION_TIME * number_of_layers
# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.
 
    :param number_of_layers: int - the number of layers added to the lasagna.
    :param elapsed_bake_time: int - the number of minutes the lasagna has been baking in the oven.
    :return: int - remaining bake time (in minutes).
 
    Function that returns the total number of minutes you've been cooking, or the sum of your preparation 
    time and the time the lasagna has already spent baking in the oven
    """
    return PREPARATION_TIME * number_of_layers + elapsed_bake_time