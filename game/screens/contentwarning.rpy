## Content Warning ##################################
##
## A custom screen that warns players of possibly upsetting content in the game
## the first time they launch the game. Based on the About screen.
## https://www.renpy.org/doc/html/splashscreen_presplash.html
### Code is from BáiYù of tofurocks.

screen content_warning():

    tag menu

    frame:

        align(0.5, 0.5)
        xmargin 50
        xpadding 100

        vbox:
            
            xsize 1200
            align(0.5, 0.5)
            spacing 50
            # xfill True
            style_prefix "presplash"

            label _("Content Warning") xalign 0.5

            text _("This game is a work of pure fiction.\nThe views and opinions expressed herein do not reflect the views of the team who worked on this game, nor do we endorse such behavior.\nAny resemblance to persons living or dead is purely coincidental.") text_align 0.5 xalign 0.5

            null height 20

            text _("{b}Player discretion is advised{/b}.\n") text_align 0.5 xalign 0.5

            null height 40

            hbox:
                xalign 0.5
                spacing 100
                textbutton _("I understand") action Return() text_align 0.5 text_size 55
                textbutton _("Quit") action Quit(confirm=not main_menu) text_align 0.5 text_size 55
    