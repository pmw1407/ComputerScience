from numpy import dot
from numpy.linalg import norm
import numpy as np
import os

def cos_sim(A, B):
    return dot(A, B) / (norm(A) * norm(B))

good_path = "./opcode/0"
mal_path = "./opcode/1"
good_file_list = os.listdir(good_path)
mal_file_list = os.listdir(mal_path)
#print("file_list: {}".format(good_file_list))
#print(len(good_file_list))
#print(len(mal_file_list))

file_dir = "opcode\\"

is_malware = "1\\"
is_goodware = "0\\"
malware = ['kernel_rk', 'user_rk', 'tools', 'bot', 'trojan', 'virus', 'worms']
opcodes = ['mov\n', 'push\n', 'call\n', 'pop\n', 'cmp\n', 'jz\n', 'lea\n', 
        'test\n', 'jmp\n', 'add\n', 'jnz\n', 'retn\n', 'xor\n', 'and\n']

goodware = [253, 195, 87, 63, 51, 43, 39, 32, 30, 30, 26, 22, 19, 13]
kernel_rk = [370, 156, 55, 27, 64, 33, 18, 18, 41, 58, 37, 17, 11, 15]
user_rk = [290, 166, 89, 51, 49, 39, 33, 32, 38, 37, 31, 23, 23, 10]
tools = [254, 190, 82, 59, 53, 43, 31, 37, 34, 34, 34, 29, 21, 13]
bot = [346, 141, 110, 68, 36, 33, 26, 26, 30, 25, 22, 30, 32, 5]
trojan = [305, 154, 100 ,73, 36, 35, 27, 34, 34, 30, 26, 32, 27, 6]
virus = [161, 227, 91, 70, 59, 44, 55, 31, 27, 35, 32, 20, 21, 15]
worms = [222, 207, 87, 62, 50 ,40, 42, 30 ,45, 30 ,32, 23, 23, 16]

mware = []

mware.append(kernel_rk)
mware.append(user_rk)
mware.append(tools)
mware.append(bot)
mware.append(trojan)
mware.append(virus)
mware.append(worms)

sample_size = 100

opcode_freq = []
good_hit_rate = 0

#goodware
for j in range(sample_size):
    #print(good_file_list[j])
    f = open(file_dir + is_goodware + good_file_list[j], mode = 'rt')
    idx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in f:
        for i in range(len(opcodes)):
            if opcodes[i] == line:
                idx[i] += 1
    sim = cos_sim(goodware, idx)
    max_sim = sim
    print("goodware similarity : ", sim)
    most_sim = 0

    for i in range(7):
        temp = cos_sim(mware[i], idx)
        if max_sim < temp:
            max_sim = temp
            most_sim = i + 1
        print(malware[i] + " similarity : ", cos_sim(mware[i], idx))

    if most_sim == 0:
        good_hit_rate += 1
        print("most similar model : goodware")
        print()
    else:
        print("most similar model : " + malware[most_sim - 1])
        print()

    #opcode_freq.append(idx)
    f.close()

print("accuracy : ", good_hit_rate / sample_size * 100, "%")
print()

'''
mal_hit_rate = 0
#malware
for j in range(sample_size):

    #print(good_file_list[j])
    f = open(file_dir + is_malware + mal_file_list[j], mode = 'rt')
    idx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in f:
        for i in range(len(opcodes)):
            if opcodes[i] == line:
                idx[i] += 1
    sim = cos_sim(goodware, idx)
    max_sim = sim
    print("goodware similarity : ", sim)
    most_sim = 0

    for i in range(7):
        temp = cos_sim(mware[i], idx)
        if max_sim < temp:
            max_sim = temp
            most_sim = i + 1
        print(malware[i] + " similarity : ", cos_sim(mware[i], idx))

    if most_sim == 0:
        print("most similar model : goodware")
        print()
    else:
        mal_hit_rate += 1
        print("most similar model : " + malware[most_sim - 1])
        print()

    opcode_freq.append(idx)
    f.close()

print("accuracy : ", mal_hit_rate / sample_size * 100, "%")
print()
'''