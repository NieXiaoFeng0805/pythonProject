#论文词频分析
#You should convert the file to text format

__anthor__ = 'chen hong'

#Read the text and save all the word in a list

def readtxt(filename):
    fr = open(filename , 'r')
    wordsL = [] #use this list to save the words
    for word in fr:
        word = word.strip()
        word = word.split()
        wordsL = wordsL + word
    fr.close()
    return wordsL

#count the frequency of every word and store in a dictionary
#And sort dictionaries by value from large to small

def count(wordsL):
    wordsD = {}
    for x in wordsL:
        #move these words that we dont't need
        if Judge(x):
            continue
        #count
        if not x in wordsD:
            wordsD[x] = 1
        wordsD[x] +=1

    #sort dictionaries by value from large to small
        wordsInorder = sorted(wordsD.items(), key = lambda x:x[1], reverse = True)
        return wordsInorder
#Juege whether the word is that we want to move such as punctuation or letter
#You can modify this function to move more words sc=uch as number

def Judge(word):
    punctList = [' ','\t','n',',','.',':','?']  #judge whether the word is punctuation
    letterList = ['a','b','c','d','m','n','x','p','t']  #judge whether the word is letter
    if word in punctList:
        return True
    elif word in letterList:
        return True
    else:
        return False


#Read the file and output the file
filename = '' #The file's directory
wordsL = readtxt(filename)
words = count(wordsL)
fw = open('')  #The file's directory
for item in words:
    fw.write(item[0] + ' ' + str(item[1]) + '\n')
fw.close()
