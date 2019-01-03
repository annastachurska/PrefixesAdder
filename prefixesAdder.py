import re

prefixDictionary = {
    'webkit': ['align-content', 'align-items', 'align-self', 'animation', 'animation-delay', 'animation-direction', 'animation-duration', 'animation-fill-mode', 'animation-iteration-count', 'animation-name', 'animation-play-state', 'animation-timing-function', 'backface-visibility', 'background-size', 'border-bottom-left-radius', 'border-bottom-right-radius', 'border-image', 'border-radius', 'border-top-left-radius', 'border-top-right-radius', 'box-decoration-break', 'box-shadow', 'box-sizing', 'column-count', 'column-fill', 'column-gap', 'column-rule', 'column-rule-color', 'column-rule-style', 'column-span', 'column-rule-width', 'columns', 'filter', 'flex', 'flex-basis', 'flex-direction', 'flex-flow', 'flex-grow', 'flex-shrink', 'flex-wrap', 'font-kerning', 'hyphens', 'justify-content', 'order', 'perspective', 'perspective-origin', 'text-decoration-color', 'text-decoration-line', 'transform', 'transform(2D)', 'transform(3D)', 'transform-origin', 'transition', 'transition-delay', 'transition-duration', 'transition-property', 'transition-timing-function', 'user-select'],
    'ms': ['flex', 'hyphens', 'overflow-x', 'overflow-y', 'transform', 'transform(2D)', 'transform-origin', 'transform-style', 'user-select'],
    'moz': ['animation', 'animation-delay', 'animation-direction', 'animation-duration', 'animation-fill-mode', 'animation-iteration-count', 'animation-name', 'animation-play-state', 'animation-timing-function', 'backface-visibility', 'background-size', 'border-bottom-left-radius', 'border-bottom-right-radius', 'border-image', 'border-radius', 'border-top-left-radius', 'border-top-right-radius', 'box-shadow', 'box-sizing', 'column-count', 'column-fill', 'column-gap', 'column-rule', 'column-rule-color', 'column-rule-style', 'column-rule-width', 'columns', 'flex', 'flex-basis', 'flex-direction', 'flex-flow', 'flex-grow', 'flex-shrink', 'flex-wrap', 'justify-content', 'order', 'perspective', 'perspective-origin', 'resize', 'tab-size', 'text-align-last', 'text-decoration-color', 'text-decoration-line', 'text-decoration-style', 'transform', 'transform(2D)', 'transform-origin', 'transform-style', 'transition', 'transition-delay', 'transition-duration', 'transition-property', 'transition-timing-function', 'user-select'],
    'o': ['animation', 'animation-delay', 'animation-direction', 'animation-duration', 'animation-fill-mode', 'animation-iteration-count', 'animation-name', 'animation-play-state', 'animation-timing-function', 'background-size', 'border-image', 'tab-size', 'text-overflow', 'transform', 'transform(2D)', 'transform-origin', 'transition', 'transition-delay', 'transition-duration', 'transition-property', 'transition-timing-function'],
    'specialSimple': ['position', 'display'],
    'specialComplex': ['opacity', '@keyframes']
    }

prefixSpecialSimple = {
    'position: sticky;': 'position: -webkit-sticky;', 
    'display: flex;': 'display: -webkit-flex;', 
    'display: inline-flex;': 'display: -webkit-inline-flex;'
}

prefixSpecialComplex = {
    'opacity: ': 'filter: alpha(opacity='
}

name = raw_input('Enter the name of css file:')
if not name.endswith('.css'): 
    print 'It is not a css file.' 
    exit()
try: 
    fhand = open(name, 'r')
except:
    print 'There is no', name, 'file in main folder of Python'
    exit()

nameModified = raw_input('Enter the name under which new file will be saved:')
newfile = open(nameModified, 'w')

hasKeyframes = False

for x in fhand:
    listX = x.strip().split(' ')
    featureWord = listX[0].replace(':','')
    for key in prefixDictionary:
        if len(listX) > 0  and featureWord in prefixDictionary[key]:
            addline = ''
            if not key.startswith('special'):
                addlineWhere = x.find(featureWord)
                addline = x[:addlineWhere] + '-' + key + '-' + x[addlineWhere:]
            elif key == 'specialSimple':
                for key2 in prefixSpecialSimple:
                    if x.find(key2)>=0:
                        addline = x
                        addline = addline.replace(key2, prefixSpecialSimple[key2])
            else: 
                if featureWord == '@keyframes': 
                    hasKeyframes = True
                elif featureWord == 'opacity':
                    addline = x
                    valueR =  'opacity: '  
                    addline = addline.replace(valueR, prefixSpecialComplex[valueR]).replace(';',');')
                    parts = x.split()
                    try:
                        valueOpacity = parts[1].replace(';','')
                        valueO = float(valueOpacity)
                        addline = addline.replace(valueOpacity, str(100*valueO))
                    except:
                        print 'Wrong syntax, the opacity value was not converted properly'
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
                print 'The number of { and } signs in your document do not match. Please correct it.'
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
  
