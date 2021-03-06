f  = open("input.txt","r")
x = int(f.readline().split(': ')[1])
# read x
x=int(input())
y = f.readline()
y = f.readline()
y = f.readline()

lines = f.readlines()
f.close()
goodies = {}
price_arr= []
for line in lines:
    val = line.split(': ')
    goodies[val[0]]=int(val[1].split('\n')[0])
    price_arr.append(int(val[1].split('\n')[0]))


ans = {k: v for k, v in sorted(goodies.items(), key=lambda item: item[1])}

output = open("output.txt","w")

output.write("The goodies selected for distribution are: \n\n")

price_arr.sort()
min_val = 100000000
ind = 0 
# calculating minimum value
for i in range(len(price_arr)-x):
    if (price_arr[i+x-1]-price_arr[i]) < min_val:
        min_val = price_arr[i+x-1]-price_arr[i]
        ind = i

flag=0
first=0
for i in ans:
    if ind<=first:
        output.write(i + ": " + str(ans[i]) + "\n")
        x-=1
    
    first+=1
    if x==0:
        break
        #print the output
output.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is "+ str(min_val))
output.close()