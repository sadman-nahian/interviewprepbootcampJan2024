def isAnagramByCount(s, t):
    if not len(s) == len(t):
        return False
    for i in s:
        if(not s.count(i)== t.count(i)):
            False
    return True
def isAnagramByMap(s, t):
    if(len(s)!=len(t)):
        return False
    countS,countT={},{}
    for i in range(len(s)):
        countS[s[i]]=1+countS.get(s[i],0)
        countT[t[i]]=1+countT.get(t[i],0)
    for j in countS:
        if countS[j]!=countT.get(j,0):
            return False
    return True

def isAnagram(s,t):
    if(len(s)!=len(t)):
        return False
    countS,countT={},{}
    for i in range(len(s)):
        if s[i] in countS:
            countS[s[i]]=1+countS[s[i]]
        else:
            countS[s[i]]=1

        if t[i] in countT:
            countT[t[i]]=1+countT[t[i]]
        else:
            countT[t[i]]=1

    return countS==countT

print(isAnagramByCount("head","deah"))        
print(isAnagramByMap("head","deah")) 
print(isAnagram("head","deah"))        