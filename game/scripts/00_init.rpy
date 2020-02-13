##########################
##
## DIALOGUE SCRIPTING PART 2
##
#########################

define joh = Character("John")
define smi = Character("Smith")
define mc = DynamicCharacter("mc_name")

default mc_name = "???"
default john_points = 0
default smith_points = 0
default have_not_made_a_choice = True
default chose_john = False

##########################
##
## ART SCRIPTING PART 1
##
#########################

define le = Character("Leona", callback=speaker("le"))

init python:
    # Automatically register images in that folder
    DefineImages('images/bgs')

# Register solid colors as images too
image black = Solid("#000")
image red = Solid("#B55")


##########################
##
## START LABEL
##
#########################

label start:
    menu:
        "Dialogue, Part 1 - Basics":
            jump dialogue
        "Dialogue, Part 2 - Variables and flow control":
            jump dialogue_part2
        "Art, Part 1 - Basics":
            jump art
        "Art, Part 2 - Animations":
            jump art_part2
