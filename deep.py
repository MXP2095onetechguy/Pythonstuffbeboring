import random
import winsound



on = 1
count = 0
de = [500, 1000, 2000, 600, 1500, 1900, 525, random.randint(500, 2000), random.randint(500, 2000)]



print("DEEEPP")
print("------------------------------------------")
print("number of item inside list: 9")
print("from index 0 to 8")
print("list content:")
print(de)
print("------------------------------------------")

while on > 0:
    count += 1
    random.shuffle(de)
    pik = random.randint(0, 7)
    beep = random.randint(500, 1000)
    print("count: " + str(count))
    print("list: ")
    print(de)
    print("delay: " + str(de[pik])+" index number: "+str(pik)+" win.beep pitch: "+str(beep))
    print("------------------------------------------")
    winsound.Beep( beep , de[pik])
