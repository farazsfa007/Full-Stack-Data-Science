def encryption(message, k):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    r = 0
    temp = 0
    out = ""
    for itr in range(len(message)):
        r = alpha.index(message[itr])
        temp = (r+k) % 26
        out = out + alpha[temp]
    return out


def decryption(message, k):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    idx = 0
    temp = 0
    out = ""
    for itr in range(len(message)):
        idx = alpha.index(message[itr])
        temp = (idx-k+26) % 26
        out = out + alpha[temp]
    return out

message = input("Enter your message to encrypt : ")
k = int(input("Enter the value of key : "))
cipher_text = encryption(message, k)
print("Encrypted message : " + cipher_text)
plain_text = decryption(cipher_text, k)
print("Decrypted message : " + plain_text)