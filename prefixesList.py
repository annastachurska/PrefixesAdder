prefixes = {
    'prefixDictionary': {
        'webkit': ['align-content', 'align-items', 'align-self', 'animation', 'animation-delay', 'animation-direction', 'animation-duration', 'animation-fill-mode', 'animation-iteration-count', 'animation-name', 'animation-play-state', 'animation-timing-function', 'backface-visibility', 'background-size', 'border-bottom-left-radius', 'border-bottom-right-radius', 'border-image', 'border-radius', 'border-top-left-radius', 'border-top-right-radius', 'box-decoration-break', 'box-shadow', 'box-sizing', 'column-count', 'column-fill', 'column-gap', 'column-rule', 'column-rule-color', 'column-rule-style', 'column-span', 'column-rule-width', 'columns', 'filter', 'flex', 'flex-basis', 'flex-direction', 'flex-flow', 'flex-grow', 'flex-shrink', 'flex-wrap', 'font-kerning', 'hyphens', 'justify-content', 'order', 'perspective', 'perspective-origin', 'text-decoration-color', 'text-decoration-line', 'transform', 'transform(2D)', 'transform(3D)', 'transform-origin', 'transition', 'transition-delay', 'transition-duration', 'transition-property', 'transition-timing-function', 'user-select'],
        'ms': ['flex', 'hyphens', 'overflow-x', 'overflow-y', 'transform', 'transform(2D)', 'transform-origin', 'transform-style', 'user-select'],
        'moz': ['animation', 'animation-delay', 'animation-direction', 'animation-duration', 'animation-fill-mode', 'animation-iteration-count', 'animation-name', 'animation-play-state', 'animation-timing-function', 'backface-visibility', 'background-size', 'border-bottom-left-radius', 'border-bottom-right-radius', 'border-image', 'border-radius', 'border-top-left-radius', 'border-top-right-radius', 'box-shadow', 'box-sizing', 'column-count', 'column-fill', 'column-gap', 'column-rule', 'column-rule-color', 'column-rule-style', 'column-rule-width', 'columns', 'flex', 'flex-basis', 'flex-direction', 'flex-flow', 'flex-grow', 'flex-shrink', 'flex-wrap', 'justify-content', 'order', 'perspective', 'perspective-origin', 'resize', 'tab-size', 'text-align-last', 'text-decoration-color', 'text-decoration-line', 'text-decoration-style', 'transform', 'transform(2D)', 'transform-origin', 'transform-style', 'transition', 'transition-delay', 'transition-duration', 'transition-property', 'transition-timing-function', 'user-select'],
        'o': ['animation', 'animation-delay', 'animation-direction', 'animation-duration', 'animation-fill-mode', 'animation-iteration-count', 'animation-name', 'animation-play-state', 'animation-timing-function', 'background-size', 'border-image', 'tab-size', 'text-overflow', 'transform', 'transform(2D)', 'transform-origin', 'transition', 'transition-delay', 'transition-duration', 'transition-property', 'transition-timing-function'],
        'specialSimple': ['position', 'display'],
        'specialComplex': ['opacity', '@keyframes']
        }
    }

prefixesSpecial = {
    'prefixSpecialSimple': {
        'position: sticky;': 'position: -webkit-sticky;', 
        'display: flex;': 'display: -webkit-flex;', 
        'display: inline-flex;': 'display: -webkit-inline-flex;'
        },
    'prefixSpecialComplex': {
        'opacity: ': 'filter: alpha(opacity='
        }
    }    