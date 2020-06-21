import cv2
import numpy as np
import os
from pathlib import Path

# Modified from:
# https://www.learnopencv.com/camera-calibration-using-opencv/

# Define the dimensions of checkerboard
CHECKERBOARD = (6,9)
# Where the photo patterns can be found
IMAGES_FOLDER = './images'
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.00001)


def get_calibration_matrix():
    # Vector to store vectors of 3D points for each checkerboard image
    objpoints = []
    # Vector to store vectors of 2D points for each checkerboard image
    imgpoints = [] 

    # Defining the world coordinates for 3D points
    objp = np.zeros((1, CHECKERBOARD[0]*CHECKERBOARD[1], 3), np.float32)
    objp[0,:,:2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
    prev_img_shape = None

    # Extracting path of individual image stored in a given directory
    images = Path(IMAGES_FOLDER).glob('*.jpg')
    for i, fname in enumerate(images):
        print(f'Working on image {i+1}: {fname}')
        img = cv2.imread(str(fname))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Find the chess board corners
        # If desired number of corners are found in the image then ret = true
        ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH+
            cv2.CALIB_CB_FAST_CHECK+cv2.CALIB_CB_NORMALIZE_IMAGE)
        
        """
        If desired number of corner are detected,
        we refine the pixel coordinates and display 
        them on the images of checker board
        """
        if ret == True:
            objpoints.append(objp)
            # refining pixel coordinates for given 2d points.
            corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
            
            imgpoints.append(corners2)

            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners2,ret)
        
        #cv2.imshow('img', img)
        #cv2.waitKey(0)

    cv2.destroyAllWindows()

    h,w = img.shape[:2]

    """
    Performing camera calibration by 
    passing the value of known 3D points (objpoints)
    and corresponding pixel coordinates of the 
    detected corners (imgpoints)
    """
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None, criteria = criteria)
    # stdDeviationsIntrinsics, stdDeviationsExtrinsics, perViewErrors
    print(f"Camera matrix: \n{mtx}")
    print(f"Distortion coeffs: \n {dist}")

    # Estimate error
    mean_error = 0
    for i in range(len(objpoints)):
        imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
        error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2)/len(imgpoints2)
        mean_error += error
    print(f"Estimated total error: {mean_error/len(objpoints):.3f}")
    return mtx

if __name__ == "__main__":
    get_calibration_matrix()