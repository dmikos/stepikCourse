import os

# print(os.getcwd())
os.chdir("main")
# print(os.getcwd())
res = set()
for cur_dir, dirs, files in os.walk("."):
    # print(cur_dir, dirs, files)
    for f in files:
        if ".py" in f:
            # print('sample' + cur_dir[1:])
            res.add('main' + cur_dir[1:] + '\n')
print(res)
res = list(res)
res.sort()
print(res)
with open("../24465-step6.txt", 'w') as fout:
    for line in res:
        fout.write(line)
