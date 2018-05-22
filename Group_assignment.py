
with open ('textfile.txt', 'r+') as text:
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
