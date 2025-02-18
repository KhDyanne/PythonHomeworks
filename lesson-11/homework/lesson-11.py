class Task:
    def __init__(self,title,description,due_date):
        self.title=title
        self.description=description
        self.due_date=due_date
        self.status='incomplete'
        
    def mark_complete(self):
        self.status='complete'
        
    def __str__(self):
        return f"{self.title} - {self.description} (Due: {self.due_date}, Status: {self.status})"
    

class ToDoList:
    def __init__(self):
        self.taskList=[]
        
    def addTask(self, title, description, due_date):
        new_task=Task(title,description,due_date)
        self.taskList.append(new_task)
        print(f"\nTask '{title}' has been added successfully.")
        
    def list_tasks(self):
        if not self.taskList:
           return "\nNo Tasks Available"
        else:
           tasks= "\n".join([f"\n{i}. {task}" for i, task in enumerate(self.taskList, 1)])
           return tasks

                
    def mark_task_complete(self, index):
        if 0<=index<len(self.taskList):
            self.taskList[index].mark_complete()
            print(f'\nTask {self.taskList[index].title} marked as complete')
        else:
            print("\nInvalid task index. Please try again")
    
    def list_incomplete_tasks(self):
        incomplete_tasks=list(filter(lambda i: i.status=="incomplete", self.taskList))
        if not incomplete_tasks:
            return "\nNo incomplete tasks"
        else:
            return "\n".join(f"\n{i + 1}. {task}" for i, task in enumerate(incomplete_tasks))
                
def print_menu():
    print("\nMy To Do List")
    print("\n1. Add a new task")
    print("2. Mark a task complete")
    print("3. List all tasks")
    print("4. List incomplete tasks")
    print("5. Exit")


def main():
    import os
   
    todo=ToDoList()
    
    while True: 
        os.system('cls') 
        print_menu()
        choice=input("Enter your choice 1-5")
        
        if choice == "1":
            title=input("Enter task title: ")
            description=input("Enter task description: ")
            due_date=input("Enter due date: ")
            
            todo.addTask(title,description,due_date)
        
        elif choice=="2":
            todo.list_tasks()            
            index=int(input("Enter task number: "))
            todo.mark_task_complete(index-1)
            
        elif choice=="3":
            print(todo.list_tasks())
            
        elif choice=="4":
            print(todo.list_incomplete_tasks())
            
        elif choice=="5":
            print(f'\nExiting program')
            break            
        
        else:
            print('Please enter numbers betweeen 1-5')
            
main()
            