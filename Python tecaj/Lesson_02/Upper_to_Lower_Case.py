import time

text = input("Please write some text: ")

print("Converting to lower case. Please hold.")

for i in range(5):
    time.sleep(.750)
    print(".")

print("Conversion completed!")
print("\nYour text in lower case: " + text.lower())