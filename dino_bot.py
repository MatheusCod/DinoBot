import pyautogui as gui
x0 = 175
y0 = 205
sizeX = 100
sizeY = 100
cont = 0
while (True):
    if (gui.locateOnScreen("cactus3.png", grayscale=True, region=(x0, y0, sizeX, sizeY), confidence=0.4)):
        gui.keyDown("space")
        gui.keyUp("space")
        cont += 1
        if (cont == 10):
            cont = 0
            sizeX += 5
