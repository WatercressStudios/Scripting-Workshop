##########################
##
## DIALOGUE SCRIPTING PART 1
##
#########################
label dialogue:
    "This is text that a narrator will say in Ren'Py."

    "This is what the narrator will continue with after a click."

    joh "Hello, Smith."

    smi "Hello, John."

    "Now let's jump to a different 'label'."

    jump dialogue_continued

##########################
label dialogue_continued:
    "The VN experiences no interruption after jumping to this label."

    "Now, let's make a choice:"

    menu:
        "John, I choose you!":
            jump dialogue_john
        "Smith, I choose you!":
            jump dialogue_smith

##########################
label dialogue_john:
    "The player has chosen John."

    jump dialogue_common

##########################
label dialogue_smith:
    "The player has chosen Smith."

    jump dialogue_common

##########################
label dialogue_common:
    "Both story branches are now back in the common label."

    "{i}This is italics{/i}. {b}This is bold{/b}."

    "{size=+10}Bigger{/size}, {size=-10}Smaller{/size}."

    "{s}Strike-through{/s}, and {u}underlined{/u}."

# https://www.renpy.org/doc/html/text.html
