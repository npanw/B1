from fileinput import filename


file ="example.txt"
file = open(filename, "w")
dataString = "Some dummy text data\n newline \t after tab"
fileContent = file.write(dataString)
file.close()

file = open(filename, "r")
fileContent = file.read()

