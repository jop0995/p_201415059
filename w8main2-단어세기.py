word='hongjimoon2gil20'
words=word.split()
d=dict()
wcount=0
ncount=0
for c in word:
        if c not in d:
            d[c]=1
            print d
        else:
            d[c]=d[c]+1
for c in d:
    if c.isdigit()and d[c]==1:
        ncount=ncount+1
    elif c.isdigit()and d[c]==2:
        ncount=ncount+2    
    elif c.isalpha()and d[c]==1:
        wcount=wcount+1
    elif c.isalpha()and d[c]==2:
        wcount=wcount+2
    elif c.isalpha()and d[c]==3:
        wcount=wcount+3
    else:
        wcount=wcount
        ncount=ncount
print wcount
print ncount
input()