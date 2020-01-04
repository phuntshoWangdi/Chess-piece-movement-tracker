import cv2
import matlab.engine
import numpy as np
import keyboard
import time
from chess_pieces import Chess_Pieces
import path_loader as pl
import pygame
from utils import XOR

pygame.init()
pygame.font.init()

#surface has to be declared earlier
screen=pygame.display.set_mode((700,700))
pygame.display.set_caption("Chess Game Presenter")
myfont = pygame.font.SysFont('Comic Sans MS', 30)
text_surface =  myfont.render('Starting...',False,(255,255,255))
screen.blit(text_surface,(320,340))

x1=[0,75,150,225,300,375,450,525]
x2=[75,150,225,300,375,450,525,600]
y1=[0,75,150,225,300,375,450,525]
y2=[75,150,225,300,375,450,525,600]
#chessboard
#pts = [[549,122],[1070,116],[541,625],[1063,644]]
pts = [[555,121],[1080,108],[552,627],[1079,641]]
org =[(35,35),(111,34),(187,34),(262,34),(339,34),(411,34),(483,34),(566,34),
      (35,111),(111,111),(187,111),(262,111),(339,111),(411,111),(483,111),(566,111),
      (35,187),(111,187),(187,187),(262,187),(339,187),(411,187),(483,187),(566,187),
      (35,262),(111,262),(187,262),(262,262),(339,262),(411,262),(483,262),(566,262),
      (35,339),(111,339),(187,339),(262,339),(339,339),(411,339),(483,339),(566,339),
      (35,411),(111,411),(187,411),(262,411),(339,411),(411,411),(483,411),(566,411),
      (35,483),(111,483),(187,483),(262,483),(339,483),(411,483),(483,483),(566,483),
      (35,566),(111,566),(187,566),(262,566),(339,566),(411,566),(483,566),(566,566)]

cropped_img_path = 'D:/Users/Phuntsho Wangdi/Desktop/D/UT/img/'

def start_matlab_engine():
    print('Starting Matlab engine..')
    eng =  matlab.engine.start_matlab()
    print('Matlab engine started...')
    return eng

def img_cropper(img,cropped_img_path):
    img_c = 0
    #img[y:x]
    for i in range(8):    
        for j in  range(8):
            img_M = img[y1[i]:y2[i],x1[j]:x2[j]]

            cv2.imwrite(cropped_img_path+'img'+str(img_c)+'.png',img_M)
            img_c += 1

def chess_board(p):
    print(' -----------------')
    print('| '+p[0]+' '+p[1]+' '+ p[2]+' '+ p[3]+' '+ p[4]+' '+ p[5]+' '+ p[6]+' '+ p[7]+ ' |')
    print('| '+p[8]+' '+p[9]+' '+ p[10]+' '+ p[11]+' '+ p[12]+' '+ p[13]+' '+ p[14]+' '+ p[15]+ ' |')
    print('| '+p[16]+' '+p[17]+' '+ p[18]+' '+ p[19]+' '+ p[20]+' '+ p[21]+' '+ p[22]+' '+ p[23]+ ' |')
    print('| '+p[24]+' '+p[25]+' '+ p[26]+' '+ p[27]+' '+ p[28]+' '+ p[29]+' '+ p[30]+' '+ p[31]+ ' |')
    print('| '+p[32]+' '+p[33]+' '+ p[34]+' '+ p[35]+' '+ p[36]+' '+ p[37]+' '+ p[38]+' '+ p[39]+ ' |')
    print('| '+p[40]+' '+p[41]+' '+ p[42]+' '+ p[43]+' '+ p[44]+' '+ p[45]+' '+ p[46]+' '+ p[47]+ ' |')
    print('| '+p[48]+' '+p[49]+' '+ p[50]+' '+ p[51]+' '+ p[52]+' '+ p[53]+' '+ p[54]+' '+ p[55]+ ' |')
    print('| '+p[56]+' '+p[57]+' '+ p[58]+' '+ p[59]+' '+ p[60]+' '+ p[61]+' '+ p[62]+' '+ p[63]+ ' |')
    print(' -----------------')

