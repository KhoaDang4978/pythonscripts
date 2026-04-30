# This is a JSON todo list
print("This is your Todo list")
print("----------------------")
class Task:
     def __init__(self, name, status, priority):
          self.name = name
          self.status = status
          self.priority = priority
     def mark_done(self):
          self.status = "done"
import json
import os
tasks = []
if os.path.exists("todolist.json"):
    with open("todolist.json") as f:
        tasks = json.load(f)
while True:
     operation = str(input("Please choose operation (add task, mark done, show all tasks, show by status or exit): "))
     if operation == "add task":
          name = str(input("Please input task's name: "))
          p = str(input("Please set priority (high/medium/low): "))
          status = "not done"
          t = Task(name, status,p )
          tasks.append({
               "name": t.name,
               "status": t.status,
               "priority": t.priority
          })
          with open("todolist.json", "w") as f:
            json.dump(tasks, f)
     elif operation == "mark done":
          name = input("Which task do you want to mark done?")
          for task in tasks:
               if task["name"] == name:
                task["status"] = "done"
          with open("todolist.json", 'w') as f:
              json.dump(tasks, f)
     elif operation == "show all tasks":
          for task in tasks:
                print(f"{task['name']} - {task['status']} - {task['priority']}")     
     elif operation == "show by status":
         if t.status == "done":
             s = input("Show which status? (done/not done): ")
             for task in tasks:
                if task["status"] == s:
                     print(f"{task['name']} - {task['priority']}")
     elif operation == "exit":
         break
     else:
         print("Invalid operation!")