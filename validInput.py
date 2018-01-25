# Valid Input Library

def floatInput(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            pass

def intInput(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            pass

def floatInputRng(prompt,low,high):
    while True:
        try:
            userInput = float(input(prompt))
            if userInput >= low and userInput < high:
                return userInput
        except:
            pass

def intInputRng(prompt,low,high):
    while True:
        try:
            userInput = int(input(prompt))
            if userInput >= low and userInput < high:
                return userInput
        except:
            pass

def floatInputGTZero(prompt):
    while True:
        try:
            userInput = float(input(prompt))
            if userInput > 0:
                return userInput
        except:
            pass

def intInputGTZero(prompt):
    while True:
        try:
            userInput = int(input(prompt))
            if userInput > 0:
                return userInput
        except:
            pass
def stringInputCI(prompt, acceptList):
    while True:
        userInput = input(prompt).lower()
        if userInput in acceptList:
            return userInput