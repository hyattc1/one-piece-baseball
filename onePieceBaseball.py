'''
One Piece baseball special features are customizable team name and color,
a strike/ball zone, tracking algorithm for fielder to catch ball, many sprites,
keeping track of the players on base to increase score if one reaches home.
There is a controls tab to learn how to play. There are shortcut keys that can
be used to speed up gameplay and are shown in the key press functions of each
section, like o for 3 outs (gameiover), s for 3 strikes (strikeout), b for 4 balls (walk),
and then some for changing between screens. I loved making this and I hope you enjoy!
'''

from cmu_graphics import *
import random

def onAppStart(app):
    app.width = 1000
    app.height = 665
    app.stepsPerSecond = 50
    
    app.backButton = "cmu://785985/29893694/78-781031_back-button-png-back-cliparts-transparent-png-removebg-preview.png"
    ### music
    app.music = Sound("cmu://785985/29890362/Untitled+video+-+Made+with+Clipchamp+(2).mp3")
    
    ### titleScreen
    app.OPlogo = "cmu://785985/29890382/OP+logo.png"
    app.baseballText = "cmu://785985/29890387/BASEBALL-3-24-2024.png"
    app.redBox = "cmu://785985/29891113/image_2024-03-24_144035182.png"
    app.oceanImages = ["cmu://785985/29890409/ocean1.png",
                       "cmu://785985/29890410/ocean2.png",
                       "cmu://785985/29890411/ocean3.png",
                       "cmu://785985/29890412/ocean4.png",
                       "cmu://785985/29890413/ocean5.png",
                       "cmu://785985/29890414/ocean6.png",
                       "cmu://785985/29890415/ocean7.png",
                       "cmu://785985/29890416/ocean8.png",
                       "cmu://785985/29890417/ocean9.png",
                       "cmu://785985/29890418/ocean10.png",
                       "cmu://785985/29890419/ocean11.png",
                       "cmu://785985/29890420/ocean12.png",
                       "cmu://785985/29890421/ocean13.png",
                       "cmu://785985/29890422/ocean14.png"]
    app.oceanIndex = 0
    app.thousandSunny = "cmu://785985/29890441/thousand_sunny.png"
    app.thousandSunnyX = app.width + 50
    app.bandai = "cmu://785985/29891752/Game_Boy_Advance_-_One_Piece_Going_Baseball_-_Bandai_Logo-removebg-preview.png"
    
    app.startButton = "cmu://785985/29890434/starrrted-removebg-preview.png"
    app.boatStep = 0
    ###setupScreen
    app.deck = "cmu://785985/29891702/wan+piisu.png"
    app.platform = "cmu://785985/29891815/Wooden_Platform-removebg-preview.png"
    app.miniLuffy = "cmu://785985/29891900/mini+luffy-fotor-bg-remover-20240324173924.png"
    app.teamEdit = "cmu://785985/29892075/TEAM-EDIT-3-24-2024.png"
    app.roundedRect = "cmu://785985/29892135/red-7262301_960_720.png"
    app.nameSelected = False
    app.nameBorder = "black"
    app.nameText = "Pirates"
    app.nameInstructions = "Click to type, press enter to confirm"
    app.nameInstructionsFill = "black"
    app.teamColor = rgb(129, 79, 176)
    app.colorMessage = "SKY BLUE"
    app.selectedPlayer = 0
    
    app.luffyTongue = "cmu://785985/29892529/Luffy+Tongue-fotor-bg-remover-20240324201042.png"
    app.robinSmirk = "cmu://785985/29892557/robinSmirk-fotor-bg-remover-20240324201440.png"
    app.arlongGrin = "cmu://785985/29892618/arrrrrrlong-fotor-bg-remover-20240324202225.png"
    app.chopperCute = "cmu://785985/29892652/choppperz-removebg-preview.png"
    
    app.luffyStand = "cmu://785985/29892773/luffyStand-removebg-preview.png"
    app.robinCrouch = "cmu://785985/29892802/Robin_render.png"
    app.arlongStand = "cmu://785985/29892836/Arlong-removebg-preview.png"
    app.chopperStand = "cmu://785985/29892850/chopperStand-removebg-preview.png"
    
    app.baseballRect = "cmu://785985/29892907/texture+rectangle.png"
    app.baseballBorder = "black"
    
    ###instructionsScreen
    app.woodBg = "cmu://785985/29891201/wood+(1).jpg"
    app.howToPlay = "cmu://785985/29891217/HOW-TO-PLAY.png"
    app.woodenPlank = "cmu://785985/29891238/plank-signage-wooden-dark-brown-600nw-1700001625-removebg-preview.png"
    app.playBall = "cmu://785985/29893627/image_2024-03-25_002751173.png"
    app.playBallBorder = "black"
    app.playBallBorder1 = "black"
    
    ###controlsScreen
    app.controlsBackground = "cmu://785985/30577343/goingMerryControls.jpg"
    app.controlsText = "cmu://785985/30577374/controlsOPtexyt.png"
    
    ###playScreen
    app.field = "cmu://785985/29915787/Untitled.jpeg"
    app.helpButton = "cmu://785985/30576914/ballHelpButton.png"
    app.OPbaseballText = "cmu://785985/29894040/NE-PIECE-BASEBALL-3-25-2024+(1).png"
    app.miniField = "cmu://785985/29917755/Untitled.png"
    app.luffy1 = "cmu://785985/29904702/luffy1-removebg-preview.png"
    app.luffy2 = "cmu://785985/29904782/luffy2-removebg-preview.png"
    app.luffy3 = "cmu://785985/29904795/luffy3-removebg-preview.png"
    app.luffy4 = "cmu://785985/29904813/luffy4-removebg-preview.png"
    app.luffy5 = "cmu://785985/29904835/luffy5-removebg-preview.png"
    app.luffy6 = "cmu://785985/29904849/luffy6-removebg-preview.png"
    app.luffy7 = "cmu://785985/29904863/luffy7-removebg-preview.png"
    app.luffy8 = "cmu://785985/29904876/luffy8-removebg-preview.png"
    app.luffy9 = "cmu://785985/29905526/luffy9-removebg-preview.png"
    app.luffyIndex = 0
    app.luffySwinging = False
    app.luffyX = 325
    app.luffyBatHit = "cmu://785985/29945243/luffyBatHit-removebg-preview.png"
    app.playerScore = 4
    app.luffySO = "cmu://785985/30594673/luffySO-removebg-preview.png"
    app.luffyGO = "cmu://785985/30595882/luffyGO-removebg-preview.png"
    
    app.zoro1 = "cmu://785985/29917362/zoro1_inPixio.png"
    app.zoro2 = "cmu://785985/29917418/zoro2_inPixio.png"
    app.zoro3 = "cmu://785985/29917437/zoro3_inPixio.png"
    app.zoro4 = "cmu://785985/29917423/zoro4_inPixio.png"
    app.zoro5 = "cmu://785985/29917441/zoro5_inPixio.png"
    app.zoro6 = "cmu://785985/29917441/zoro5_inPixio.png"
    app.zoro7 = "cmu://785985/29917457/zoro7_inPixio.png"
    app.zoro8 = "cmu://785985/29917461/zoro9_inPixio.png"
    app.zoro9 = "cmu://785985/29917461/zoro9_inPixio.png"
    app.zoro10 = "cmu://785985/29917474/zoro10_inPixio.png"
    app.zoro11= "cmu://785985/29917480/zoro11_inPixio.png"
    app.zoroPitching = False
    app.zoroIndex = 0
    app.zoroFace = "cmu://785985/29969595/zoro_facep-removebg-preview.png"
    
    app.playerSwingTimer = 0
    app.pitcherTimer = 0
    app.pitches = 0
    
    app.playerNames = ["Luffy", "Robin", "Arlong", "Chopper"]
    app.currentPlayerIndex = 0
    
    app.baseball = "cmu://785985/29919003/baseball-drawing-sport-pixel-art-260nw-2323843349_inPixio.png"
    app.baseballShadow = "cmu://785985/29919020/kindpng_3155538.png"
    app.baseballX = 506
    app.baseballY = 274
    app.dx = 0
    app.dy = 0
    app.ballRotation = 0
    app.finalBallAngle = 0
    app.currentlyPitching = False
    
    app.strikes = 0
    app.balls = 0
    app.outs = 0
    app.swung = False
    app.ballAcrossPlateX = 0
    app.yWhenSwung = 0
    app.isStrike = True
    app.ballIsHit = False
    
    app.strikeoutText = "cmu://785985/30293124/STRIKE-OUT-4-14-2024.png"
    app.walkText = "cmu://785985/30293126/W4LK-4-14-2024.png"
    app.gameOverText = "cmu://785985/30293147/GAME-OVER-4-14-2024.png"
    app.gameOver = False
    
    app.baseRunners = [False, False, False]
    ###outfieldScreen
    #setActiveScreen("outfieldScreen")
    app.outfield = "cmu://785985/29945750/outfield+pixel.jpeg"
    app.miniBaseballX = 496
    app.miniBaseballY = 524
    app.zoroCx = 500
    app.zoroCy = 420
    app.standing = "cmu://785985/30199566/standing-removebg-preview.png"
    app.caught = "cmu://785985/30199568/caught-removebg-preview.png"
    app.zoroCaught = False
    app.outText = "cmu://785985/30291577/UT-4-14-2024.png"
    app.hitText = "cmu://785985/30291585/HiTOPBB.png"
    app.homerun = False
    app.homerunText = "cmu://785985/30292503/HOMERUN-4-14-2024.png"
    app.luffyRunner = "cmu://785985/30577583/luffyRunner-removebg-preview.png"
    
    ### victory and defeat screen
    app.endWallpaper = "cmu://785985/30597771/pirateBeach.png"
    app.victoryText = "cmu://785985/30597716/victoryText.png"
    app.defeatText = "cmu://785985/30597701/defeatText.png"
    
    app.lp1 = "cmu://785985/30599922/lp1.png"
    app.lp2 = "cmu://785985/30599924/lp2.png"
    app.lp3 = "cmu://785985/30599926/lp3.png"
    app.lp4 = "cmu://785985/30599927/lp4.png"
    app.lp5 = "cmu://785985/30599928/lp5.png"
    app.lp6 = "cmu://785985/30599931/lp6.png"
    app.lp7 = "cmu://785985/30599932/lp7.png"
    app.lp8 = "cmu://785985/30599933/lp8.png"
    app.lp9 = "cmu://785985/30599936/lp9.png"
    app.lp10 = "cmu://785985/30599937/lp10.png"
    app.lp11 = "cmu://785985/30599939/lp11.png"
    app.lpIndex = 0
    
    setActiveScreen("titleScreen")

