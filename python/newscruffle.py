from idConstants import idConstants
import random
import time

synergyRain = ['brain', 'bush', 'door', 'duck', 'grass', 'paintbrush', 'rain', 'rainbow', 'sun', 'umbrella']

def runClosingCredits(teamWon):
    global teamList, oppList
    # This function simply prints words of thanks, and conclusions.
    print()
    if teamWon:
        print("CONGRATS, YOU WON!")
    else:
        print("OOF, you lost haha.")
    # Here, it shares the composition that was randomly generated.
    print("Here were your percent compositions!")
    print("On the opposing team:")
    for i in oppList:
        print(f'{i[0]}: {round(i[1]*100,3)}%')
    print("On your team: ")
    for i in teamList:
        print(f'{i[0]}: {round(i[1]*100,3)}%')
    print()
    print("Thank you for playing!")

def setSetting():
    global isRaining
    # this function determines the setting of the game.
    # Currently, the only option is rain.
    # As the user is given simply one chance to decide the weather, the try and except blocks exist merely to ensure the program continues when a person does not wish for it to rain.
    try:
        isRaining = int(input("I am providing to you the chance to make it rain. You may enter any integer. Else, rain will not come. "))
        print()
        return True
    except ValueError:
        print("I guess rain just isn't in your brain's plans today!")
    print()
    return False
        
def calculateHealth(lst):
    # this function calculates the health based on a list in the format of the output of identifyDoodle().
    # it is a return function.
    global idConstants
    # the lst is guaranteed to be in the correct format.
    returnedHealth = 0
    for i in range(len(lst)):
        returnedHealth += lst[i][1] * idConstants[lst[i][0]][2]
    return returnedHealth
    
def calculateDamage(lst):
    # this function calculates the damage based on a list in the format of the output of identifyDoodle().
    # it is a return function.
    global idConstants
    global synergyRain
    # the lst is guaranteed to be in the correct format.
    returnedDamage = 0
    for i in range(len(lst)):
        # it still takes len(lst) because I may increase the amount of identified objects from 3.
        returnedDamage += lst[i][1] * idConstants[lst[i][0]][3]
    return returnedDamage
    
def scribbleScruffle(ioru):
    # This function plays out the battling part of the game, using while loops.
    # It runs differently depending on who is going first.
    global teamMain, oppMain
    global teamDamage, oppDamage
    global teamHealth, oppHealth
    global idConstants
    # global variables are used in this function
    teamAttack = idConstants[teamMain][7]
    oppAttack = idConstants[oppMain][7]
    teamDefense = idConstants[teamMain][8]
    oppDefense = idConstants[oppMain][8]
    # Figuring out the string that is their attack.
    # The string is premade in idConstants, personalised by me.
    nahIdWin = False
    # This is a boolean determining whether the team has won.
    print("LET THE SCRUFFLE BEGIN!!")
    print()
    turnNumber = 1
    # the variable above will increment by 1 each time.
    if(ioru == "i"):
        # if they go first, this code runs, else, if the opposition if going first, it skips to that
        # most of this is just string formatting and subtraction
        print("Turn number " + str(turnNumber))
        print(f'{teamMain} attacks with {teamAttack}!')
        print(f'it does {teamDamage} damage!')
        time.sleep(0.1)
        print(f'and {oppMain} tries to defend with {oppDefense}!')
        oppHealth -= teamDamage
        time.sleep(1)
        if oppHealth > 0:
            print("AND THE DEFENSE WORKS! (for now)")
            print(f'{oppMain} has {oppHealth} health left.')
        else:
            print("BUT IT ISN'T ENOUGH!")
            print(f'the opposition, {oppMain}, crashes out. o7')
            print(f'the team, {teamMain}, is the WINNER!')
            nahIdWin = True
            runClosingCredits(nahIdWin)
            return
            # nahIdWin is a boolean determining whether the team won.
        turnNumber += 1
    time.sleep(0.2)
    print()
    print("Turn number " + str(turnNumber))
    # for formatting reasons, every turn, there is a newline
    # again, below, it's all just string formatting, if statements, subtraction
    turnNumber += 1
    print(f'{oppMain} attacks with {oppAttack}!')
    print(f'it does {oppDamage} damage!')
    time.sleep(0.1)
    print(f'and {teamMain} tries to defend with {teamDefense}!')
    teamHealth -= oppDamage
    time.sleep(1)
    if teamHealth > 0:
        print("AND THE DEFENSE WORKS! (for now)")
        print(f'{teamMain} has {teamHealth} health left.')
    else:
        print("BUT IT ISN'T ENOUGH!")
        print(f'the team, {teamMain}, crashes out. o7')
        print(f'the opposition, {oppMain}, is the WINNER!')
        nahIdWin = False
        runClosingCredits(nahIdWin)
        return
    # This is a while loop in case the combat lasts longer.
    # It's all code that has shown up before (with additional breaks when one side is knocked out)
    while(teamHealth > 0 and oppHealth > 0):
        print()
        time.sleep(0.2)
        print("Turn number " + str(turnNumber))
        print(f'{teamMain} attacks with {teamAttack}!')
        print(f'it does {teamDamage} damage!')
        time.sleep(0.1)
        print(f'and {oppMain} tries to defend with {oppDefense}!')
        oppHealth -= teamDamage
        time.sleep(1)
        if oppHealth > 0:
            print("AND THE DEFENSE WORKS! (for now)")
            print(f'{oppMain} has {oppHealth} health left.')
        else:
            print("BUT IT ISN'T ENOUGH!")
            print(f'the opposition, {oppMain}, crashes out. o7')
            print(f'the team, {teamMain}, is the WINNER!')
            nahIdWin = True
            break
        print(f'{oppMain} attacks with {oppAttack}!')
        print(f'it does {oppDamage} damage!')
        time.sleep(0.1)
        print(f'and {teamMain} tries to defend with {teamDefense}!')
        teamHealth -= oppDamage
        time.sleep(1)
        if teamHealth > 0:
            print("AND THE DEFENSE WORKS! (for now)")
            print(f'{teamMain} has {teamHealth} health left.')
        else:
            print("BUT IT ISN'T ENOUGH!")
            print(f'the team, {teamMain}, crashes out. o7')
            print(f'the opposition, {oppMain}, is the WINNER!')
            nahIdWin = False
            break
    time.sleep(0.5)
    # When one side is knocked out, the while loop breaks, and this function runs this next function
    runClosingCredits(nahIdWin)

