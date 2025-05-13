mood=input("How are you feeling today?-The most feeling you felt today?")
with open("mood.txt", "a") as file:
    file.write(mood +"\n")
            

yn=input("\nWanna see your past moods: ")
if yn == "y" or yn == "yes":
    print("\nHere are your past moods:")

    with open("mood.txt", "r") as file:
        for line in file:
            print(line.strip()) 

else:
    quit()
