colors = ["red", "blue", "yellow", "green", "purple"]
index = -1
program_loop = True

while(program_loop == True):
    for y in colors:
        index += 1
        print(y + " " + "(position " + str(index) + ")")

    add_or_delete = input("(add or delete?): ")
    if(add_or_delete == "add"):
        added_color = input("Color to add: ")
        lwr_case_added_color = added_color.lower()
        colors.append(lwr_case_added_color)
        
    elif(add_or_delete == "del"):
        index = input("What index would you like to delete: ")
        index = int(index)
        colors.pop(index)

    elif(add_or_delete == "exit"):
        print("\n")
        break

    
    else:
        print("\n**Unknown command**\n")
        

    index = -1