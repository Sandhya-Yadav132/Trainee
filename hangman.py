import time
import random
import os


categories = {
    "animals": [
        "ant", "bear", "camel", "cat", "cheetah",
        "cow", "deer", "dog", "dolphin", "elephant",
        "fox", "giraffe", "goat", "horse", "lion",
        "monkey", "rabbit", "tiger", "wolf", "zebra"
    ],

    "fruits": [
        "apple", "apricot", "banana", "cherry", "coconut",
        "fig", "grape", "guava", "kiwi", "lemon",
        "mango", "melon", "orange", "papaya", "peach",
        "pear", "pineapple", "plum", "strawberry", "watermelon"
    ],

    "vegetables": [
        "beetroot", "broccoli", "cabbage", "carrot", "cauliflower",
        "celery", "corn", "cucumber", "eggplant", "garlic",
        "ginger", "lettuce", "onion", "pea", "pepper",
        "potato", "pumpkin", "radish", "spinach", "tomato"
    ],

    "countries": [
        "argentina", "australia", "brazil", "canada", "china",
        "denmark", "egypt", "france", "germany", "india",
        "italy", "japan", "kenya", "mexico", "nepal",
        "norway", "portugal", "spain", "sweden", "thailand"
    ],

    "colors": [
        "beige", "black", "blue", "brown", "crimson",
        "cyan", "gold", "green", "indigo", "ivory",
        "lavender", "maroon", "orange", "pink", "purple",
        "red", "silver", "teal", "violet", "yellow"
    ],

    "sports": [
        "archery", "baseball", "basketball", "boxing", "cricket",
        "cycling", "football", "golf", "hockey", "judo",
        "karate", "rowing", "rugby", "skating", "skiing",
        "soccer", "swimming", "tennis", "volleyball", "wrestling"
    ],

    "vehicles": [
        "airplane", "bicycle", "boat", "bus", "car",
        "helicopter", "jeep", "locomotive", "motorcycle", "scooter",
        "ship", "skateboard", "submarine", "taxi", "tractor",
        "tram", "train", "truck", "van", "yacht"
    ],

    "professions": [
        "architect", "artist", "chef", "dentist", "designer",
        "doctor", "driver", "engineer", "farmer", "firefighter",
        "lawyer", "mechanic", "musician", "nurse", "painter",
        "pilot", "plumber", "scientist", "teacher", "writer"
    ],

    "household": [
        "blanket", "bottle", "bucket", "chair", "clock",
        "cooker", "curtain", "cushion", "drawer", "fan",
        "fridge", "kettle", "lamp", "mirror", "pillow",
        "plate", "shelf", "sofa", "table", "towel"
    ],

    "technology": [
        "android", "browser", "camera", "computer", "database",
        "desktop", "email", "internet", "keyboard", "laptop",
        "monitor", "mouse", "network", "printer", "program",
        "router", "server", "software", "tablet", "website"
    ],

    "birds": [
        "eagle", "falcon", "flamingo", "goose", "hawk",
        "heron", "kingfisher", "kiwi", "macaw", "owl",
        "parrot", "peacock", "pelican", "penguin", "pigeon",
        "robin", "sparrow", "swan", "turkey", "woodpecker"
    ],

    "insects": [
        "ant", "bee", "beetle", "butterfly", "caterpillar",
        "cockroach", "cricket", "dragonfly", "flea", "fly",
        "grasshopper", "hornet", "ladybug", "mosquito", "moth",
        "scorpion", "spider", "termite", "wasp", "weevil"
    ],

    "ocean": [
        "clam", "coral", "crab", "dolphin", "eel",
        "jellyfish", "lobster", "octopus", "oyster", "pelican",
        "plankton", "seahorse", "seal", "shark", "shrimp",
        "squid", "starfish", "stingray", "turtle", "whale"
    ],

    "clothing": [
        "blazer", "blouse", "boots", "cap", "coat",
        "dress", "gloves", "hat", "jacket", "jeans",
        "leggings", "pajamas", "pants", "scarf", "shirt",
        "shorts", "skirt", "socks", "sweater", "trousers"
    ],

    "food": [
        "burger", "burrito", "cake", "cereal", "curry",
        "dumpling", "fries", "lasagna", "noodles", "omelet",
        "pancake", "pasta", "pizza", "popcorn", "sandwich",
        "sausage", "soup", "steak", "taco", "waffle"
    ],

    "drinks": [
        "coffee", "cola", "cocoa", "espresso", "juice",
        "lemonade", "milk", "milkshake", "mocha", "smoothie",
        "soda", "tea", "water", "buttermilk", "cappuccino",
        "latte", "mocktail", "punch", "shake", "syrup"
    ],

    "places": [
        "airport", "beach", "bridge", "castle", "cinema",
        "college", "desert", "forest", "garden", "hospital",
        "library", "museum", "office", "park", "restaurant",
        "school", "stadium", "station", "theater", "zoo"
    ],

    "nature": [
        "canyon", "cave", "cliff", "cloud", "desert",
        "forest", "glacier", "hill", "island", "jungle",
        "lake", "mountain", "ocean", "rainbow", "river",
        "rock", "sky", "storm", "valley", "waterfall"
    ],

    "music": [
        "album", "banjo", "bass", "beat", "choir",
        "drum", "flute", "guitar", "harmony", "melody",
        "music", "opera", "piano", "rhythm", "singer",
        "song", "trumpet", "violin", "vocal", "xylophone"
    ],

    "school": [
        "algebra", "biology", "calculator", "classroom", "college",
        "dictionary", "exam", "homework", "library", "notebook",
        "pencil", "physics", "project", "science", "student",
        "teacher", "textbook", "university", "writing", "worksheet"
    ]
}

