import numpy as np
import cv2

#frame=cv2.imread('blue1.png')

cap = cv2.VideoCapture(0)
num0=0
num1=0
num2=0
num3=0
num4=0
num5=0
k=10                       

while(k):
    k=k-1
    ret, frame = cap.read()
            
    w,h=frame.shape[:2]
    cv2.imshow('frame',frame)
    if cv2.waitKey(2000) & 0xFF == ord('q'):
        break

#BLUE            
            
            # convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # define range of blue colour in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

            # blue colour threshold
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow('Mask',mask)

    for i in range(0,mask.shape[0]):
        for j in range(0,mask.shape[1]):
            if mask[i,j]==255:
                num0=num0+1

            # bitwise and mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
            #cv2.imshow('res',res)
            #img=res.convert('RGB')
            #val=most_frequent_colour(img)
            
           
            #to find hsv value of green, for example, this code is used.
            #To compare colour of landmark and frame, hsv values can be compared


  #GREEN
            # define range of blue colour in HSV
    green = np.uint8([[[0,255,0 ]]])
    hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
            #print(hsv_green)
            

    lower_green = np.array([80,50,50])
    upper_green = np.array([100,255,255])

            # blue colour threshold
    mask2 = cv2.inRange(hsv_green, lower_green, upper_green)
    for i in range(0,mask2.shape[0]):
        for j in range(0,h):
            if mask2[i,j]==255:
                num1=num1+1

            # bitwise and mask and original image
            

   #RED
    red = np.uint8([[[0,0,255 ]]])
    hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)

            
            # define range of blue colour in HSV
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])

            # blue colour threshold
    mask3 = cv2.inRange(hsv_red, lower_red, upper_red)

            # bitwise and mask and original image
    for i in range(0,mask3.shape[0]):
        for j in range(0,h):
            if mask3[i,j]==255:
                num2=num2+1
 #ORANGE
    orange = np.uint8([[[255,127,0]]])
    hsv_orange = cv2.cvtColor(orange,cv2.COLOR_BGR2HSV)

            
            # define range of blue colour in HSV
    lower_orange = np.array([20,50,50])
    upper_orange = np.array([40,255,255])

            # blue colour threshold
    mask4 = cv2.inRange(hsv_orange, lower_orange, upper_orange)

            # bitwise and mask and original image
    for i in range(0,mask4.shape[0]):
        for j in range(0,h):
            if mask4[i,j]==255:
                num3=num3+1

 #YELLOW
    yellow = np.uint8([[[255,255,0 ]]])
    hsv_yellow = cv2.cvtColor(yellow,cv2.COLOR_BGR2HSV)

            
            # define range of blue colour in HSV
    lower_yellow = np.array([50,50,50])
    upper_yellow = np.array([70,255,255])

            # blue colour threshold
    mask5 = cv2.inRange(hsv_yellow, lower_yellow, upper_yellow)

            # bitwise and mask and original image
    for i in range(0,mask5.shape[0]):
        for j in range(0,h):
            if mask5[i,j]==255:
                num4=num4+1

 #VIOLET
    violet = np.uint8([[[148,0,211]]])
    hsv_violet = cv2.cvtColor(violet,cv2.COLOR_BGR2HSV)

            
            # define range of blue colour in HSV
    lower_violet = np.array([270,50,50])
    upper_violet = np.array([300,255,255])

            # blue colour threshold
    mask6 = cv2.inRange(hsv_violet, lower_violet, upper_violet)

            # bitwise and mask and original image
    for i in range(0,mask6.shape[0]):
        for j in range(0,mask6.shape[1]):
            if mask6[i,j]==255:
                num5=num5+1

    if num0>num1 and num0>num2 and num0>num3 and num0>num4 and num0>num5:
        print("blue")

    elif num1>num0 and num1>num2 and num1>num3 and num1>num4 and num1>num5:
        print("green")

    elif num2>num1 and num0<num2 and num2>num3 and num2>num4 and num2>num5:
        print("red")

    elif num3>num0 and num3>num1 and num3>num2 and num3>num4 and num3>num5:
        print("orange")

    elif num4>num0 and num4>num1 and num4>num2 and num4>num3 and num4>num5:
        print("yellow")

    elif num5>num0 and num5>num1 and num5>num2 and num5>num3 and num5>num4:
        print("violet")

    else:
        print("No colour on screen")
                
        
cap.release()
cv2.destroyAllWindows()
