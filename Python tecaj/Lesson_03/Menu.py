"""
Tvoj prijatelj je bil tako zadovoljen s tvojim programom, da je vsem poznanim povedal kako super programer/ka si!
Neki lastnik restavracije je tako slišal zate in te nemudoma kontaktiral.
Rad bi namreč imel program, v katerega vneseš dnevni meni: vsako jed posebej ter ceno zanjo.
Jedi se nato shranijo v datoteko menu.txt.
"""

menu_dict = {}

with open("menu_file.txt", "w+") as menu_file:
    menu_file.write("Menu for today:\n")
    dish_nu = 1
    while True:

        dish_name = input("Dish nu. %s is: " % dish_nu)
        dish_price = float(input("Price of dish nu. %s is: " % dish_nu))
        dish_nu += 1

        menu_dict[dish_name] = dish_price

        length = len(menu_dict)

        for item in menu_dict:
            print("%s - %s €" % (item, menu_dict[item]))

        answer = input("Add more dishes? (Y/N)")

        if answer.lower() != "y":
            break

    menu_file.write("Menu for today:\n")

    for item in menu_dict:
        menu_file.write("%s - %s €\n" % (item, menu_dict[item]))

menu_file.close()