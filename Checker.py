#!/usr/bin/python3
# Mock Inputs
a=[2,2,4,5,6,7,8,9,1]
b=[1,2,3,4,5,6,7,8,9]
c=[1,2,4,5,4,5,6,6,8]
d=[1,3,4,6,5,7,9,8,1]
e=[3,4,5,6,7,8,9,2,1]
f=[1,3,5,7,8,9,6,7,3]
g=[1,2,4,5,6,6,7,7,8]
h=[1,2,3,5,6,7,8,9,3]
z=[1,3,4,5,6,7,8,9,1]
#Comparing row elements
print("Checking for duplicate entries in row elements")
for i in a:
    if a.count(i)>1:
     print("Error in Puzzle,duplicate value at row a "+"is " +str(i))
for j in b:
    if b.count(j)>1:
     print("Error in Puzzle,duplicate value at row b "+"is " +str(j))
for k in c:
    if c.count(k)>1:
     print("Error in Puzzle,duplicate value at row c "+"is " +str(k))
for l in d:
    if d.count(l)>1:
     print("Error in Puzzle,duplicate value at row d "+"is " +str(l))
for m in e:
    if e.count(m)>1:
     print("Error in Puzzle,duplicate value at row e "+"is " +str(m))
for n in f:
    if f.count(n)>1:
     print("Error in Puzzle,duplicate value at row f "+"is " +str(n))
for o in g:
    if g.count(o)>1:
     print("Error in Puzzle,duplicate value at row g "+"is " +str(o))
for p in h:
    if h.count(p)>1:
     print("Error in Puzzle,duplicate value at row h "+"is " +str(p))
for q in z:
    if z.count(q)>1:
     print("Error in Puzzle,duplicate value at row z "+"is " +str(q))
#Comparing column elements
print("Checking for duplicate entries in column elements")
for i in range(len(a)):
    if a[i]==b[i] or a[i]==c[i] or a[i]==d[i] or a[i]==e[i] or a[i]==f[i] or a[i]==g[i] or a[i]==h[i] or a[i]==z[i]:
        print("Error in Puzzle,duplicate value at column number "+str(i+1)+" is "+ str(a[i]))
    if b[i]==c[i] or b[i]==d[i] or b[i]==e[i] or b[i]==f[i] or b[i]==g[i] or b[i]==h[i] or b[i]==z[i]:
        print("Error in Puzzle,duplicate value at column number "+str(i+1)+" is "+ str(b[i]))
    if c[i]==d[i] or c[i]==e[i] or c[i]==f[i] or c[i]==g[i] or c[i]==h[i] or c[i]==z[i]:
        print("Error in Puzzle,duplicate value at column number "+str(i+1)+" is "+ str(c[i]))
    if d[i]==e[i] or d[i]==f[i] or d[i]==g[i] or d[i]==h[i] or d[i]==z[i]:
        print("Error in Puzzle,duplicate value at column number "+str(i+1)+" is "+ str(d[i]))
    if e[i]==f[i] or e[i]==g[i] or e[i]==h[i] or e[i]==z[i]:
        print("Error in Puzzle,duplicate value at column number "+str(i+1)+" is "+ str(e[i]))
    if f[i]==g[i] or f[i]==h[i] or f[i]==z[i]:
        print("Error in Puzzle,duplicate value at column number "+str(i+1)+" is "+ str(f[i]))
    if g[i]==h[i] or g[i]==z[i]:
        print("Error in Puzzle,duplicate value at column number "+str(i+1)+" is "+ str(g[i]))
    if h[i]==z[i]:
        print("Error in Puzzle,duplicate value at column number "+str(i+1)+" is "+ str(h[i]))

print('\n'"************Check the console for duplicates*****************")
print("No duplicates found?Perfect Puzzle!!\nElse,you have submitted an Incorrect one, try again..")
