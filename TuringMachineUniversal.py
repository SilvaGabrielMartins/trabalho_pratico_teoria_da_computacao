def convertInput (string):
    inputConverted = [];
    inputConverted.append(1110);

    for character in string:
        if(character == 'a'):
            inputConverted.append(10);

        elif(character == 'b'):
            inputConverted.append(110)
    
    inputConverted.append(000);