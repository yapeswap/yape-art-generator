#!/usr/bin/env python

import random
import numpy
import json
from gimpfu import *

#  ___    ___ ________  ________  _______   ________  ___       __   ________  ________   
# |\  \  /  /|\   __  \|\   __  \|\  ___ \ |\   ____\|\  \     |\  \|\   __  \|\   __  \  
# \ \  \/  / | \  \|\  \ \  \|\  \ \   __/|\ \  \___|\ \  \    \ \  \ \  \|\  \ \  \|\  \ 
#  \ \    / / \ \   __  \ \   ____\ \  \_|/_\ \_____  \ \  \  __\ \  \ \   __  \ \   ____\
#   \/  /  /   \ \  \ \  \ \  \___|\ \  \_|\ \|____|\  \ \  \|\__\_\  \ \  \ \  \ \  \___|
# __/  / /      \ \__\ \__\ \__\    \ \_______\____\_\  \ \____________\ \__\ \__\ \__\   
#|\___/ /        \|__|\|__|\|__|     \|_______|\_________\|____________|\|__|\|__|\|__|   
#\|___|/                                      \|_________|                                

ceil = 474
hatCeil = 14
gradCeil = 29

elements = [True, False]

#Lord forgive me for I have sinned
hatTable = [(True, False, False),(False, True, False),(False, False, True)]
hatAssist = [0, 1, 2]
hatChoice = [0.15, 0.25, 0.6,]

hatWeight = [0.1, 0.9]
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


def analytics(monkies):
    accessoryCount = 0
    hatsCount = 0
    shadesCount = 0
    fangsCount = 0
    caneCount = 0

    pats = []
    hats = []
    grad = []

    for x in range(ceil):
        pats.append((x, 0))
    for x in range(hatCeil):
        hats.append((x, 0))
    for x in range(gradCeil):
        grad.append((x, 0))

    for x in monkies:
        if x.hasAcc:
            accessoryCount += 1
        if x.shadesAcc:
            shadesCount += 1
        if x.fangsAcc:
            fangsCount += 1
        if x.caneAcc:
            caneCount += 1
        pats.append(x.coinPat, x.hairpat, x.faceEarsPat, x.cansOuterPat, x.cansInnerPat)
        hats.append(x.cmdrOuterPat, x.cmdrOuterStarPat, x.cmdrInnerStarPat, x.duragPat)
        grad.append(x.shadesPat, x.canePat, x.eyeMouthPat)


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

