clear all; close all; clc;

% Create a set of calibration images.
images = imageDatastore(fullfile('./'), ...
'IncludeSubfolders',true,'FileExtensions','.jpg','LabelSource','foldernames');

imageFileNames = images.Files;

% Detect calibration pattern.
[imagePoints, boardSize] = detectCheckerboardPoints(imageFileNames);

% Generate world coordinates of the corners of the squares.
squareSize = 25; % millimeters
worldPoints = generateCheckerboardPoints(boardSize, squareSize);

% Calibrate the camera.
I = readimage(images, 1); 
imageSize = [size(I, 1), size(I, 2)];

[cameraParams, ~, estimationErrors] = estimateCameraParameters(imagePoints, worldPoints, ...
                                     'ImageSize', imageSize, 'EstimateSkew', false);

[camMatrix, reprojectionErrors] = cameraMatrix(imagePoints, worldPoints);




% figure; 
% showExtrinsics(cameraParams, 'PatternCentric');

% figure; 
% showReprojectionErrors(cameraParams);

% displayErrors(estimationErrors, cameraParams);