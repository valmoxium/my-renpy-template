init python:
    renpy.music.register_channel("Ambience", mixer="ambience") # channel is capitalized bc of the preferences menu. SUCKS
    renpy.music.register_channel("sound2", "sfx", loop=False) # for layering any SFX. may need more in the future. we will seeeee

    if not persistent.custom_volumes_set:
        persistent.custom_volumes_set = True
        preferences.set_volume('ambience', 0.8)