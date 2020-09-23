from cv2 import *

WINDOW_NAME = "Image"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def take_key_input(image1):
    cv2.putText(image1, "PRESS A KEY", (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (200, 100, 200), 1)
    cv2.imshow(WINDOW_NAME, image1)
    key = cv2.waitKey(0)
    while True:
        keypressedimage = image.copy()
        print(f'keyPressed = {key}')
        if key:
            cv2.putText(keypressedimage, f'Key pressed={key}', (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (200, 255, 200), 2)
            cv2.imshow(WINDOW_NAME, keypressedimage)
            break
        # break
    k = cv2.waitKey(10000) & 0xFF
    cv2.destroyAllWindows()


def draw_rectangle(action, x, y, flags, userdata):
    # Referencing global variables
    global topleftX, topleftY
    dummy = image.copy()
    if action == cv2.EVENT_LBUTTONDOWN:
        topleftX = x
        topleftY = y
    elif action == cv2.EVENT_LBUTTONUP:
        global bottomrightX, bottomrightY
        bottomrightX = x
        bottomrightY = y
        cv2.rectangle(dummy, (topleftX, topleftY), (bottomrightX, bottomrightY), (0, 0, 0), 2)
        cropped_image = dummy[topleftY: bottomrightY, topleftX: bottomrightX]
        cv2.imshow(WINDOW_NAME, dummy)
        cv2.imshow("face.png", cropped_image)
        cv2.imwrite('face.png', cropped_image)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('''Choose top left, and drag, press 'q' to exit''')
    image = cv2.imread('sample.jpg', cv2.IMREAD_COLOR)
    dummy = image.copy()
    # take_key_input(image.copy())
    cv2.namedWindow(WINDOW_NAME)
    cv2.setMouseCallback(WINDOW_NAME, draw_rectangle, None)

    # Show image 'Image mouse':
    while True:
        cv2.putText(image, '''Face Annotation : ''',
                    (10, 470), cv2.FONT_ITALIC,
                    0.7, (255, 255, 255), 2)
        cv2.putText(image, '''Choose top left, and drag, press 'q' to exit''',
                    (10, 500), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (255, 255, 255), 2)
        cv2.imshow(WINDOW_NAME, image)
        # Continue until 'q' is pressed:
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
