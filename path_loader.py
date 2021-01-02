import os
#location of chess piece images
dirPath = os.getcwd()
img_path = os.path.join(dirPath,'chess_pieces\\')
chessboard_path = os.path.join(dirPath,'chessboard\\'

#chess board
def cb():
	return chessboard_path+"cb.jpg"
#King & Queen
def wK():
	return img_path+"w_king.png"
def wQ():
	return img_path+"w_queen.png"
#Rook
def wr1():
	return img_path+"w_rook1.png"
def wr2():
	return img_path+"w_rook2.png"
#Knight
def wk1():
	return img_path+"w_knight1.png"
def wk2():
	return img_path+"w_knight2.png"
#Bishop
def wb1():
	return img_path+"w_bishop1.png"
def wb2():
	return img_path+"w_bishop2.png"
#Pawn
def wp1():
	return img_path+"w_pawn1.png"
def wp2():
	return img_path+"w_pawn2.png"
def wp3():
	return img_path+"w_pawn3.png"
def wp4():
	return img_path+"w_pawn4.png"
def wp5():
	return img_path+"w_pawn5.png"
def wp6():
	return img_path+"w_pawn6.png"
def wp7():
	return img_path+"w_pawn7.png"
def wp8():
	return img_path+"w_pawn8.png"
#black pieces
#King and Queen
def bK():
	return img_path+"b_king.png"
def bQ():
	return img_path+"b_queen.png"
#Rook
def br1():
	return img_path+"b_rook1.png"
def br2():
	return img_path+"b_rook2.png"
#Knight
def bk1():
	return img_path+"b_knight1.png"
def bk2():
	return img_path+"b_knight2.png"
#Bishop
def bb1():
	return img_path+"b_bishop1.png"
def bb2():
	return img_path+"b_bishop2.png"
#Pawn
def bp1():
	return img_path+"b_pawn1.png"
def bp2():
	return img_path+"b_pawn2.png"
def bp3():
	return img_path+"b_pawn3.png"
def bp4():
	return img_path+"b_pawn4.png"
def bp5():
	return img_path+"b_pawn5.png"
def bp6():
	return img_path+"b_pawn6.png"
def bp7():
	return img_path+"b_pawn7.png"
def bp8():
	return img_path+"b_pawn8.png"
