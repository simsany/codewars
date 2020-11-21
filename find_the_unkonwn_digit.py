import re


def decide(list):
    for num_str in list:
        if len(str(int(num_str))) < len(num_str):
            return True


def solve_runes(a):
    b = re.findall(r"[\d']+", a.replace('?', '0'))
    if decide(b):
        for i in range(1, 10):
            if eval(a[:a.index("=")].replace("?", str(i))) == int(a[a.index("=")+1:].replace("?", str(i))) and str(i) not in a:
                return i
            
        return -1
    else:
        for i in range(10):
            if eval(a[:a.index("=")].replace("?", str(i))) == int(a[a.index("=")+1:].replace("?", str(i))) and str(i) not in a:
                return i
            
        return -1
        