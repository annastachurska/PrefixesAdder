import re
from prefixesList import *

name = input('Enter the name of css file:')
if not name.endswith('.css'): 
    print('It is not a css file.') 
    exit()
try: 
    fhand = open(name, 'r')
except:
    print('There is no', name, 'file in main folder of Python')
    exit()

nameModified = input('Enter the name under which new file will be saved:')
newfile = open(nameModified, 'w')

hasKeyframes = False

for x in fhand:
    listX = x.strip().split(' ')
    featureWord = listX[0].replace(':','')
    for key in prefixes["prefixDictionary"]:
        if len(listX) > 0  and featureWord in prefixes["prefixDictionary"][key]:
            addline = ''
            if not key.startswith('special'):
                addlineWhere = x.find(featureWord)
                addline = x[:addlineWhere] + '-' + key + '-' + x[addlineWhere:]
            elif key == 'specialSimple':
                for key2 in prefixesSpecial["prefixSpecialSimple"]:
                    if x.find(key2)>=0:
                        addline = x
                        addline = addline.replace(key2, prefixesSpecial["prefixSpecialSimple"][key2])
            else: 
                if featureWord == '@keyframes': 
                    hasKeyframes = True
                elif featureWord == 'opacity':
                    addline = x
                    valueR =  'opacity: '  
                    addline = addline.replace(valueR, prefixesSpecial["prefixSpecialComplex"][valueR]).replace(';',');')
                    parts = x.split()
                    try:
                        valueOpacity = parts[1].replace(';','')
                        valueO = float(valueOpacity)
                        addline = addline.replace(valueOpacity, str(100*valueO))
                    except:
                        print('Wrong syntax, the opacity value was not converted properly')
            newfile.write(addline)
    newfile.write(x)
newfile.close()

if hasKeyframes == True:
    newfile = open(nameModified, 'r+')
    textModified = newfile.read()
    keyframesPositions = re.finditer('@keyframes', textModified)
    listOfPositions = list()
    for match in keyframesPositions:
        listOfPositions.append(match.start())
    listOfPositions.sort(reverse=True)
    for position in listOfPositions:
        findEnd = textModified.find('}', position)
        basicFragment = textModified[position+11:findEnd+1]
        nr1 = len(re.findall('{', basicFragment))
        nr2 = len(re.findall('}', basicFragment))
        while nr1 != nr2:
            if len(re.findall('{',textModified)) != len(re.findall('}',textModified)):
                print('The number of { and } signs in your document do not match. Please correct it.')
                exit()
            findEnd = textModified.find('}', findEnd+1)
            basicFragment = textModified[position+11:findEnd+1]
            nr1 = len(re.findall('{', basicFragment))
            nr2 = len(re.findall('}', basicFragment))
        toInclude = '@-webkit-keyframes '+basicFragment+'\n'+'@-moz-keyframes '+basicFragment+'\n'+'@-o-keyframes '+basicFragment+'\n'
        firstPart = textModified[:position]
        secondPart = textModified[position:]
        textModified = firstPart + toInclude + secondPart
    newfile.close()     
    newfile = open(nameModified, 'w')
    newfile.write(textModified)
    newfile.close()
  
