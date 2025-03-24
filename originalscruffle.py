import random
import time
# above, I import random, as part of my game is based on chance.
# I also import time, because a sudden wall of text isn't as cool
# so I use time.sleep() in places as a breather.

idConstants = {'alarm clock': [False, 0, 6, 3, 7, 7, 'special?', 'EAR-HURTING, SLEEP-INTERRUPTING ALARM CLOCK', 'STURDY, ABLE-TO-WITHSTAND-BEING-THROWN-ACROSS-THE-ROOM-CLOCK', ['this alarm clock is quite annoying.',"you will not attack on time."], 'notes'], 'apple': [False, 0, 4, 7, 7, 7, 'special?', 'FALLING ON BIG HEADS', 'YOUR PERSONAL INFORMATION THAT THEY HAVE BEEN COLLECTING WHILE YOU USE THEIR PRODUCTS', ['maybe it falls on your head'], 'notes'], 'banana': [False, 0, 3, 5, 7, 7, 'special?', 'BOOMERANG BANANANANANANANANA', 'I-AM-MOLDY-ALREADY, DON\'T INGEST ME', ['not a boomerang'], 'notes'], 'brain': [False, 0, 2, 7, 7, 7, 'special?', 'BRAINCELL 1-2-3', 'SKULL!!', ['how many braincells in here?'], 'notes'], 'bush': [False, 0, 2, 2, 7, 7, 'special?', 'POKE. BUSH. COOL. CUTE. BUSH.', 'POKE.', ['two years ago our family\'s budgie, named bushy, died. I still think about her.'], 'notes'], 'cactus': [False, 0, 10, 9, 7, 7, 'special?', 'PROVOKED POKE.', 'PROVOKED MORE-POKE.', ['spikey cactus! strawberry cactus!'], 'notes'], 'calculator': [False, 0, 8, 9, 7, 7, 'special?', 'PROJECTILE CALCULATOR!!!!!!!', 'CLAIMS OF "I\'M NOT AN ILLEGAL DEVICE, JUST A CALCULATOR"', ['maybe you drew a cell phone but the model doesn\'t recognise that...','the damage is emotional. no projectile calculators in the physics classroom'], 'notes'], 'cat': [False, 0, 7, 8, 7, 7, 'special?', 'CUTE OWO', 'CUTE OWO', ['I like cats :)','magolor is a cat. magolor wears a crown hmm.'], 'notes'], 'cello': [False, 0, 3, 5, 7, 7, 'special?', 'UNLEASHING RAAAAAAAAGE AFTER BEING CALLED BIG VIOLIN FOR THE 9TH TIME', 'AN ESSAY ABOUT WHY THEY ARE NOT A BIG VIOLIN', ['maybe you were trying to draw a violin? these two look kinda the same anyway'], 'notes'], 'chair': [False, 0, 6, 6, 7, 7, 'special?', 'HAMILTON, SIT DOWN', 'ITS NATURAL ABILITY TO BE STURY', ['hamilton, sit down - wise words','the damage is also emotional, probably? hopefully nobody is throwing chairs around here.'], 'notes'], 'circle': [False, 0, 4, 4, 7, 7, 'special?', 'CIRCULAR REASONING! AND FALLACY FALLACY!', 'FALLACY FALLACY! AND CIRCULAR REASONING!', ['this is a jigglypuff viewed from above.'], 'notes'],  'clarinet': [False, 0, 6, 7, 7, 7, 'special?', 'UNLEASHING RAAAGE AFTER BEING CALLED SQUIDWARD FOR THE 12TH TIME', 'SQHRIEALK (THIS COULD HAVE BEEN AN ATTACK)', ['like squidward.'], 'notes'], 'coffee cup': [False, 0, 2, 9, 7, 7, 'special?', 'CAFFEINE', 'CAFFEINE', ['don\'t get addicted to caffeine, kids'], 'notes'], 'crown': [False, 0, 8, 7, 7, 7, 'special?', 'INTRUSIVE URGES OF WORLD DOMINATION ON ITS WEARER', 'ITS NEW DOMINATED WORLD', ['this crown is a magolor reference!'], 'notes'], 'door': [False, 0, 1, 0, 7, 7, 'special?', '...lol haha bold of you to assume this door has any power', '"b-but I was busy! doing work! not procrastinating at all nopenope!"', ['that\'s me! door!! I don\'t do much damage and don\'t have the best health bar lol.',"I'm a self insert!"], 'notes'], 'duck': [False, 0, 8, 5, 7, 7, 'special?', 'AQUACKATTACK', 'AQUACKQUEFENSE', ['ducc meets every week on wednesday after school in room 344.','do you have grapes?'], 'notes'], 'eye': [False, 0, 2, 5, 7, 7, 'special?', 'SEEING', 'CLOSING', ['the all-seeing eye...has a speck of dust in it'], 'notes'], 'grapes': [False, 0, 4, 4, 7, 7, 'special?', 'PROJECTILE GRAPE', 'GROUP-OF-GRAPES', ['hey...got any grapes?'], 'notes'], 'grass': [False, 0, 2, 9, 7, 7, 'special?', 'A POMPOUS MESSAGE TELLING YOU TO TOUCH GRASS', '"OKAY BUT BEFORE YOU ATTACK YOU SHOULD TOUCH GRASS RIGHT"', ['it is common courtesy to remind people to touch grass','the damage is probably also emotional'], 'notes'], 'hand': [False, 0, 5, 4, 7, 7, 'special?', 'A LOT OF BADLY-DRAWN FINGERS', 'A LOT OF BADLY-DRAWN FINGERS', ['wow this is the power I wish to have! the ability to draw a hand.','it does 4 damage for the amount of fingers I sometimes draw.'], 'notes'], 'ice cream': [False, 0, 3, 7, 7, 7, 'special?', 'BRAIN FREEZE', 'SHEER COLDNESS', ['my sister likes ice cream! she also likes screaming in general. that is why this does a lot of damage.'], 'notes'], 'line': [False, 0, 1, 1, 7, 7, 'special?', '________', '__________', ['wow. what an unassuming line'], 'notes'], 'microphone': [False, 0, 2, 8, 7, 7, 'special?', 'SQUIREHKEEEEEEEEEEEEEALK', 'SQUEEEEEEEEEIRREALK', ['stage crew wishes people talked better into these.','it does a lot of damage when people don\'t talk properly into these, or when stage crew increases the gain too much.'], 'notes'], 'mushroom': [False, 0, 10, 10, 7, 7, 'special?', 'POISON POWDER', 'HYPNOSHROOM', ["wow it's standknee", 'this is your sign to go tell my friend that she is a mushroom','this mushroom does a lot of damage and has a lot of health, because my friend is cool like that'], 'notes'], 'octopus': [False, 0, 8, 8, 7, 7, 'special?', 'ZIPCASTER OCTOBRUSH', 'ITS EIGHT NOT TEN TENTACLES', ['this is a splatoon reference','8 damage and health... get it?', 'dialogue'], 'notes'], 'paintbrush': [False, 0, 2, 10, 7, 7, 'special?', 'EMOTIONAL DAMAGE (AND INK)(AND KIRBY ARTIST VIVIDRIA)', 'FRIDGE KIRBY', ['take a breath, paint a bush. a forest grown from memories.','I had a best friend and she left me / it was a sudden surprise. / dissonance, they called it harmony / and maybe her love was a lie.','emotional damage. to me :('], 'notes'], 'parrot': [False, 0, 2, 10, 7, 7, 'special?', 'CHOMP', 'OVO', ['they are so fragile but their bites hurt so much'], 'notes'], 'pineapple': [False, 0, 7, 3, 7, 7, 'special?', 'SPIKEY', 'SPIKEY', ['this belongs on pizza.','SQUIDWARD LIVES IN THIS (no I think it was spongebob but I dunno. never watched that show)','spikey defense?'], 'notes'], 'pizza': [False, 0, 3, 7, 7, 7, 'special?', 'A DELICIOUS PIZZA SLAP', '"B-BUT THE EARTH IS A FLAT PIZZA SO YOU SHOULDN\'T HURT THE CRUST :(', ['this belongs under pineapple.','now I want to eat pizza','happy late pi day! or early pi day...it is circular'], 'notes'], 'rain': [True, 0, 2, 3, 2, 7, 'special?', 'sploosh', 'sploosh', ['I had quite a lot of settings with different modifiers that I manually set. but they did not make the cut. only rain did. not even clouds and leaves because I forgot they could have cool synergy oops. but yes rain. let it RAAAAIN'], 'notes'], 'rainbow': [False, 0, 10, 3, 7, 7, 'special?', 'ITS SHEER BEAUTY PERSONIFIED', 'RAINBOWS ARE JUST FANCY LIGHT AND WATER INTERACTIONS', ['there was no pot of gold :(','ever heard of the rainbow bridge?','rainbows won\'t light up the sky unless you let it rain! (but in this game rainbows exist anyway lol)'], 'notes'], 'saxophone': [False, 0, 6, 8, 7, 7, 'special?', 'HONKBLASTISSIMO', '"UMM I\'M JUST A SAXOPHONE I CAN\'T COUNT :(', ['pretending to be a brass instrument','blastissimo!!'], 'notes'], 'skull': [False, 0, 8, 4, 7, 7, 'special?', 'SKULL EMOJI', 'SKULL EMOJI', ['skull emoji!!'], 'notes'], 'squiggle': [False, 0, 9, 8, 7, 7, 'special?', 'SQUIGGLEY SQUIGGLELELGLELGLE', 'WIGGLEY SQUIGGLE', ['wow the power of a squiggle is immense'], 'notes'], 'squirrel': [False, 0, 6, 9, 7, 7, 'special?', 'DROPPING AN ACORN ON YOUR HEAD', 'RUNNING AWAY, BACK TO THE DREY', ['whoa a squirrel. is it russian? (EL + HK reference)'], 'notes'], 'strawberry': [False, 0, 4, 8, 7, 7, 'special?', 'FIREBOMBSTRAWBERRY', 'SEED RESPAWN', ['strawberry cactus.','super strawberry.'], 'notes'], 'sun': [False, 0, 9, 10, 7, 7, 'special?', 'MWAHAHHA KICK PUNCH KICK PUNCH SUNSHINE AND RAINBOWS', '"I\'M JUST AN INNOCENT LITTLE KID"', ['oh hey my little sister is sunny! the power of being annoying. it does a lot of damage'], 'notes'], 'triangle': [False, 0, 4, 4, 7, 7, 'special?', 'POKE', 'A CONSPIRACY THEORY OR TWO', ['I dunno what triangle-shaped thing you were trying to draw. tortillas or illuminati or the number 4?'], 'notes'], 'trombone': [False, 0, 6, 6, 7, 7, 'special?', 'LOUD TROMBONE NOISES', 'SAD TROMBONE NOISES :(', ['sad trombone noises.'], 'notes'], 'trumpet': [False, 0, 6, 7, 7, 7, 'special?', 'BLASTHONKTISSIMO', '"UMM THAT NOTE IS TOO HIGH"', ['your beautiful honking...','blastissimo!!'], 'notes'], 'umbrella': [False, 0, 7, 4, 7, 7, 'special?', 'SPLAT BRELLA!!!!', 'BRELLA SHIELD...oops it flew off', ['undercover brella wowee','this was supposed to protect from the rain but I don\'t feel like hardcoding it','I dunno about you, but my umbrellas break too easily.'], 'notes'], 'zigzag': [False, 0, 3, 2, 7, 7, 'special?', 'LIGHTNING BOLT!!! OR NOT OOOPS', '"ZZZZZZZZ"', ['were you trying to draw a lightning bolt? lol'], 'notes']}

