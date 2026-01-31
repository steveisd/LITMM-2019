label act_5_start:
    play music riddle_battle
    show riddleman smile at talk_start
    u "Prepare yourself!"
    "..."
    u "My first riddle:"
    #python:
        #readle = open(riddle_text[13:-27], "r")
        #riddles = readle.readlines()
        #readle.close()
    jump act_5_riddles

label act_5_over:
    $ riddle_attempts += 1
    show riddleman shout
    $ riddle_wrong = renpy.random.choice(["...Wrong!", "WRONG!", "That is WRONG!", "Incorrect!", "By goodness, you are wrong!", "Haha, wrong!"])
    u "%(riddle_wrong)s"
    if riddle_attempts > 3:
        u "The answer is %(answer)s."
        pause 1
        show riddleman smile
        u "And so, you have lost..."
        pause 5
        $ renpy.quit(relaunch=False, status=0) #or wake up? or #i was turned into a book... (ok???)
    else:
        $ chance = renpy.random.randint(1, 10)
        if chance > 10:
            show riddleman mad
            $ riddle_chances = renpy.random.choice(["Try again.", "I'll give you another chance."])
            u "%(riddle_chances)s"
        jump act_5_riddle_answer

label act_5_more_riddles:
    $ another_riddle = renpy.random.choice(["Here's another riddle:", "Okay, now answer this:", "That's not all! Answer this:", "Next one:", "Grrr...", "Hmp!"])
    u "%(another_riddle)s"
    jump act_5_riddles

label act_5_riddles:
    python:
        renpy.random.shuffle(riddles)
        chosen = renpy.random.choice(riddles)
        riddles.remove(chosen)
        riddle_now = chosen[8:]
        answer = ' '.join(riddle_now.split(" ")[riddle_now.split(" ").index("Answer:") + 1:]).strip().lower()
        if answer.endswith(" "):
            answer = answer[:-1]
        if answer.endswith("."):
            answer = answer[:-1]
        riddle_now = ' '.join(riddle_now.split(" ")[:riddle_now.split(" ").index("Answer:")])
    show riddleman smile
    u "%(riddle_now)s"

label act_5_riddle_answer:
    #timer here? #nah
    $ renpy.block_rollback()
    show riddleman smile
    $ riddle_guess = renpy.input(_("")).strip().lower()
    if answer.lower() in riddle_guess:
        $ right_riddles += 1
        $ riddle_attempts = 0
        show riddleman mad
        $ riddle_huh = renpy.random.choice(["Huh...", "Really?", "You just got lucky.", "Fine then.", "That's... correct.", "That is the answer.", "Correct.", "That is correct."])
        u "%(riddle_huh)s"
    elif riddle_guess == "debug_rid":
        jump act_5_riddle_pass
    else:
        jump act_5_over
    if right_riddles > 3:
        $ chance = renpy.random.randint(1, 5)
        if chance == 5:
            pass
        else:
            jump act_5_more_riddles
    else:
        jump act_5_more_riddles

label act_5_riddle_pass:
    show riddleman mad
    u "So, you think you have all the answers, fool?"
    show riddleman shout
    u "I shall want to see how long it takes until you see how wrong that is."
    show riddleman smile
    u "I will see how long until I break you..."
    show riddleman at talk_end
    "Yeah, no."
    "If anything, I'd probably break from hunger."
    "More likely from boredom."
    "..."
    scene bg black with dissolve
    stop music fadeout 6.0
    $ renpy.pause(delay=6, hard=True)
    return
