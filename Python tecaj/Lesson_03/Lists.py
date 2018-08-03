todo_list = []

todo_file = open("todo_file.txt", "w+")

loop = True

while loop:
    task = input("What should I do? ")
    todo_list.append(task)

    length = len(todo_list)

    i = 0

    for i in range(length):
        print("%s. %s" % (i+1, todo_list[i]))

    answer = input("Add more things? (Y/N)")
    if answer.lower() != "y":
        break

i = 0
length = len(todo_list)
todo_file.write("All tasks:\n")

for i in range(length):
    todo_file.write(todo_list[i] + "\n")

todo_file.close()