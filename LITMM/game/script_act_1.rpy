# Need:
#  Cafe backgrounds (at least 3, of the same cafe)
#  Coffeelady sprite
#  Anime guard sprite

# Revised:
#  Points for choices made?
#  Benefit for phone still being alive?
#  Disable rollback when done
#  Want to actually use music I listened to when I wrote the stuff this is based on?

# Update:
#  Will keep notes in for archival purposes

label act_1_start:
    #a "Still a work in progress, luv."
    #o "Yes. Please get out kindly."
    #e "You can be a little nicer, you know."
    #a "Huh?"
    #o "Wha-?"
    #e "Come on, you can act better than that."
    #i "Aha aha yeah..."

    stop music
    "..."
    window hide
    $ renpy.pause(delay=5, hard=True)
    play music default_ambience
    scene bg black
    "Okay, try not to panic..."
    "This is okay. This is okay."
    "..."
    play sound rummage_1
    window hide
    $ renpy.pause(delay=5, hard=True)
    play sound tap
    scene mm_front
    $ dark_af = False
    $ renpy.pause(delay=1, hard=True)
    "Thank god for phone flashlights."
    "At least it's not a dark alleyway or some shady forest."
    "Could be worse. Could really be worse."
    "Whew..."
    "..."
    "Okay, I think I feel a bit better."
    "But what the heck do I do now?"

label menu_1:
    menu:
        "Check the entrance." if not m1_choice_1:
            #if you explode and then check this second, you get through
            $ m1_choice_1 = True
            jump menu_1_choice_1
        "Call out." if not m1_choice_2:
            #if you explode and check the entrance, someone mysterious will answer and
            $ m1_choice_2 = True
            jump menu_1_choice_2
        "Try contacting someone on the phone." if not m1_choice_3:
            #if you explode, check the entrance, and call out and do this, someone mysterious will answer
            $ m1_choice_3 = True
            jump menu_1_choice_3
        "Spontaneously explode." if not m1_choice_4:
            #random chance someone says to shut up and the game glitches and you're awakened (take room shots!)
            $ m1_choice_4 = True
            jump menu_1_choice_4
        "Wait it out.":
            $ m1_choice_5 = True
            jump menu_1_choice_5

label menu_1_choice_1:
    if dark_af:
        scene mm_entrance_dark with dissolve
    else:
        scene mm_entrance with dissolve
    $ entrance_scene_there = True
    window hide
    $ renpy.pause(delay=0.5, hard=True)
    play sound door
    $ renpy.pause(delay=2, hard=True)
    "The entrance is locked."
    "Of course it is..."
    jump menu_1

label menu_1_choice_2:
    a "Hello?"
    a "Is anyone out there?"
    "..."
    a "HELLO!?"
    "..."
    a "Ugh. Who's going to hear me anyway?"
    u "HELLO!?"
    "!"
    "..."
    a "Oh, it's just an echo..."
    a "Nevermind..."
    jump menu_1

label menu_1_choice_3:
    "Of course..."
    "Duh!"
    "Now, if I could only-"
    "..."
    "I have no load."
    "No wifi either."
    $ renpy.pause(delay=1, hard=True)
    if entrance_scene_there:
        scene bg black
        pause 0.5
        scene mm_entrance_dark
    else:
        scene bg black
    $ phone = False
    $ dark_af = True
    "And my phone just died."
    "WTF."
    "Very funny, fate."
    jump menu_1

label menu_1_choice_4:
    "What, do you mean get angry?"
    "Like @#$^*&(P)(*&$&^*&*("
    "&$*^&(*)()**&*!)!(!&)!*&!&!&!!!!!!!!"
    "..."
    "Okay, I feel better now."
    jump menu_1

label menu_1_choice_5:
    "I guess I have no choice."
    "Anyway, someone should be here soon- if not by morning."
    "..."
    "It's going to be a looong wait."
    "Hm..."
    jump menu_2

label menu_2:
    menu:
        "What should I do for now?"
        "Sleep.":
            jump menu_2_choice_1
        "Read a book." if not m2_choice_2:
            #if you didn't explode, you will read random notes
            $ m2_choice_2 = True
            if not dark_af:
                $ m2_choice_5 = True
            jump menu_2_choice_2
        "Jack off." if not m2_choice_3:
            #if you didn't explode, you'll wake up
            $ m2_choice_3 = True
            jump menu_2_choice_3
        "IDK." if not m2_choice_4:
            #game quits if you didn't explode
            $ m2_choice_4 = True
            jump menu_2_choice_4
        "Ask myself how the heck I even got here." if not m2_choice_5:
            #wake up if you didn't explode
            $ m2_choice_5 = True
            jump menu_2_choice_5
        "Listen to music" if not m2_choice_6 and phone:
            #if you explode, FF4 music plays and you fight zeromus but wake up after the battle
            $ m2_choice_6 = True
            jump menu_2_choice_6

label menu_2_choice_1:
    "Well, it is late."
    "Makes sense."
    "Let's see if there's any place here I can use as a makeshift bed or something."
    "..."
    jump sleeping

