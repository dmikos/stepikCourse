with open("finput.txt", "r") as fin, open("foutput.txt", "w") as fout:
    for line in fin:
        print(line.rstrip())
        fout.write(line)
