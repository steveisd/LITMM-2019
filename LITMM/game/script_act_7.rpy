label act_7_start:
    show paperman_1 talk at talk_start
    o "I have come to battle ya!"
    show paperman_1 sword
    o "And to fight!"
    play music battle_2
    $ renpy.pause(delay=0.5, hard=True)
    play sound battle_cries
    $ renpy.pause(delay=0.5, hard=True)
    show paperman_1 fight: #move paperman to right while riddleman reappears from bottom with sword and shield
        linear 0.5 xalign 0.75
        pause 1
    show riddleman fight: #move riddleman towards paperman, and both out of frame
        ypos 2000 xalign 0.25
        linear 0.5 ypos 0
        pause 1
        linear 1.75 xalign 5.0
    $ renpy.pause(delay=1.50, hard=True)
    show paperman_1 fight:
        linear 0.75 xalign 2.0
    $ renpy.pause(delay=0.75, hard=True)
    play audio paper_attack_3
    $ renpy.pause(delay=1, hard=True)
    "Idk what just happened,"
    "..."
    "But-"
    "Now is my chance to escape!"
    play sound ruffle_1
    $ renpy.pause(delay=0.5, hard=True)
    play audio zipper_1
    $ renpy.pause(delay=0.5, hard=True)
    scene mm_battle_scene_1 with dissolve
    play sound battle_cries
    "..."
    play audio battle_cries
    show paperwarrior_1 at talk_start_p with dissolve
    o "YIELD!"
    o "YIELD!!!"
    o "Yield! Yield thy weapons!"
    show paperwarrior_1: #move paperwarrior_1 to right
        linear 0.5 xalign 0.75
    show paperwarrior_2 at left_center with dissolve
    o "Today, this place shall be ours!"
    hide paperwarrior_1 with dissolve
    hide paperwarrior_2 with dissolve
    "????"
    "..."
    play audio battle_charge
    scene papercg1 with dissolve #shake with ATL?
    "!!!!!"
    show paperwarrior_1 with dissolve
    play sound battle_charge_yell
    $ renpy.pause(delay=0.5, hard=True)
    hide paperwarrior_1 with dissolve
    play audio battle_cries
    w "AHHHHHHHHHHHHHHHHHHHHHHHHHHH!"
    $ renpy.pause(delay=2, hard=True)
    play sound intense_paper_clash
    $ renpy.pause(delay=0.5, hard=True)
    scene papercg2 with dissolve
    show paperwarrior_2 at talk_start_p with dissolve
    o "WE WILL NOT CEASE TO FIGHT!"
    hide paperwarrior_2 with dissolve
    "..."
    "Amazing..."
    "WAIT no!"
    "I gtg gtfo here!"
    "Now-{nw}"
    play audio paper_clashes
    show paperwarrior_1 flip at right_center with dissolve
    o "GIANT!"
    show paperbud_1 at left_center with dissolve
    w "Take him down!"

    play audio glitch_3 #"ambush.ogg"
    show white
    pause 1
    play music battle_1
    scene bg battleground
    call act_7_first_battle from _call_act_7_first_battle

    play music battle_2
    play audio paper_clashes
    scene papercg2 with dissolve:
        zoom 1.1 truecenter
    "Huh."
    "That was quick."
    scene papercg2:
        zoom 1.1 truecenter
        linear 0.075 yalign 0.9
        linear 0.075 yalign 0.3
        linear 0.075 yalign 0.9
    play sound grab
    "Crap-!"
    $ renpy.pause(delay=0.5, hard=True)
    play sound drop
    $ renpy.pause(delay=0.2, hard=True)
    scene mm_floor with dissolve
    "Stupid shoelaces!"
    w "Take the giant!!!"
    scene mm_floor_empty with dissolve
    show papermen_army_2 at right
    show papermen_army_1 at left
    with dissolve
    pause 1
    play audio battle_cries
    w "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!"
    show papermen_army_1 at left with dissolve:
        linear 1.0 zoom 3.0 truecenter
    show papermen_army_2 at right with dissolve:
        linear 1.0 zoom 3.0 truecenter
    hide papermen_army_1 with dissolve
    hide papermen_army_2 with dissolve
    play sound paper_attack_2
    "AH!"
    "..."
    "Danggit, as much as that doesn't hurt it's annoying my legs."
    "*sigh* Sorry guys, but-"
    "You're in the way of my feet!"
    play audio paper_crush_multiple
    play sound battle_retreat
    $ renpy.pause(delay=3, hard=True)
    play audio running_on_paper
    $ renpy.pause(delay=3, hard=True)
    scene mm_tunnel_papers with dissolve
    $ renpy.pause(delay=3, hard=True)
    scene mm_dino_papers with dissolve
    $ renpy.pause(delay=2, hard=True)

label entrance:
    play sound distant_battle
    $ renpy.pause(delay=1, hard=True)
    scene mm_entrance_day with dissolve
    $ renpy.pause(delay=0.5, hard=True)
    show papergiant:
        xalign -2.5
        linear 0.5 xalign 0.5
    "..."
    "Ugh,"
    "Danggit"

    play audio glitch_3 #"ambush.ogg"
    show white
    pause 1
    play music boss_battle
    scene bg battleground
    call act_7_second_battle from _call_act_7_second_battle

    play music battle_2
    scene mm_entrance_day with dissolve
    "..."
    scene mm_entrance_day:
        linear 0.5 zoom 1.3
    play sound two_footsteps
    $ renpy.pause(delay=0.5, hard=True)
    play sound banging_1
    $ renpy.pause(delay=1, hard=True)
    scene mm_front_out with dissolve
    a "Hello!"
    "..."
    a "Help!"
    play sound banging_2
    "..."
    "The one time I want someone to notice me..."
    "No,"
    "The one time I {i}need{/i} someone to notice me- and help me {i}gtfo{/i} of here!!!"
    play sound paper_clashes
    $ renpy.pause(delay=1, hard=True)
    "Fukk"
    "Fucc"
    "..."
    play audio glitch_2
    show white
    pause 0.2
    hide white
    play audio glitch_3
    show white
    pause 0.2
    hide white
    b "You are looking at an illusion."
    "Huh?"
    "Who... who's that?"
    "..."
    b "You're not supposed to be here."
    play audio ringing
    $ renpy.pause(delay=4, hard=True)
    return
