import pyautogui
import time
import numpy as np
from stockfish import Stockfish
from PIL import ImageGrab, ImageChops, Image
stockfish = Stockfish(path="C:/Users/SgO/workspace/automatic-chess-bot/stockfish_15.1_win_x64_avx2/stockfish-windows-2022-x86-64-avx2")
stockfish.update_engine_parameters({"Hash": 2048, "UCI_Chess960": "true"}) 
pieces = ["black_rook_a.png", "black_horsey_b.png", "black_bishop_a.png", "black_queen_b.png", "black_king_a.png", "black_bishop_b.png", "black_horsey_a.png", "black_rook_b.png","black_pawn_b.png", "black_pawn_a.png", "empty_space_a.png", "empty_space_b.png", "white_pawn_a.png", "white_pawn_b.png", "white_rook_b.png", "white_horsey_a.png", "white_bishop_b.png", "white_queen_a.png", "white_king_b.png", "white_bishop_a.png", "white_horsey_b.png", "white_rook_a.png"]
letter_to_number_index = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}
rowPositions = []
filePositions = []
#get coordinates boxes for every file and row
def getCoordinates():
    x, y = pyautogui.locateCenterOnScreen("img/references/white_rook_b.png")
    x1, y1 = pyautogui.locateCenterOnScreen("img/references/white_horsey_a.png")
    delta = x1 - x
    for i in range(0, 8):
        rowPositions.append(x)
        filePositions.append(y)
        x = x + delta
        y = y - delta
    filePositions.reverse()
#getCoordinates()
rowPositions = [605, 697, 789, 881, 973, 1065, 1157, 1249]
filePositions = [209, 301, 393, 485, 577, 669, 761, 853]
delta = 92
def screenshotsIniciales():
    counter = 0
    #this gets all of blacks pieces for the first file (8, a-h)
    for i in range(0, 8): 
        actual_piece = pyautogui.screenshot(region=(rowPositions[i] - delta/2, filePositions[0] - delta/2, delta, delta))
        actual_piece.save(r"./img/"+pieces[counter])  
        counter+=1
    #2 pawns for white
    for i in range(0, 2):
        actual_piece = pyautogui.screenshot(region=(rowPositions[i] - delta/2, filePositions[1] - delta/2, delta, delta))
        actual_piece.save(r"./img/"+pieces[counter])   
        counter+=1
    #2 blank squares
    for i in range(0, 2):
        actual_piece = pyautogui.screenshot(region=(rowPositions[i] - delta/2, filePositions[2] - delta/2, delta, delta))
        actual_piece.save(r"./img/"+pieces[counter])   
        counter+=1
    #2 pawns for black
    for i in range(0, 2):
        actual_piece = pyautogui.screenshot(region=(rowPositions[i] - delta/2, filePositions[6] - delta/2, delta, delta))
        actual_piece.save(r"./img/"+pieces[counter])   
        counter+=1
    #this gets all of whites pieces for the first file (1, a-h)
    for i in range(0, 8):
        actual_piece = pyautogui.screenshot(region=(rowPositions[i] - delta/2, filePositions[7] - delta/2, delta, delta))
        actual_piece.save(r"./img/"+pieces[counter])  
        counter+=1
#screenshotsIniciales()
def reemplazarColor(color_inicial, archivoInicial, archivoFinal):
    #ejemplo ('rojito RGBA, blanquito RGBA', white_queen_a.png, white_queen_b.png)
    #no existen todavia, editar imagen (son la foto de su contraparte)
    #"black_king_b.png"
    #"black_queen_a.png"
    #"white_queen_b.png"
    #"white_king_a.png"
    #rojito: b58863 (181, 136, 99)
    #blanquito: f0d9b5 (240, 217, 181)
    img = Image.open(archivoInicial)
    img = img.convert("RGB")
    datas = img.getdata()
    new_image_data = []
    if color_inicial == "a":
        for item in datas:
            # change all white (also shades of whites) pixels to yellow
            if item[0] in list((240, 217, 181)):
                new_image_data.append((181, 136, 99))
            else:
                new_image_data.append(item)
    elif color_inicial == "b":
        for item in datas:
            # change all white (also shades of whites) pixels to yellow
            if item[0] in list((181, 136, 99)):
                new_image_data.append((240, 217, 181))
            else:
                new_image_data.append(item)
    img.putdata(new_image_data)
    img.save(archivoFinal)
