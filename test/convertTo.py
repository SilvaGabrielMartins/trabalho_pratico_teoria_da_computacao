class convertTo:
    def __init__(self):
        self.inputs = open("entrada.txt", "r", encoding="utf-8")

        self.machine = open("maquina.txt", "r", encoding="utf-8")

        self.encodeInput = []
        self.encodeMachine = ''
        self.tape = []

    def __convertInput__(self):
        for rows in self.inputs:
            encode = ''
            encode += '111'  # init tape input
            for char in rows:
                if(char == 'a'):
                    encode += '01'  # encode character 'a'

                elif(char == 'b'):
                    encode += '011'  # encode character 'b'
            encode += '000'  # end tape input
            self.encodeInput.append(encode)

    def __convertMachine__(self):
        control = False
        encode = ''

        for transition in self.machine:
            temp = [] 

            # remove unused characters
            transition = transition.strip()
            transition = transition.replace('(', '')
            transition = transition.replace(')', '')
            transition = transition.replace('[', '')
            transition = transition.replace(']', '')
            transition = transition.replace(' ', '')
            transition = transition.split('=')

            for row in transition:
                temp = row.split(',') # remove unused characters and split string
                for char in temp:
                    if(control == True):
                        encode += '0'

                    if(char[0] == 'q'):
                        encode += str('1'*(int(char[1])+1)) # the amount of character depend the (q + number)
                        if(control == False): # control for don't put zero in the beginning
                            control = True

                    elif(char == 'B'): # encode character 'B'
                        encode += '111'

                    elif(char == 'R'): # encode character 'R'
                        encode += '11'

                    elif(char == 'L'): # encode character 'L'
                        encode += '1'

                    elif(char == '0'): # encode number '0'
                        encode += '1'

                    elif(char == '1'): # encode number '1'
                        encode += "11"
        self.encodeMachine += encode

    # this method make a tape concatenating encoded machine and the encoded input.
    # the 0's in the begining and end of encoded machine is necessary to show the end and start of machine
    def __makeTape__(self):
        for language in self.encodeInput:
            self.tape.append('000' + self.encodeMachine + '000' + language)

    # method for debbug, print encoded input, encoded machine and the tape.
    def __print__(self):
        for row in self.encodeInput:
            print('encoded input -> ' + row)

        print('\encoded machine -> ' + self.encodeMachine + '\n')

        for tape in self.tape:
            print('tape -> ' + tape)
