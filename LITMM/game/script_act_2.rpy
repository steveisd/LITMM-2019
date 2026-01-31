label act_2_start:
    $ renpy.pause(delay=1, hard=True)
    play sound snore
    $ renpy.pause(delay=8, hard=True)
    play sound zipper_2
    "..."
    play sound ruffle_2
    "..."
    "Huh?"
    scene mm_dome_in with dissolve
    "*Yawn*{w} I thought I heard something."
    "Based on my watch, it's... 1 AM."
    "..."
    "Maybe it was nothin{nw=2}"
    o "Who dare use our fort as a bed?"
    "..."
    "That was definitely a voice."
    "Who could it be?"
    play sound clothes
    show paperman_1 talk with dissolve
    pause 0.1
    show paperman_1 talk at talk_start
    o "You have intruded our fortress, giant!"
    "What...{w} is going on?"
    play sound paper_sword_1
    show paperman_1 sword
    $ o = Character("Paperman", color="#319954", what_color="#000011")
    o "And for that, you shall pay the price!"
    show paperman_1 sword at talk_end
    hide paperman_1 with dissolve
    play sound paper_attack_1
    "..."
    "..."
    "He's trying to slice my legs."
    "That's cute and disturbing at the same time."
    "Let me pick him up to see if he's for real."
    show paperman_1 talk:
        ypos 2000 xalign 0.5
        linear 0.60 ypos -150
    play sound paper_pick_1
    "..."
    "I can definitely feel him."
    "The feel of breathing paper is so weir-"
    play sound paper_cut
    show paperman_1 sword:
        ypos -50 xalign 0.5
        linear 0.75 ypos 2000
    "Ah!"
    hide paperman_1 with dissolve
    a "Paper cut!"
    pause 0.1
    show paperman_1 smile:
        ypos 500 xalign 0.5
        linear 0.25 ypos 0
    o "Ha! Wait till an army of me will get ya!"
    menu:
        "Pick up and throw away paperman":
            hide paperman_1
            play sound paper_pick_2
            $ renpy.pause(delay=0.7, hard=True)
            play sound whoosh
            $ renpy.pause(delay=1, hard=True)
            "The paperman, half crumpled, flies away like a discarded letter."
            "..."
            $ chance = renpy.random.randint(1,5)
            if chance == 5:
                "Why did I even bother to narrate that?"
        "Crush paperman.":
            hide paperman_1
            play sound paper_crush
            $ renpy.pause(delay=1, hard=True)
            "..."
            "He just lay there, and then glided off like a paper plane..."
            "Okay..."
        "Unfold paperman":
            hide paperman_1
            play sound paper_unfold
            $ renpy.pause(delay=3, hard=True)
            "..."
            "He stopped moving."
            "Did... did I kill him?"
            "Ah well. It's not like I don't see papers littering basically every place imaginable at some point."
            "There's nothing on him too. Just... plain old paper."
    "I must be dreaming."
    #window hide
    play sound book_4
    show white
    pause 0.2
    hide white
    $ renpy.pause(delay=0.5, hard=True)
    "Ow!"
    "What the-"
    play sound book_2
    "A book?"
    show book with dissolve
    "{i}Riddles{/i}..."
    "What a plain name."
    hide book with dissolve
    "..."
    "Wait a damn second..."
    "Mind Museum..."
    "Weird papermen..."
    "And now, a riddle book coming from nowhere..."
    "The fact that I can't remember much from before here can only mean th{nw=1.5}"
    "Ugh..."
    "S-{w=0.5}Suddenly I feel an urge to read this book."
    "And..."
    "I'm suddenly getting sleepy."
    "W-{w=0.5}What-"
    "What was I gonna say again?"
    "I was..."
    "Let's...{w} let's read.{w}..?"
    scene bg black with dissolve
    "Uh..."
    play sound snore
    "Zzzzzzzzzzzzzzzzzzzz"
    window hide
    $ renpy.pause(delay=8, hard=True)
    "..."
    return