def tlGen(monkey):
    
    if(monkey.name == "Lucy"):

        image = pdb.gimp_file_load("/home/notes/Programming/Yapeswap/yape-art-generator/Assets/lucy.xcf", "lucy.xcf")

        image.active_layer = image.layers[17]
        drawable = image.active_layer
        pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[12])
        pdb.gimp_context_set_pattern(monkey.coinPat)
        pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

        image.active_layer = image.layers[16]
        drawable = image.active_layer
        pdb.gimp_context_set_pattern(monkey.hairPat)
        pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[11])
        pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

        image.active_layer = image.layers[15]
        drawable = image.active_layer
        pdb.gimp_context_set_pattern(monkey.faceEarsPat)
        pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[10])
        pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

        image.active_layer = image.layers[14]
        drawable = image.active_layer
        pdb.gimp_context_set_pattern(monkey.eyeMouthPat)
        pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[9])
        pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

        #Accessories

        #Shades
        if(monkey.shadesAcc):
            image.layers[11].visible = True
            image.active_layer = image.layers[11]
            drawable = image.active_layer
            pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[4])
            pdb.gimp_context_set_pattern(monkey.shadesPat)
            pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)
            image.layers[9].visible = True
        else:
            image.layers[11].visible = False
            image.layers[10].visible = False

        #Cans
        if(monkey.cansAcc):
            image.layers[9].visible = True
            image.active_layer = image.layers[9]
            drawable = image.active_layer
            pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[1])
            pdb.gimp_context_set_pattern(monkey.cansOuterPat)
            pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

            image.layers[8].visible = True
            image.active_layer = image.layers[8]
            drawable = image.active_layer
            pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[0])
            pdb.gimp_context_set_pattern(monkey.cansInnerPat)
            pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)           

            image.layers[7].visible = True

        else:
            image.layers[9].visible = False
            image.layers[8].visible = False
            image.layers[7].visible = False

        #cmdrHat
        if(monkey.cmdrAcc):
            
            image.layers[6].visible = True
            image.active_layer = image.layers[6]
            drawable = image.active_layer
            pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[7])
            pdb.gimp_context_set_pattern(monkey.cmdrOuterPat)
            pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

            pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[6])
            pdb.gimp_context_set_pattern(monkey.cmdrOuterStarPat)
            pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

            pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[5])
            pdb.gimp_context_set_pattern(monkey.cmdrInnerStarPat)
            pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

            image.layers[5].visible = True

        else:
            image.layers[6].visible = False
            image.layers[5].visible = False

        
        if(monkey.duragAcc):
            image.layers[4].visible = True
            image.active_layer = image.layers[4]
            drawable = image.active_layer
            pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[2])
            pdb.gimp_context_set_pattern(monkey.duragPat)
            pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)
        else:
            image.layers[4].visible = False
            image.layers[3].visible = False

        if(monkey.caneAcc):
            image.layers[2].visible = True
            image.active_layer = image.layers[2]
            drawable = image.active_layer
            pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[3])
            pdb.gimp_context_set_pattern(monkey.canePat)
            pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)
        else:
            image.layers[2].visible = False
            image.layers[1].visible = False

        if(monkey.fangsAcc):
            image.layers[0].visible = True
        else:
            image.layers[0].visible = False


        image.active_layer = image.layers[0]
        drawable = image.active_layer

        image.add_layer(pdb.gimp_layer_new_from_visible(image, image, "vis"))

        image.active_layer = image.layers[0]
        drawable = image.active_layer

        pdb.file_png_save(image, drawable, "/home/notes/Programming/Yapeswap/yape-art-generator/Yapes/" + str(monkey.ident) + ".png", str(monkey.ident) + ".png", 0, 0, 0, 0, 0, 1, 1)
        pdb.gimp_image_delete(image)

    else:

        image = pdb.gimp_file_load("/home/notes/Programming/Yapeswap/yape-art-generator/Assets/titus.xcf", "titus.xcf")

        image.active_layer = image.layers[18]
        drawable = image.active_layer
        pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[12])
        pdb.gimp_context_set_pattern(monkey.coinPat)
        pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

        image.active_layer = image.layers[17]
        drawable = image.active_layer
        pdb.gimp_context_set_pattern(monkey.hairPat)
        pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[11])
        pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

        image.active_layer = image.layers[16]
        drawable = image.active_layer
        pdb.gimp_context_set_pattern(monkey.faceEarsPat)
        pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[10])
        pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

        image.active_layer = image.layers[14]
        drawable = image.active_layer
        pdb.gimp_context_set_pattern(monkey.eyeMouthPat)
        pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[8])
        pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)


        #Accessories

        #Shades
        if(monkey.shadesAcc):
            image.layers[10].visible = True
            image.active_layer = image.layers[10]
            drawable = image.active_layer
            pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[2])
            pdb.gimp_context_set_pattern(monkey.shadesPat)
            pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)
            image.layers[9].visible = True
        else:
            image.layers[10].visible = False
            image.layers[9].visible = False

        #Cans
        if(monkey.cansAcc):
            image.layers[8].visible = True
            image.active_layer = image.layers[7]
            drawable = image.active_layer
            pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[0])
            pdb.gimp_context_set_pattern(monkey.cansOuterPat)
            pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

            image.layers[7].visible = True
            image.active_layer = image.layers[8]
            drawable = image.active_layer
            pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[1])
            pdb.gimp_context_set_pattern(monkey.cansInnerPat)
            pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)           

            image.layers[6].visible = True

        else:
            image.layers[8].visible = False
            image.layers[7].visible = False
            image.layers[6].visible = False

        #cmdrHat
        if(monkey.cmdrAcc):
            
            image.layers[5].visible = True
            image.active_layer = image.layers[5]
            drawable = image.active_layer
            pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[7])
            pdb.gimp_context_set_pattern(monkey.cmdrOuterPat)
            pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

            pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[6])
            pdb.gimp_context_set_pattern(monkey.cmdrOuterStarPat)
            pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

            pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[5])
            pdb.gimp_context_set_pattern(monkey.cmdrInnerStarPat)
            pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)

            image.layers[4].visible = True
            image.layers[3].visible = True

        else:
            image.layers[4].visible = False
            image.layers[3].visible = False

        
        if(monkey.duragAcc):
            image.layers[2].visible = True
            image.active_layer = image.layers[2]
            drawable = image.active_layer
            pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[3])
            pdb.gimp_context_set_pattern(monkey.duragPat)
            pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)
            image.layers[1].visible = True
        else:
            image.layers[2].visible = False
            image.layers[1].visible = False

        if(monkey.caneAcc):
            image.layers[12].visible = True
            image.active_layer = image.layers[12]
            drawable = image.active_layer
            pdb.gimp_image_select_item(image,CHANNEL_OP_REPLACE,image.vectors[4])
            pdb.gimp_context_set_pattern(monkey.canePat)
            pdb.gimp_edit_bucket_fill(drawable,2,0,100,0,FALSE,0,0)
            image.layers[11].visible = True
        else:
            image.layers[12].visible = False
            image.layers[11].visible = False

        if(monkey.fangsAcc):
            image.layers[0].visible = True
        else:
            image.layers[0].visible = False

        image.active_layer = image.layers[0]
        drawable = image.active_layer

        image.add_layer(pdb.gimp_layer_new_from_visible(image, image, "vis"))

        image.active_layer = image.layers[0]
        drawable = image.active_layer

        pdb.file_png_save(image, drawable, "/home/notes/Programming/Yapeswap/yape-art-generator/Yapes/" + str(monkey.ident) + ".png", str(monkey.ident) + ".png", 0, 0, 0, 0, 0, 1, 1)
        pdb.gimp_image_delete(image)

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

        with open("/home/notes/Programming/Yapeswap/yape-art-generator/Metadata/" + str(mk.ident) + ".json", "w") as outfile:
            outfile.write(json_object)
        outfile.close()

def yapePlugin(timg, tdrawable):
    loadNames()
    ident = 0
    monkies = []
    #Basically youd loop here to generate all monkeys if theres an error try again with same id
    while(len(monkies) < 10):
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
        tlGen(monkey)
        metadataGenerator(monkey)


register(
    "yapePlugin",
    "Generates Yapes",
    "Generates Yapes",
    "0xSumna",
    "0xSumna",
    "2021",
    "<Image>/Filters/Artistic/YapePlugin",
    "",
    [],
    [],
    yapePlugin)

main()