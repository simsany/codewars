def validBraces(a):
    
    while True:
        
        if '()' in a:
            i=a.index('()')
        elif '[]' in a:
            i=a.index('[]')
        elif '{}' in a:
            i=a.index('{}')
        else:
            if a:
                return False
            else:
                return True
        a=a[:i]+a[i+2:] 
        