#*********************Pygame Setup**************************#
#64 locaitons on chessboard
lst=[[67, 67], [142, 67], [214, 67], [284, 67], [357, 67], [427, 67], [498, 67], [570, 67],
     [67, 138], [142, 138], [214, 138], [284, 138], [357, 138], [427, 138], [498, 138], [570, 138], 
     [67, 211], [142, 211], [214, 211], [284, 211], [357, 211], [427, 211], [498, 211], [570, 211],
     [67, 282], [142, 282], [214, 282], [284, 282], [357, 282], [427, 282], [498, 282], [570, 282],
     [67, 353], [142, 353], [214, 353], [284, 353], [357, 353], [427, 353], [498, 353], [570, 353], 
     [67, 424], [142, 424], [214, 424], [284, 424], [357, 424], [427, 424], [498, 424], [570, 424], 
     [67, 496], [142, 496], [214, 496], [284, 496], [357, 496], [427, 496], [498, 496], [570, 496], 
     [67, 566], [142, 566], [214, 566], [284, 566], [357, 566], [427, 566], [498, 566], [570, 566]]

#***********************************************************#
eng = start_matlab_engine()

cap=cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)
######################chess piece sprites###################
#black pieces
#king & queen
bking=Chess_Pieces(pl.bK())
bqueen=Chess_Pieces(pl.bQ())
#rook
br1=Chess_Pieces(pl.br1())
br2=Chess_Pieces(pl.br2())
#bishop
bb1=Chess_Pieces(pl.bb1())
bb2=Chess_Pieces(pl.bb2())
#knight
bk1=Chess_Pieces(pl.bk1())
bk2=Chess_Pieces(pl.bk2())
#pawn
bp1=Chess_Pieces(pl.bp1())
bp2=Chess_Pieces(pl.bp2())
bp3=Chess_Pieces(pl.bp3())
bp4=Chess_Pieces(pl.bp4())
bp5=Chess_Pieces(pl.bp5())
bp6=Chess_Pieces(pl.bp6())
bp7=Chess_Pieces(pl.bp7())
bp8=Chess_Pieces(pl.bp8())

#white pieces
#king & queen
wking=Chess_Pieces(pl.wK())
wqueen=Chess_Pieces(pl.wQ())
#rook
wr1=Chess_Pieces(pl.wr1())
wr2=Chess_Pieces(pl.wr2())
#bishop
wb1=Chess_Pieces(pl.wb1())
wb2=Chess_Pieces(pl.wb2())
#knight
wk1=Chess_Pieces(pl.wk1())
wk2=Chess_Pieces(pl.wk2())
#pawn
wp1=Chess_Pieces(pl.wp1())
wp2=Chess_Pieces(pl.wp2())
wp3=Chess_Pieces(pl.wp3())
wp4=Chess_Pieces(pl.wp4())
wp5=Chess_Pieces(pl.wp5())
wp6=Chess_Pieces(pl.wp6())
wp7=Chess_Pieces(pl.wp7())
wp8=Chess_Pieces(pl.wp8())

#A container class to hold and manage
container =[
    br1,bk1,bb1,bqueen,bking,bb2,bk2,br2,
    bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,
    -1,-1,-1,-1,-1,-1,-1,-1,
    -1,-1,-1,-1,-1,-1,-1,-1,
    -1,-1,-1,-1,-1,-1,-1,-1,
    -1,-1,-1,-1,-1,-1,-1,-1,
    wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8,
    wr1,wk1,wb1,wqueen,wking,wb2,wk2,wr2]

#multiple Sprite objects.
all_sprites_list=pygame.sprite.Group()

all_sprites_list.add(bking,bqueen,br1,br2,bb1,bb2,bk1,
    bk2,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,wking,wqueen,wr1,
    wr2,wb1,wb2,wk1,wk2,wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8)

#set background
background=pygame.image.load(pl.cb()).convert()

#get the size of the window
x,y=screen.get_size()

#resize the image to fit the 700x700 size window
background=pygame.transform.scale(background,(x,y))

done=False

#create an object to help track time
clock=pygame.time.Clock()
#***********************************************************#
print('press \'k\' to start')

count = 0
chess_piece_counter = True
pts1=np.float32([pts[0],pts[1],pts[2],pts[3]])
pts2=np.float32([[0,0],[600,0],[0,600],[600,600]])

