from graphics import root, game_out, game_text
import time

gstate = 1

def main():
    root.mainloop()
    
def gamestate(text):
    if gstate == 1:
        gamestate1(text)
    elif gstate == 2:
        gamestate2(text)
    elif gstate == 3:
        gamestate3(text)
    elif gstate == 4:
        gamestate4(text)
    elif gstate == 5:
        gamestate5(text)
    elif gstate == 6:
        gamestate6(text)
    elif gstate == 7:
        gamestate7(text)
    elif gstate == 8:
        gamestate8(text)
        
        
def gamestate1(text):
    if text.lower() == "play":
        game_out(text.capitalize())
        game_out("Enter character name:", "output")
        global gstate
        gstate = 2
        
def gamestate2(text):
    if 1 < len(text) < 13:
        game_out(text)
        game_out(f"Welcome, {text.capitalize()}!", "title")
    global char_name 
    char_name = text.capitalize()
    with open("text_files/narrative.txt") as class_desc:
        class_desc = class_desc.readlines()
    count = 0
    beginning = "***ClassDescStart***"
    end = "***ClassDescEnd***"
    section = []
    for line in class_desc:
        if beginning in line:
            section.append(count)
        if end in line:
            section.append(count)
        count += 1
    print(section)
    for line in range(section[0]+1, section[1]):
        game_out(class_desc[line], "output")
        
        

def gamestate3(text):
    pass

def gamestate4(text):
    pass

def gamestate5(text):
    pass

def gamestate6(text):
    pass

def gamestate7(text):
    pass

def gamestate8(text):
    pass     
        
main()