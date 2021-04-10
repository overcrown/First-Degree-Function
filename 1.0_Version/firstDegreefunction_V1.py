class LimitedDisplay(Exception):
    """
    This class provides a correction to the code, is raised when the number 
    of the straight cant demonstrated on display
    """
    def __init__(self):
        pass
    def someError(self, window):
        """
        This function of LimitedDisplay Class warn the user about the error ocurred
        """
        if window == 0:
            pygame.quit()
        import pygame
        pygame.init()
        opendWindow = True
        while opendWindow:
            pygame.time.delay(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    opendWindow = False
            font = pygame.font.SysFont('arial black', 15) 
            text = font.render("SOMETHING IS WRONG, CLOSE THE WINDOW TO FINISHE THE CODE", True, (255,0,0), (0,0,0))
            textPosition = text.get_rect()
            textPosition.center = (400,50) 
            window.blit(text, textPosition)
            pygame.display.update()
        pygame.quit() 
              

class ValuesUnequal(Exception): 
    """
    This class provides a correction to the code, is raised when the size of 
    the X list and Angular Coefficient are different
    """
    def __init__(self):
        self.result = list()
    def __str__(self):
        return 'Error on system'
    def appendElementsToAngular(self, angularCoefficient, amount): 
        """
        This function of ValuesUnequal Class solve the issue about 
        the size of the Angular Coefficient list, adding elements to get 
        Angular Coefficient list size to the same size of X list
        """
        from random import randint
        for element in range(amount):
            randomElement = randint(int(min(angularCoefficient)), int(max(angularCoefficient)))
            angularCoefficient.append(randomElement)
        self.result = angularCoefficient.copy()

    def appendElementsToX(self, listX, amount): 
        """
        This function of ValuesUnequal Class solve the issue about 
        the size of the X list, adding elements to get X list size
        to the same size of Angular Coefficient
        """
        maxElement = listX[len(listX) - 1] # Taking the last element from X list
        for element in range(amount):
            maxElement += 20 # Growing every 20
            listX.append(maxElement)
        self.result = listX.copy()


class FunctionCore():
    """
    This class provides the size of the straight, throught the Expression Variable Y.
    It calculates the function of first degree with the values received by parameter.
    """
    __endResult = float()
    def __init__(self, varX, angularCoefficient,linearCoefficient, window=0):
        # a = angular coefficient, b = linear coefficient, x = expression variable
        # f(t) = ax  + b  (first degree)
        self.varX = varX # Expression variable of the function (x)
        self.angularCoefficient = angularCoefficient # Angular coefficient (a)
        self.linearCoefficient = linearCoefficient  # Linear coefficient (b) 
        self.window = window     


    def calculate(self):
        """
        This method is gonna calculate the function, throught the values passed by constructor method 
        Obs: I subtracted 500 from function cause the Y line start from position 500 
        according pygame metrics.
        """
        try:
            y = 500 # Variable y have the value of limit line y cause y start - 500
            __endResult = y - ((self.angularCoefficient * self.varX) + self.linearCoefficient) # equation of first degree                        
            if not 800 > __endResult > 0: # Condition to ensure the straight can be written on display
                print(self.angularCoefficient)
                print(__endResult)
                raise LimitedDisplay()                        
            return __endResult
        except LimitedDisplay:
            objLimitedDisplay = LimitedDisplay()
            objLimitedDisplay.someError(self.window)
        else:
            pass


def calculatePositionLetter(listY, size_listY, y):
    # This function calculates the straight description position, exactly the height of the straight (y) 
    if size_listY <= 1:
        if listY[0] < 0:
            return y + 10 
        elif listY[0] > 0:
            return y - 10
    elif size_listY > 1:
        if listY[size_listY - 1] > listY[size_listY - 2]:
            return y + 10
        elif listY[size_listY - 1] < listY[size_listY -2]:
            return y - 10


def drawStraight(listX, window, angularCoefficient):
    """
    This function will draw the straight on display and write on display each position respectively
    """
    import pygame
    pygame.init() 
    try:
        # Declaring variables
        font = pygame.font.SysFont('arial black', 8) 
        text = font.render("Position: ", True, (255,255,255), (0,0,0))
        textPosition = text.get_rect()
        textPosition.center = (60,50)    
        initialPositionX = 50
        initialPositionY = 500
        listY = list()
        for c in range(len(listX)):  
            pygame.time.delay(50)           
            finalPositionY = FunctionCore(listX[c], angularCoefficient[c], 50, window) # Instaciando a classe FunctionCore
            pygame.draw.aaline(window, (255, 255, 255), (initialPositionX, initialPositionY), (listX[c], finalPositionY.calculate()))
            initialPositionX = listX[c] 
            initialPositionY = finalPositionY.calculate() 
            listY.append(finalPositionY.calculate())
            # Start the part that we write the position for each straight 
            position = calculatePositionLetter(listY, len(listY), finalPositionY.calculate()) # text variable position
            textPosition.center = (listX[c],position) 
            text = font.render("(%d:%d)"%(listX[c],position), True, (255,255,255), (0,0,0)) 
            window.blit(text, textPosition) # This function will write the variable text on display
            pygame.display.update() # Update the display
    except:
        pass
    finally:
        pass


def main():
    """
    This is the main function, the core of the code, it builds the X and Y axle 
    beyond create all the straights based on Angular Coefficient list and X list
    """
    import pygame
    while True:
        try:
            pygame.init()
            # Describling variables
            listX = [100, 120, 140, 160, 180, 190, 200, 220, 240, 260, 280, 300, 320, 340, 360] # X position can get any value to discovery the Y position, the height
            angularCoefficient = [1, 0.20, 2, -0.20, 0.85, 1.5, 0.10, -0.80, 0.80, 1.3, 0.70, 1.10, 0.50, 1, 0.33]
            X = 800 # This variable represents the X axle
            Y = 800 # This variable represents the Y axle
            # Setting the enviroment
            window = pygame.display.set_mode((X, Y))
            background = pygame.display.set_caption('Graphic')
            openWindow = True
            # Starting the main part of the Code
            while openWindow:
                try:
                    if len(listX) != len(angularCoefficient):
                        raise ValuesUnequal()
                    pygame.time.delay(50) # Delay in milliseconds to do not update too fast
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            openWindow = False  
                    pygame.draw.aaline(window, (255, 255, 255), (50, 500), (750, 500)) # X axle
                    pygame.draw.aaline(window, (255, 255, 255), (50, 500), (50, 100)) # Y axle 
                    drawStraight(listX, window, angularCoefficient)
                    pygame.display.update()             
                except ValuesUnequal:
                    objValuesUnequal = ValuesUnequal()
                    if len(listX) < len(angularCoefficient):          
                        objValuesUnequal.appendElementsToX(listX, len(angularCoefficient) - len(listX))
                        listX = objValuesUnequal.result.copy()
                    elif len(angularCoefficient) < len(listX):
                        objValuesUnequal.appendElementsToAngular(angularCoefficient, len(listX) - len(angularCoefficient))
                        angularCoefficient = objValuesUnequal.result.copy()
                else:
                    pass
            pygame.quit()
        except: 
            print('Ocurred an unexpected error')
            raise Exception
            break
        else:
            break
  



def control():
    from time import sleep
    # This is the function where i control, where i decide if the code gets run
    decision = str(input("Do you want to run this code? [YES/NO] ")).upper()[0]
    if decision == 'Y':
        main()
    else:
        print('Finishing...')
        sleep(3)


# MAIN PART OF CODE
if __name__ == '__main__': 
    # This function just execute this code in this file
    control()
    
