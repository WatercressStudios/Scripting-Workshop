##########################
##
## ART SCRIPTING PART 2
##
#########################

label art_part2:

    "Very slowly fade in the BG"

    scene cockpit_ground with Dissolve(3.0)

    "Now dissolve through to it BG scene."

    scene cave with dissolve

    "Zoom into the BG scene..."
    show cave:
        ease 1.0 zoom 1.5

    "Zoomed in at 1.5x..."

    show le frustrated a2 with hpunch
    le "Arrived with a punch!"

    show le frustrated a1 with dissolve
    le "Dissolve into the next expression."

    show le:
        ease 1.0 xalign 1.0
    pause 1.0

    show le:
        xalign 1.0
        easein 0.2 ypos 0.95
        easeout 0.2 ypos 1.0
        repeat
    le "Bouncing up and down..."

    show le frustrated a2:
        xalign 1.0 ypos 1.0
        ease 1.0 zoom 1.5 ypos 1.5
    pause 1.0
    le "Zoom in a little bit..."

    "Sending Leona off by sliding her off screen before hiding."
    show le:
        xalign 1.0 ypos 1.5
        ease 1.0 xalign 2.0
    pause 1.0
    hide le

    scene black with dissolve
