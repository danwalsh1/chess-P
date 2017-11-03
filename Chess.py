#>> Chess
#>> Daniel Walsh

#######################################
############## Imports ################
#######################################

import tkinter as tk
import tkinter.font
import tkinter.messagebox
import ChessValidation as cv

#######################################
########## Global Variables ###########
#######################################

currSelectBtn = None
currSelected = ""
currSelectedColour = ""

#######################################
############## Functions ##############
#######################################

#>> (A8 -> H8) -> (A1 -> H1)
labelsP = ["C", "H", "B", "Q", "K", "B", "H", "C", "P", "P", "P", "P", "P", "P", "P", "P", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "P", "P", "P", "P", "P", "P", "P", "P", "C", "H", "B", "Q", "K", "B", "H", "C"]
#>> (A8 -> H8) -> (A1 -> H1)
labelsC = ["B", "B", "B", "B", "B", "B", "B", "B", "B", "w", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "w", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]

#######################################
########### Button Functions ##########
#######################################

def updateBoard():
    ''' Sets the text and font colour for all buttons on the board '''
    count = 0
    for btn in btnList:
        btn.config(text = labelsP[count])

        if(labelsC[count] == "B"):
            btn.config(fg = "black")
        else:
            btn.config(fg = "white")
        count += 1

def updateSelected():
    ''' Updates the label that indicates what position has been selected (to be moved) '''
    if(currSelected != ""):
        lblSelected.configure(text = "Selected: " + currSelected)
    else:
        lblSelected.configure(text = "Selected: ##")

def getButtonInfo(pos, infoType = "btn"):
    ''' Takes string position [letter][number] and returns a button object '''
    if(pos[0] == "A"):
        lPos = 0
    elif(pos[0] == "B"):
        lPos = 1
    elif(pos[0] == "C"):
        lPos = 2
    elif(pos[0] == "D"):
        lPos = 3
    elif(pos[0] == "E"):
        lPos = 4
    elif(pos[0] == "F"):
        lPos = 5
    elif(pos[0] == "G"):
        lPos = 6
    elif(pos[0] == "H"):
        lPos = 7

    if(infoType == "btn"):
        return btnList[lPos + (8*(8 - int(pos[1])))]
    elif(infoType == "num"):
        return (lPos + (8*(8 - int(pos[1]))))
    else:
        print("Error:: getButtonInfo >> invalid infoType :>>>:" + str(infoType))
        return None

def validateMove(pos):
    ''' Validates whether a move is legal or not (return boolean) '''
    return False

def btnFunction(pos):
    ''' Function is run whenever a button is pressed '''
    global currSelected
    global currSelectedColour
    global currSelectedBtn

    #>> Is the player choosing a piece to move, or a place to move it to? (Or deselecting their chosen piece?)
    if(currSelected == ""):
        #>> Player is selecting a piece to move
        currSelected = pos
        updateSelected()
        btnSelected = getButtonInfo(pos)
        currSelectedColour = btnSelected['bg']
        btnSelected.config(bg = "gold")
        currSelectedBtn = btnSelected
    else:
        if(currSelected == pos):
            #>> Player is deselecting their chosen piece
            currSelected = ""
            updateSelected()
            btnSelected = getButtonInfo(pos)
            btnSelected.config(bg = currSelectedColour)
            currSelectedColour = ""
        else:
            #>> Player is choosing a place to move their piece to.
            #>> Reset selected position
            currSelected = ""
            updateSelected()
            currSelectedBtn.config(bg = currSelectedColour)
            currSelectedColour = ""
            #>> Validate move
            validMove = validateMove(pos)
            #>> Is the move valid
            if(validMove == True):
                #>> Make the move
                #>> Next player
                pass
            else:
                tk.messagebox.showwarning("Invalid Move","You attempted to make an illegal move!")
    

#######################################
################ GAME #################
#######################################

root = tk.Tk()

btnHeight = 2
btnWidth = 5
btnFont = tk.font.Font(size = 25)
lblFont = tk.font.Font(size = 25)
initialText = ""
systemColour = "light grey"
darkColour = "saddle brown"
lightColour = "sandy brown"

root.configure(background = systemColour)
root.resizable(0,0)

root.title("Chess")

#>> Labels
lblA = tk.Label(root, text = "A", fg = "black", bg = systemColour, font = lblFont)
lblA.grid(row = 0, column = 1)
lblB = tk.Label(root, text = "B", fg = "black", bg = systemColour, font = lblFont)
lblB.grid(row = 0, column = 2)
lblC = tk.Label(root, text = "C", fg = "black", bg = systemColour, font = lblFont)
lblC.grid(row = 0, column = 3)
lblD = tk.Label(root, text = "D", fg = "black", bg = systemColour, font = lblFont)
lblD.grid(row = 0, column = 4)
lblE = tk.Label(root, text = "E", fg = "black", bg = systemColour, font = lblFont)
lblE.grid(row = 0, column = 5)
lblF = tk.Label(root, text = "F", fg = "black", bg = systemColour, font = lblFont)
lblF.grid(row = 0, column = 6)
lblG = tk.Label(root, text = "G", fg = "black", bg = systemColour, font = lblFont)
lblG.grid(row = 0, column = 7)
lblH = tk.Label(root, text = "H", fg = "black", bg = systemColour, font = lblFont)
lblH.grid(row = 0, column = 8)

