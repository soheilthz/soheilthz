# change base of a number
def decimal(adad,mf):
    total=0
    num=0
    i=0
    mfb=mf

    for char in adad:  
        mf**=pro[i]
        num=mf*adad[i]
        total+=num
        i+=1
        mf=mfb
    return total
def change(deci,mb):
    x=deci
    l=[]
    while True:
        l.append(x%mb)
        x//=mb
        if x<mb:
            l.append(x)
            break
    l=l[-1::-1]
    return l

pro=[0,1,2,3,4,5,6,7,8,9,10,11,12]
ada=list(input())
adad=[]
for c in ada:
    adad.append(int(c))
adad=adad[-1::-1]
mf=int(input())
mb=int(input())
deci=decimal(adad,mf)
final=change(deci,mb)

minal=final[-1::-1]

if final==minal:
    print("YES")
else:
    print("NO")



