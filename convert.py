import random
def mocker(str):
    rand = 0.5
    str1 = ""
    for i in range(0,len(str)):
        if (rand>=0.7 or rand < 0.2 ):
            str1 = str1 + str[i].upper()
        else:
            str1 = str1 + str[i].lower()
        # to alternate case instead of random
        #if (rand<0.4):
        #    rand = rand + 1
        #else:
        #    rand = rand - 1
        rand = random.random()

    return str1

s = raw_input (str("Enter any sentence: "))
print (mocker(s))
