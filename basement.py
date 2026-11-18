import random

inventory = []
current_room = "basement"
turns = 0

print("=" * 50)
print("        ESCAPE FROM THE BASEMENT")
print("=" * 50)
print("You wake up on a cold concrete floor.")
print("You don't remember how you got here.")
print("Somewhere above you a door slams shut.")
print()
print("Type 'help' if you're lost.")
print()

while True:
    turns = turns + 1
    print("-" * 50)

    # show the room
    if current_room == "basement":
        print("BASEMENT")
        print("Dusty shelves. A wobbly staircase leads UP.")
        print("A small window is boarded shut with planks.")
        print("A rat watches you from the corner.")
    elif current_room == "hallway":
        print("HALLWAY")
        print("Peeling wallpaper. Doors lead WEST and EAST.")
        print("The front door is SOUTH. The basement is DOWN.")
    elif current_room == "kitchen":
        print("KITCHEN")
        if "rusty key" in inventory:
            print("Dirty dishes everywhere. The counter is empty now.")
        else:
            print("Dirty dishes everywhere. A rusty key sits on the counter.")
        print("The hallway is EAST.")
    elif current_room == "workshop":
        print("WORKSHOP")
        if "crowbar" in inventory:
            print("Sawdust and tools. The bench is empty now.")
        else:
            print("Sawdust and tools. A crowbar leans on the bench.")
        print("The hallway is WEST.")
    elif current_room == "porch":
        print("PORCH")
        print("Cold night air. You're outside. The road is right there.")
        print("You can walk NORTH to the road.")

    print()
    command = input("> ").strip().lower()
    words = command.split()
    verb = ""
    if len(words) > 0:
        verb = words[0]

    if verb == "help":
        print("commands: look, inventory, take <thing>, use <thing>,")
        print("          go <direction>, quit")

    elif verb == "look":
        print("You look around really hard. Nothing new.")

    elif verb == "inventory" or verb == "i":
        if len(inventory) == 0:
            print("You are carrying nothing.")
        else:
            print("You have: " + ", ".join(inventory))

    elif verb == "quit":
        print("You sit down on the floor and give up. The rat wins.")
        break

    elif verb == "take":
        thing = ""
        if len(words) > 1:
            thing = words[1]

        if current_room == "kitchen" and thing == "key" or thing == "rusty key":
            if "rusty key" in inventory:
                print("You already took it.")
            elif current_room == "kitchen":
                inventory.append("rusty key")
                print("You pocket the rusty key.")
            else:
                print("There's no key here.")
        elif current_room == "workshop" and thing == "crowbar":
            if "crowbar" in inventory:
                print("You already took it.")
            else:
                inventory.append("crowbar")
                print("You pick up the crowbar. It's heavier than it looks.")
        else:
            print("You can't take that.")

    elif verb == "use":
        thing = ""
        if len(words) > 1:
            thing = words[1]

        if thing == "key":
            if "rusty key" not in inventory:
                print("You don't have a key.")
            elif current_room == "hallway":
                print("The key grinds in the lock. The front door swings open.")
                print("You step out onto the porch.")
                current_room = "porch"
            else:
                print("No lock to use it on here.")
        elif thing == "crowbar":
            if "crowbar" not in inventory:
                print("You don't have a crowbar.")
            elif current_room == "basement":
                print("You wedge the crowbar under the planks and pull.")
                print("The boards splinter away. Moonlight pours in.")
                print("You squeeze through the window and drop outside.")
                current_room = "porch"
            else:
                print("Nothing to pry open here.")
        else:
            print("You can't use that.")

    elif verb == "go" or verb == "walk":
        direction = ""
        if len(words) > 1:
            direction = words[1]

        if current_room == "basement" and direction == "up":
            current_room = "hallway"
        elif current_room == "hallway" and direction == "down":
            current_room = "basement"
        elif current_room == "hallway" and direction == "west":
            current_room = "kitchen"
        elif current_room == "hallway" and direction == "east":
            current_room = "workshop"
        elif current_room == "kitchen" and direction == "east":
            current_room = "hallway"
        elif current_room == "workshop" and direction == "west":
            current_room = "hallway"
        elif current_room == "porch" and direction == "north":
            print()
            print("You walk down the driveway and don't look back.")
            print("YOU ESCAPED in " + str(turns) + " turns!")
            break
        elif current_room == "hallway" and direction == "south":
            if "rusty key" in inventory:
                print("The front door is locked. Maybe try 'use key'.")
            else:
                print("The front door is locked and you have no key.")
        else:
            print("You can't go that way.")

    else:
        print("That's not a command. Try 'help'.")

    # little random flavor so it isn't totally static
    if random.randint(1, 8) == 1:
        print("[the house creaks somewhere above you]")