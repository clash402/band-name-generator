# MAIN
print("Hello peoples!\n")

app_is_in_progress = True

while app_is_in_progress:
    city = input("What city did you grow up in?\n")
    pet = input("\nWhat was the name of your favorite pet?\n")
    band_name = city + " " + pet

    print("\nCongratulations! Your band name is " + band_name + ".")

    res = input("Try again? (y/n)\n")

    if res != "y":
        app_is_in_progress = False
