#enumerate function
#basically gives us the index number

marks=[76,90,55,94,67]

for index, mark in enumerate(marks):
    print(mark);
    if(index==3):
        print("congrats you got highest marks")