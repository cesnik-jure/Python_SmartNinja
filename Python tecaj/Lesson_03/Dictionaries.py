dictionary = {}

loop = True

while loop:
    post_nu = input("Post number: ")
    city = input("City: ")
    dictionary[post_nu] = city

    length = len(dictionary)

    i = 0

    for item in dictionary:
        print(item + " - " + dictionary[item])

    answer = input("Add more post numbers? (Y/N)")
    if answer.lower() != "y":
        break

