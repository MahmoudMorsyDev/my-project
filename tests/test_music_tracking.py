from lib.music_tracking import *
def test_music_tracking():
    """
    Given the name of a song
    #add_song adds a new song to the list of songs
    """
    music_tracking = MusicTracking()
    music_tracking.add_song("Birds are singing")
    """"
    #get_songs returns the list of songs
    """

    assert music_tracking.get_songs() == ["Birds are singing"]
    music_tracking.add_song("Billie Jean")
    assert music_tracking.get_songs() == ["Birds are singing", "Billie Jean"]