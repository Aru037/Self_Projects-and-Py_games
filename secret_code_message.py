import random

def encode_word(word):
    if len(word) >= 3:
        r1 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
        r2 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
        return r1 + word[1:] + word[0] + r2
    else:
        return word[::-1]

def decode_word(word):
    if len(word) >= 3:
        stnew = word[3:-3]
        return stnew[-1] + stnew[:-1]
    else:
        return word[::-1]

def main():
    st = input("Enter message: ")
    words = st.split(" ")
    coding = input("1 for Coding or 0 for Decoding: ")
    coding = True if (coding == "1") else False

    nwords = []
    if coding:
        nwords = [encode_word(word) for word in words]
    else:
        nwords = [decode_word(word) for word in words]

    result = " ".join(nwords)
    print(result)

if __name__ == "__main__":
    main()
