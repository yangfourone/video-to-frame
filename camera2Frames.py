# macOS 14.6
# Python 3.6
# openCV 3.4.2

# You should use original terminal to execute it.

import os.path
import time
import cv2

# path about saving images
saveFolder = 'dataset/test'
# fetch frequency
frameRate = 3
# file index
index = 0
# camera source
vc = cv2.VideoCapture(0)


def save_frame(file_index):
    write_name = saveFolder + '/image_' + str(file_index) + '.jpg'
    print('save image_' + str(file_index))
    cv2.imwrite(write_name, frame)


print('start!')

if not os.path.isdir(saveFolder):
    os.mkdir(saveFolder)

while True:
    # delay for capture
    time.sleep(frameRate)

    rval, frame = vc.read()

    index += 1
    save_frame(index)

