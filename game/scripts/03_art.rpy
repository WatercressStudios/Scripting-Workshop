##########################
##
## ART SCRIPTING PART 1
##
#########################

label art:
    "Show BG in the next line as a scene."

    scene cave

    "Cave now shown as a scene."

    "Go to a different BG scene."

    scene cockpit_ground

    "Arrived!"

    "Can also fade to solid colors, defined by HEX codes. E.g."

    scene red

    "Go to red..."

    jump art_sprites

label art_sprites:

    show le speaking a1
    le "Hi, this is Leona speaking!"

    show le frustrated a2
    le "Now with a {b}very{/b} different expression..."

    hide le
    "Hiding Leona away."

    jump art_part2