lbl1 = tk.Label(root, text = "1", fg = "black", bg = systemColour, font = lblFont)
lbl1.grid(row = 8, column = 0)
lbl2 = tk.Label(root, text = "2", fg = "black", bg = systemColour, font = lblFont)
lbl2.grid(row = 7, column = 0)
lbl3 = tk.Label(root, text = "3", fg = "black", bg = systemColour, font = lblFont)
lbl3.grid(row = 6, column = 0)
lbl4 = tk.Label(root, text = "4", fg = "black", bg = systemColour, font = lblFont)
lbl4.grid(row = 5, column = 0)
lbl5 = tk.Label(root, text = "5", fg = "black", bg = systemColour, font = lblFont)
lbl5.grid(row = 4, column = 0)
lbl6 = tk.Label(root, text = "6", fg = "black", bg = systemColour, font = lblFont)
lbl6.grid(row = 3, column = 0)
lbl7 = tk.Label(root, text = "7", fg = "black", bg = systemColour, font = lblFont)
lbl7.grid(row = 2, column = 0)
lbl8 = tk.Label(root, text = "8", fg = "black", bg = systemColour, font = lblFont)
lbl8.grid(row = 1, column = 0)

lblTurn = tk.Label(root, text = "Player: WHITE", fg = "black", bg = systemColour, font = lblFont)
lblTurn.grid(row = 9, column = 1, columnspan = 4)
lblSelected = tk.Label(root, text = "Selected: ##", fg = "black", bg = systemColour, font = lblFont)
lblSelected.grid(row = 9, column = 5, columnspan = 4)

#>> Buttons
btnA1 = tk.Button(root, text = "R", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("A1"))
btnA1.grid(row = 8, column = 1)
btnB1 = tk.Button(root, text = "N", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("B1"))
btnB1.grid(row = 8, column = 2)
btnC1 = tk.Button(root, text = "B", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("C1"))
btnC1.grid(row = 8, column = 3)
btnD1 = tk.Button(root, text = "Q", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("D1"))
btnD1.grid(row = 8, column = 4)
btnE1 = tk.Button(root, text = "K", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("E1"))
btnE1.grid(row = 8, column = 5)
btnF1 = tk.Button(root, text = "B", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("F1"))
btnF1.grid(row = 8, column = 6)
btnG1 = tk.Button(root, text = "N", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("G1"))
btnG1.grid(row = 8, column = 7)
btnH1 = tk.Button(root, text = "R", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("H1"))
btnH1.grid(row = 8, column = 8)

btnA2 = tk.Button(root, text = "P", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("A2"))
btnA2.grid(row = 7, column = 1)
btnB2 = tk.Button(root, text = "P", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("B2"))
btnB2.grid(row = 7, column = 2)
btnC2 = tk.Button(root, text = "P", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("C2"))
btnC2.grid(row = 7, column = 3)
btnD2 = tk.Button(root, text = "P", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("D2"))
btnD2.grid(row = 7, column = 4)
btnE2 = tk.Button(root, text = "P", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("E2"))
btnE2.grid(row = 7, column = 5)
btnF2 = tk.Button(root, text = "P", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("F2"))
btnF2.grid(row = 7, column = 6)
btnG2 = tk.Button(root, text = "P", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("G2"))
btnG2.grid(row = 7, column = 7)
btnH2 = tk.Button(root, text = "P", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("H2"))
btnH2.grid(row = 7, column = 8)

btnA3 = tk.Button(root, text = "", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("A3"))
btnA3.grid(row = 6, column = 1)
btnB3 = tk.Button(root, text = "", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("B3"))
btnB3.grid(row = 6, column = 2)
btnC3 = tk.Button(root, text = "", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("C3"))
btnC3.grid(row = 6, column = 3)
btnD3 = tk.Button(root, text = "", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("D3"))
btnD3.grid(row = 6, column = 4)
btnE3 = tk.Button(root, text = "", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("E3"))
btnE3.grid(row = 6, column = 5)
btnF3 = tk.Button(root, text = "", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("F3"))
btnF3.grid(row = 6, column = 6)
btnG3 = tk.Button(root, text = "", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("G3"))
btnG3.grid(row = 6, column = 7)
btnH3 = tk.Button(root, text = "", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("H3"))
btnH3.grid(row = 6, column = 8)

btnA4 = tk.Button(root, text = "", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("A4"))
btnA4.grid(row = 5, column = 1)
btnB4 = tk.Button(root, text = "", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("B4"))
btnB4.grid(row = 5, column = 2)
btnC4 = tk.Button(root, text = "", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("C4"))
btnC4.grid(row = 5, column = 3)
btnD4 = tk.Button(root, text = "", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("D4"))
btnD4.grid(row = 5, column = 4)
btnE4 = tk.Button(root, text = "", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("E4"))
btnE4.grid(row = 5, column = 5)
btnF4 = tk.Button(root, text = "", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("F4"))
btnF4.grid(row = 5, column = 6)
btnG4 = tk.Button(root, text = "", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("G4"))
btnG4.grid(row = 5, column = 7)
btnH4 = tk.Button(root, text = "", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("H4"))
btnH4.grid(row = 5, column = 8)

