def reads_20():
    fin=open('words.txt')
    for line in fin:
        if(len(line.strip())>20):
            return line.strip()
print(reads_20())