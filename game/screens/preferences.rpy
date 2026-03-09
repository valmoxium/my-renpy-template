
## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use game_menu(_("Settings"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"
        has vbox

        # General options, toggles
        vbox:
            spacing 20
            box_wrap True
            if renpy.variant("pc") or renpy.variant("web"):
                # Only need fullscreen/windowed on desktop and web builds

                hbox:
                    style_prefix "radio"
                    label _("Display")
                    textbutton _("Window"):
                        # Ensures this button is selected when
                        # not in fullscreen.
                        selected not preferences.fullscreen
                        action Preference("display", "window")
                    textbutton _("Fullscreen"):
                        action Preference("display", "fullscreen") xoffset 20

            hbox:
                style_prefix "check"
                label _("Skip")
                textbutton _("Unseen Text"):
                    action Preference("skip", "toggle")
                textbutton _("After Choices"):
                    action Preference("after choices", "toggle") xoffset 20
                textbutton _("Transitions"):
                    action InvertSelected(Preference("transitions", "toggle")) xoffset 40

            hbox:

                label "Toggle":
                    style_prefix "check"        

                vbox: 
                    hbox: 
                        style_prefix "check"
                        textbutton _("Sound Captions"):
                            action ToggleVariable("persistent.sound_captions") alt "Toggle Sound Captions"

                        textbutton _("Image Captions"):
                            action ToggleVariable("persistent.image_captions") alt "Toggle Image Captions" xoffset 20

                    # Self-voicing does not work on smartphone devices, so this option only shows if the user is playing on a PC.
                        if renpy.variant("pc"):
                            textbutton _("Self-Voicing") action Preference("self voicing", "toggle") alt "Toggle Self-Voicing" xoffset 40
                    # This shows Ren'Py's built-in accessibility menu, added to Ren'Py in Ren'Py 7.2.2. This can also be displayed by pressing "A" on the keyboard when playing on a PC. As this option can break the way the game is displayed and also does not support translation as of Ren'Py build 7.3.2, you may want to hide the option. The button should also be removed if your version of Ren'Py is under 7.2.2, as the menu does not exist in previous versions.
                    hbox:
                        style_prefix "check"
                        textbutton _("Screenshake"):
                            action ToggleField(persistent,"screenshake",true_value=True,false_value=False) alt "Toggle Screenshake" 
                        textbutton _("More Options...") action Show("_accessibility") ypos 7 alt "Open More Options" style "button" xoffset 20                                             
            
#            null height 10

        ## Text Options

        vbox:
            style_prefix "header"
            label "Text"

        vbox: 
            box_wrap True
            spacing 20

            hbox:
                style_prefix "radio"
                label "Dialogue Font"

                textbutton "{font=fonts/StampatelloFaceto.otf}{size=24}Default{/size}{/font}":
                    action [gui.SetPreference("font", "fonts/StampatelloFaceto.otf"), SetVariable("persistent.typeface", "Stampatello Faceto")] 
                    alt "Change dialogue font to default"
                    selected persistent.typeface == "Stampatello Faceto"
                
                textbutton "{font=fonts/Vollkorn.ttf}Serif{/font}":
                    action [gui.SetPreference("font", "fonts/Vollkorn.ttf"), SetVariable("persistent.typeface", "Vollkorn")]
                    alt "Change dialogue font to serif"
                    selected persistent.typeface == "Vollkorn"
                    xoffset 16

                textbutton "{font=fonts/Cadman_Roman.otf}Sans Serif{/font}":
                    action [gui.SetPreference("font", "fonts/Cadman_Roman.otf"), SetVariable("persistent.typeface", "Cadman")]
                    alt "Change dialogue font to sans serif"
                    selected persistent.typeface == "Cadman"  
                    xoffset 40              
            
            hbox: 
                style_prefix "radio"
                label "Dialogue Size"
                
                textbutton "{size=24}Default{/size}":
                    action [gui.SetPreference("size", 24)] 
                    alt "Change dialogue size to default"
                textbutton "{size=28}Large{/size}":
                    action [gui.SetPreference("size", 28)]
                    alt "Change dialogue size to large" xoffset 20

            hbox:
                style_prefix "radio"
                label "Dialogue Color"

                textbutton _("White") action gui.SetPreference("color", "#ffffff") alt "Change dialogue color to white" 
                textbutton _("Cream") action gui.SetPreference("color", "#FFFDD0") text_idle_color "#FFFDD0" alt "Change dialogue color to cream" xoffset 32           

            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.

            null height 10

        # Text, volume adjustment
        vbox:
            style_prefix "slider"
            box_wrap True

            hbox:
                label _("Text Speed")
                bar value Preference("text speed") alt "Adjust text speed"

            vbox:
                hbox:
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time") alt "Adjust auto-forward time speed"
            
            vbox:
                hbox:
                    label _("Textbox Opacity")
                    bar value FieldValue(persistent, 'say_window_alpha', 1.0, max_is_zero=False, offset=0, step=.2) xsize 500 style "slider" yalign 0.5 alt "Adjust textbox opacity"

        vbox:
            style_prefix "header"
            label "Audio"

        vbox: 
            style_prefix "slider"
            box_wrap True

            vbox:
                if config.has_music:
                    hbox:
                        label _("Music Volume")
                        bar value Preference("music volume") alt "Adjust music volume"
 
                if config.has_sound:
                    hbox:
                        label _("Sound Volume")
                        bar value Preference("sound volume") alt "Adjust sound volume"
                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)
            
                hbox:
                    label _("Ambience Volume")
                    bar value Preference("ambience volume") alt "Adjust ambience volume"

                if config.has_voice:
                    hbox:
                        label _("Voice Volume")
                        bar value Preference("voice volume") alt "Adjust voice volume"
                        if config.sample_voice:
                            textbutton _("Test") action Play("voice", config.sample_voice) 

### PREF
style pref_label:
    xsize 450
    xoffset 60

style pref_label_text:
    yalign 0.5
    outlines [ (1, "#2b262609", 0, 0),  (2, "#00000007", 0, 0), (3, "#00000010", 0, 0), (4, "#00000007", 0, 0) ]

style pref_vbox:
    yalign 0.5
    spacing 30

style pref_hbox:
    align (0.5,0.5)
    xfill True
    spacing 20

## RADIO
style radio_label:
    is pref_label

style radio_label_text:
    is pref_label_text

style radio_vbox:
    is pref_vbox

style radio_hbox:
    yalign 0.5

style radio_button:
    foreground "gui/button/radio_[prefix_]foreground.png"
    padding (35, 6, 6, 6)
    yalign 0.5

## CHECK
style check_label:
    is pref_label
    
style check_label_text:
    is pref_label_text

style check_vbox:
    is pref_vbox

style check_hbox:
    spacing 0

style check_button:
    foreground "gui/button/check_[prefix_]foreground.png"
    padding (35, 6, 6, 6)

## SLIDER
style slider_label:
    is pref_label
style slider_label_text:
    is pref_label_text

style slider_slider:
    xsize 500
    yalign 0.5

style slider_button:
    yalign 0.5
    left_margin 15

style slider_vbox:
    is pref_vbox
    xsize 500

style header_label:
    text_align 0.5
    align(0.5,0.5)

style header_vbox:
    align (0.5,0.5)
    ysize 200
    spacing 100