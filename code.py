#PYTHON CHATBOT
import os


readPy = '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'
writePy = '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'
negative_emotions = r"C:/Users/1005447/Documents/negative.txt" #Download the file "negative.txt" (in files) and change the file path here to your file path.
positivie_emotions = r"C:/Users/1005447/Documents/positive.txt" #Download the file "positive.txt" (in files) and change the file path here to your file path

print("Welcome to the chatbot.")
name = input("Please enter your name: ")
name = name.capitalize()
feel = input(f"Hi there, {name}. How are you today? --> ")
feel = feel.lower()
with open(negative_emotions, "r") as f:
    negative_words = f.read().split(" ")
with open(positivie_emotions, "r") as p:
    pos_words = p.read().split(" ")
if feel in negative_words:
    why = input(f"I am sorry to hear that you feel {feel}. Why do you feel {feel}, {name}? --> ")
if feel in pos_words:
    what = input(f"What makes you feel {feel}? --> ")
else:
    def add():
        global pos_words, negative_words, what, why, pos, neg, showPos, showNeg, feel
        new = feel
        where_to = input(f"I'm not sure I understand the word {feel}. Is it a positive or negative emotion? (Type P for positive or N for negative) --> ")
        if where_to.upper() == "N":
    #Open the file in append mode
            with open("C:/Users/1005447/Documents/negative.txt", "a") as z:
    # Add the new word to the file
                z.write(new)
                showPos = False
                showNeg = True
                print(f"Noted. '{new}' is now in the list of negative emotions.")
                why = input(f"I am sorry to hear that you feel {new}, {name}. Why do you feel {new}? --> ")
                neg = f"Your name is {name}, and you feel {feel} today. Here is what you said about why you feel {feel}: '{why}'"
# Open the file in append mode
        elif where_to.upper() == "P":
            with open("C:/Users/1005447/Documents/positive.txt", "a") as x:
    # Add the new word to the file
                x.write(new)
                showPos = True
                showNeg = False
                print(f"Noted. '{new}' is now in the list of positive emotions.")
                what = input(f"I am glad to hear that you feel {new}, {name}. What makes you feel {new}? --> ")
                pos = f"Your name is {name}, and you feel {feel} today. Here is what you said about why you feel {feel}: '{what}'"
        else:
            print("That's not a valid input. Please enter a valid input.")
            add()
        feel = new
    add()
       
if showPos:
    print(pos)
if showNeg:
    print(neg)