def runGame():
    # This function runs the game.
    global idConstants, isRaining
    global teamMain, oppMain
    global teamDamage, oppDamage
    global teamHealth, oppHealth
    global teamList, oppList
    global synergyRain
    isRaining = False
    isRaining = setSetting()
    if isRaining:
        print("It is raining. Some scribbles may have synergistic relations with the rain.")
    teamList = identifyDoodle()
    teamMain = teamList[0][0]
    oppMain = oppList[0][0]
    teamCaption = random.choice(idConstants[teamMain][9])
    oppCaption = random.choice(idConstants[oppMain][9])
    teamDamage = calculateDamage(teamList)
    oppDamage = calculateDamage(oppList)
    teamHealth = calculateHealth(teamList)
    oppHealth = calculateHealth(oppList)
    if(isRaining):
        if synergyRain.count(teamMain) == 1:
            teamDamage += idConstants['rain'][3]
            teamHealth += idConstants['rain'][2]
            print("The team is BOOSTED by the rain!")
        if synergyRain.count(oppMain) == 1:
            oppDamage += idConstants['rain'][3]
            oppHealth += idConstants['rain'][2]
            print("The opposition is BOOSTED by the rain!")
    # Rounding to three decimal places, for the sake of order
    teamDamage = round(teamDamage,3)
    oppDamage = round(oppDamage,3)
    teamHealth = round(teamHealth,3)
    oppHealth = round(oppHealth,3)
    time.sleep(1)
    print(f'your team has an attack of {teamDamage} and a health of {teamHealth}.')
    print(f'the opposition has an attack of {oppDamage} and a health of {oppHealth}')
    time.sleep(2)
    print(f'your team is mainly...{teamMain}')
    print(f'this {teamMain} is captioned: {teamCaption}')
    time.sleep(2)
    print(f'and your opposition is mainly...{oppMain}')
    print(f'this {oppMain} is captioned: {oppCaption}')
    print("...")
    time.sleep(4)
    print("Now we look towards the gaze of fate, which shall guide us-")
    time.sleep(2)
    print("Haha, joking. We look at the confidence of the revered function, identifyDoodle().")
    time.sleep(2)
    print(f'The confidence in {teamMain}\'s ID was... {teamList[0][1]*100}% wow!')
    print(f'The confidence in {oppMain}\'s ID was... {oppList[0][1]*100}% wow!')
    time.sleep(2.5)
    if(teamList[0][1] > oppList[0][1]):
        print("INCREDIBLE! The " + teamMain + " is making the first move!")
        scribbleScruffle("i")
    elif(teamList[0][1] < oppList[0][1]):
        print("HAHA! The " + oppMain + " is making the first move!")
        scribbleScruffle("u")
    else:
        # This case is highly unlikely, so it receives a special acknowledgement.
        print(f'ACTUALLY COOL! Both the doodles of {teamMain} and the doodles of {oppMain} were either incredibly reassuring OR incredibly bad!')
        print("so now we DO look towards the gaze of fate...")
        goingFirst = random.choice([teamMain,oppMain])
        print("aaaaand...")
        time.sleep(1)
        print("The " + goingFirst + " TEMPTS FATE! It moves first.")
        if(goingFirst == teamMain):
            scribbleScruffle("i")
        else:
            scribbleScruffle("u")

def getSampleSize():
    # this function ensures no faulty input
    sampleSize = 0
    try:
        sampleSize = int(input("Input an integer: "))
    except ValueError:
        print("Input an integer,please.")
    return sampleSize

# This is the global
# And this is my introduction to the project
print("Scribble Scruffles!")
time.sleep(1)
print("Set two doodles at war against each other!")
time.sleep(1)
print("(Eventually, deep learning and a functioning user interface will be implemented.)")
throwaway = input("Disclaimer: This game contains capslock, which may be considered unprofessional in some projects. This project, however, is a game, and the capslock is for dramatic effect. By entering anything into the input, you acknowledge this disclaimer! ")

print("Firstly, please enter (below) the amount of times you would like to play.")
numStuff = 0
numStuff = getSampleSize()

# This while loop will constantly ask the user for a positive integer.
while numStuff <= 0:
    if(numStuff <= 0):
        print("That wasn't a positive integer.")
    numStuff = getSampleSize()

# This runs for each time the user would like to play the game.
for i in range(numStuff):
    runGame()
    if(numStuff > 1):
        print()
        print("you said you wanted to play " + str(numStuff) + " times!")
        print("you have " + str(numStuff-i-1) + " play(s) left!")
        throwaway = input("Enter anything to keep playing! ")
        # Throwaway is not a variable that is used for anything in particular. It just serves as a pause until the user enters anything to continue.
print("Thanks again for playing. :D")