#reemplazarColor("b", "img/black_queen_b.png", "img/black_queen_a.png")
#reemplazarColor("a", "img/black_king_a.png", "img/black_king_b.png")
#reemplazarColor("a", "img/white_queen_a.png", "img/white_queen_b.png")
#reemplazarColor("b", "img/white_king_b.png", "img/white_king_a.png")
pieces = ["black_rook_a.png", "black_horsey_b.png",  "black_bishop_a.png",  "black_queen_a.png",  "black_queen_b.png",  "black_king_a.png",  "black_king_b.png",  "black_bishop_b.png",  "black_horsey_a.png", "black_rook_b.png", "black_pawn_b.png",  "black_pawn_a.png",  "empty_space_a.png",  "empty_space_b.png", "white_pawn_a.png",  "white_pawn_b.png",  "white_rook_b.png",  "white_horsey_a.png",  "white_bishop_b.png",  "white_queen_a.png",  "white_queen_b.png",  "white_king_a.png", "white_king_b.png",  "white_bishop_a.png",  "white_horsey_b.png",  "white_rook_a.png"]
def conseguirFEN():
    FEN = str("")
    for y in range(0, 8):
        actual_line = ""
        for x in range(0, 8):
            image_one = pyautogui.screenshot(region=(rowPositions[x] - delta/2, filePositions[y] - delta/2, delta, delta))
            for piece in pieces:
                image_two = Image.open("img/"+piece)
                if list(image_one.getdata()) == list(image_two.getdata()):
                    if(piece == "black_rook_a.png" or piece == "black_rook_b.png"):
                        actual_line+="r"
                    elif(piece == "black_horsey_a.png" or piece == "black_horsey_b.png"):
                        actual_line+="n"
                    elif(piece == "black_bishop_a.png" or piece == "black_bishop_b.png"):
                        actual_line+="b"
                    elif(piece == "black_queen_a.png" or piece == "black_queen_b.png"):
                        actual_line+="q"
                    elif(piece == "black_king_a.png" or piece == "black_king_b.png"):
                        actual_line+="k"
                    elif(piece == "black_pawn_a.png" or piece == "black_pawn_b.png"):
                        actual_line+="p"
                    elif(piece == "white_rook_a.png" or piece == "white_rook_b.png"):
                        actual_line+="R"
                    elif(piece == "white_horsey_a.png" or piece == "white_horsey_b.png"):
                        actual_line+="N"
                    elif(piece == "white_bishop_a.png" or piece == "white_bishop_b.png"):
                        actual_line+="B"
                    elif(piece == "white_queen_a.png" or piece == "white_queen_b.png"):
                        actual_line+="Q"
                    elif(piece == "white_king_a.png" or piece == "white_king_b.png"):
                        actual_line+="K"
                    elif(piece == "white_pawn_a.png" or piece == "white_pawn_b.png"):
                        actual_line+="P"
                    elif(piece == "empty_space_a.png" or piece == "empty_space_b.png"):
                        actual_line+="1"
            if(len(actual_line) == 8):
                arr = list(actual_line)
                arr.append("a")
                actual_empty_spaces = 0
                final_string = ""
                for char in arr:
                    if(char == "1"):
                        actual_empty_spaces+=1
                        if(actual_empty_spaces == 8):
                            final_string+=str(actual_empty_spaces)
                    else:
                        if(actual_empty_spaces > 0):
                            final_string+=str(actual_empty_spaces)
                            final_string+=char
                        else:
                            final_string+=char
                        actual_empty_spaces = 0
                final_string = final_string[:-1]
                #me siento sucio pero funciona
                if(final_string == "88"):
                    final_string = "8"
                FEN+=final_string
        if(y != 7):
            FEN+="/"
    return FEN
def play():
    stockfish.set_fen_position(conseguirFEN()+" w KQkq - 0 1")
    move = stockfish.get_best_move()
    split_move = list(move)
    new_array = []
    for item in split_move:
        if(item.isnumeric() is False):
            new_array.append(letter_to_number_index[item])
        else:
            new_array.append(item)
    filePositions.reverse()
    pyautogui.click(rowPositions[int(new_array[0])], filePositions[int(new_array[1])-1])
    time.sleep(2)
    pyautogui.click(rowPositions[int(new_array[2])], filePositions[int(new_array[3])-1])
    filePositions.reverse()
for i in range (0, 70):
    play()
    pyautogui.moveTo(1, 1)
    time.sleep(5)