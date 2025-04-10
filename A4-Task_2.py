# Task 2: Write and Append Data to a File
with open("output.txt","w") as file:
    writingfile=file.write(input("Enter text to write to the file: "))
    print("Data successfully written to output.txt\n")
with open("output.txt","a") as file:
    appendfile=file.write("\n")
    appendfile=file.write(input("Enter additional text to append: "))
    print("Data successfully appended !\n")
with open("output.txt","r") as file:
    print("Final content of Output.txt:")
    readingfile=file.read()
    print(readingfile)


