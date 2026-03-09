# ## Splashscreen ############################################################
# ## A portion of the game that plays at launch, before the main menu is shown.
# ## https://www.renpy.org/doc/html/splashscreen_presplash.html

# ## The animation is boring so I recommend using something else.
# ## ATL documentation: https://www.renpy.org/doc/html/atl.html

# image splash_anim_1:
#     #replace this during actual development 
#     "gui/renpy-logo.png"
#     xalign 0.5 yalign 0.5

# default persistent.firstlaunch = False

# label splashscreen:
    
#     scene black

#     ## Here begins our splashscreen animation.
#     show splash_anim_1
#     show text "{size=60}username{/s}":
#         xalign 0.5 yalign 0.7

#     pause(2)

#     scene black
#     with fade
 
#     label skip_splash:
 
#         pass
    
#     call screen content_warning

#     ## The first time the game is launched, players can set their accessibility settings.
#     if not persistent.firstlaunch:

#         call screen splash_settings

#         call screen preferences

#         ## This screen will not appear in subsequent launches of the game when
#         ## the following variable becomes true.
#         $ persistent.firstlaunch = True

#     return


# ## Splashscreen Settings ##################################
# ##
# ## A custom screen that tells players to adjust their settings in the Preferences
# ## Screen. Edited so you don't have to keep track of two different pages.

# screen splash_settings():

#     tag menu

#     frame:

#         align(0.5, 0.5)
#         xmargin 50
#         xpadding 100

#         vbox:
            
#             align(0.5, 0.5)
#             spacing 50
#             # xfill True
#             style_prefix "presplash"

#             label _("First-Time Setup") xalign 0.5

#             text _("You can set your game settings in the next menu. These options can be adjusted at any time.") text_align 0.5 xalign 0.5

#             textbutton _("Okay") action Return() xalign 0.5 text_align 0.5 text_size 55

# style presplash_label:
#     top_margin 3
#     bottom_margin 3
#     text_align 0.5

# style presplash_label_text:
#     yalign 1.0
#     size 100
