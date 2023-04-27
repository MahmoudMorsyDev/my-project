from lib.diary_entry import DiaryEntry

class Diary:
    def __init__(self):
        self.entry_list = []
    
    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.entry_list.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.entry_list

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        count = 0
        for entry in self.entry_list:
            count += entry.count_words()
        return count

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        time = 0
        for entry in self.entry_list:
            time += entry.reading_time(wpm)
        return time

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.

        best_entry = DiaryEntry("initial", "")
        valid_entry_exists = False
        for entry in self.entry_list:
            time = entry.reading_time(wpm)
            if time <= minutes and time > best_entry.reading_time(wpm):
                best_entry = entry
                valid_entry_exists = True
        if valid_entry_exists:
            return best_entry
        else: return "error"