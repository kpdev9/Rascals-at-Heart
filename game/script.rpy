# Defining characters here
define b = Character(None, kind=nvl)
define huh = Character("???", color="#ffffff")
define r = Character("Rika", image="rika", color="#4906e7")
define s = Character("Satoko", image="satoko", color="#ebeb34")
define h = Character("Hanyuu", image="hanyuu", color="#7c46fa")
define k = Character("Keiichi", image="keiichi", color="#5d4001")
define re = Character("Rena", image="rena", color="#ff6f00")
define m = Character("Mion", image="mion", color="#00e304")
define sh = Character("Shion", image="shion", color="#39fa3c")
define i = Character("Irie", image="irie", color="#f8f282")
define t = Character("Tomitake", image="tomitake", color="#006e02")

# Sprites will always dissolve into the scene whenever shown
define _scene_show_hide_transition = Dissolve(0.5)

init python:
    # Code for crossfading music
    renpy.music.register_channel("music1", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)

    def audio_crossFade(fadeTime, music):
        oldChannel = None
        newChannel = None
        if renpy.music.get_playing(channel="music") is not None and renpy.music.get_playing(channel="music1") is None:
            oldChannel = "music"
            newChannel = "music1"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is not None:
            oldChannel = "music1"
            newChannel = "music"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is None:
            oldChannel = None
            newChannel = "music"
            
        if oldChannel is not None:
            renpy.music.stop(channel= oldChannel, fadeout=fadeTime)
            
        if newChannel is not None:
            renpy.music.play(music, channel=newChannel, loop=None,fadein=fadeTime)

label start:

    $ audio_crossFade(3, "Over the sky.mp3")

    scene fure2
    with Fade(1.0, 1.0, 2.0, color="#fff")

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
    stop music1 fadeout 2.0

    jump chapter1