import cv2
cam = cv2.VideoCapture(0)

inp = input('Enter person name')
while(1):
        result,image = cam.read()
        cv2.imshow(inp, image)
        k = cv2.waitKey(1)
        if k == ord('e'):
                break
        if k == ord('q'):
                cv2.imwrite("images/"+inp+".png", image)
                print("image taken")
else:
	print("No image detected. Please! try again")

cam.release()
cv2.destroyAllWindows()	


