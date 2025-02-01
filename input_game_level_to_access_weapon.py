
level = int(input()) # Don't change this line
has_training = input() == "True" # Don't change this line

if level >= 1 and level <= 5:
    print("Basic weapons only")
elif level >= 6 and level <= 10 and not has_training:
    print("Need weapon training first")
elif level >= 6 and level <= 10 and has_training:
    print("Access to advanced weapons granted")
elif level >= 11:
    print("Access to all weapons granted")
elif level == 0 or level < 0:
    print("Invalid level")