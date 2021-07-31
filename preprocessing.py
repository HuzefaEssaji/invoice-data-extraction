import os
import cv2
import numpy as np
import pytesseract
# from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'H:\Games\tesseract.exe'
def boxes():
    img_2 = cv2.imread('./invoice.png')
    img_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)
    hImg,wImg,_ = img_2.shape
    boxes = pytesseract.image_to_data(img_2)
    row = [[] for i in range(100)]
    x = boxes.splitlines()
    for y,b in enumerate(x):
        b=b.split()
        x[y] = b
    d=0

    for i in range(len(x)):
        
        if x[i][0] == '5':
            if len(x[i])==12:
                row[d].append(x[i][6] +','+ x[i][11])
            else:
                row[d].append(x[i][6] +','+ x[i][10])
            
        else:
            d=d+1
   
    rows=[]
    for i in range(len(row)):
        if len(row[i])!=0:
            rows.append(row[i])
    row=[]
   

    for b in rows:
       for l,s in enumerate(b):
           s=s.split(',')
           b[l] = s
    for b in rows:
       for l,s in enumerate(b):
           print(b[l][0])
            # print(int(s[0])-int(b[l][l+1]))               


    print(rows)
    # for x,b in enumerate(boxes.splitlines()):
    #     j=0
    #     if x!=0:
    #         b = b.split()
            
    #         # if(len(b)==12):
    #         #     x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
    #         #     cv2.rectangle(img_2,(x,y),(w+x,h+y),(0,0,255),1)
    #         print(b)
    #         if b[0]=='5' and len(b)==12:
    #             row[j].append(b[6]+','+b[11])
    #         elif b[0]=='5' and len(b)!=12:
    #             row[j].append(b[6]+','+b[10])
    #         else:
    #             j=j+1
    #             print(j)



    # return row

    # cv2.imshow('boxes_making_result',img_2)
    # cv2.waitKey(0)






def preprocessing(filename):
    
    # Read image using opencv
    img_path = './' + filename
    img = cv2.imread(img_path)
    
    items_to_remove = []


    # img = np.array(img)
    # Convert to gray

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    # img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)    # Apply blur to smooth out the edges
    # img = cv2.GaussianBlur(img, (5, 5), 0)
    # # Apply threshold to get image with only b&w (binarization)
    # img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    thresh = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 4)
    # cv2.imshow('hello',thresh)
    # cv2.waitKey(0)
    # Recognize text with tesseract for python
    image_text = pytesseract.image_to_data(thresh, lang="eng")
    image_text=image_text.split('\n')
    image_text = image_text
    for y,b in enumerate(image_text):
        b=b.split()
        image_text[y] = b
    print(len(image_text))
    
    
    image_text = [n for n in image_text if len(n) == 12]
    list_len = len(image_text)
    print(list_len)
    for i in range(1,list_len):
        if i == list_len-1:
            break
        if (int(image_text[i+1][6])-int(image_text[i][6]))<=40 and (int(image_text[i+1][6])-int(image_text[i][6]))>0:
            image_text[i][11] = image_text[i][11] + ' ' + image_text[i+1][11]
            items_to_remove.append(i+1)
        else:
            print('i am %d',i)
    image_text.pop(items_to_remove[0])
    for i in range(1,len(items_to_remove)):
        image_text.pop(items_to_remove[i]-i)
        print(items_to_remove[i]-1)
    

    for i in range(len(image_text)):
        image_text[i] = image_text[i][11]
    print(image_text)
    return

# print (preprocessing("invoice.png"))
# print(boxes())
print(preprocessing('./invoice.png'))

