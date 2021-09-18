x = int(input())
for i in range(0,x):
    if x==i*i:
        flag = True
        break
    else:
        flag = False
if flag == True:
    print("Dung")
else:
    print("Sai")