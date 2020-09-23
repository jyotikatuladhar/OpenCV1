import cv2

image = cv2.imread('./truth.png', cv2.IMREAD_COLOR)
maxScaleUp = 100
minScaleFactor = 1
scaleFactor = 1
scaleType = 0
maxType = 1
WINDOW_NAME = "IMAGE"
TRACKBAR_NAME = "TRACKBAR"
TRACKBAR_VALUE = "Scale Factor"
TRACKBAR_TYPE = 'Type: \n 0: Scale Up \n 1: Scale Down'


def scaleImage(*args):
    global scaleFactor
    global scaleType

    scaleFactor = args[0]
    # Get the scale factor from the trackbar
    if scaleType == 0:
        scaleFactor = 1 + scaleFactor / 100.0
    else:
        if scaleFactor == 100:
            scaleFactor = 1 - 99.9 / 100.0
        else:
            scaleFactor = 1 - scaleFactor / 100.0

    # Perform check if scaleFactor is zero
    if scaleFactor == 0:
        scaleFactor = minScaleFactor

    # Resize the image
    scaledImage = cv2.resize(image, None, fx=scaleFactor, fy=scaleFactor, interpolation=cv2.INTER_LINEAR)
    cv2.imshow(WINDOW_NAME, scaledImage)


def scaleTypeImage(*args):
    global scaleType
    global scaleFactor
    scaleType = args[0]

    # Perform check if scaleFactor is zero
    if scaleFactor == 0:
        scaleFactor = minScaleFactor
    else:
        scaleFactor = minScaleFactor

    cv2.setTrackbarPos(TRACKBAR_VALUE, TRACKBAR_NAME, minScaleFactor)
    scaledImage = cv2.resize(image, None, fx=scaleFactor, fy=scaleFactor, interpolation=cv2.INTER_LINEAR)
    cv2.imshow(WINDOW_NAME, scaledImage)


if __name__ == '__main__':
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow(TRACKBAR_NAME, cv2.WINDOW_NORMAL)
    cv2.createTrackbar(TRACKBAR_VALUE, TRACKBAR_NAME, scaleFactor, maxScaleUp, scaleImage)
    cv2.createTrackbar(TRACKBAR_TYPE, TRACKBAR_NAME, scaleType, maxType, scaleTypeImage)
    cv2.putText(image, "Note : Use 'TRACKBAR' window to resize", (10, 470), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (255, 255, 0), 1)
    cv2.putText(image, "Press 'q' to exit", (10, 500), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (255, 255, 255), 1)
    cv2.imshow(WINDOW_NAME, image)
    cv2.waitKey(0)

