# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character(None, kind=nvl)
define pov = Character(None)
define r = Character("Rika", image="rika", color="#4906e7")
define s = Character("Satoko", image="satoko", color="#ebeb34")

# The game starts here.

label start:

    play music "Over the sky.mp3"

    scene fure2
    with Fade(1.0, 1.0, 2.0, color="#fff")

    # These display lines of dialogue.

    b """
    Oh the stories you'll survey in this sea of fragments,

    So many fragments to choose, so many scenarios to experience,

    As I would've guessed, the possibilities for loads of different tales are endless,

    It's all so overwhelming to take in!

    There's so many things that I have yet to see after her 100 year long journey for the perfect ending.
    
    There's so much that we could observe in that perfect world that has been found recently, but I'll leave that for later.
    """

    nvl clear

    scene fure1
    with wipeleft

    b """
    Hm, what is it?

    Found an interesting piece? Well, let me take a glimpse at this.
    """

    nvl clear

    scene kakera
    with dissolve

    b """
    ...I see. A fragment set after that fateful day, huh?

    This isn't a piece that we usually came by.

    Most of the time, it's been set in weeks before that day, even only a few days.

    A fragment set after the night of Watanagashi ought to be fun, wouldn't you agree?

    {clear}

    Perhaps we might be just in time to see our protagonist fulfill one of her wildest dreams yet.

    If it doesn't turn out right, there's always those other fragments to look back to.

    We'll see how that idea turns out whether the story goes their way or not.

    Right, on with the show.
    """

    # This ends the game.
    nvl clear
    stop music fadeout 2.0

    jump chapter1