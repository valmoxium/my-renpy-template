
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## Replace this with your background image, if you like
image main_menu_background = "gui/main_menu_bg.png"

default persistent.disable_continue = True 
# This variable is used to deactivate the continue button

init python:
    def enable_continue_callback(*args, **kwargs):  # This function changes that variable, every time the game saves
        persistent.disable_continue = False
        renpy.save_persistent()

    config.save_json_callbacks.append(enable_continue_callback)

screen main_menu():
    $ recent_save = renpy.newest_slot()

    style_prefix "main_menu"

    ## This ensures that any other menu screen is replaced.
    tag menu

    add "main_menu_background"

    vbox:
        xalign 0.5
        yalign 0.75
        spacing 25

        textbutton _("{size=+5}New Game{/size}") action Start() alt "start a new game"

        if not persistent.disable_continue and recent_save is not None:
            textbutton _("{size=+5}Continue{/size}"):
                action Function(renpy.load, renpy.newest_slot())
                sensitive (renpy.newest_slot() is not None)

            textbutton _("{size=+5}Load Game{/size}") action ShowMenu("load") alt "load game"

        else:
            textbutton _("{size=+5}Load Game{/size}") action ShowMenu("load") alt "load game"

        textbutton _("{size=+5}Gallery{/size}") action ShowMenu("gallery") alt "access the gallery" #Change this to conditional later when gallery screen is figured out

    hbox:
        xalign 0.5
        yalign 0.9
        spacing 50 

        textbutton _("Settings") action ShowMenu("preferences") alt "open settings"

        textbutton _("About") action ShowMenu("about") alt "see about page"

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help") alt "open help menu"

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu) alt "quit game"

    hbox:
        xalign 0.95
        yalign 0.95

        textbutton _("Changelog") action OpenURL("valmoxium.itch.io/GAME/devlog") alt "Open change log. This will open your web browser."


style main_menu_button:
    xalign 0.5
