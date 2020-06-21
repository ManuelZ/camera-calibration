import time
import cv2
import numpy as np
from pathlib import Path

# Modified from:
# https://answers.opencv.org/question/98447/camera-calibration-using-charuco-and-python/?answer=98451#post-id-98451

NUM_BOARD_SQUARES_X, NUM_BOARD_SQUARES_Y = 9, 6
SQUARES_LENGTH = 0.025
MARKER_LENGTH = 0.0125
OUT_IMG_SIZE_X, OUT_IMG_SIZE_Y = 200 * NUM_BOARD_SQUARES_X, 200 * NUM_BOARD_SQUARES_Y # px
IMAGES_FOLDER = './images_charuco/focus_middle'

def create_charuco_board(aruco_dict, save=True):
    board = cv2.aruco.CharucoBoard_create(NUM_BOARD_SQUARES_X, 
                                          NUM_BOARD_SQUARES_Y, 
                                          SQUARES_LENGTH, 
                                          MARKER_LENGTH, 
                                          aruco_dict)
    if save:
        img = board.draw((OUT_IMG_SIZE_X, OUT_IMG_SIZE_Y), marginSize=40)
        cv2.imwrite('charuco_board.png', img)
    return board

if __name__ == '__main__':
    # Markers of of size 4x4 with identifiers from 0 to 50
    # https://docs.opencv.org/trunk/d9/d6a/group__aruco.html
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    board = create_charuco_board(aruco_dict)

    allCorners = []
    allIds = []
    images = Path(IMAGES_FOLDER).glob('*.jpg')
    for i, fname in enumerate(images):
        print(f'Working on image {i+1}: {fname}')
        im = cv2.imread(str(fname))
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
        arucoCorners, arucoIds, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict)

        if len(arucoCorners) > 0:
            # Return the 2D position of the chessboard corners from a ChArUco board
            retval, charucoCorners, charucoIds = cv2.aruco.interpolateCornersCharuco(arucoCorners, arucoIds, gray, board)
            if (charucoCorners is not None) and (charucoIds is not None) and (len(charucoCorners) > 3):
                allCorners.append(charucoCorners)
                allIds.append(charucoIds)
            gray = cv2.aruco.drawDetectedMarkers(gray, arucoCorners, arucoIds)
        else:
            print(f'Failed finding Aruco corners in this image.')
        
        # cv2.imshow('', gray)
        # cv2.waitKey(0)
    
    try:
        print(f'\nEstimating camera calibration parameters...')
        retval, cameraMatrix, distCoeffs, rvecs, tvecs = \
            cv2.aruco.calibrateCameraCharuco(allCorners, allIds, board, gray.shape, None, None)
        
        print(f'Camera Matrix:\n {cameraMatrix}')
        print(f'Distortion coeffs:\n {distCoeffs}')
    except:
        print(f'Failed :(')
    
    cv2.destroyAllWindows()