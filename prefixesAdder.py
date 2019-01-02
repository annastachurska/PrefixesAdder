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

newfile = open('modified.css', 'w')
name = 'style.css'
hasKeyframes = False

try: 
    fhand = open(name, 'r')
except:
    print 'There is no file style in selected localization'
    exit()

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
    newfile = open('modified.css', 'r+')
    textModified = newfile.read()
    print 'write', textModified[:10]
    shallRepeat = True
    startsAtKF = 0
    keyFramesPrefixes = ['@-webkit-keyframes', '@-moz-keyframes', '@-o-keyframes'] 
    while shallRepeat:
        shallRepeat = False    
        keyframesPosition = textModified.find('@keyframes',startsAtKF)
        print keyframesPosition
        if keyframesPosition >= 0:
            shallRepeat = True
            startsAtKF = keyframesPosition+1
            print 'startsAtKF', startsAtKF
            findEnd = textModified.find('}',startsAtKF)
            print 'end', findEnd
            toInclude = '@-webkit-keyframes'+textModified[startsAtKF+10:findEnd+1]+'\n'+'@-moz-keyframes'+textModified[startsAtKF+10:findEnd+1]+'\n'+'@-webkit-keyframes'+textModified[startsAtKF+10:findEnd+1]
            print toInclude
            textModified = textModified[:keyframesPosition]+toInclude+textModified[findEnd+1:]         
    newfile.close()





 

    





  



    




