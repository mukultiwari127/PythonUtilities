# Banana Vowels and Consonents

def minion_game(string):
    vowels = ["A", "E", "I", "O", "U"]
    count_kevin = 0
    count_stuart = 0
    for i in range(0, len(string)):
        if string[i] in vowels:
            count_kevin = count_kevin + (len(string)-i)
        else:
            count_stuart = count_stuart + (len(string)-i)
    if(count_kevin>count_stuart):
        print("Kevin {}".format(count_kevin))
    elif(count_kevin<count_stuart):
        print("Stuart {}".format(count_stuart))
    elif(count_kevin==count_stuart):
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)