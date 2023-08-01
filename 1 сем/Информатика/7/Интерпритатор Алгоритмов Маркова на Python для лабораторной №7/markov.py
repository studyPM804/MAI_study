import string
rules = []
rul_t = open("rules.txt")
k = False
for stri in rul_t:
    i = False
    if stri.count('/*') != 0:
        k = True
        continue
    elif stri.count('*/') != 0:
        k = False
        continue
    elif k == True:
        continue
    elif stri.isspace() == True or stri[0:2] == "//":
        continue
    elif stri.count("//") != 0:
        if stri.count(' //') != 0:
            stri = stri.split(' /')[0].rstrip()
        else:
            stri = stri[:stri.index("//")]
    elif "->." in stri:
        i = True
    l_s = stri.strip(string.whitespace).split("->")
    n1 = l_s[0]
    n2 = l_s[1].strip(".")
    rules.append((n1, n2, i))
strm = input()
while True:
    c = True
    b = False
    for rule in rules:
        ch = strm.find(rule[0])
        if ch == -1:
            continue
        else:
            c = False
            strm = strm[0:ch] + rule[1] + strm[ch+len(rule[0]):]
            print(strm)
            if rule[2]:
                b = True
                break
            else:
                break
    if b or c:
        break