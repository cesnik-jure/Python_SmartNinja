# Sassy converter is sassy

another_try = True

print(
    'Why hello ther... Oh.. It\'s you...\n'
    'Well, since you don\'t know how to do simple conversions, it seems I\'ll have to do it for you.\n')

km_to_m = str(input("OK, let me guess... Kilometers to miles, right? (Y/N) "))

if km_to_m == "Y" or km_to_m == "y":
    print("\n*sigh*")
    print("You're American, aren't you?")

while another_try:
    if km_to_m == "Y" or km_to_m == "y":
        km = float(input("\nSo, how many kilometers do you have? "))
        print(str(km) + " kilometers is exactly " + str(km*0.621371) + " miles.")
        print(".\n.\n.\nDumbass...")

    else:
        print("\nSorry, but I'm not doing any other conversions today. Tough luck buddy.")
        break

    decision = str(input('\nSo... Want to do another "amazing" [km] to [mile] conversion? (Y/N) '))
    if decision == "Y" or decision == "y":
        print("\nUgh...")
    else:
        print("\nThank the Binary System! See ya!")
        another_try = False

