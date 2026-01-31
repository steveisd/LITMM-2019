label act_6_start:
    play music default_ambience
    scene mm_dome_in_morning_lit with dissolve:
        zoom 1.1 truecenter
    show riddleman smile with dissolve
    "Ugh..."
    "The sun's out now."
    "Heck, it may even be breakfast already."
    "When is this gonna end???"
    a "This has been fun and all..."
    a "But, I think I'mma go now."
    a "Besides, the museum will be opening soon and I gtg home like NOW."
    a "When that happens, don't you have to go off into hiding or whatever you anomalous things usually do in movies and stuff?"
    show riddleman amused
    "..."
    a "Seriously though,{w} unless you want like the government or CIA or Foundation going berserk on you guys."
    "..."
    show riddleman righthand at talk_start
    u "Well, you must know about the time here."
    show riddleman smile
    u "It stops when guardians and humans are engaged in a contest or game."
    u "We are technically pure knowledge, just in physical body, and so we have the knowledge to control time and even space!"
    "Bullshi-{nw}"
    "Then how come the sun is clearly rising???"
    "Explain that?"
    show riddleman amused
    u "There is a reason, and as everyone, even you humans say it: everything has a reason."
    u "Let me tell you a short story about my heritage."
    "No pls"
    show riddleman smile
    u "It began 200 years ago, when we were as you can say, 'Nomadic'."
    show riddleman lefthand
    u "We traveled from museum to museum, chancing upon humans."
    show riddleman mad
    u "Cursed were they, for the treated us in a mean manner!"
    show riddleman shout
    u "They experimented with us!"
    u "The scientist called us 'animals' and your filthy researchers had torn us to pieces to study our parts."
    show riddleman mad
    u "I had a friend before that witnessed these events."
    show riddleman shout
    u "Man wrote about us, your kind did. Luckily, your human instincts told you to think that those writings about us were nothing."
    show riddleman mad
    u "That's why, we want to challenge you humans, and to avoid other humans, we stop time outside the museum."
    u "By our law, we cannot harm you, so we instead challenge you, and until we are satisfied, you will stay here forever!"
    show riddleman shout
    u "And you are far from satisfying!"
    show riddleman mad
    "I have so many questions,{w} but not because I'm really interested."
    "I mean- wow, just look at all those plotholes!"
    show riddleman shout
    "And... there he goes."
    "Blah blah blah. Whatever..."
    hide riddleman with dissolve
    "Well... looks like it's my chance."
    play sound ruffle_1
    "While he's busy lecturing to god knows- it's like he's not even talking to me anymore, but to the walls and stuff-"
    "I'mma run out."
    play sound zipper_1
    pause 0.1
    "I gently open the door{nw}"
    scene mm_dome_in_morning_lit:
        linear 0.1 zoom 1.2 truecenter
        linear 0.1 zoom 1.1 truecenter
    play sound grab
    $ renpy.pause(delay=0.5, hard=True)
    show riddleman shout with Dissolve(0.25)
    u "We are not finished yet!"
    show riddleman mad
    u "Y-{nw}"
    scene mm_dome_in_morning_lit:
        zoom 1.1 truecenter
        linear 0.075 yalign 0.9
        linear 0.075 yalign 0.3
        linear 0.075 yalign 0.9
    play sound book_4
    show riddleman surprised
    "!"
    "..."
    window hide
    $ renpy.pause(delay=2, hard=True)
    play sound paper_sword_1
    show riddleman surprised: #riddleman slides down
        yalign 0.0
        linear 0.90 ypos 2000
    $ renpy.pause(delay=1, hard=True)
    show paperman_1 mad with dissolve
    return
