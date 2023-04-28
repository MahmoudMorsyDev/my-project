class Diary:
    #public properties: 
    #   diary_entries_list
    #   todo_list

    def __init__(self):
        # side-effects:
        # initializes the diary entries list
        # initializes the todo list
        self.diary_entries_list = []
        self.todo_list = []

    def add_todo(self, todo):
        # Parameters:
        #   todo: An instance of a Todo entry
        # Side-effects:
        #   add a todo instance to the list of todos
        self.todo_list.append(todo)

    def add_diary_entry(self, entry):
        # Parameters:
        #   entry: An instance of a diary entry
        # Side-effects:
        #   add a diary entry instance to the list of entries
        self.diary_entries_list.append(entry)

    def get_all_todos(self):
        # Returns:
        #   A list of all tasks to do
        return self.todo_list

    def get_all_entries(self):
        # Returns: 
        #  A list of all diary entries instances
        return self.diary_entries_list

    def get_time_based_entries(self, wpm, minutes):
        # Parameters:
        #   wpm: Number of words a user can read in a minute
        #   minutes: time that the user has to read
        # Returns: 
        #   A list of the entries that can be read at this pace during the given time period
        words = wpm * minutes
        time_based_entries = []
        for entry in self.diary_entries_list:
            if len(entry.contents.split(" ")) <= words:
                time_based_entries.append(entry)
        return time_based_entries