############ helper functions start
def drawImageHelper(image, x, y, resizeFactor):
    imageWidth, imageHeight = getImageSize(image)
    drawImage(image, x, y, width = imageWidth * resizeFactor, height = imageHeight * resizeFactor, align = "center")

def pressIn(left,top,width,height, x, y):
    x0 = left
    y0 = top
    x1 = left + width
    y1 = top + height
    return (x0 <= x and x1 >= x and y0 <= y and y1 >= y)

def distance(x0,y0,x1,y1):
    return ((x0 - x1)**2 + (y0 - y1)**2)**0.5
    
############ helper functions end

class Baseball:
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy

def newGame(app):
    app.oceanIndex = 0
    app.thousandSunnyX = app.width + 50
    app.boatStep = 0
    
    app.nameSelected = False
    app.nameBorder = "black"
    app.nameText = "Pirates"
    app.nameInstructions = "Click to type, press enter to confirm"
    app.nameInstructionsFill = "black"
    app.teamColor = rgb(129, 79, 176)
    app.colorMessage = "SKY BLUE"
    app.selectedPlayer = 0
    app.baseballBorder = "black"
    app.playBallBorder = "black"
    
    app.luffyIndex = 0
    app.luffySwinging = False
    app.luffyX = 325
    app.playerScore = 4
    
    app.zoroPitching = False
    app.zoroIndex = 0
    app.playerSwingTimer = 0
    app.pitcherTimer = 0
    app.pitches = 0
    app.playerNames = ["Luffy", "Robin", "Arlong", "Chopper"]
    app.currentPlayerIndex = 0
    app.baseballX = 506
    app.baseballY = 274
    app.dx = 0
    app.dy = 0
    app.ballRotation = 0
    app.finalBallAngle = 0
    app.currentlyPitching = False
    app.strikes = 0
    app.balls = 0
    app.outs = 0
    app.swung = False
    app.ballAcrossPlateX = 0
    app.yWhenSwung = 0
    app.isStrike = True
    app.ballIsHit = False
    app.gameOver = False
    app.baseRunners = [False, False, False]
    
    app.miniBaseballX = 496
    app.miniBaseballY = 524
    app.zoroCx = 500
    app.zoroCy = 420
    app.zoroCaught = False
    app.homerun = False
    
    setActiveScreen("titleScreen")

####################################################
# Title Screen
####################################################

def titleScreen_redrawAll(app):
    drawImageHelper(app.oceanImages[app.oceanIndex], app.width / 2, app.height / 2, 2.38)
    drawImageHelper(app.OPlogo, app.width/2 - 10, 110, 0.14)
    drawImageHelper(app.thousandSunny, app.thousandSunnyX, 330, 0.3)
    drawImageHelper(app.baseballText, app.width/2 + 13, 250, 0.6)
    drawImageHelper(app.redBox, 814, 198, 0.2)
    drawLabel("112", 807, 196, size = 35, fill = "white", border = "black", borderWidth = 1, bold = True)
    drawImageHelper(app.startButton, app.width/2 + 5, 505, 0.4)
    drawLabel("Press space or click", app.width/2 + 5, 590, size = 20, fill = "white", bold = True)
    drawLabel("Connor Hyatt ®", 915, 640, size = 20, fill = "white", bold = True)
    drawImageHelper(app.bandai, 60, 620, 1)
    drawLabel("Inspired by", 60, 570, size = 20, fill = "white", bold = True)
    
def titleScreen_onStep(app):
    app.boatStep+= 1
    app.music.play(loop = True)
    if app.boatStep % 5 == 0:
        app.oceanIndex = (app.oceanIndex + 1) % 14
    if app.thousandSunnyX < -100:
            app.thousandSunnyX = app.width + 100
    else:
        app.thousandSunnyX -= 1

def titleScreen_onMousePress(app,mouseX,mouseY):
    startImageWidth, startImageHeight = getImageSize(app.startButton)
    startImageWidth = startImageWidth * 0.4
    startImageHeight = startImageHeight * 0.4
    if pressIn(app.width / 2 - startImageWidth/2 + 9, 505 - startImageHeight/ 2 + 10, startImageWidth - 10, startImageHeight - 10, mouseX, mouseY):
        setActiveScreen('setupScreen')

def titleScreen_onKeyPress(app, key):
    if key == "t":
        setActiveScreen('titleScreen')
    elif key == "p":
        setActiveScreen('playScreen')
    elif key == "o":
        app.outs = 3
    elif key == "s":
        app.strikes = 3
    elif key == "b":
        app.balls = 4
    elif key == "l":
        app.baseRunners = [True, True, True]
    elif key == "space":
        setActiveScreen("setupScreen")


