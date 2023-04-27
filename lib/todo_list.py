class TodoList:
    def __init__(self):
        self.todos_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todos_list.append(todo)
        

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_todos = []
        for todo in self.todos_list:
            if not todo.complete:
                incomplete_todos.append(todo)
        return incomplete_todos        
    
    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_todos = []
        for todo in self.todos_list:
            if todo.complete:
                complete_todos.append(todo)
        return complete_todos        
    

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for todo in self.todos_list:
            todo.mark_complete()