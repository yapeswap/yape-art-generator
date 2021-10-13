#!/usr/bin/env python

import random
import numpy
import json

#  ___    ___ ________  ________  _______   ________  ___       __   ________  ________   
# |\  \  /  /|\   __  \|\   __  \|\  ___ \ |\   ____\|\  \     |\  \|\   __  \|\   __  \  
# \ \  \/  / | \  \|\  \ \  \|\  \ \   __/|\ \  \___|\ \  \    \ \  \ \  \|\  \ \  \|\  \ 
#  \ \    / / \ \   __  \ \   ____\ \  \_|/_\ \_____  \ \  \  __\ \  \ \   __  \ \   ____\
#   \/  /  /   \ \  \ \  \ \  \___|\ \  \_|\ \|____|\  \ \  \|\__\_\  \ \  \ \  \ \  \___|
# __/  / /      \ \__\ \__\ \__\    \ \_______\____\_\  \ \____________\ \__\ \__\ \__\   
#|\___/ /        \|__|\|__|\|__|     \|_______|\_________\|____________|\|__|\|__|\|__|   
#\|___|/                                      \|_________|                                

#Todo

#Tend to zen garden.

#Will run gas cost tests to make sure
#Finish Analytics File

ceil = 474
hatCeil = 14
gradCeil = 29

elements = [True, False]

#Lord forgive me for I have sinned
hatTable = [(True, False, False),(False, True, False),(False, False, True)]
hatAssist = [0, 1, 2]
hatChoice = [0.15, 0.25, 0.6,]

hatWeight = [0.9, 0.1]
shadesWeight = [0.1, 0.9]
caneWeight = [0.1, 0.9]
fangsWeight = [0.1, 0.9]

patNames = []
hatNames = []
gradNames = []

#Make it to where you can only have one of cmdr durag or cans then make it pick randomly between the three
class Monkey():
    def __init__(self, ident, coinPat, hairPat, faceEarsPat, eyeMouthPat, canePat, cmdrOuterPat, cmdrOuterStarPat, cmdrInnerStarPat, duragPat, cansInnerPat, cansOuterPat, shadesPat):
    
        self.ident = ident
        self.name = ""
        self.coinNum = coinPat
        self.hairNum = hairPat
        self.faceEarsNum = faceEarsPat
        self.eyeMouthNum = eyeMouthPat
        self.hatAcc = numpy.random.choice(elements, p=hatWeight)
        self.cmdrAcc = False
        self.duragAcc = False
        self.cansAcc = False

        self.shadesAcc = numpy.random.choice(elements, p=shadesWeight)
        self.caneAcc = numpy.random.choice(elements, p=caneWeight)
        self.fangsAcc = numpy.random.choice(elements, p=fangsWeight)

        #METADATA: Numbers of Accessories, to be mapped to names and given rarity. 
        self.cmdrOuterNum = cmdrOuterPat
        self.cmdrOuterStarNum = cmdrOuterStarPat
        self.cmdrInnerStarNum = cmdrInnerStarPat
        self.duragNum = duragPat
        self.cansOuterNum = cansOuterPat
        self.cansInnerNum = cansInnerPat
        self.shadesNum = shadesPat
        self.caneNum = canePat

        #Translated to Names Later
        self.coinPat = "pat"+str(coinPat)+".png"
        self.hairPat = "pat"+str(hairPat)+".png"
        self.faceEarsPat = "pat"+str(faceEarsPat)+".png"
        self.cansOuterPat = "pat"+str(cansOuterPat)+".png"
        self.cansInnerPat = "pat"+str(cansInnerPat)+".png"

        #Also Translated to names. 
        self.cmdrOuterPat = "hat"+str(cmdrOuterPat)+".png"
        self.cmdrOuterStarPat = "hat"+str(cmdrOuterStarPat)+".png"
        self.cmdrInnerStarPat = "hat"+str(cmdrInnerStarPat)+".png"
        self.duragPat = "hat"+str(duragPat)+".png"

        #Canes and Shades can be the same, see gradNum
        self.shadesPat = "grad"+str(shadesPat)+".png"
        self.canePat = "grad"+str(canePat)+".png"
        self.eyeMouthPat = "grad"+str(eyeMouthPat)+".png"

        self.whatHat = ""
        if(self.hatAcc == True or self.shadesAcc == True or self.caneAcc == True or self.fangsAcc == True):
            self.hasAcc = True
        else:
            self.hasAcc = False 

    def hatValidate(self):
        #pick one of the three to make true at random
        if(self.hatAcc):
            choice = numpy.random.choice(hatAssist, p=hatChoice)
            self.cmdrAcc = hatTable[choice][0]
            self.duragAcc = hatTable[choice][1]
            self.cansAcc = hatTable[choice][2]
            if self.cmdrAcc:
                self.whatHat = "Commander"
            if self.duragAcc:
                self.whatHat = "Rag"
            if self.cansAcc:
                self.whatHat = "Cans"

    def setSelfName(self, n):
        self.name = n


def monkeyGen(ident):

    patNum = random.sample(range(ceil), 6)
    accNum = random.sample(range(hatCeil), 4)
    gradNum = random.randint(0, gradCeil)

    #Need to generate a lot more numbers, need some ceilings and some more patterns, also need to ensure none of the numbers match for 

    newMonkey = Monkey(
                    ident,
                    patNum[0],
                    patNum[1],
                    patNum[2],
                    gradNum,
                    gradNum,
                    accNum[0],
                    accNum[1],
                    accNum[2],
                    accNum[3],
                    patNum[4],
                    patNum[5],
                    gradNum
                    )

    return newMonkey


