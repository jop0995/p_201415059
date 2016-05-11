score=[["English",100,"Math",200],["English",200,"Math",200],
           ["English",100,"Math",300]]
eSum=0
mSum=0
for i in score:
    eSum=i[1]+eSum
    mSum=i[3]+mSum
eAver=eSum/len(score)
mAver=mSum/len(score)
print eAver, mAver