label menu_2_choice_2:
    if dark_af:
        "Yeah, because I have night vision vision..."
        "I mean just night vision."
        "Hm..."
    else:
        "Hm..."
        play sound rummage_2
        window hide
        $ renpy.pause(delay=2, hard=True)
        play sound book_2
        "Here's one."
        "{i}Lemonade - Locally Grown -{/i}"
        "Oh wait, it's a notebook."
        play sound book_1
        "..."
        $ chance = renpy.random.randint(1, 5)
        if chance == 5:
            show doodle with dissolve
            "..."
            hide doodle with dissolve
            "..."
        "There's just dumb doodles and stuff in here."
        #if you exploded, you see a glimpse of a drawing (need note pic then)
        play sound book_3
        window hide
        $ renpy.pause(delay=1, hard=True)
        "Oh right..."
        "I was supposed to be taking notes on some field trip."
        "But I don't even know how I ended up stuck here..."
        "My head hurts a bit thinking about it. I'll probably think about it later."
        "For now..."
    jump menu_2

label menu_2_choice_3: #edit more!
    "..."
    "Now's not the time."
    "What's up with these thoughts?"
    "Of all times to think about that..."
    jump menu_2

label menu_2_choice_4:
    "..."
    "..."
    "..."
    #if all four menu 1 choices taken, boss battle, shitpost route
    "..."
    "Danggit, I gotta make up my mind."
    "I gotta do something."
    jump menu_2

label menu_2_choice_5:
    "Hm..."
    "If only I had not..."
    "Huh."
    "How'd I even get here?"
    "...yeah."
    "That's strange."
    "Wasn't I on some field trip?"
    "Although, it was around lunchtime. And it's waaay past that, like the opposite of lunchtime."
    "Wait a minu{nw}"
    play sound glitch_2
    show white
    pause 0.2
    hide white
    "Ow!"
    "Whew..."
    "My head hurts a bit thinking about it."
    "I'll probably think about it later."
    "For now..."
    jump menu_2

label menu_2_choice_6:
    "Alright!"
    "And this time, I remembered to bring my earphones."
    play sound rummage_1
    window hide
    $ renpy.pause(delay=3, hard=True)
    play sound taps
    $ renpy.pause(delay=3, hard=True)
    play sound plug
    $ renpy.pause(delay=2, hard=True)
    menu:
        "What should I listen to now?"
        "Track 1.mp3":
            $ renpy.pause(delay=1, hard=True)
            play music renpy.random.choice([st01, st02, st03])
        "Track 2.mp3":
            $ renpy.pause(delay=1, hard=True)
            play music renpy.random.choice([st01, st02, st03])
        "Videoplayback.mp4":
            $ renpy.pause(delay=1, hard=True)
            play music renpy.random.choice([st01, st02, st03])
    $ renpy.pause(delay=1, hard=True)
    "..." #move along here
    "Oh, hell yeah!"
    $ random_duration = renpy.random.randint(5, 10)
    $ renpy.pause(delay=random_duration, hard=True)
    stop music
    $ renpy.pause(delay=1, hard=True)
    $ phone = False
    $ dark_af = True
    if entrance_scene_there:
        scene bg black
        pause 0.5
        scene mm_entrance_dark
    else:
        scene bg black
    "..."
    "Yaaay."
    "Now, I forgot to bring another thing:"
    "A damn power bank..."
    "Looks like music's out of the list."
    "Danggit!"
    jump menu_2

label sleeping:
    $ renpy.pause(delay=1, hard=True)
    play sound walking
    $ renpy.pause(delay=5, hard=True)
    if dark_af:
        scene bg black with dissolve
        play sound thud
        $ renpy.pause(delay=0.5, hard=True)
        "Ouch..."
        "..."
    else:
        scene mm_dino with dissolve
        "..."
    play sound walking
    $ renpy.pause(delay=5, hard=True)
    if dark_af:
        "..."
    else:
        scene mm_tunnel with dissolve
        "..."
    play sound walking
    $ renpy.pause(delay=5, hard=True)
    if phone:
        scene mm_tunnel_dark
        $ renpy.pause(delay=1, hard=True)
        #scene bg black
        $ phone = False
        $ dark_af = True
        "Ah, my phone died."
        "I think I see a light though."
    else:
        scene mm_tunnel_dark with dissolve
        "Huh."
        "I think I see a light."
    play sound walking
    $ renpy.pause(delay=5, hard=True)
    scene mm_dome with dissolve
    $ dark_af = False
    "Hm..."
    "Light's suspiciously on, but I ain't complaining."
    "I guess that dome will do."
    "Since they use that for movie presentations, I could have had my own private movie night at least."
    "Heh, whatevs."
    play sound zipper_1
    $ renpy.pause(delay=2, hard=True)
    scene mm_dome_in with dissolve
    "Let's sleep."
    play sound ruffle_1
    "..."
    "..."
    scene bg black with dissolve
    $ renpy.pause(delay=2, hard=True)
    return
