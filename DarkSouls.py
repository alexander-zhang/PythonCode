# type "backpack" to open backpack.


def dead(why):
    print why, "You Died."
    exit(0)


def add_to_backpack(item):
    backpack.append(item)


def open_backpack():
    print "You open your backpack.\n"
    for stuff in backpack:
        print '{}'.format(stuff)


# idk why this loops only once if you type else. It so weird. Only does this if I start
# script with graveyard. So I don't anymore.
def path_choice():
    print "Which path do you choose?"

    action = raw_input("Path: ")

    if "exit" in action:
        print "You see a massive sword sticking out of the ground, and two large doors behind it."
    elif "dark" in action or "cave" in action:
        cave()
    else:
        print "That's not a path."
        path_choice()


def graveyard():
    print "You are in a graveyard which is empty and ominous."
    print "You see an an exit in the distance, and a dark cave to your left."

    while "Rusty Sword" not in backpack:
        print "There is a rusty sword on the ground."
        rusty_sword()

    path_choice()
    return None


def rusty_sword():
    print "You see a rusty sword on the ground."
    print "Do you pick up the rusty sword?"

    action = raw_input("Action: ")

    if "yes" in action:
        print "Rusty Sword added to the bag."
        add_to_backpack("Rusty Sword")
        first_encounter()
    elif "no" in action:
        print "You leave the rusty sword on the ground."
        first_encounter()
    elif "backpack" in action:
        open_backpack()
        rusty_sword()
    else:
        print "Type either \"yes\", \"no\", or \"backpack\""
        rusty_sword()


def first_encounter():
    print "A nearby skeleton animates and starts walking towards you."
    print "Do you fight or run?"
    cornered = False
    exhausted = False

    while True:
        action = raw_input("Action: ")

        if "fight" in action and "Rusty Sword" in backpack:
            print "You use your sword to stab the skeleton through the rib socket."
            print "The skeleton crumbles to dust."
            graveyard()
            return None
        elif "fight" in action and "Rusty Sword" not in backpack:
            dead("You punch the skeleton. It does nothing.")
        elif "run" in action and "Rusty Sword" not in backpack and not exhausted:
            print "You see the rusty sword on the ground as you run back to where you came from."
            print "Do you pick it up?"
            choice = raw_input("Pick up? ")

            if choice == "yes":
                print "You picked it up."
                add_to_backpack("Rusty Sword")
            elif choice == "no":
                print "You leave it on the ground."
                exhausted = True
            else:
                dead("Too slow. The skeleton caught you.")

            print "Do you fight, run, or surrender?"
        elif "run" in action and "Rusty Sword" in backpack and not cornered:
            print "You run until you are trapped against the wall."
            print "Do you fight, run, or surrender?"
            cornered = True
        elif "run" in action and cornered or exhausted:
            dead("You run into the wall and fall to the floor unconscious.")
        elif "run" in action and cornered:
            dead("You run into the wall and fall to the floor unconscious.")
        elif "surrender" in action and "Rusty Sword" in backpack and cornered:
            dead("The dead have no mercy.")
        else:
            dead("You stand there paralyzed as the skeleton rips your body apart.")


# In Progress
def cave():
    print "You pick up a torch from the the wall of the cave."
    print "You arrive at a fork in the cave."
    print "The left path has light in the distance. The right path is pitch black."
    print "The pitch black path has footprints on the floor heading deeper."
    print "Which path do you follow?"

    action = raw_input("Left or Right?: ")

    if action == "left" or action == "Left":
        dead("Test the LEFT")
    elif action == "right" or action == "Right":
        dead("Test the RIGHT")
    else:
        dead("Test Else Cave")


backpack = []

print "You wake up in a graveyard with nothing but a backpack."
rusty_sword()

