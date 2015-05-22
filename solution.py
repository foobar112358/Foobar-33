def answer(document, searchTerms):
    from collections import deque
    docQ=deque(document.split(' '))
    while docQ[0] not in searchTerms:
        docQ.popleft()
    while docQ[-1] not in searchTerms:
        docQ.pop()
    shortest=''
    while len(docQ)>=len(searchTerms):
        notfound=set(searchTerms)
        temp=[]
        while notfound and docQ:
            x = docQ.popleft()
            if x in notfound:
                notfound.remove(x)
            temp.append(x)
        print temp
        if not notfound:
	        if not shortest:
	            shortest=" ".join(temp)
	        else:
	            s=" ".join(temp)
	            if len(s)<len(shortest):
	                shortest=s
        temp.reverse()
        docQ.extendleft(temp)
        docQ.popleft()
        while docQ[0] not in searchTerms:
        	docQ.popleft()
    return shortest
document = "many google employees can program"
searchTerms = ["google", "program"]
print answer(document, searchTerms)
