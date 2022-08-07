HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выход. """

today = []
tommorow = []
other = []

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP) 
  elif command == "show":
    print(today, tommorow, other)
  elif command == "add":
    task = input("Введите название задачи: ")
    data = input("Введите дату задачи: ")
    if data == ("Сегодня"):
      today.append(task)
      print("Задача добавлена")
    elif data == ("Завтра"):
      task.append(task)
      print("Задача добавлена")
    elif data == ("В другой день"):
      data.append(task)
      print("Задача добавлена")
    else:
      print("Неизвестная команда, попробуйте еще раз.")
      
  elif command ==  "exit":
    print("Спасибо за использование! До свидания!")
    break
  else: 
    print("Неизвестная команда, попробуйте еще раз.")
    