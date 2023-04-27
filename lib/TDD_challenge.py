class MusicTracker:
    def __init__(self):
        # Parameters:
        #   nothing
        # Properties:
        #   tracks_list : List of tracks 
        self.tracks_list = []

    def add_track(self, track_title):
        # Parameters:
        #    track_title : The title of the track that needs to be added
        # Returns:
        #    nothing
        # Side Effects:
        #   Adds a track to the list of tracks
        self.tracks_list.append(track_title)

    def get_tracks(self):
        # Parameters:
        #    nothing
        # Returns:
        #    the list of tracks
        # Side Effects:
        #   nothing
        return self.tracks_list