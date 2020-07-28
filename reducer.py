import sys#sys.argv[i]
import subprocess
import itertools

readf = open(sys.argv[1], "r")
ori_line = len(readf.readlines())
print("ORIGINAL FILE SIZE IS ", ori_line)
parse = []
readf.seek(0)
for i in range(ori_line):
        parse.append(readf.readline())
readf.close()

divide_time = 2
group = []
group_len = divide_time
while(divide_time <= ori_line):
    line = len(parse)
    for i in range(group_len):#generation groups
        srt = int( i + i*int(line/group_len))
        end = int( (i+1) + (i+1)*int(line/group_len))
        if(end > (line-1)):
            end = line
        group.append(parse[srt : end])
    for i in range(group_len):
        f = open(sys.argv[1],"w")
        f.write(''.join(group[i]))
        f.close()
        check = subprocess.call(['bash',sys.argv[2]])
        if(check == 0):#other don't need
            parse = group[i]
            parse = sum(parse,[])
            print("Delete only the ",i,"-th group...\n")
            break
        else:
            if((i == group_len-1) and (group_len > 2)):
                j = 0
                for _ in range(group_len):
                    part = group[:]
                    part.pop(j)
                    part = sum(part,[])
                    f=open(sys.argv[1],"w")
                    f.write(''.join(part))
                    f.close()
                    check = subprocess.call(['bash',sys.argv[2]])
                    if(check == 0):

                        rem = group.pop(j)
                        parse= group[:]
                        parse = sum(parse,[])
                        print("Delete",j,"group...\n")
                    else:
                        j +=1
    if((ori_line != divide_time) and (divide_time * 2 > ori_line)):
        divide_time = ori_line
        group_len = ori_line
    else:
        divide_time = divide_time*2
        group_len = len(group)*2
    group = []
print("===========================================")
print("                Report                     ")
print("===========================================")
print("original file's Total # of lines : ",ori_line);
print("reduced file's Total # of lines : ",len(parse));
