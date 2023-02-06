import cv2

videoCapture = cv2.VideoCapture('OpenCV/MyInputVid.avi')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

#Uncompressed YUV encoding, compatible but produces large files, file extension must be .avi
videoWriter = cv2.VideoWriter('MyOutputVid.avi', cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)

success, frame = videoCapture.read()

#Loop until there are no more frames
while success:
    videoWriter.write(frame)
    success, read = videoCapture.read()