btnA5 = tk.Button(root, text = "", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("A5"))
btnA5.grid(row = 4, column = 1)
btnB5 = tk.Button(root, text = "", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("B5"))
btnB5.grid(row = 4, column = 2)
btnC5 = tk.Button(root, text = "", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("C5"))
btnC5.grid(row = 4, column = 3)
btnD5 = tk.Button(root, text = "", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("D5"))
btnD5.grid(row = 4, column = 4)
btnE5 = tk.Button(root, text = "", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("E5"))
btnE5.grid(row = 4, column = 5)
btnF5 = tk.Button(root, text = "", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("F5"))
btnF5.grid(row = 4, column = 6)
btnG5 = tk.Button(root, text = "", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("G5"))
btnG5.grid(row = 4, column = 7)
btnH5 = tk.Button(root, text = "", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("H5"))
btnH5.grid(row = 4, column = 8)

btnA6 = tk.Button(root, text = "", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("A6"))
btnA6.grid(row = 3, column = 1)
btnB6 = tk.Button(root, text = "", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("B6"))
btnB6.grid(row = 3, column = 2)
btnC6 = tk.Button(root, text = "", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("C6"))
btnC6.grid(row = 3, column = 3)
btnD6 = tk.Button(root, text = "", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("D6"))
btnD6.grid(row = 3, column = 4)
btnE6 = tk.Button(root, text = "", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("E6"))
btnE6.grid(row = 3, column = 5)
btnF6 = tk.Button(root, text = "", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("F6"))
btnF6.grid(row = 3, column = 6)
btnG6 = tk.Button(root, text = "", fg="white", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("G6"))
btnG6.grid(row = 3, column = 7)
btnH6 = tk.Button(root, text = "", fg="white", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("H6"))
btnH6.grid(row = 3, column = 8)

btnA7 = tk.Button(root, text = "P", fg="black", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("A7"))
btnA7.grid(row = 2, column = 1)
btnB7 = tk.Button(root, text = "P", fg="black", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("B7"))
btnB7.grid(row = 2, column = 2)
btnC7 = tk.Button(root, text = "P", fg="black", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("C7"))
btnC7.grid(row = 2, column = 3)
btnD7 = tk.Button(root, text = "P", fg="black", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("D7"))
btnD7.grid(row = 2, column = 4)
btnE7 = tk.Button(root, text = "P", fg="black", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("E7"))
btnE7.grid(row = 2, column = 5)
btnF7 = tk.Button(root, text = "P", fg="black", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("F7"))
btnF7.grid(row = 2, column = 6)
btnG7 = tk.Button(root, text = "P", fg="black", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("G7"))
btnG7.grid(row = 2, column = 7)
btnH7 = tk.Button(root, text = "P", fg="black", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("H7"))
btnH7.grid(row = 2, column = 8)

btnA8 = tk.Button(root, text = "R", fg="black", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("A8"))
btnA8.grid(row = 1, column = 1)
btnB8 = tk.Button(root, text = "N", fg="black", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("B8"))
btnB8.grid(row = 1, column = 2)
btnC8 = tk.Button(root, text = "B", fg="black", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("C8"))
btnC8.grid(row = 1, column = 3)
btnD8 = tk.Button(root, text = "Q", fg="black", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("D8"))
btnD8.grid(row = 1, column = 4)
btnE8 = tk.Button(root, text = "K", fg="black", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("E8"))
btnE8.grid(row = 1, column = 5)
btnF8 = tk.Button(root, text = "B", fg="black", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("F8"))
btnF8.grid(row = 1, column = 6)
btnG8 = tk.Button(root, text = "N", fg="black", bg = lightColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("G8"))
btnG8.grid(row = 1, column = 7)
btnH8 = tk.Button(root, text = "R", fg="black", bg = darkColour, height = btnHeight, width = btnWidth, font = btnFont, command = lambda: btnFunction("H8"))
btnH8.grid(row = 1, column = 8)

#>> (A8 -> H8) -> (A1 -> H1)
btnList = [btnA8, btnB8, btnC8, btnD8, btnE8, btnF8, btnG8, btnH8, btnA7, btnB7, btnC7, btnD7, btnE7, btnF7, btnG7, btnH7, btnA6, btnB6, btnC6, btnD6, btnE6, btnF6, btnG6, btnH6, btnA5, btnB5, btnC5, btnD5, btnE5, btnF5, btnG5, btnH5, btnA4, btnB4, btnC4, btnD4, btnE4, btnF4, btnG4, btnH4, btnA3, btnB3, btnC3, btnD3, btnE3, btnF3, btnG3, btnH3, btnA2, btnB2, btnC2, btnD2, btnE2, btnF2, btnG2, btnH2, btnA1, btnB1, btnC1, btnD1, btnE1, btnF1, btnG1, btnH1]

root.mainloop()