def show_welcome_message():
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("\n                  Welcome To HANGMAN\n")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    time.sleep(5)


def list_categories():
    print("\nAvailable Categories:\n")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")


def choose_category():
    category_names = list(categories.keys())
    choice = input("\nEnter category number: ")

    if choice == '':
        return random.choice(category_names)

    try:
        choice = int(choice)

        if choice >= 1 and choice <= len(category_names):
            return category_names[choice - 1]
        else:
            print("Invalid Choice")
            return random.choice(category_names)

    except ValueError:
        print("Invalid Input")
        return random.choice(category_names)


def pick_word(chosen_category):
    word = random.choice(categories[chosen_category])
    return word


def display_initial_state(word_length, category):
    os.system("cls" if os.name == "nt" else "clear")

    print("\nCategory:", category)
    print("\nWord:", end=" ")

    for _ in range(word_length):
        print("_", end=" ")
    print()

def game_setup():
    show_welcome_message()
    list_categories()
    category = choose_category()
    word = pick_word(category)
    word_length = len(word)
    display_initial_state(word_length, category)
    return word, len(word), category



# person 3
def guess_letter():
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter only one letter.")
            continue

        if not guess.isalpha():
            print("Please enter a valid letter.")
            continue
        return guess

def update_word_state(word, guesses):
    word_state = ""
    for letter in word:
        if letter in guesses:
            word_state += letter
        else:
            word_state += "_"
    return word_state

def check_win(word_state):
    return "_" not in word_state

def check_lose(incorrect_guesses):
    return incorrect_guesses >= 6

def draw_hangman(incorrect_guesses):
    if incorrect_guesses == 1:
        print("O")

    elif incorrect_guesses == 2:
        print("O")
        print("|")

    elif incorrect_guesses == 3:
        print(" O ")
        print("/|")

    elif incorrect_guesses == 4:
        print(" O ")
        print("/|\\")

    elif incorrect_guesses == 5:
        print(" O ")
        print("/|\\")
        print("/  ")

    elif incorrect_guesses == 6:
        print(" O ")
        print("/|\\")
        print("/ \\")

    return incorrect_guesses


def update_hangaman(incorrect_guesses):
    draw_hangman(incorrect_guesses)
    print(f"Incorrect guesses={incorrect_guesses}")


while True:
    word, word_length, category = game_setup()
    incorrect_guesses = 0
    correct_guess = 0

    guesses = []
    word_state = update_word_state(word, guesses)
    

    while True:
        print("Previous guesses:", guesses)
        guess = guess_letter()

        if guess in guesses:
            print("You already guessed that letter.")
            continue

        guesses.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            update_hangaman(incorrect_guesses)

        word_state = update_word_state(word, guesses)
        print("Word:", " ".join(word_state))
        

        if check_win(word_state):
            
            print("Congratulations! You won!")
            print("The word was:", word)
            # correct = print(check_win[1])
            print(f"Your Score is : {(len(word) * 2) - incorrect_guesses}")
            choice = input("Want to play again? (y/n): ").lower().strip()

            if choice == "y":
                break
            else:
                print("Thanks for playing!")
                exit()

        if check_lose(incorrect_guesses):
            print("Game Over!")
            print("The word was:", word)
            print(f"Your Score is : {correct_guess - incorrect_guesses}")

            choice = input("Want to play again? (y/n): ").lower().strip()

            if choice == "y":
                break
            else:
                print("Thanks for playing!")
                exit()