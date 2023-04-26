class MusicTracking:
    def __init__(self):
        # Parameters:
        #    Nothing
        # Side Effects:
        #    Initiates a list of songs

        # music_list = ["Allo", "Dog", "My love"]
        self.music_list = []
    def add_song(self, song_title):
        
        # Parameters:
        #     song_title: The title of the song to be added
        # Returns:
        #     Nothing
        # Side Effects:
        #     Adds the song to the songs list
        self.music_list.append(song_title)
    
    def get_songs(self):
        # Parameters:
        #    Nothing
        # Returns:
        #    The list of songs listened
        # Side Effects:
        #    Nothing
        return self.music_list