no_chess_pieces = 0

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    
    if keyboard.is_pressed('k'):
        print('Request accepted...')

        _,frame = cap.read()
        #holds the result of each chess box piece
        out = []
        
        #perspective transformation
        matrix = cv2.getPerspectiveTransform(pts1,pts2)

        c_ful_img = cv2.warpPerspective(frame,matrix,(600,600))
        #c_ful_img = cv2.normalize(c_ful_img,None,0,255,cv2.NORM_MINMAX)
        #crop the full image to 64 pieces of image for prediction
        #store it in the img folder
        img_cropper(c_ful_img,cropped_img_path)

        print('Starting prediction with matlab...')

        #goes through the folders and predicts for each image
        #found in the folder
        results = eng.predicter(cropped_img_path)
        #convert matlab array to numpy array
        print('Converting to numpy array...')
        results = np.asarray(results)
        results = np.squeeze(results)
        print('Done!')

        #filtering results into out
        # for o in results:
        #     if o[1] > o[0]:
        #         out.append(1)
        #     elif o[1] < o[0]:
        #         out.append(0)

        for o in results:
            if o[1] >= 0.7:
                out.append(1)
            elif o[1] < 0.7:
                out.append(0)
        
        #print state of each boxes on chessboard
        chess_board([str(out[i]) for i in range(64)])
        
        #out variable is related to current results
        if count > 0:
            #current locations and results
            cur = out.copy()
            if sum(out[:])==no_chess_pieces:#this condition helps to detect if chess piece is added to the board
                if XOR(cur,prev) == 2:                
                    #if (prev != cur):
                    old_loc_flag = False #it becomes true when old location is found
                    new_loc_flag = False #it becomes true when new lcoation is found

                    for i in range(64):
                        if not old_loc_flag:
                            if (prev[i]==1) and (cur[i]==0):
                                old_loc = i
                                old_loc_flag = True
                    
                        if not new_loc_flag:
                            if(prev[i]==0) and (cur[i]==1):
                                new_loc = i
                                new_loc_flag = True
                
                    container[old_loc],container[new_loc] = container[new_loc],container[old_loc]
                    
                    #plotting all the pieces into right position
                    for i in range(64):
                        if out[i] == 1:
                            container[i].rect.x,container[i].rect.y = lst[i]
                    prev = cur.copy()
                else:
                    print('Too many movement. Only one movement is allowed at a time. Reset the board and try again')
                    print('press \'r\' to reset whole setup.')
            else:
                print('new pieces is detected...or wrong prediction by AI')

        if count == 0:
            no_chess_pieces = sum(out[:])
            for i in range(64):
                if sum(out[16:64])==0:
                    if sum(out[:16]) != 16:
                        chess_piece_counter = False #means all the chess pieces are not there or not detected

                    if i < 16 or i > 47:
                        if out[i] == 1:
                            container[i].rect.x,container[i].rect.y = lst[i]
                    
                    prev = out.copy()
                    count += 1
                    print('Chess piece initialization completed.....')
                else:
                    print('Please reset the chess piece to its initial position and try again.')
                    break
            if chess_piece_counter == False:
                        chess_piece_counter = True
                        print('COULD NOT FIND ALL THE CHESS PIECES ON THE BOARD. PROGRAM WILL CONTINUE ON WITH MISSING PIECES.')
        ##################################################

        all_sprites_list.update()
        #put the chess board image into the window
        screen.blit(background,(0,0))
        
        #update window to see changes
        all_sprites_list.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)#60fps          

        if keyboard.is_pressed('q'):
            break
        print('press \'k\' to start')
    elif keyboard.is_pressed('r'):
                    del prev[:]
                    count = 0
                    container =[
                                br1,bk1,bb1,bqueen,bking,bb2,bk2,br2,
                                bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,
                                -1,-1,-1,-1,-1,-1,-1,-1,
                                -1,-1,-1,-1,-1,-1,-1,-1,
                                -1,-1,-1,-1,-1,-1,-1,-1,
                                -1,-1,-1,-1,-1,-1,-1,-1,
                                wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8,
                                wr1,wk1,wb1,wqueen,wking,wb2,wk2,wr2]
                    print('reset done. Press \'k\' to start')

pygame.quit()
cap.release()
cv2.destroyAllWindows()
