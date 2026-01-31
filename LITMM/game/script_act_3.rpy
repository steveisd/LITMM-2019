label act_3_start:
    "..."
    "..."
    play sound ruffle_1
    $ renpy.pause(delay=1, hard=True)
    u "Wake up, boy..."
    play sound ruffle_3
    "..."
    "Huh?"
    "Is it morning yet?"
    scene mm_dome_in_morning with dissolve
    play sound ruffle_1
    $ renpy.pause(delay=1, hard=True)
    show guard with dissolve
    $ renpy.pause(delay=0.5, hard=True)
    a "Oh."
    "..."
    $ chance = renpy.random.randint(1,5)
    if chance == 5:
        "Why is he anime?"
    a "Are you here to take me home?"
    $ u = Character("Guard", color="#319954", what_color="#000011")
    show guard at talk_start
    u "Let's play a game."
    "..."
    a "Excuse me?"
    "That was a random reply."
    a "I kinda need to go home,"
    a "So,{nw=1}"
    u "What game do you like?"
    a "WTF DID YOU EVEN HEAR ME???"
    $ chance = renpy.random.randint(1, 3)
    if chance == 3:
        $ u = Character("Weird-ass Guard", color="#319954", what_color="#000011")
    u "I don't know that game."
    show guard at talk_end
    "Man, first thing in the morning..."
    "I could just whack this guy with this riddle book."
    "..."
    "He must have read my mind. He's looking at it...{w} but smiling."
    show guard at talk_start
    u "Ah, how about riddles?"
    "This guy is clearly nuts. I need to get away from him."
    "There must be some way, aside from whacking him straight up."
    a "Can I...{w=0.5} uh...{w=0.5} go to the restroom?"
    u "Nope."
    a "Can I have a drink?"
    "..."
    u "If you try to escape, I'll call the police."
    a "Okay,"
    a "Maybe those guys will actually help me from YOU."
    "Besides, isn't he kind of the police?"
    hide guard with dissolve
    "Whatever. I'mma just shove through this guy."
    scene mm_dome_in_morning:
        linear 0.1 zoom 1.1 truecenter
        linear 0.1 zoom 1.0 truecenter
        pause 0.5
        linear 0.1 zoom 1.5
    play sound ruffle_4
    "!"
    "AH! WTF?"
    u "You will play, or else."
    scene mm_dome_in_morning:
        zoom 1.5 truecenter
        linear 0.5 zoom 1.0
    a "Or{w} what-"
    a "!?"
    show riddleman smile with dissolve
    pause 0.1
    show riddleman at talk_start
    $ u = Character("Riddleman", color="#319954", what_color="#000011")
    u "Or I'll punish you."
    "..."
    menu:
        "Play?"
        "Hell no.":
            show riddleman mad
            $ renpy.pause(delay=2, hard=True)
            play sound glitch_2
            show white
            pause 0.2
            hide white
            show riddleman smile
            a "AH!"
        "Fine.":
            pass
    "..."
    "Okay..."
    "Let's go play some riddles with a gigantic piece of paper in the morning."
    "I mean, this may still be a dream. Might as well have some fun."
    a "Okay,"
    a "Who goes first?"
    return