# do not try scrolling right to read this entire dictionary. it will take too long.
# idConstants is a dictionary. the keys are possible IDs and the values are lists with specific items at indices
# For example, at idConstants['cactus'], there is a list [False, 0, 10, 9, 7, 7, 'special?', 'PROVOKED POKE.', 'PROVOKED MORE-POKE.', ['spikey cactus! strawberry cactus!'], 'notes']
# let's call this exampleCommentList, or eCL for short.
# eCL = [False, 0, 10, 9, 7, 7, 'special?', 'PROVOKED POKE.', 'PROVOKED MORE-POKE.', ['spikey cactus! strawberry cactus!'], 'notes']
# eCL[0]: boolean value. whether this is a setting, which is a special battleground with exceptions and modifiers.
# eCL[1]: int. class. In the future, these items will be split into classes, and there will be bonuses for team synergy among other things.
# eCL[2]: int. health (/10. may change to /17 for balancing)
# eCL[3]: int. damage (/10.)
# eCL[4] and eCL[5]: int. future attributes, "braincell count" and "klutz", for future settings.
# eCL[6]: string. a hardcoded indicator for special things. not yet implemented.
# ecl[7]: string. ATTACK! the move that they use when attacking. may change to have multiple someday.
# ecl[8]: string. DEFENSE! the move that they use when defending. may change to have multiple someday.
# ecl[9]: list containing strings. randomly selected in the game. I called this "dialogue" but you may consider it "caption" or something.
# ecl[10]: string. "notes" are notes for myself. I haven't yet put any because I needed more content in the list of dialogue.
# For what it is worth, I did use list methods when making idConstants and synergyRain.

