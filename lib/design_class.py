class UserTodo:
    def __init__(self):
        """
        Class Object:
            self.list_of_todos : a nested dictionary containing the Task title, description and 
            whether it's done or not
        Side effects:
            no side effects    
        """
        self.list_of_todos = {}

    def get_all_todo_tasks(self):
        """
        Parameters:
            No parameter
        Returns: 
            Returns a list of all the tasks (title and description) that are still todo
        Side Effects:
            no side effects
        """
        list_of_tasks = []
        for key, value in self.list_of_todos.items():
            task_title = key
            task_description = value['description']
            if not value['done']:
                list_of_tasks.append(f"{task_title}: {task_description}")
        return list_of_tasks
    
    def add_task(self, task_title, task_description):
        """
        Parameters: 
            task_title: a string, 
            task_description: a string
        Side-effects:
            appends a new task to the task dictionary    
            
        """
        self.list_of_todos[task_title]= {"description": task_description, "done": False}
        
    def done_task(self, task_title):
        """
        Parameters:
            task_title: the title of task that was completed.
        Returns: 
            No return
        Side Effects:
            It does not remove the task from the list, only changes the "done" entry of its dictionary
        """
        self.list_of_todos[task_title]["done"] = True