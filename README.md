# Chess-piece-movement-tracker
Keeps track of chess piece movement with help of deep learning.

Demo: https://youtu.be/NJkBtBw-Dd0

# Welcome to the Chess-piece-movement-tracker!
The project’s main goal was to detect movement of chess pieces. In order to achieve that I scan through each of the 64 spaces using deep learning model to find out if there is a chess piece in that space and then display the result on graphical interface.
The deep learning model identifies if the space is empty or not.

# Flow Chart
![](https://github.com/phuntshoWangdi/Chess-piece-movement-tracker/blob/master/doc/c1.PNG?raw=true)

* The first step is to take picture of chessboard. After that, crop out only the chessboard. To do that I get four corners of chessboard and base on that corner I crop out the chessboard and perform perspective transformation so that any tilt in the image is corrected.
![](https://github.com/phuntshoWangdi/Chess-piece-movement-tracker/blob/master/doc/before_and_after_transformation.PNG?raw=true)

*After the transformation, it is divided into 64 images of size 75x75 and saved into a folder named ‘img’.
![](https://github.com/phuntshoWangdi/Chess-piece-movement-tracker/blob/master/doc/cropped_chess_pieces.PNG?raw=true)

* Then from python code MATLAB function is called which reads images in ‘img’ folder and feed into the model and the prediction is returned to python variable holding the prediction results. Base on that result small GUI is run displaying all the detected pieces. GUI is implemented using pygame.

# Deep Learing Model Architecture
This model was implemented and trained in MATLAB.
![](https://github.com/phuntshoWangdi/Chess-piece-movement-tracker/blob/master/doc/model_architecture.PNG?raw=true)