def loadNames():
    with open("/home/notes/Programming/Yapeswap/yape-art-generator/PatternNames/pixNames.txt", "r") as txt_file:
        for line in txt_file:
            patNames.append(line)
    txt_file.close()

    with open("/home/notes/Programming/Yapeswap/yape-art-generator/PatternNames/hatNames.txt", "r") as txt_file:
        for line in txt_file:
            hatNames.append(line)
    txt_file.close()

    with open("/home/notes/Programming/Yapeswap/yape-art-generator/PatternNames/gradNames.txt", "r") as txt_file:
        for line in txt_file:
            gradNames.append(line)
    txt_file.close()


#Take a monkey
#Get list of attributes
#Get a description and a name. Description optional Name will be defined in the monkey
#If the attribute is active then add it to the attributes metadata
#If not then skip
def metadataGenerator(mk):
        metadata = mk.__dict__
        accessories = []
        cleanedAccessories = []
        #This will store all the stuff every yape has. these will be merged into the same attributes thing
        baseAttributes = []

        #Give ikeaML names and collect true attributes
        for x, y in metadata.items():
            if type(y) == str and "hat" in y:
                dex = ''.join(char for char in y if char.isdigit())
                metadata[x] = hatNames[int(dex)-1].strip('\n')
            if type(y) == str and "pat" in y:
                dex = ''.join(char for char in y if char.isdigit())
                metadata[x] = patNames[int(dex)-1].strip('\n')
            if type(y) == str and "grad" in y:
                dex = ''.join(char for char in y if char.isdigit())
                metadata[x] = gradNames[int(dex)-1].strip('\n')
            if y == True:
                if x == "cmdrAcc" or x == "duragAcc" or x == "cansAcc" or x == "shadesAcc" or x == "caneAcc" or x == "fangsAcc":
                    accessories.append(x)
            if x == "coinPat":
                baseAttributes.append({"trait_type": "Coin Pattern", "value": metadata[x]})
            if x == "hairPat":
                baseAttributes.append({"trait_type": "Hair Pattern", "value": metadata[x]})
            if x == "faceEarsPat":
                baseAttributes.append({"trait_type": "Face/Ears Pattern", "value": metadata[x]})
            #Maybe do a rename if shades are present thats too detailed for this
            if x == "eyeMouthPat":
                baseAttributes.append({"trait_type": "Eyes/Mouth Pattern", "value": metadata[x]})

        for x in accessories:
            if x == "cmdrAcc":
                cleanedAccessories.append({"trait_type": 'Hat', "value" :"Commander"})
                cleanedAccessories.append({"trait_type": 'Outer Pattern', "value" : metadata["cmdrOuterPat"]})
                cleanedAccessories.append({"trait_type": 'Inner Pattern', "value" : metadata["cmdrOuterStarPat"]})
                cleanedAccessories.append({"trait_type": 'Star Pattern', "value" : metadata["cmdrInnerStarPat"]})
            if x == "duragAcc":
                cleanedAccessories.append({"trait_type": 'Rag Pattern', "value": metadata["duragPat"]})
            if x == "cansAcc":
                cleanedAccessories.append({"trait_type": "Cans Pattern", "value": metadata["cansOuterPat"]})
                cleanedAccessories.append({"trait_type": "Strap Pattern", "value": metadata["cansInnerPat"]})
            if x == "shadesAcc":
                cleanedAccessories.append({"trait_type": "Shades Pattern", "value": metadata["shadesPat"]})
            if x == "caneAcc":
                cleanedAccessories.append({"trait_type": "Cane Pattern", "value": metadata["canePat"]})
            if x == "fangsAcc":
                cleanedAccessories.append({"trait_type": "Fangs", "value": "NOSFERATU"})

       
       
        attributes = cleanedAccessories + baseAttributes
        fullName = metadata["name"] + " #" + str(metadata["ident"])
        final = {"attributes": attributes, "description": "Thanks for Yaping", "image" : "Put PINATA HERE", "name" : fullName}

        json_object = json.dumps(final, indent = 4)

        with open("/home/notes/Programming/Yapeswap/yape-art-generator/TestMetadata/" + str(mk.ident) + ".json", "w") as outfile:
            outfile.write(json_object)
        outfile.close()



def yapePlugin():
    loadNames()
    ident = 0
    monkies = []
    #Basically youd loop here to generate all monkeys if theres an error try again with same id
    while(len(monkies) < 1):
        nm = monkeyGen(ident)
        if nm not in monkies:
            monkies.append(nm)
            ident += 1

    for monkey in monkies:
        if(monkey.ident % 3 == 0):
            monkey.setSelfName("Titus")
        else:
            monkey.setSelfName("Lucy")
        monkey.hatValidate()

        metadataGenerator(monkey)

        # metadata = monkey.__dict__

        # for x, y in metadata.items():
        #     if(y == True):
        #         metadata[x] = 1
        #     if(y == False):
        #         metadata[x] = 0
        #     if type(y) == str and "hat" in y:
        #         dex = ''.join(char for char in y if char.isdigit())
        #         metadata[x] = hatNames[int(dex)-1].strip('\n')
        #     if type(y) == str and "pat" in y:
        #         dex = ''.join(char for char in y if char.isdigit())
        #         metadata[x] = patNames[int(dex)-1].strip('\n')
        #     if type(y) == str and "grad" in y:
        #         dex = ''.join(char for char in y if char.isdigit())
        #         metadata[x] = gradNames[int(dex)-1].strip('\n')

        # json_object = json.dumps(metadata, indent = 4)

        # with open("/home/notes/Programming/Yapeswap/yape-art-generator/TestMetadata/" + str(monkey.ident) + ".json", "w") as outfile:
        #     outfile.write(json_object)
        # outfile.close()


yapePlugin()