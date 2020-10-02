import pyautogui,time
from PIL import Image,ImageGrab

def press(key):
    pyautogui.keyDown(key)
    return
def prs(key):
    pyautogui.press(key)
    return

def checktime():
    for i in range(200,300):
        for j in range(200,250):
            if data[i,j]>100:
                return "day"
            else:
                return "n8"
            
def isCollidenight(data):
    for i in range(200, 345):
        for j in range(360,455):
            if data[i, j] > 100:
                press("up")
                return

    for i in range(230, 300):
        for j in range(300,350):
            if data[i, j] > 100:
                prs("down")
                return
            
    return

def isCollideday(data):
    for i in range(180, 345):
        for j in range(395,455):
            if data[i, j] < 100:
                press("up")
                return

    for i in range(230, 360):
        for j in range(300,350):
            if data[i, j] < 100:
                prs("down")
                return
            
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(3)
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        if checktime()=="day":
            isCollideday(data)
        else:
            isCollidenight(data)
        '''
        # Draw the rectangle for cactus
        for i in range(180,345):
            for j in range(385,455):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(230, 300):
            for j in range(300,350):
                data[i, j] = 171
        
        image.show()
        break'''
      

