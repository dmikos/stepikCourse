with open("dataset_24465_4.txt", "r") as fin, open("foutput.txt", "w") as fout:
    for line in fin.readlines()[::-1]:
        fout.writelines(line.rstrip() + '\n')
