##########################
##
## DIALOGUE SCRIPTING PART 2
##
#########################

label dialogue_part2:
    "The MC will now say something. Observe their name title."

    mc "Hello. Who am I?"

    menu:
        "Your name is Anonymous":
            $ mc_name = "Anonymous"
        "Your name is no one.":
            $ mc_name = "no one."

    mc "I see... thank you. [mc_name] is a good name."

    "And henceforth, the MC is now known as [mc_name]."

    jump dialogue_part2_choose

#########################
label dialogue_part2_choose:
    "[mc_name] currently has [john_points] John point, and [smith_points] Smith point."

    if have_not_made_a_choice:
        mc "Um so who do I choose between John and Smith?"
    else:
        mc "Can you choose for me again?"

    menu:
        "You choose John":
            $ john_points = john_points + 1
            $ chose_john = True
        "You choose Smith":
            $ smith_points = smith_points + 1
            $ chose_john = False

    $ have_not_made_a_choice = False

    jump dialogue_part2_after_choosing

#########################
label dialogue_part2_after_choosing:
    mc "I see."

    if not chose_john:
        mc "Do you hate John?"
    else:
        mc "Do you like John?"

    menu:
        "Wait, I'll choose again.":
            jump dialogue_part2_choose
        "We're done here.":
            pass

    "The end!"
