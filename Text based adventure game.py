import time

rooms = {
    "entrance": {
        "description": "You stand at the entrance of a mysterious ancient castle. Two paths lie ahead.",
        "choices": {
            "1": ("Enter the dark forest", "forest"),
            "2": ("Walk toward the abandoned village", "village")
        }
    },
    "forest": {
        "description": "Tall trees surround you. You discover a glowing key beside an old tree.",
        "item": "glowing key",
        "choices": {
            "1": ("Follow a narrow trail", "river"),
            "2": ("Return to the castle entrance", "entrance")
        }
    },
    "village": {
        "description": "The village is silent. Inside an abandoned house, you find a mysterious map.",
        "item": "ancient map",
        "choices": {
            "1": ("Explore the ruined tower", "tower"),
            "2": ("Return to the castle entrance", "entrance")
        }
    },
    "river": {
        "description": "A deep river blocks your path. An old wooden bridge leads to a hidden cave.",
        "choices": {
            "1": ("Cross the bridge", "cave"),
            "2": ("Return to the forest", "forest")
        }
    },
    "tower": {
        "description": "You climb the ruined tower and discover a locked treasure chest.",
        "choices": {
            "1": ("Try opening the chest", "treasure"),
            "2": ("Descend to the village", "village")
        }
    },
    "cave": {
        "description": "Inside the cave, you find a massive stone door with a glowing keyhole.",
        "choices": {
            "1": ("Use the glowing key", "secret"),
            "2": ("Return to the river", "river")
        }
    },
    "treasure": {
        "description": "The treasure chest is locked. Perhaps something you found can open it.",
        "choices": {
            "1": ("Use the ancient map as a clue", "map_ending"),
            "2": ("Leave the tower", "village")
        }
    },
    "secret": {
        "description": "The key unlocks the stone door. Beyond it lies a chamber filled with ancient treasures.",
        "ending": "treasure"
    },
    "map_ending": {
        "description": "The map reveals a hidden mechanism. The chest opens, revealing a legendary crown!",
        "ending": "crown"
    }
}

inventory = []


def display_text(text):
    print("\n" + text)
    time.sleep(0.5)


def show_inventory():
    if inventory:
        print("Inventory:", ", ".join(inventory))
    else:
        print("Inventory: Empty")


def collect_item(room):
    item = rooms[room].get("item")

    if item and item not in inventory:
        inventory.append(item)
        display_text(f"You discovered and collected: {item}!")


def choose_option(choices):
    for number, (description, destination) in choices.items():
        print(f"{number}. {description}")

    while True:
        choice = input("\nChoose an option: ").strip()

        if choice in choices:
            return choices[choice][1]

        print("Invalid choice. Please try again.")


def play_game():
    current_room = "entrance"

    display_text("WELCOME TO THE MYSTERIOUS CASTLE!")
    display_text("Explore forgotten places, discover secrets, and choose your destiny.")

    while True:
        room = rooms[current_room]

        display_text(room["description"])

        collect_item(current_room)
        show_inventory()

        if current_room == "cave":
            if "glowing key" not in inventory:
                print("\nYou do not have the glowing key.")
                print("The stone door remains locked.")
                current_room = "river"
                continue

        if current_room == "treasure":
            if "ancient map" not in inventory:
                print("\nYou have no map to help unlock the chest.")
                print("You return to the village to search for clues.")
                current_room = "village"
                continue

        if "ending" in room:
            if room["ending"] == "treasure":
                display_text("ENDING: THE HIDDEN TREASURE")
                display_text("You uncover a forgotten fortune and become the castle's new guardian.")
            elif room["ending"] == "crown":
                display_text("ENDING: THE LEGENDARY CROWN")
                display_text("You claim the legendary crown and become ruler of the ancient kingdom.")

            break

        current_room = choose_option(room["choices"])

    print("\nThanks for playing!")


if __name__ == "__main__":
    play_game()