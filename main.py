HELP = """
Помощь - напечатать справку по программе.

Добавить - добавить задачу в список.

Показать - Показать добавленные задачи.

Случайно - добавляет случайную задачу на сегодня.

Выход - выход. 
"""

random_task = "Сходить в магазин"

tasks = {
  
}

run = True

while run:
  command = input("Введите команду: ")
  if command == "Помощь":
    print(HELP) 
  elif command == "Показать":
    data = input("Введите дату, для просмотра задач: ")
    if data in tasks:
     for task in tasks[data]:
       print("- ", task)
    else:
      print("Задач на эту дату не найдено")
    
  elif command == "Добавить":
    data = input("Введите дату задачи: ")
    task = input("Введите название задачи: ")
    if data in tasks:
      tasks[data].append(task)
    else:
      tasks[data] = []
      tasks[data].append(task)
    print("Задача", task, "добавлена на", data)  

  elif command == "Случайно":
    if "Сегодня" in tasks:
      tasks["Сегодня"].append(random_task)
    else:
      tasks["Сегодня"] = []
      tasks["Сегодня"].append(random_task)
      print("Задача", random_task, "добавлена на сегодня.")
      
  elif command == "Выход": #Последняя команда
    print("Спасибо за использование! До свидания!")
    break
  else: 
    print("Неизвестная команда, попробуйте еще раз.")
    