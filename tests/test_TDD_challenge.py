from lib.TDD_challenge import MusicTracker
# add tracks that the user has listened to to the list
# view list of tracks the user has listened to

"""
Given a track title
#add_track adds the given track to the tracks list. 
"""
def test_add_and_get_track():
    music_tracker = MusicTracker()
    assert music_tracker.tracks_list == []
    music_tracker.add_track("YMCA")
    assert music_tracker.tracks_list == ["YMCA"]
    music_tracker.add_track("Billie Jean")
    assert music_tracker.tracks_list == ["YMCA", "Billie Jean"]
    assert music_tracker.get_tracks() == ["YMCA", "Billie Jean"]