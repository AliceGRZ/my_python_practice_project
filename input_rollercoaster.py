
age = int(input()) # Don't change this line
height = int(input()) # Don't change this line
has_adult = input() == "True" # Don't change this line


if age >= 12:
    if height >= 150:
        if has_adult:
            if age < 15:
                print("You can ride with adult supervision!")
        elif age >= 15:
            print("You can ride by yourself!")  
        else:
            print("Sorry, you need an adult with you")
    else:
        print("Sorry, you're not tall enough")
else:
    print("Sorry, you're too young")
