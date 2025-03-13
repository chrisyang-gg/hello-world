names = []
heights = []
while True:
    name = input("Please enter your name, type in any number to stop: ")
    height = input("Please enter your height in the form of ABC, like if you're 5'11'' then enter 511; type in any letter to stop: ")
    try:
        str_name = str(name)
        names.append(str_name)
        int_height = int(height)
        heights.append(int_height)
    except:
        break