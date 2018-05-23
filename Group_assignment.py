#this program is to remove punctuations and add the word count
with open ('new_file.txt', 'r+') as text:
    text_read = text.read().lower().strip()
    word_read = text_read.split()

    wordcount = {}
    for word in word_read:
        if word.isalpha():
            
            if word not in wordcount:
                wordcount[word] = 1
            else: 
                wordcount[word] += 1

    for key,count in wordcount.items():
        print("%s: %d" %(key, count))
