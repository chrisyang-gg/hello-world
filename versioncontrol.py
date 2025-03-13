names = []
heights = []
while True:
    
    name = input("Please enter your name, type in any number to stop: ")
    if name.isdigit():
        break
    
    height = input("Please enter your height in the form of ###, for example, if you're 5'08'' then enter 508; type in any letter to stop: ")
    if not height.isdigit():
        break
    
    try:
        str_name = str(name)
        names.append(str_name)
        int_height = int(height)
        heights.append(int_height)
    except:
        print("Invalid input try again...")

    if int_height >= 509:
        print("Wow", name, "your pretty tall!")
    else:
        print("Yikes...", name, "your REALLY short")

print("\nSummary of entered names and heights:")
for i in range(len(names)):
    print(names[i] + ": " + str(heights[i]))
