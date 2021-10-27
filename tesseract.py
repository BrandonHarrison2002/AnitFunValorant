import numpy as np
from PIL import ImageGrab, Image
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def imageGrab(x, y, offx, offy):
    while(True):
        img = ImageGrab.grab(bbox=(x, y, x + offx, y + offy)).convert('L')
            
        img = np.array(img)
        #cv2.imwrite('bg.png', img)
        
        return img

        # if cv2.waitKey(25) & 0xFF == ord('q'):  
        #     cv2.destroyAllWindows()
        #     break


class tesseract:
    def __init__(self):
        self.currentHealth = 100
        self.ocrErr = False

    def changed(self, x, y, offx, offy):
        self.currentHealth
        txt = pytesseract.image_to_string(imageGrab(x,y,offx,offy))
        if txt == '♀':
            return False
        if txt == '' or txt == '|1oo':
            #print(txt)
            return False
        try:        
            health = abs(int(txt))
            self.ocrErr = False
        except:
            health = self.currentHealth
            if not self.ocrErr:
                #health = self.currentHealth - 1
                self.ocrErr = True
        
        if health >= self.currentHealth:
            return False
        elif health < self.currentHealth and health != 99:
            print(f'{health} == {self.currentHealth}')
            self.currentHealth = health
            return True
        return False


# tess = tesseract()
# while (True):
#     if (tess.changed(760, 1320, 110, 80)):
#         print("dmg")
#     else:
#         print("nodmg")