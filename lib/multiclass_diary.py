class Diary:
    #public properties: 
    #   diary_entries_list
    #   todo_list

    def __init__(self):
        # side-effects:
        # initializes the diary entries list
        # initializes the todo list
        pass

    def add_todo(self, todo):
        # Parameters:
        #   todo: An instance of a Todo entry
        # Side-effects:
        #   add a todo instance to the list of todos
        pass

    def get_all_todos(self):
        # Returns:
        #   A list of all tasks to do
        pass

    def get_all_entries(self):
        # Returns: 
        #  A list of all diary entries instances
        pass

    def get_time_based_entries(self, wpm, minutes):
        # Parameters:
        #   wpm: Number of words a user can read in a minute
        #   minutes: time that the user has to read
        pass