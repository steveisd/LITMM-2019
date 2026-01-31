# Classes
init python:
    import math

    # Variables

    #  Act 1
    dark_af = True
    entrance_scene_there = False
    m1_choice_1 = False
    m1_choice_2 = False
    m1_choice_3 = False
    m1_choice_4 = False
    m2_choice_2 = False
    m2_choice_3 = False
    m2_choice_4 = False
    m2_choice_5 = False
    m2_choice_6 = False
    phone = True

    #  Act 5
    riddles = ["   1.  It has a golden head. It has a golden tail. It has no body. Answer: coin. ",
            "    2.  It wears a leather coat to keep its skins in working order. Escorts you to other realms, without a magic portal. Answer: Book. ",
            "    3.  It dampens as it dries. Answer: Towel. ",
            "    4.  What has two hands on its face but no arms? Answer: clock ",
            "    5.  What kind of coat is always wet when you put it on? Answer: coat of paint. ",
            "    6.  Many have heard me, yet nobody has seen me. I won’t speak back unless spoken to. What am I? Answer: echo. ",
            "    7.  What five long word become shorter when you add two letters? Answer: Short ",
            "    8.  What is not alive but grows, does not breaths but needs air. Answer: Fire ",
            "    9.  Better old than young; the healthier it is, the smaller it will be. Answer: Wound. ",
            "    10. This fire is smothered best not by water or sand but by words. Answer: Desire. ",
            "    11. Two friends stand and travel together, one nearly useless without the other. Answer: Boots ",
            "    12. Feed me and I will live, give me a drink and I will die. Answer: Fire. ",
            "    13. A curved stick and a straight twig means red sap and a snapped trunk. Answer: Death by arrow. ",
            "    14. No warning of Timber could have stopped the dropping petals. Answer: Death by axe. ",
            "    15. A fitting cravat for a poorly chosen suit. Answer: Death by hanging. ",
            "    16. I build castles, yet tear down mountains, make some men blind, and others see. What am I? Answer: Sand. ",
            "    17. As I was going to St Ives I met a man with 7 wives. Each wife had 7 kids. Each kid had 7 cats. Each cat had 7 kittens. How many were going to St Ives? Answer: 1.  ",
            "    21. What is it that you keep when you need it not, but throw out when you do need it? Answer: anchor. ",
            "    22. The foolish man wastes me, The average man spends me, And wise man invests me, Yet all men succumb to me. What am I? Answer: Time. ",
            "    23. What is something that dawns on you even when it shouldn’t? Answer: obvious. ",
            "    24. When you come to the end of all you know, I am there. Who am I? HINTS: I start out wonderful, but then begin worse. Answer: W. ",
            "    25. What has four legs in the morning, two legs in the afternoon and three legs in the evening? Answer: Man. ",
            "    26. I’m made out of five letters, And I’m made out of seven letters; I have keys but I don’t have locks, I’m concerned with time, but not with clocks. Answer: Piano. ",
            "    27. Forty white horses on a red hill. They champ, they stamp, and then stand still. Answer: Teeth. ",
            "    28. I can fly like a bird not in the sky, which can always swim and can always dry. I say goodbye at night and morning hi. I’m part of you what am I. I follow and lead as you pass, dress yourself in black my darkness lasts. I flee the light but without the sun, Your view of me would be gone. Answer: shadow. ",
            "    29. I am what men love more than life, fear more than death or mortal strife, what dead men have and rich require. I’m what contented men desire. Answer: Nothing. ",
            "    31. Towns without houses, forests without trees, mountains without boulders and waterless seas. Answer: Map. ",
            "    32. Two bodies in one, the longer I stand, the faster I run. Answer: Hourglass. ",
            "    33. Men desire me in public, but fear me in private. Answer: Truth. ",
            "    34. What is so fragile, even speaking its name will break it? Answer: Silence. ",
            "    35. What must you first give to me in order to keep it? Answer: Your word. ",
            "    36. Though I’m tender, I’m not to be eaten, Nor — though, mint fresh — your breath to sweeten. Answer: Money. ",
            "    37. You never see it, but it’s almost always there, and most people quickly notice when it’s absent. Answer: air ",
            "    38. An untiring servant it is, carrying loads across muddy earth. But one thing that cannot be forced, is a return to the place of its birth. Answer: River. ",
            "    39. Blessed are the first. Slow are the second. Playful are the third. Bold are the fourth. Brave are the fifth. Answer: Answer: Blade. ",
            "    40. Brought to the table. Cut and served. Never eaten. Answer: Cards. ",
            "    41. It can pierce the best armor, And make swords crumble with a rub. Yet for all its power, It can’t harm a club. Answer: Rust. ",
            "    42. It is a journey whose path depends, on an other’s vision of where it ends. Answer: Book. ",
            "    43. Men seize it from its home, tear apart its flesh, drink the sweet blood, then cast its skin aside. Answer: Orange. ",
            "    44. Names give power, Magic to control. But what is broken, by naming it? Answer: Silence. ",
            "    45. Passed from father to son, And shared between brothers. Its importance is unquestioned, Though it is used more by others. Answer: Name. ",
            "    46. Today he is there to trip you up, And he will torture you tomorrow. Yet he is also there to ease the pain, When you are lost in grief and sorrow. Answer: Alcohol. ",
            "    47. In the form of fork or sheet, I hit the ground. And if you wait a heartbeat, You can hear my roaring sound. Answer: Lightning. ",
            "    48. I have no tears but I perspire, I stretch but cannot respire, I can jump, walk, run and dance, Though I have no mind. I’ll take a stance. What am I? Answer: leg. ",
            "    49. The beast of the plains, it goes through the ground, constantly on the search for its next meal. While it hates the taste of dwarves and elves, it loves the taste of halfling. Answer: Bulette. ",
            "    50. This thing can stay completely hidden in even the broadest of daylight. In halls and rooms that monster waits to ambush its next victim. Watch out from below, because it is the floor that this thing waits. Answer: Rug of smothering. ",
            "    51. In the world below, almost everything below has a heart as dark as their surroundings. This thing is the one exception, giving a light glow in the world of the Underdark. Answer: Flumph. ",
            "    52. You keep it, but it never ages. Once shared it is gone forever. Answer: Secret. ",
            "    53. I can bring down the mightiest of men. Nobody can defy me. I am the enemy of flight. Yet you can’t even sense my presence. What am I? Answer: Gravity ",
            "    54. The more you walk on me the more we get along, and while other may still use me, with you is where I belong. What am I? Answer: Shoes ",
            "    55. I give mirth and merriment and they say I smell quite old but I can turn a timid man into one that is quite bold. What am I? Answer: Wine ",
            "    56. I am green with envy when I am placed below the sky. I do not breathe the air you breathe but I never wonder why. If you go and shelter me, I simply shrink and die. The answer to this riddle is simply who am I? Answer: plant ",
            "    57. I guard precious treasures and yet my body never moves, but I open like a book when something of yours is used. When finally I’m gutted always feel quite blue. I always feel so useless without the gold that I consume. What am I? Answer: Treasure Chest ",
            "    58. My body’s thin and slender and I grow shorter every day. You can use my single purpose, and I’ll be sure to lead the way. When I am placed upon a pastry then my life is soon to fade. What am I? Answer: candle ",
            "    59. I am what’s desired above of all fame and wealth. Without me it’s assured that you’ll begin to lose your health. I’m not a fluid dancer, but you can put me on a shelf. What am I? Answer: Food ",
            "    60. I give people purpose, I am the gardener pulling weeds. In fact I keep a watchful eye over everybody’s deeds. I am the cobbler making shoes I am the blacksmith shoeing steeds. What am I? Answer: job ",
            "    61. Born by fire, stone, or rain I feel most comfortable at home on the planes. When I am out of my element, I feel much disarray. What am I? Answer: elemental ",
            "    62. I am gifted to you only when I am unwanted. I have the power to kill kings or the lowliest paupers. My strength is unquestioned and I move far and wide, yet my power can falter from potions imbibed. What am I? Answer: Sickness ",
            "    63. The more you take out the bigger I get. What am I? Answer: hole ",
            "    64. I am green for some time, but blue thereafter. If it is dark, I am likely to eat you. What am I? Answer: Grue ",
            "    65. Up and down they go and travel, but never do they move an inch. Answer: Stairs ",
            "    66. 8 _ _ _ 1 _ _ _ 2 0' Answer: 549763 ",
            "    67. Halo of water, tongue of wood, skin of stone and long I’ve stood. My fingers short reach to the sky, inside my heart men live and die. What am I? Answer: Castle ",
            "    68. Flying on invisible wings. I am massive in size. Then if my master commands, I am as small as he wishes. All men wish to own me, but when I touch them, They cannot touch me. I cry when I am with my brothers. Darkness follows wherever I go. I’m a friend, I’m an enemy. I am freedom. What am I? Answer: Cloud ",
            "    69. A face I do have, but see I do not. When they see my hands, they oft ponder in thought Answer: watch ",
            "    70. The more you take, the more you leave behind. What am I? Answer: Footsteps ",
            "    71. What kind of room can you never enter? Answer: Mushroom. ",
            "    72. What is long, brown, and sticky? Answer: stick. ",
            "    73. What has a head and a tail, can flip but has no legs? Answer: coin. ",
            "    74. What is black when you buy it, red when you use it, and white when you throw it away? Answer: Coal. ",
            "    75. What belongs to you, but other people use it more than you do? Answer: Your name. ",
            "    76. Tall I am young, Short I am old, While with life I glow, Wind is my foe. What am I? Answer: candle. ",
            "    77. I can build castles, I can stop a flood, I can show the time flow, I can make people blind, I can make others see. What am I? Answer: Sand ",
            "    78. If I’m in front I don’t matter, If I’m in back I make everything be more, I am something yet I am nothing. What am I? Answer: Zero ",
            "    79. I shine brightest in the dark. I am there but cannot be seen. To have me costs you nothing. To be without me costs you everything. Answer: Hope. ",
            "    80. I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost everybody. Answer: Pencil lead. ",
            "    81. What goes round the house and in the house but never touches the house? Answer: sun. ",
            "    82. What comes once in a minute, twice in a moment, but never in a thousand years? Answer: M. ",
            "    83. He who has it doesn’t tell it. He who takes it doesn’t know it. He who knows it doesn’t want it. What is it? Answer: fake money. ",
            "    84. What goes round and round the wood but never goes into the wood? Answer: bark of a tree. ",
            "    85. I have a little house in which I live all alone. It has no doors or windows, and if I want to go out I must break through the wall. Answer: chick in an egg. ",
            "    87. A cloud was my mother, the wind is my father, my son is the cool stream, and my daughter is the fruit of the land. A rainbow is my bed, the earth my final resting place, what am I? Answer: Rain. ",
            "    88. Poke your fingers in my eyes and I will open wide my jaws. Linen cloth, quills or paper, all will split before my might. What am I? Answer: Scissors ",
            "    89. What goes with a carriage, comes with a carriage, is of no use to a carriage and yet the carriage cannot go without it? Answer: Noise. ",
            "    90. What stands on one leg with its heart in its head? Answer: cabbage. ",
            "    91. It’s been around for millions of years, but it’s no more than a month old. What is it? Answer: moon. ",
            "    92. I met a man with a load of wood which was neither straight nor crooked. What kind of wood was it? Answer: Sawdust. ",
            "     93. What binds two people yet touches only one? Answer: wedding ring. ",
            "    94. I am the beginning of sorrow and the end of sickness. There’s no happiness without me nor is there sadness. I am always in risk, yet never in danger. You will find me in the sun, but I am never out of darkness. Answer: S. ",
            "    95. What holds water yet is full of holes? Answer: sponge. ",
            "    96. Lives without a body, hears without ears, speaks without a mouth, to which the air alone gives birth. Answer: echo. ",
            "    98. When one does not know what it is, then it is something. When one knows what it is, then it is nothing. Answer: riddle. ",
            "    99. It is the beginning of eternity, the end of time and space, the beginning of the end and the end of every space. What is it? Answer: E ",
            "    100. What tastes better than it smells? Answer: tongue. "]
    riddle_attempts = 0
    right_riddles = 0


    # Audio
    #  Ambience
    aircon = "audio/sfx/aircon.ogg"
    default_ambience = "audio/sfx/ambience.ogg"
    mountains_sfx = "audio/sfx/mountains.ogg"
    waves_sfx = "audio/sfx/Waves.mp3"
    #  Music
    battle_1 = "audio/music/battle 1.ogg"
    battle_2 = "audio/music/battle 2.wav"
    boots = "audio/music/boots.ogg"
    boss_battle = "audio/music/boss battle.ogg"
    credit_music = "audio/music/credits.ogg"
    st01 = "audio/music/t1.mp3"
    st02 = "audio/music/t2.mp3"
    st03 = "audio/music/t3.mp3"
    #  SFX
    badum = "audio/sfx/badum.ogg"
    banging_1 = "audio/sfx/banging 1.ogg"
    banging_2 = "audio/sfx/banging 2.ogg"
    battle_charge = "audio/sfx/battle charge.ogg"
    battle_charge_yell = "audio/sfx/battle charge yell.ogg"
    battle_cries = "audio/sfx/battle cries.ogg"
    battle_retreat = "audio/sfx/battle retreat.ogg"
    bed_1 = "audio/sfx/bed 1.ogg"
    bed_2 = "audio/sfx/bed 2.ogg"
    bed_3 = "audio/sfx/bed 3.ogg"
    book_1 = "audio/sfx/book 1.ogg"
    book_2 = "audio/sfx/book 2.ogg"
    book_3 = "audio/sfx/book 3.ogg"
    book_4 = "audio/sfx/book 4.ogg"
    chair = "audio/sfx/chair.ogg"
    cliff = "audio/sfx/cliff.ogg"
    clothes = "audio/sfx/clothes.ogg"
    december1 = "audio/sfx/december1.ogg"
    december2 = "audio/sfx/december2.ogg"
    distant_battle = "audio/sfx/distant battle.ogg"
    door = "audio/sfx/door.ogg"
    drop = "audio/sfx/drop.ogg"
    dsr = "audio/sfx/dsr.ogg"
    error = "audio/sfx/error.ogg"
    farmer = "audio/sfx/farmer.ogg"
    festive = "audio/sfx/festive.ogg"
    fireworks = "audio/sfx/fireworks.ogg"
    glitch_2 = "audio/sfx/Glitch 2.mp3"
    glitch_3 = "audio/sfx/Glitch 3.mp3"
    glitch_4 = "audio/sfx/Glitch 4.mp3"
    grab = "audio/sfx/grab.ogg"
    groundl = "audio/sfx/ground.ogg"
    error = "audio/sfx/error.ogg"
    here = "audio/sfx/here.ogg"
    horns = "audio/sfx/horns.ogg"
    intense_paper_clash = "audio/sfx/intense paper clash.ogg"
    I = "audio/sfx/I.ogg"
    marbles = "audio/sfx/marbles.ogg"
    marbles2 = "audio/sfx/marbles2.ogg"
    nothing = "audio/sfx/nothing.ogg"
    page_turn = "audio/sfx/page_turn.ogg"
    paper_attack_1 = "audio/sfx/paper attack 1.ogg"
    paper_attack_2 = "audio/sfx/paper attack 2.ogg"
    paper_attack_3 = "audio/sfx/paper attack 3.ogg"
    paper_clashes = "audio/sfx/paper clashes.ogg"
    paper_crush = "audio/sfx/paper crush.ogg"
    paper_crush_multiple = "audio/sfx/paper crush multiple.ogg"
    paper_cut = "audio/sfx/paper cut.ogg"
    paper_pick_1 = "audio/sfx/paper pick 1.ogg"
    paper_pick_2 = "audio/sfx/paper pick 2.ogg"
    paper_sword_1 = "audio/sfx/paper sword 1.ogg"
    paper_unfold = "audio/sfx/paper unfold.ogg"
    plug = "audio/sfx/plug.ogg"
    ringing = "audio/sfx/ringing.ogg"
    ruffle_1 = "audio/sfx/ruffle 1.ogg"
    ruffle_2 = "audio/sfx/ruffle 2.ogg"
    ruffle_3 = "audio/sfx/ruffle 3.ogg"
    ruffle_4 = "audio/sfx/ruffle 4.ogg"
    ruffle_5 = "audio/sfx/ruffle 5.ogg"
    rummage_1 = "audio/sfx/rummage 1.ogg"
    rummage_2 = "audio/sfx/rummage 2.ogg"
    running_on_paper = "audio/sfx/running on paper.ogg"
    snore = "audio/sfx/snore.ogg"
    surprise = "audio/sfx/surprise.ogg"
    tap = "audio/sfx/tap.ogg"
    taps = "audio/sfx/taps.ogg"
    thud = "audio/sfx/thud.ogg"
    tones = "audio/sfx/tones.ogg"
    two_footsteps = "audio/sfx/two footsteps.ogg"
    walking = "audio/sfx/walking.ogg"
    whoosh = "audio/sfx/whoosh.ogg"
    zipper_1 = "audio/sfx/zipper 1.ogg"
    zipper_2 = "audio/sfx/zipper 2.ogg"


# Definition
define a = Character("You", color="#319954", what_color="#000011")
define b = Character("???", color="#319954", what_color="#000011")
define e = Character("???", color="#319954", what_color="#000011")
define o = Character("???", color="#319954", what_color="#000011")
define u = Character("???", color="#319954", what_color="#000011")
define w = Character("Papermen", color="#319954", what_color="#000011")


# Transforms
transform talk_start(x=0.2, y=1.025):
    xalign 0.5 center
    linear x zoom y
transform talking(y=1.025):
    xalign 0.5 zoom y center
transform talk_end(x=0.2, y=1.0):
    xalign 0.5 center
    linear x zoom y
transform talk_start_p(x=0.2, y=1.025):
    xalign 0.5 center
    pause 0.5
    linear x zoom y
transform talk_end_p(x=0.2, y=1.0):
    xalign 0.5 center
    pause 0.5
    linear x zoom y
transform left_center(x=0.10):
    xalign x
transform right_center(x=0.90):
    xalign x
transform tackle(x=0.2, y=50.0):
    xalign 0.25 center
    linear x zoom y
