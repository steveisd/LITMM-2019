label init_skills:
    # init_skills is a label that is called to initalize skill fighter_skill objects.
    # All skills should be declared here first otherwise if an undeclared skill is used by a fighter
    # inside label init_fighters, it will return an error.
    $ GenericAttack = fighter_skill(
        SKL = "Attack",
        DMG = 50,
        AOE = False,
        COST = 0,
        ELEM = "None",
        DESC = "The equivalent of a bitchslap basically.",
        GFX = "smack",
        SFX = "audio/sfx/paper flick.ogg",
        PAUSE = 0.30
    )

    $ HigherAttack = fighter_skill(
        SKL = "Stomp",
        DMG = 400,
        AOE = False,
        COST = 40,
        ELEM = "None",
        DESC = "Crush an opponent with your feet.",
        GFX = "shoe",
        SFX = "audio/sfx/paper crush.ogg",
        PAUSE = 0.30
    )

    $ AOEattack = fighter_skill(
        SKL = "Crush",
        DMG = 200,
        AOE = True,
        COST = 40,
        ELEM = "None",
        DESC = "Stomp multiple enemies into paper balls.",
        GFX = "shoe",
        SFX = "audio/sfx/paper smash.ogg",
        PAUSE = 0.30
    )

    $ HighAttack = fighter_skill(
        SKL = "Papercut Slash",
        DMG = 100,
        AOE = False,
        COST = 40,
        ELEM = "None",
        DESC = "Painful as fuck.",
        GFX = "slash",
        SFX = "audio/sfx/paper cut.ogg",
        PAUSE = 0.30
    )

    $ OuchAttack = fighter_skill(
        SKL = "Papercut Fury",
        DMG = 200,
        AOE = False,
        COST = 40,
        ELEM = "None",
        DESC = "The bane of most writers.",
        GFX = "slash",
        SFX = "audio/sfx/paper pick 2.ogg",
        PAUSE = 0.30
    )

    $ PaperAxe = fighter_skill(
        SKL = "Paper Axe",
        DMG = 900,
        AOE = False,
        COST = 50,
        ELEM = "None",
        DESC = "Deals a heck lot of damage for cartolina.",
        GFX = "slash",
        SFX = "audio/sfx/paper crush.ogg",
        PAUSE = 0.30
    )
