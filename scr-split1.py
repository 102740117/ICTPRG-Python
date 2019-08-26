myInputSplit = []
while (len(myInputSplit) < 2):
    myInput = input("Enter a Sentence: ")
    myInputSplit = myInput.split()
    print("Enter at least three words")
      
else:
    print(myInputSplit[1])
    print(myInputSplit[len(myInputSplit)-1])


