## ATLs for my projects

############################################################################
## From https://lemmasoft.renai.us/forums/viewtopic.php?t=69468 ############
############################################################################

# DISPLAY IMAGE ############################################################
# This sets the transparency to 0 and then takes 1 second to return to 100%.
# This is useful when you want to display the image a little faster than dissolve, but more slowly than instantaneous.

transform b_fade: 
        alpha 0.0 
        easein 1.0 alpha 1.0

# PRECISE PLACEMENT ########################################################
# This is useful when you want to specify more precise placement than the default .

transform two_right: 
        xalign 0.25

# MOVEMENT #################################################################
#  If you lower it a little, it may look like it's doing some kind of movement.

transform ugougo: 
        yoffset 0 
        linear 0.1 yoffset 50 
        linear 0.1 yoffset 0

transform ugo2: 
        yoffset 0 
        linear 0.2 yoffset 10 
        linear 0.2 yoffset 0

# ATTACK DAMAGE ############################################################
#  It's a movement that looks like it's been damaged

transform damage: 
        ease .06 yoffset 34 
        ease .06 yoffset 5 
        ease .05 yoffset 30 
        ease .05 yoffset 5 
        ease .04 yoffset 26 
        ease .04 yoffset 5 
        ease .03 yoffset 22 
        ease .03 yoffset 5 
        ease .02 yoffset 18 
        ease .02 yoffset 2 
        ease .01 yoffset 14 
        ease .01 yoffset 2 
        ease .01 yoffset 0

# SCARED TREMBLING #########################################################
#  It will continue to shake until you specify show~ again or hide.

transform shake2(rate= 0.090 ): 
        linear rate xoffset 2 yoffset 0 
        linear rate xoffset - 2.8 yoffset 2 
        linear rate xoffset 2.8 yoffset 0 
        linear rate xoffset - 2 yoffset 2 
        linear rate xoffset + 0 yoffset + 0 
        repeat


# STEPPING AROUND #########################################################
#  (If you click the mouse rapidly, it may not return to the zoom position.)

transform stepfwd: 
        yoffset 0 
        linear 0.2 yoffset 10
        ease .5 zoom 1.1 yalign 0.1
        linear 0.2 yoffset 0

transform stepfwd2: 
        yoffset 0 
        linear 0.2 yoffset 10 
        ease .5 zoom 1.25 yalign 0.1
        linear 0.2 yoffset 0

transform stepback: 
        yoffset 0 
        linear 0.2 yoffset 10 
        ease .5 zoom 1.1 yalign 1.0 yoffset 0
        linear 0.2 yoffset 0

transform stepback2: 
        yoffset 0 
        linear 0.2 yoffset 10 
        ease .5 zoom 1.0 yalign 1.0 yoffset 0
        linear 0.2 yoffset 0

transform stepback1: 
        yoffset 0 
        linear 0.2 yoffset 10 
        ease .5 zoom 0.9 yalign 1.0 yoffset 0        
        linear 0.2 yoffset 0

transform stepleft:
        yoffset 0 
        xoffset 0
        linear 0.2 yoffset 10 
        linear 0.3 xoffset -125 
        linear 0.2 yoffset 0

transform stepcenter:
        yoffset 0 
        linear 0.2 yoffset 10
        linear 0.3 xoffset 0
        linear 0.2 yoffset 0

transform stepright:
        yoffset 0 
        xoffset 0
        linear 0.2 yoffset 10 
        linear 0.3 xoffset 125
        linear 0.2 yoffset 0


# ROLLING SHAKE #############################################################
#  It literally rocks side to side. 

transform rollshake(rate= 0.090 ): 
        linear rate xoffset 2 
        linear rate xoffset - 2.8 
        linear rate xoffset 2.8 
        linear rate xoffset - 2 
        linear rate xoffset + 0 
        repeat