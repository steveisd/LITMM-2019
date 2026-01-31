label act_4_start:
    show riddleman amused
    u "Why, me of course, the ruler of this museum."
    a "What, are you nuts?"
    show riddleman sneer
    u "Oh, you kiddy kid! You should know we are not just ordinary paper."
    show riddleman smile
    u "We represent the knowledge of this home you call a 'museum'."
    u "The knowledge is written on us, and to protect this knowledge, we were given life."
    show riddleman lefthand
    u "We are guardians of the Mind Museum!"
    show riddleman at talk_end
    a "..."
    a "Well, this plot is starting to go downhill..."
    show riddleman smile at talk_start
    u "We are not fiction, myths, or fictional myths or mythical fiction! All I say are the same, but I assure you we are real, and-"
    a "Just tell me your riddle danggit."
    show riddleman mad
    u "Very well!"
    "..."
    show riddleman smile
    u "Who am I?{w=1} I am taller when I sit and I am shorter when I stand-"
    menu:
        "Dog":
            pass
    show riddleman at talk_end
    a "Dog."
    "..."
    show riddleman mad
    u "Very well,"
    show riddleman at talk_start
    u "Let's see how long you last."
    a "My turn."
    play sound ruffle_5
    show riddleman shout:
        ypos 720 xalign 0.5
        linear 0.05 ypos 730
        pause 0.05
        linear 0.05 ypos 720
        pause 0.05
        linear 0.05 ypos 730
        pause 0.05
        linear 0.05 ypos 720
        pause 0.05
        linear 0.05 ypos 730
        pause 0.05
        linear 0.05 ypos 720
    u "No!"
    show riddleman amused
    u "Only I shall give the riddles."
    show riddleman at talk_end
    a "Fine."
    "If it means we get to do this quicker, or that I don't have to do anything much."
    a "Bring it on."
    $ renpy.pause(delay=0.5, hard=True)
    return
