screen changelog():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use game_menu(_("Changelog"))

    viewport:
        style_prefix 'game_menu'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical" yinitial 1.0

        has vbox

        style_prefix "history"
                
        label "{size=+2}0.1a (2/6/25){/size}"
        text "- Hello world!\n- Added changelog"