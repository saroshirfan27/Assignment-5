class Task:
    
    task_name = ""
    priority = 0
    
    def set_task_detail(self, task_name, priority):
        
        self.task_name = task_name
        self.priority = priority
    
    def mark_as_complete(self):
        self.priority = 0
    
    def display_task_info(self):
        print(str(self.task_name) , end = " ")
        if( self.priority == 0 ):
            print("PENDING")
        else:
            print("COMPLETED")
        
task1 = Task()
