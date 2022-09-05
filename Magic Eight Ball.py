import random
import time
print('  __  __          _____ _____ _____    ___  ')
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
print("")
print("")
print("")
print("       ____")
print("    ,dP9CGG88@b,")
print("  ,IP  _   Y888@@b,")
print(" dIi  (_)   G8888@b")
print("dCII  (_)   G8888@@b")
print("GCCIi     ,GG8888@@@")
print("GGCCCCCCCGGG88888@@@")
print("GGGGCCCGGGG88888@@@@...")
print("Y8GGGGGG8888888@@@@P.....")
print(" Y88888888888@@@@@P......")
print(" `Y8888888@@@@@@@P'......")
print("    `@@@@@@@@@P'.......")
print("        ''''........" )
print("")
print("")
print("By Marco Waisman-Garzon")
print("")
eight_ball = [ "It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
               "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
               "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
               "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful","Fuck off",
               "Ask a normal question","Does a bear shit in the woods?","I'm not sober enough to answer", "Well, D'uh", "Low Battery"
               "Yaaaaas bitch", "When birds fly", "The future is dissapointing for you", "I'm not a psychic", "Good vibes your way","Shut up nerd"
               ,"Maybe if you tried again it might work","Sorry it was too dark, what did you say?", "Huh?", "Type like a human and I'll answer",
               "I only answer questions from tall people", "Nope, unlucky short king", "Sadly Yes","I can safely say...","Shush I'm waiting for an adult to ask me something"
               ,"Uh Oh Spaghetti-o's","Tut tut, looks like no","Yes,if yes meant no","Only on days ending in y","Speak up, couldn't hear you", "I was distracted, try again",
               "No, but I can offer you some soup?"]
def question():
    question = input("Ask your yes or no question and the Magic 8 Ball will respond!\n")
    print("")
    print("Thinking...")
    print("")
    time.sleep(random.randrange(0,5))
    print(random.choice(eight_ball))
    print("")
while True:
    question()
    repeat = input("Would you like to ask another question? (Y or N)")
    print("")
    if not (repeat == "y" or repeat == "Y"):
        print("")
        print("")
        print("")
        print("88                                  ")
        print("88                                  ")
        print("88                                  ")
        print("88,dPPYba,  8b       d8  ,adPPYba,  ")
        print("88P'    '8a `8b     d8' a8P_____88  ")
        print("88       d8  `8b   d8'  8PP""""""")
        print("88b,   ,a8    8b,d8      8b,    ,aa")
        print("8Y Ybbd8       Y88         Ybbd8 ")
        print("                d8'                 ")
        print("               d8'                  ")
        print("")
        print("")
        print("Come back if you have more questions!")
        print("This has been the magic eight ball experience!")
        print("Please do come back")
        time.sleep(4)
        break