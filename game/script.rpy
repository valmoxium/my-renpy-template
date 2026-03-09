# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define e_nvl = Character("Eileen", kind=nvl)
define narrator = Character(None, what_italic=True)
define narrator_nvl = Character(None, what_italic=True, kind=nvl)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Did you change the name and save directory of the game in options.rpy?"

    $ answer = renpy.input("Did you change the values at the top of options.rpy?").strip().lower()

    if answer == "yes":
        "Good job"
    else:
        e "If not, you should do so right away! Saves will not work properly until you do."

    $ renpy.notify("This is a notification")

    menu:
        "This is a sample choice menu"
        "Choice 1":
            pass
        "Choice 2":
            pass
    
    e "Line 1{p}Line 2{p=1.0}Line 3"
    
    e_nvl "Now let's test out NVL mode."
    narrator_nvl "Lorem ipsum dom porum"


    # This ends the game.

    scene black with dissolve
    pause 2.0
    
    $ persistent.disable_continue = True
    
    return