synergyRain = ['brain', 'bush', 'door', 'duck', 'grass', 'paintbrush', 'rain', 'rainbow', 'sun', 'umbrella']
# These are items that I have personally decided should have synergy with rain. Some make sense, some don't.

def identifyDoodle():
    # This function would implement DL.
    # It would return a 2D list in a format like this: [["apple", 0.9],["banana",0.05],["cat",0.05]]
    return []

def makeshiftDoodle():
    # This function was made for my battle mechanic testing.
    # This function generates a random percent composition of three random IDs and sorts the 2D list.
    # It uses the random module.
    returnDoodle = []
    possiblID = ['alarm clock', 'apple', 'banana', 'brain', 'bush', 'cactus', 'calculator', 'cat', 'cello', 'chair', 'circle', 'clarinet', 'coffee cup', 'crown', 'door', 'duck', 'eye', 'grapes', 'grass', 'hand', 'ice cream', 'line', 'microphone', 'mushroom', 'octopus', 'paintbrush', 'parrot', 'pineapple', 'pizza', 'rain', 'rainbow', 'saxophone', 'skull', 'squiggle', 'squirrel', 'strawberry', 'sun', 'triangle', 'trombone', 'trumpet', 'umbrella', 'zigzag']
    id1 = random.choice(possiblID)
    c1 = random.random()
    c1 = round(c1,4)
    returnDoodle.append([id1,c1])
    # I add lists to the list returnDoodle, as that is the format that my game runs on.
    possiblID.remove(id1)
    id2 = random.choice(possiblID)
    c2 = random.uniform(0,1-c1)
    c2 = round(c2,4)
    returnDoodle.append([id2,c2])
    possiblID.remove(id2)
    id3 = random.choice(possiblID)
    # c3 does not need to be random, as the percentages must sum to 1.
    c3 = 1-c1-c2
    c3 = round(c3,4)
    returnDoodle.append([id3,c3])
    returnDoodle = sorted(returnDoodle,key=lambda l:l[1],reverse=True)
    return returnDoodle

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
    # These global variables are also used in other functions.
    isRaining = False
    # isRaining is a boolean, which describes the setting of the game (either non-existent or raining are the two options right now.)
    isRaining = setSetting()
    if isRaining:
        print("It is raining. Some scribbles may have synergistic relations with the rain.")
    # At this identifyDoodle() section, there would be a prompt for the user to doodle on a screen.
    teamList = identifyDoodle()
    # Then, there would be a prompt for them to draw the opposition, or to pass the device to an enemy for them to draw the opposition.
    oppList = identifyDoodle()
    # For the sake of this project, the makeshift doodles are used.
    teamList = makeshiftDoodle()
    oppList = makeshiftDoodle()
    # these lists are two-dimensional
    # the percentage calculated the most likely
    teamMain = teamList[0][0]
    oppMain = oppList[0][0]
    teamCaption = random.choice(idConstants[teamMain][9])
    oppCaption = random.choice(idConstants[oppMain][9])
    # below are floats
    teamDamage = calculateDamage(teamList)
    oppDamage = calculateDamage(oppList)
    teamHealth = calculateHealth(teamList)
    oppHealth = calculateHealth(oppList)
    # now, check with the rain
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
    # The rest of this function is just printing information.
    # I use string formatting as it is easier than many string additions.
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
    # The function has called scribblScruffle(), and the game continues there.

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