####################################################
# setupScreen
####################################################

def setupScreen_redrawAll(app):
    drawImageHelper(app.deck, app.width / 2, app. height / 2, 4.17)
    drawImageHelper(app.platform, 825, 580, 0.8)
    plankWidth, plankHeight = getImageSize(app.woodenPlank)
    drawImage(app.woodenPlank, app.width / 2, 83, width = plankWidth * 1.2, height = plankHeight * 1.1, align = "center")
    drawCircle(267, 36, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(733, 36, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(267, 130, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(733, 130, 5, fill = "grey", border = "black", borderWidth = 1)
    drawImageHelper(app.teamEdit, app.width / 2, 83, 0.6)
    drawImageHelper(app.backButton, 923, 70, 0.25)
    rectWidth, rectHeight = getImageSize(app.roundedRect)
    drawImage(app.roundedRect, 200, 237, width = rectWidth * 0.25, height = rectHeight * 0.15, align = "center")
    drawLabel("Team Name:", 200, 237,fill = "white", size = 26, bold = True)
    drawRect(200, 330, 227, 30, fill = "white", border = "black", borderWidth = 3, align = "center")
    drawLabel(f'{app.nameInstructions}', 200, 332, size = 13, fill = app.nameInstructionsFill)
    drawRect(200, 297, 270, 50, fill = "white", border = app.nameBorder, borderWidth = 3, align = "center")
    drawLabel(f'{app.nameText}', 200, 297, size = 28, font='grenze')
    rectWidth, rectHeight = getImageSize(app.roundedRect)
    drawImage(app.roundedRect, 200, 388, width = rectWidth * 0.25, height = rectHeight * 0.15, align = "center")
    drawLabel("Team Color:", 200, 388,fill = "white", size = 26, bold = True)
    squareSize = 80
    colorList = ["gold", "red", rgb(129, 79, 176), rgb(75, 156, 251)]
    for i in range(4):
        drawRect(82 + i * squareSize, 466, squareSize, squareSize, fill= "white", border = "black", borderWidth = 5, align = "center")
        drawRect(82 + i * squareSize, 466, 75, 75, fill = colorList[i], align = "center")
    drawRect(82 - 40, 466 - 40, 320, 80, fill = None, border = "black", borderWidth = 5)
    drawRect(200, 536, 145, 45, fill = "white", border = "black", borderWidth = 3, align = "center")
    drawLabel(f'{app.colorMessage}', 200, 536, size = 25, fill = app.teamColor, bold = True)
    
    #line-up characters
    rectWidth, rectHeight = getImageSize(app.roundedRect)
    drawImage(app.roundedRect, 530, 237, width = rectWidth * 0.25, height = rectHeight * 0.15, align = "center")
    drawLabel("Select Player", 530, 237, fill = "white", size = 26, bold = True)
    characterIcons = [app.luffyTongue, app.robinSmirk, app.arlongGrin, app.chopperCute ]
    characterNames = ["Luffy", "Robin", "Arlong", "Chopper"]
    for i in range(4):
        drawRect(595, 320 + i * 95, 25, 25, fill = "white", align = "center", border = "black")
        drawLabel(f'{i + 1}', 595, 320 + i * 95, size = 16)
        if i == app.selectedPlayer:
            drawRect(530, 320 + i * 95, 80, 80, fill = rgb(218, 145, 0), align = "center")
            drawRect(530, 320 + i * 95, 75, 75, fill = rgb(252, 194, 0), align = "center")
            drawRect(530, 320 + i * 95, 68, 68, fill = rgb(218, 145, 0), align = "center")
            drawRect(530, 320 + i * 95, 63, 63, fill = app.teamColor, align = "center")
            drawImage(characterIcons[i], 530, 320 + i * 95, width = 63, height = 63, align = "center")
        else:
            drawRect(530, 320 + i * 95, 80, 80, align = "center")
            drawRect(530, 320 + i * 95, 80, 80, fill = rgb(218, 145, 0), align = "center", opacity = 40)
            drawRect(530, 320 + i * 95, 75, 75, fill = rgb(252, 194, 0), align = "center", opacity = 40)
            drawRect(530, 320 + i * 95, 68, 68, fill = rgb(218, 145, 0), align = "center", opacity = 40)
            drawRect(530, 320 + i * 95, 63, 63, fill = app.teamColor, align = "center", opacity = 40)
            drawImage(characterIcons[i], 530, 320 + i * 95, width = 63, height = 63, align = "center", opacity = 40)
    
    #platform character
    if app.selectedPlayer == 0:
        drawImageHelper(app.luffyStand, 821, 379, 0.64)
    elif app.selectedPlayer == 1:
        drawImageHelper(app.robinCrouch, 821, 382, 0.21)
    elif app.selectedPlayer == 2:
        drawImageHelper(app.arlongStand, 821, 370, 0.59)
    elif app.selectedPlayer == 3:
        drawImageHelper(app.chopperStand, 821, 435, 0.58)
    drawLabel(f'Batter {app.selectedPlayer + 1}: {characterNames[app.selectedPlayer]}', 823, 639, fill = "white", bold = True, size = 30, border = "black", borderWidth = 1)
    
    #start game
    #if app.mouseOverStart:
    drawRect(200, 615, 194, 94, fill = None, border = app.baseballBorder, borderWidth = 6, align = "center" )
    baseballRectW, baseballRectH = getImageSize(app.baseballRect)
    drawImage(app.baseballRect, 200, 615, width = baseballRectW * 0.07, height = baseballRectH *0.12, rotateAngle = -90, align = "center")
    drawLabel("Start Game", 200, 615, fill = app.baseballBorder,size = 25, bold = True)

def setupScreen_onMouseMove(app,mouseX, mouseY):
    if pressIn(200 - 184 / 2, 615 - 83 / 2, 184, 83, mouseX, mouseY):
        app.baseballBorder = rgb(255, 192, 0)
    else:
        app.baseballBorder = "black"
    
def setupScreen_onKeyPress(app, key):
    if app.nameSelected:
        if key == "enter":
            app.nameSelected = not app.nameSelected
            app.nameBorder = "black"
            app.nameInstructions = "Click to type, press enter to confirm"
            app.nameInstructionsFill = "black"
        elif key == "backspace" or key == "delete":
            app.nameText = app.nameText[:len(app.nameText) - 1]
            app.nameInstructions = "Click to type, press enter to confirm"
            app.nameInstructionsFill = "black"
        elif len(app.nameText) < 14:
            if key.lower() in "abcdefghijklmnopqrstuvwxyz" or key == "space":
                if key == "space":
                    app.nameText += " "
                    app.nameInstructions = "Click to type, press enter to confirm"
                    app.nameInstructionsFill = "black"
                else:
                    app.nameText += key
                    app.nameInstructions = "Click to type, press enter to confirm"
                    app.nameInstructionsFill = "black"
            else:
                app.nameInstructions = "must enter valid character"
                app.nameInstructionsFill = "red"
        else:
            app.nameInstructions = "Name length must be < 14"
            app.nameInstructionsFill = "red"
    elif key == "1":
        app.selectedPlayer = 0
    elif key == "2":
        app.selectedPlayer = 1
    elif key == "3":
        app.selectedPlayer = 2
    elif key == "4":
        app.selectedPlayer = 3
    #no shortcuts due to typing name on keyboard
    
def setupScreen_onMousePress(app, mouseX, mouseY):
    if pressIn(200 - 270 / 2, 297 - 50 / 2, 270, 50, mouseX, mouseY):
        app.nameSelected = not app.nameSelected
        if app.nameSelected:
            app.nameBorder = rgb(255, 192, 0)
        else:
            app.nameBorder = "black"
    elif pressIn(200 - 184 / 2, 615 - 83 / 2, 184, 83, mouseX, mouseY):
        setActiveScreen('instructionsScreen')
    #color in yellow box
    elif pressIn(45, 429, 75, 75, mouseX, mouseY):
        app.teamColor = "gold"
        app.colorMessage = "GOLD"
    #color in red box
    elif pressIn(125, 429, 75, 75, mouseX, mouseY):
        app.teamColor = "red"
        app.colorMessage = "RED"
    #color in purple box
    elif pressIn(205, 429, 75, 75, mouseX, mouseY):
        app.teamColor = rgb(129, 79, 176)
        app.colorMessage = "PURPLE"
    #color in sky blue box
    elif pressIn(285, 429, 75, 75, mouseX, mouseY):
        app.teamColor = rgb(75, 156, 251)
        app.colorMessage = "SKYBLUE"
    
    #character select Luffy
    elif pressIn(530 - 31, 320 - 36, 63, 63, mouseX, mouseY):
        app.selectedPlayer = 0
    #character select Robin
    elif pressIn(530 - 31, 320 + 95 - 36, 63, 63, mouseX, mouseY):
        app.selectedPlayer = 1
    #character select Arlong
    elif pressIn(530 - 31, (320 + 2 * 95) - 36, 63, 63, mouseX, mouseY):
        app.selectedPlayer = 2
    #character select Chopper
    elif pressIn(530 - 31, (320 + 3 * 95) - 36, 63, 63, mouseX, mouseY):
        app.selectedPlayer = 3
    elif pressIn(923 - 47, 70 - 55, 90, 95, mouseX, mouseY):
        setActiveScreen("titleScreen")

####################################################
# instructionsScreen
####################################################

def instructionsScreen_redrawAll(app):
    drawImageHelper(app.woodBg, app.width / 2, app.height / 2,1)
    plankWidth, plankHeight = getImageSize(app.woodenPlank)
    drawImage(app.woodenPlank, app.width / 2, 83, width = plankWidth * 1.5, height = plankHeight * 1.1, align = "center")
    drawCircle(207, 36, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(793, 36, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(207, 124, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(793, 124, 5, fill = "grey", border = "black", borderWidth = 1)
    drawImageHelper(app.howToPlay, app.width / 2, 80, 0.7)
    drawImageHelper(app.backButton, 923, 70, 0.25)
    
    #description
    drawRect(500, 275, 780, 215, fill = "darkGoldenrod", border = "black", align = "center")
    drawCircle(128, 183, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(872, 183, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(128, 368, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(872, 368, 5, fill = "grey", border = "black", borderWidth = 1)
    drawLabel("IT'S THE BOTTOM OF THE 9TH!", app.width / 2, 200, size = 40, fill = "white", border ="black", font='montserrat', borderWidth = 1, bold = True)
    drawLabel(f'The {app.nameText} are 3 runs down.', app.width / 2, 250, size = 40, fill = "white", border ="black", font='montserrat', borderWidth = 1, bold = True)
    drawLabel("Can you comeback and win", app.width / 2, 300, size = 40, fill = "white", border ="black", font='montserrat', borderWidth = 1, bold = True)
    drawLabel("with only 3 outs left?", app.width / 2, 350, size = 40, fill = "white", border ="black", font='montserrat', borderWidth = 1, bold = True)
    
    bW, bH = getImageSize(app.playBall)
    drawRect(739, 527, 280, 140, fill = "white", border = app.playBallBorder, borderWidth = 5, align = "center")
    drawImageHelper(app.playBall, 742, 534, 0.5)
    
    drawLabel("Controls", 283, 430, fill = "white", size = 40, bold = True, border = "black", borderWidth = 1)
    drawRect(283, 527, 280, 140, fill = "darkGoldenRod", border = app.playBallBorder1, borderWidth = 5, align = "center")
    drawLabel("Click Here", 283, 527, fill = "white", size = 40, bold = True, border = "black", borderWidth = 1)

def instructionsScreen_onMouseMove(app,mouseX, mouseY):
    if pressIn(739 - 280 / 2, 527 - 140 / 2, 280, 140, mouseX, mouseY):
        app.playBallBorder = rgb(255, 192, 0)
    else:
        app.playBallBorder = "black"
    if pressIn(283 - 280 / 2, 527 - 140 / 2, 280, 140, mouseX, mouseY):
        app.playBallBorder1 = rgb(255, 192, 0)
    else:
        app.playBallBorder1 = "black"
    

def instructionsScreen_onMousePress(app, mouseX, mouseY):
    if pressIn(923 - 47, 70 - 55, 90, 95, mouseX, mouseY):
        setActiveScreen("setupScreen")
    elif pressIn(599, 497, 219, 87, mouseX, mouseY):
        setActiveScreen("playScreen")
    elif pressIn(143, 457, 280, 140, mouseX, mouseY):
        setActiveScreen("controlsScreen")

def instructionsScreen_onKeyPress(app,key):
    if key == "t":
        setActiveScreen('titleScreen')
    elif key == "p":
        setActiveScreen('playScreen')
    elif key == "o":
        app.outs = 3
    elif key == "s":
        app.strikes = 3
    elif key == "b":
        app.balls = 4
    elif key == "l":
        app.baseRunners = [True, True, True]


####################################################
# controlsScreen
####################################################

def controlsScreen_redrawAll(app):
    drawImageHelper(app.controlsBackground, app.width / 2, app.height / 2, 0.98)
    plankWidth, plankHeight = getImageSize(app.woodenPlank)
    drawImage(app.woodenPlank, app.width / 2, 83, width = plankWidth * 1.5, height = plankHeight * 1.1, align = "center")
    drawCircle(207, 36, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(793, 36, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(207, 124, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(793, 124, 5, fill = "grey", border = "black", borderWidth = 1)
    drawImageHelper(app.controlsText, app.width / 2, 87, 0.5)
    drawImageHelper(app.backButton, 923, 70, 0.25)
    drawLabel("How to play screen", 923, 140, fill = "white", size = 14, bold = True)
    
    #controls text directions
    drawRect(35, 170, 570, 370, fill = "midnightBlue", border = "black", opacity = 70)
    drawCircle(55, 193, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(580, 193, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(55, 517, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(580, 517, 5, fill = "grey", border = "black", borderWidth = 1)
    drawLabel("Press space to pitch", 320, 200, size = 40, fill = "white", border ="black", font='montserrat', borderWidth = 1, bold = True)
    drawLabel(f'Click when the ball is', 320, 250, size = 40, fill = "white", border ="black", font='montserrat', borderWidth = 1, bold = True)
    drawLabel("approaching to swing",320, 300, size = 40, fill = "white", border ="black", font='montserrat', borderWidth = 1, bold = True)
    drawLabel("Press enter to play the", 320, 350, size = 40, fill = "white", border ="black", font='montserrat', borderWidth = 1, bold = True)
    drawLabel("next batter on SO/walk", 320, 400, size = 40, fill = "white", border ="black", font='montserrat', borderWidth = 1, bold = True)
    drawLabel("Use left and right arrow", 320, 450, size = 40, fill = "white", border ="black", font='montserrat', borderWidth = 1, bold = True)
    drawLabel("keys to move batter", 320, 500, size = 40, fill = "white", border ="black", font='montserrat', borderWidth = 1, bold = True)
    
    #play ball button
    bW, bH = getImageSize(app.playBall)
    drawRect(785, 565, 280, 140, fill = "white", border = app.playBallBorder, borderWidth = 5, align = "center")
    drawImageHelper(app.playBall, 788, 572, 0.5)

def controlsScreen_onMousePress(app,mouseX,mouseY):
    if pressIn(923 - 47, 70 - 55, 90, 95, mouseX, mouseY):
        setActiveScreen("instructionsScreen")
    elif pressIn(785 - 280 / 2, 565 - 140 / 2, 280, 140, mouseX, mouseY):
        setActiveScreen("playScreen")

def controlsScreen_onMouseMove(app,mouseX,mouseY):
    if pressIn(785 - 280 / 2, 565 - 140 / 2, 280, 140, mouseX, mouseY):
        app.playBallBorder = rgb(255, 192, 0)
    else:
        app.playBallBorder = "black"

def controlsScreen_onKeyPress(app,key):
    if key == "t":
        setActiveScreen('titleScreen')
    elif key == "p":
        setActiveScreen('playScreen')
    elif key == "o":
        app.outs = 3
    elif key == "s":
        app.strikes = 3
    elif key == "b":
        app.balls = 4
    elif key == "l":
        app.baseRunners = [True, True, True]



####################################################
# playScreen
####################################################

def playScreen_redrawAll(app):
    infieldBall = Baseball(app.baseballX, app.baseballY)
    drawImageHelper(app.field, app.width / 2, 240, 1.4)
    drawImageHelper(app.OPbaseballText, app.width / 2, 31, 0.4)
    
    
    drawImageHelper(app.miniField, 900, 100, 0.1)
    
    #score board
    drawRect(151,76, 275, 125, fill = gradient(app.teamColor, "lightSeaGreen", start = "left"), border = "black", borderWidth = 3, align = "center")
    if len(app.nameText) < 8:
        drawRect(151 - 72, 38, 90, 26, fill = "white", border = "black", align = "center")
        drawRect(151 + 72, 38, 90, 26, fill = "white", border = "black", align = "center")
    else:
        drawRect(151 - 72, 38, 120, 26, fill = "white", border = "black", align = "center")
        drawRect(151 + 72, 38, 120, 26, fill = "white", border = "black", align = "center")
    drawRect(151 - 72, 87, 50, 60, fill = "white", border = "black", align = "center")
    drawRect(151 + 72, 87, 50, 60, fill = "white", border = "black", align = "center")
    drawLabel(f'{app.playerScore}', 151 - 72, 87, size = 55, bold = True, font='orbitron') #team score
    drawLabel("7", 151 + 72, 87, size = 55, bold = True,font='orbitron') #Marines score
    drawLabel(f'{app.nameText}', 151 - 72, 38, size = 15, fill = app.teamColor, bold = True,font = 'cinzel')
    drawLabel("Marines", 151 + 72, 38, size = 15, fill = "lightSeaGreen", bold = True, font = 'cinzel')
    drawRect(151, 68, 63, 20, fill = "white", border = "black", align = "center")
    drawRect(151, 100, 35, 34, fill = "white", border = "black", align = "center")
    drawLabel("Pitches", 151, 68, size = 10, font = "cinzel", bold = True)
    drawLabel(f'{app.pitches}', 151, 100, size = 25, font = "orbitron", bold = True)
    
    colorList = ["gold", "red", rgb(129, 79, 176), rgb(75, 156, 251)]
    
    #draw team batter icon
    drawRect(7, 379, 210, 224)
    drawRect(9, 381, 206, 220, fill = rgb(218, 145, 0))
    drawRect(14, 386, 196, 210, fill = rgb(252, 194, 0))
    drawRect(19, 391, 186, 200, fill = rgb(218, 145, 0))
    drawRect(24, 396, 176, 190, fill = app.teamColor)
    luffyTongueW, luffyTongueH = getImageSize(app.luffyTongue)
    drawImage(app.luffyTongue, 114, 489, width = luffyTongueW * 0.355, height = luffyTongueH * 0.385, align = "center")#0.355 prev height 0.425
    drawRect(114, 637, 140, 35, fill = "white", border = "black", align = "center")
    drawLabel(app.playerNames[app.currentPlayerIndex], 114, 637, fill = app.teamColor, size = 21, bold = True, font='cinzel')
    #draw Enemy team player
    drawRect(783, 379, 210, 224)
    drawRect(785, 381, 206, 220, fill = rgb(218, 145, 0))
    drawRect(790, 386, 196, 210, fill = rgb(252, 194, 0))
    drawRect(795, 391, 186, 200, fill = rgb(218, 145, 0))
    drawRect(800, 396, 176, 190, fill = "lightSeaGreen")
    zoroPicW, zoroPicH = getImageSize(app.zoroFace)
    drawImage(app.zoroFace, 888, 491.5, width = zoroPicW * 3.13, height = zoroPicH * 3.4, align = "center")
    drawRect(890, 637, 140, 35, fill = "white", border = "black", align = "center")
    drawLabel("Zoro", 890, 637, fill = "lightSeaGreen", bold = True, size = 21, font='cinzel')
    
    #draw Zoro pitcher
    zoroList = [app.zoro1, app.zoro2, app.zoro3, app.zoro4, app.zoro5, app.zoro6, app.zoro7, app.zoro8, app.zoro9, app.zoro10, app.zoro11]
    zoroW, zoroH = getImageSize(zoroList[app.zoroIndex])
    drawImage(zoroList[app.zoroIndex], 450, 220, width = zoroW * 5, height = zoroH * 5, align = "left")
    
    #baseball
    if app.currentlyPitching:
        baseballWidth, baseballHeight = getImageSize(app.baseball)
        drawImage(app.baseball, infieldBall.cx, infieldBall.cy, width = baseballWidth * 0.2, height = baseballHeight * 0.2, align = "center", rotateAngle = app.finalBallAngle)
        drawImageHelper(app.baseballShadow, infieldBall.cx, infieldBall.cy + 50, 0.04)
    
    #drawLuffy
    luffyList = [app.luffy1, app.luffy2, app.luffy3, app.luffy4, app.luffy5, app.luffy6, app.luffy7, app.luffy8, app.luffy9]
    imageW, imageH = getImageSize(luffyList[app.luffyIndex])
    if app.strikes != 3 and app.outs != 3:
        if app.luffyIndex != 8:
            if app.luffyIndex == 4 or app.luffyIndex == 5 or app.luffyIndex == 6:
                if app.currentlyPitching and hitBall(app):
                    drawImageHelper(app.luffyBatHit, app.luffyX + 195, 485, 2)
            drawImage(luffyList[app.luffyIndex], app.luffyX, 520, width = imageW * 3.5, height = imageH * 3.5, align = "left")
        #else last frame, which is offplaced to the right
        else:
            drawImage(luffyList[app.luffyIndex], app.luffyX-39, 520, width = imageW * 3.5, height = imageH * 3.5, align = "left")
    elif app.strikes == 3:
        drawImageHelper(app.luffyGO, app.luffyX + 50, 515, 3.5)
    elif app.outs == 3:
        drawImageHelper(app.luffySO, app.luffyX+ 85, 505, 3.5)
    
    
    #strikes
    drawLabel("S", 863, 225, fill = "red", border = "black", borderWidth = 1, bold = True, size = 30, font = "montserrat")
    drawCircle(900, 225, 12, fill = "black")
    drawCircle(935, 225, 12, fill = "black")
    if app.strikes == 1:
        drawCircle(900, 225, 9, fill = "gold")
    elif app.strikes >= 2:
        drawCircle(900, 225, 9, fill = "gold")
        drawCircle(935, 225, 9, fill = "gold")
    
    #balls
    drawLabel("B", 863, 270, fill = "red", border = "black", borderWidth = 1, bold = True, size = 30, font = "montserrat")
    drawCircle(900, 270, 12, fill = "black")
    drawCircle(935, 270, 12, fill = "black")
    drawCircle(970, 270, 12, fill = "black")
    if app.balls == 1:
        drawCircle(900, 270, 9, fill = "gold")
    elif app.balls == 2:
        drawCircle(900, 270, 9, fill = "gold")
        drawCircle(935, 270, 9, fill = "gold")
    elif app.balls >= 3:
        drawCircle(900, 270, 9, fill = "gold")
        drawCircle(935, 270, 9, fill = "gold")
        drawCircle(970, 270, 9, fill = "gold")
    
    #outs
    drawLabel("O", 863, 315, fill = "red", border = "black", borderWidth = 1, bold = True, size = 30, font = "montserrat")
    drawCircle(900, 315, 12, fill = "black")
    drawCircle(935, 315, 12, fill = "black")
    if app.outs == 1:
        drawCircle(900, 315, 9, fill = "gold")
    elif app.outs >= 2:
        drawCircle(900, 315, 9, fill = "gold")
        drawCircle(935, 315, 9, fill = "gold")
    
    #baseRunners
    if app.baseRunners[0] == True:
        drawRect(965,80,12,24, fill = "yellow", border = "black", borderWidth = 1)
    if app.baseRunners[1] == True:
        drawRect(895,10,12,24, fill = "yellow", border = "black", borderWidth = 1)
    if app.baseRunners[2] == True:
        drawRect(824,80,12,24, fill = "yellow", border = "black", borderWidth = 1)
    
    #strikeout or walk text
    if app.outs == 3:
        drawRect(0,0,app.width, app.height, opacity = 50)
        drawImageHelper(app.gameOverText, app.width / 2, 220, 0.6)
        drawLabel("Press enter to continue", app.width / 2, 375, size = 30, font = "cinzel", fill = "white", bold = True)
    elif app.strikes == 3:
        drawRect(0,0,app.width, app.height, opacity = 50)
        drawImageHelper(app.strikeoutText, app.width / 2, 220, 0.6)
        drawLabel("Press enter to continue", app.width / 2, 375, size = 30, font = "cinzel", fill = "white", bold = True)
    elif app.balls == 4:
        drawRect(0,0,app.width, app.height, opacity = 50)
        drawImageHelper(app.walkText, app.width / 2, 220, 0.4)
        drawLabel("Press enter to continue", app.width / 2, 375, size = 30, font = "cinzel", fill = "white", bold = True)
    #help button
    drawRect(75, 284, 125, 140, align = "center", fill = "goldenRod", border = app.baseballBorder, borderWidth = 4)
    drawImageHelper(app.helpButton, 75, 270, 0.13)
    drawLabel("CONTROLS", 75, 330, size = 18, font = "cinzel", fill = "white", bold = True)

def playScreen_onMouseMove(app,mouseX,mouseY):
    if pressIn(75 - 125 / 2, 284 - 140 / 2, 125, 140, mouseX, mouseY):
        app.baseballBorder = rgb(255, 192, 0)
    else:
        app.baseballBorder = "black"

def playScreen_onStep(app):
    if app.balls == 4 or app.strikes == 3 or app.outs == 3:
        return
    app.playerSwingTimer += 1
    app.pitcherTimer += 1
    if app.playerScore > 7:
        setActiveScreen('victoryScreen')
    elif app.outs >= 3:
        setActiveScreen('defeatScreen')
    if app.playerSwingTimer % 2 == 0:
        if app.luffySwinging and app.luffyIndex < 8:
            app.luffyIndex +=1
    if app.pitcherTimer % 4 == 0:
        if app.zoroPitching and app.zoroIndex < 10:
            app.zoroIndex += 1
    if app.zoroIndex == 10:
        app.zoroPitching = False
        app.zoroIndex = 6
        app.currentlyPitching = True #begin ball movement and ball becomes visible
    if app.currentlyPitching:
        app.baseballX += app.dx
        app.baseballY += app.dy
        app.finalBallAngle += app.ballRotation
        if app.baseballY > 430:
            app.zoroIndex = 0
        if app.baseballY > 560 and app.baseballY < 580:
            app.ballAcrossPlateX = app.baseballX
        if app.baseballY > app.height:
            app.luffySwinging = False
            if isStrike(app):
                app.strikes += 1
                if app.strikes == 3:
                    app.outs += 1
            else:
                app.balls += 1
                print("balls", app.balls)
                print(app.baseRunners)
                if app.balls == 4:
                    configureRunners(app)
            #resets for next pitch
            app.currentlyPitching = False
            app.baseballX = 506
            app.baseballY = 274
            app.swung = False #resets if players swung each new pitch
        #ball movement into infield
        elif app.ballIsHit:
            app.dx = -(app.dx) * 13
            app.dy = -(app.dy) * 1.5
            app.ballIsHit = False
    if app.baseballY < 150:
        toOutfieldScreen(app)
        setActiveScreen("outfieldScreen")
    if app.currentlyPitching == False:
        app.luffyIndex = 0

def playScreen_onMousePress(app, mouseX, mouseY):
    if pressIn(75 - 125 / 2, 284 - 140 / 2, 125, 140, mouseX, mouseY):
        setActiveScreen("controlsScreen")
        return
    if app.balls == 4 or app.strikes == 3 or app.outs == 3:
        return
    if app.currentlyPitching != True:
        return
    app.ballIsHit = False
    app.swung = True
    app.yWhenSwung = app.baseballY + app.dy/ 175
    #app.luffyIndex = 0
    app.luffySwinging = not app.luffySwinging
    if hitBall(app):
        app.ballIsHit = True

def playScreen_onKeyPress(app, key):
    if app.outs == 3:
        if key == "enter":
            setActiveScreen("defeatScreen")
        else:
            return
    if app.strikes == 3 or app.balls == 4:
        if key == "enter":
            newBatter(app)
        else:
            return
    if app.currentlyPitching == True or app.zoroPitching == True:
        return
    if key == "left" and app.luffyX > 285:
        app.luffyX -= 10
    elif key == "right" and app.luffyX < 345:
        app.luffyX += 10
    elif key == "space":
        app.pitches += 1
        app.zoroIndex = 0
        app.zoroPitching = not app.zoroPitching
        app.baseballX = 506
        app.baseballY = 274
        app.dx = random.randint(-92,165) / 100
        app.dy = random.randint(350, 850) / 100
        getRotation(app)
    elif key == "t":
        setActiveScreen('titleScreen')
    elif key == "p":
        setActiveScreen('playScreen')
    elif key == "o":
        app.outs = 3
    elif key == "s":
        app.strikes = 3
        app.outs += 1
    elif key == "b":
        app.balls = 4
        configureRunners(app)
    elif key == "l":
        app.baseRunners = [True, True, True]


########################
#game code
########################

def newBatter(app):
    app.strikes = 0
    app.balls = 0
    app.ballIsHit = False
    app.swung = False
    app.currentlyPitching = False
    app.zoroIndex = 0
    app.zoroPitching = False
    app.baseballX = 506
    app.baseballY = 274
    app.dx = random.randint(-92,165) / 100
    app.dy = random.randint(350, 850) / 100
    app.luffySwinging = False
    app.luffyIndex = 0
    

def configureRunners(app):
    if app.homerun == True:
        for i in range(len(app.baseRunners)):
            if app.baseRunners[i] == True:
                app.playerScore += 1
                app.baseRunners[i] = False
    elif app.zoroCaught == False:
        if app.baseRunners[2] == True:
            app.playerScore += 1
            app.baseRunners[2] = False
        if app.baseRunners[1] == True:
            app.baseRunners[2] = True
            app.baseRunners[1] = False
        if app.baseRunners[0] == True:
            app.baseRunners[1] = True
        app.baseRunners[0] = True


def getRotation(app):
    if app.dx > 0.75:
        app.ballRotation = 40
    elif app.dx > 0.50:
        app.ballRotation = 25
    elif app.dx > 0.25:
        app.ballRotation = 19
    elif app.dx > 0:
        app.ballRotation = 11
    elif app.dx > -0.25:
        app.ballRotation = -11
    elif app.dx > -0.50:
        app.ballRotation = -19
    else:
        app.ballRotation = -40


def isStrike(app):
    if app.ballAcrossPlateX > 466 and app.ballAcrossPlateX < 554 and app.swung == False:
        print("strike with no swing")
        return True
    elif app.swung and not hitBall(app):
        print("swing and a miss")
        return True
    elif hitBall(app):
        print("not strike because hit")
        return False
    else:
        print("ball, off plate")
        return False

def hitBall(app):
    if app.baseballX - app.luffyX < 235 and app.baseballX - app.luffyX > 115:
        if app.yWhenSwung > 450 and app.yWhenSwung < 555:
            return True
    else:
        False

def isHomerun(app, cx, cy):
    #oval is centered at 500, 370
    #oval width is 770 and oval height is 675
    #oval x radius is 385, oval y radius is 337.5
    #if equation comes out to be more than 1, then ball cx, cy is not in oval
    if (((cx - 500)**2 / (385**2)) + ((cy - 370)**2 / (337.5**2))) > 1:
        return True
    return False

def toOutfieldScreen(app):
    app.miniBaseballX = 496
    app.miniBaseballY = 524
    app.zoroCx = 500
    app.zoroCy = 420
    app.zoroCaught = False
    app.homerun = False

def backToPlayScreen(app):
    app.luffyIndex = 0
    app.luffySwinging = False
    app.luffyX = 325
    app.zoroPitching = False
    app.zoroIndex = 0
    app.playerSwingTimer = 0
    app.pitcherTimer = 0
    
    app.baseballX = 506
    app.baseballY = 274
    app.dx = 0
    app.dy = 0
    app.ballRotation = 0
    app.finalBallAngle = 0
    app.currentlyPitching = False
    
    app.strikes = 0
    app.balls = 0
    app.swung = False
    app.ballAcrossPlateX = 0
    app.yWhenSwung = 0
    app.isStrike = True
    app.ballIsHit = False
    app.baseballBorder = "black"
    
    
####################################################
# outfieldScreen
####################################################

def outfieldScreen_redrawAll(app):
    outfieldBall = Baseball(app.miniBaseballX, app.miniBaseballY)
    outfieldW, outfieldH = getImageSize(app.outfield)
    drawImage(app.outfield, app.width / 2, 320 , width = outfieldW * 1.1, height = outfieldH * 1.1, align = "center")
    #drawOval(500, 370, 770, 675, fill = "cyan") ...sets infield borders
    
    #draw team batter icon
    drawRect(7, 379, 210, 224)
    drawRect(9, 381, 206, 220, fill = rgb(218, 145, 0))
    drawRect(14, 386, 196, 210, fill = rgb(252, 194, 0))
    drawRect(19, 391, 186, 200, fill = rgb(218, 145, 0))
    drawRect(24, 396, 176, 190, fill = app.teamColor)
    luffyTongueW, luffyTongueH = getImageSize(app.luffyTongue)
    drawImage(app.luffyTongue, 114, 489, width = luffyTongueW * 0.355, height = luffyTongueH * 0.385, align = "center")#0.355 prev height 0.425
    drawRect(114, 637, 140, 35, fill = "white", border = "black", align = "center")
    drawLabel(app.playerNames[app.currentPlayerIndex], 114, 637, fill = app.teamColor, size = 21, bold = True, font='cinzel')
    #draw Enemy team player
    drawRect(783, 379, 210, 224)
    drawRect(785, 381, 206, 220, fill = rgb(218, 145, 0))
    drawRect(790, 386, 196, 210, fill = rgb(252, 194, 0))
    drawRect(795, 391, 186, 200, fill = rgb(218, 145, 0))
    drawRect(800, 396, 176, 190, fill = "lightSeaGreen")
    zoroPicW, zoroPicH = getImageSize(app.zoroFace)
    drawImage(app.zoroFace, 888, 491.5, width = zoroPicW * 3.13, height = zoroPicH * 3.4, align = "center")
    drawRect(890, 637, 140, 35, fill = "white", border = "black", align = "center")
    drawLabel("Zoro", 890, 637, fill = "lightSeaGreen", bold = True, size = 21, font='cinzel')
    
    if app.baseRunners[0] == True:
        drawImageHelper(app.luffyRunner, 606, 420, 1.9)
    if app.baseRunners[1] == True:
        drawImageHelper(app.luffyRunner, 500, 315, 1.9)
    if app.baseRunners[2] == True:
        drawImageHelper(app.luffyRunner, 390, 420, 1.9)
    if app.zoroCaught == False:
        drawImageHelper(app.standing, app.zoroCx, app.zoroCy, 2)
    else:
        drawImageHelper(app.caught, app.zoroCx, app.zoroCy, 2)
    if app.dy != 0:
        baseballW, baseballH = getImageSize(app.baseball)
        drawImage(app.baseball, outfieldBall.cx, outfieldBall.cy, width = baseballW * 0.18, height = baseballH * 0.18, rotateAngle = app.finalBallAngle, align = "center")
    elif app.dy == 0 and app.homerun == True:
        drawImageHelper(app.homerunText, app.width / 2, 150, 0.6)
    elif app.dy == 0 and app.zoroCaught == False:
        drawImageHelper(app.hitText, app.width / 2, 150, 0.4)
    elif app.dy == 0 and app.zoroCaught == True:
        drawImageHelper(app.outText, app.width / 2, 150, 0.4)
    #return to infield button
    if app.dy == 0:
        drawRect(110, 60, 194, 94, fill = None, border = app.baseballBorder, borderWidth = 6, align = "center" )
        baseballRectW, baseballRectH = getImageSize(app.baseballRect)
        drawImage(app.baseballRect, 110, 60, width = baseballRectW * 0.07, height = baseballRectH *0.12, rotateAngle = -90, align = "center")
        drawLabel("Return to Infield", 110, 60, fill = app.baseballBorder,size = 22, bold = True)
    #scoreboard
    drawRect(800, 13, 190, 125, fill = "peru", border = "black", borderWidth = 4)
    drawRect(895, 35, 130, 40, fill = "white", border = "black", borderWidth = 2, align = "center")
    drawLabel("Scoreboard", 895, 35, font = "cinzel", bold = True, size = 16)
    drawRect(830, 60, 40, 50, fill = "white", border = "black", borderWidth = 2)
    drawRect(920, 60, 40, 50, fill = "white", border = "black", borderWidth = 2)
    drawRect(895, 85, 22, 10, align = "center")
    drawRect(810, 115, 80, 20, fill = "white", border = "black", borderWidth = 2)
    drawRect(900, 115, 80, 20, fill = "white", border = "black", borderWidth = 2)
    drawLabel(f'{app.playerScore}', 850, 85, size = 30, font = "orbitron", bold = True)
    drawLabel('7', 940, 85, size = 30, font = "orbitron", bold = True)
    drawLabel(app.nameText, 850, 125, size = 12, font = "cinzel", fill = app.teamColor, bold = True)
    drawLabel("Marines", 940, 125, size = 12, font = "cinzel", fill = "lightSeaGreen", bold = True)

def outfieldScreen_onStep(app):
    app.miniBaseballX += app.dx / 10 #modifies delta x and delat y values to look better for outfield
    app.miniBaseballY += app.dy / 5
    app.finalBallAngle += app.ballRotation / 6 #changes spin for outfield
    if app.dy != 0:
        if app.miniBaseballX < 496 and app.zoroCx > app.miniBaseballX:
            app.zoroCx -= 0.8
        elif app.miniBaseballX > 496 and app.zoroCx < app.miniBaseballX:
            app.zoroCx += 0.8
        if app.miniBaseballY < 440 and app.zoroCy > app.miniBaseballY:
            app.zoroCy -= 0.85
        
        if app.dy > -3 and app.dy < -2.8:
            if distance(app.zoroCx, app.zoroCy, app.miniBaseballX, app.miniBaseballY) < 30:
                app.zoroCaught = True
                app.dy = 0
                app.outs += 1
                configureRunners(app)
            else:
                app.zoroCaught = False
                app.dy = 0
                configureRunners(app)
        if isHomerun(app, app.miniBaseballX, app.miniBaseballY):
            app.homerun = True
            app.playerScore += 1
            app.dy = 0
            configureRunners(app)
        else:
            app.homerun = False

    if (app.dy / 5) < -0.3:
        app.dy += 0.025
        if app.dx < -15:
            app.dx = -15
        if app.dx > 0:
            app.dx -= 0.025
        elif app.dx < 0:
            app.dx += 0.025
    else:
        app.dy = 0
        app.dx = 0
        app.finalBallAngle = 0

def outfieldScreen_onMouseMove(app,mouseX,mouseY):
    if app.dy == 0:
        if pressIn(110 - 184 / 2, 60 - 83 / 2, 184, 83, mouseX, mouseY):
            app.baseballBorder = rgb(255, 192, 0)
        else:
            app.baseballBorder = "black"

def outfieldScreen_onMousePress(app,mouseX,mouseY):
    if app.dy == 0:
        if pressIn(110 - 184 / 2, 60 - 83 / 2, 184, 83, mouseX, mouseY):
            backToPlayScreen(app)
            setActiveScreen('playScreen')

def outfieldScreen_onKeyPress(app,key):
    if key == "t":
        setActiveScreen('titleScreen')
    elif key == "o":
        app.outs = 3
    elif key == "s":
        app.strikes = 3
    elif key == "b":
        app.balls = 4
    elif key == "l":
        app.baseRunners = [True, True, True]
    
####################################################
# victoryScreen
####################################################

def victoryScreen_redrawAll(app):
    drawImageHelper(app.endWallpaper, app.width / 2 + 98, app. height / 2, 1.1)
    drawRect(app.width / 2, 260, 520, 80, fill = "white", border = "black", borderWidth = 3, opacity = 70, align = "center")
    drawLabel(f'Final Score: {app.playerScore} - 7', app.width / 2, 260, size = 51, fill = "gray", bold = True, font = "cinzel", border = "black", borderWidth = 2)
    drawRect(500, 450, 194, 94, fill = None, border = app.baseballBorder, borderWidth = 6, align = "center" )
    baseballRectW, baseballRectH = getImageSize(app.baseballRect)
    drawImage(app.baseballRect, 500, 450, width = baseballRectW * 0.07, height = baseballRectH *0.12, rotateAngle = -90, align = "center")
    drawLabel("Main Menu", 500, 450, fill = app.baseballBorder,size = 22, bold = True)
    
    #top plank label
    plankWidth, plankHeight = getImageSize(app.woodenPlank)
    drawImage(app.woodenPlank, app.width / 2, 83, width = plankWidth * 1.2, height = plankHeight * 1.1, align = "center")
    drawCircle(267, 36, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(733, 36, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(267, 130, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(733, 130, 5, fill = "grey", border = "black", borderWidth = 1)
    drawImageHelper(app.victoryText, app.width / 2 + 8, 90, 0.43)

def victoryScreen_onMousePress(app, mouseX, mouseY):
    if pressIn(500 - 184 / 2, 450 - 83 / 2, 184, 83, mouseX, mouseY):
        newGame(app)

def victoryScreen_onMouseMove(app,mouseX,mouseY):
    if pressIn(500 - 184 / 2, 450 - 83 / 2, 184, 83, mouseX, mouseY):
        app.baseballBorder = rgb(255, 192, 0)
    else:
        app.baseballBorder = "black"

def victoryScreen_onKeyPress(app,key):
    if key == "t":
        setActiveScreen('titleScreen')
    elif key == "p":
        setActiveScreen('playScreen')
    elif key == "o":
        app.outs = 3
    elif key == "s":
        app.strikes = 3
    elif key == "b":
        app.balls = 4
    elif key == "l":
        app.baseRunners = [True, True, True]


####################################################
# defeatScreen
####################################################

def defeatScreen_redrawAll(app):
    drawImageHelper(app.endWallpaper, app.width / 2 + 98, app. height / 2, 1.1)
    drawRect(app.width / 2, 260, 520, 80, fill = "white", border = "black", borderWidth = 3, opacity = 70, align = "center")
    drawLabel(f'Final Score: {app.playerScore} - 7', app.width / 2, 260, size = 51, fill = "gray", bold = True, font = "cinzel", border = "black", borderWidth = 2)
    drawRect(500, 450, 194, 94, fill = None, border = app.baseballBorder, borderWidth = 6, align = "center" )
    baseballRectW, baseballRectH = getImageSize(app.baseballRect)
    drawImage(app.baseballRect, 500, 450, width = baseballRectW * 0.07, height = baseballRectH *0.12, rotateAngle = -90, align = "center")
    drawLabel("Main Menu", 500, 450, fill = app.baseballBorder,size = 22, bold = True)
    
    #top plank label
    plankWidth, plankHeight = getImageSize(app.woodenPlank)
    drawImage(app.woodenPlank, app.width / 2, 83, width = plankWidth * 1.2, height = plankHeight * 1.1, align = "center")
    drawCircle(267, 36, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(733, 36, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(267, 130, 5, fill = "grey", border = "black", borderWidth = 1)
    drawCircle(733, 130, 5, fill = "grey", border = "black", borderWidth = 1)
    drawImageHelper(app.defeatText, app.width / 2 + 8, 90, 0.38)

def defeatScreen_onMousePress(app, mouseX, mouseY):
    if pressIn(500 - 184 / 2, 450 - 83 / 2, 184, 83, mouseX, mouseY):
        newGame(app)

def defeatScreen_onMouseMove(app,mouseX,mouseY):
    if pressIn(500 - 184 / 2, 450 - 83 / 2, 184, 83, mouseX, mouseY):
        app.baseballBorder = rgb(255, 192, 0)
    else:
        app.baseballBorder = "black"

def defeatScreen_onKeyPress(app,key):
    if key == "t":
        setActiveScreen('titleScreen')
    elif key == "p":
        setActiveScreen('playScreen')
    elif key == "o":
        app.outs = 3
    elif key == "s":
        app.strikes = 3
    elif key == "b":
        app.balls = 4
    elif key == "l":
        app.baseRunners = [True, True, True]



####################################################
# main function
####################################################

def main():
    runAppWithScreens(initialScreen='titleScreen')

main()
