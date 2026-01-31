label act_8_start:
    #play sound "<loop 5.0>ringing.ogg"
    scene white with Dissolve(3)
    $ renpy.pause(delay=1, hard=True)
    stop music
    scene bg black
    pause 0.2
    play sound nothing
    #play like morning sound here or something (wake up early, record)
    scene bedroom_1
    "..."
    "..."
    $ renpy.pause(delay=1, hard=True)
    play sound bed_1
    scene bedroom_2 with dissolve
    $ renpy.pause(delay=1, hard=True)
    "It was all{w} a dream."
    scene bg black
    #triggered or something
    pause 5
    scene bedroom_2
    "..."
    "As much as the 'it was all a dream' trope has been used to death,"
    play sound bed_2
    scene bedroom_3 with dissolve
    "Thank god, I wasn't trapped back in 2012 after all.{w} Much less, my own crappy story book."
    "Anyways, I just remembered:"
    play sound bed_3
    $ renpy.pause(delay=3, hard=True)
    play sound chair
    scene bedroom_4 with dissolve
    "This was just some project we made in 2019 based on some book we made seven years ago."
    "The plot I used for this probably made me dream weird things again."
    "Knowledge beings that can control time that can't even solve their own problems or smtn, sure..."
    "One of these days, we should make a Renpy game that's actually good or at least decent"
    "Although we were busy with other stuff, and probably are still."
    "Ah."
    "Whatever."
    pause 1
    scene bedroom_5 with dissolve
    "Yup..."
    "So,"
    "End of story!"
    "Now to get some coffee..."
    pause 2
    scene bg black
    play music credit_music
    $ renpy.pause(delay=1.25, hard=True)
    scene credit_1 #FIN
    $ renpy.pause(delay=4.5, hard=True)
    scene credit_2 with dissolve #LOCKED IN THE MIND MUSEUM
    $ renpy.pause(delay=4.5, hard=True)
    scene credit_3 with dissolve #MADE BY
    $ renpy.pause(delay=1.8, hard=True)
    scene credit_3a with dissolve #MADE BY AM 06'02'2019
    $ renpy.pause(delay=1.8, hard=True)
    scene credit_4 with dissolve #SPECIAL THANKS:
    $ renpy.pause(delay=1.8, hard=True)
    scene credit_4a with dissolve #SPECIAL THANKS: TO [DATA EXPUNGED] FOR SUPPORT AND PLAYING u
    #You do know that I played 'b', not 'u', right?
    #Ah, my mistake... although you did help program 'u' still, so... we can stretch that.
    $ renpy.pause(delay=0.3, hard=True)
    scene bg black
    stop music
    "'Ideas never die.'"
    return
