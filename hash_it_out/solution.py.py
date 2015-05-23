def answer(digest):
    message=[]
    for i in range(0, len(digest)):
        if i==0:
            j=0
            while (j*256+digest[i] ^ 0) % 129 !=0 and j*256+digest[i]<=256*128:
                j+=1
            message.append((j*256+digest[i] ^ 0) / 129)
        else:
            j=0
            while (j*256+digest[i] ^ message[i-1]) % 129 !=0 and j*256+digest[i]<=256*128:
                j+=1
            message.append((j*256+digest[i] ^ message[i-1]) / 129)
    return message
digest = [0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]
print answer(digest)