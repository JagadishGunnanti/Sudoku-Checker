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
#Comparing list elements in a row
print("Checking for matches in row elements")
for i in a:
    if a.count(i)>1:
     print("Error in Puzzle,duplicate values at row:a")
     print(i)
     break;
for j in b:
    if b.count(j)>1:
     print("Error in Puzzle,duplicate values at row:b")
     print(j)
     break;
for k in c:
    if c.count(k)>1:
     print("Error in Puzzle,duplicate values at row:c")
     print(k)
     break;
for l in d:
    if d.count(l)>1:
     print("Error in Puzzle,duplicate values at row:d")
     print(l)
     break;
for m in e:
    if e.count(m)>1:
     print("Error in Puzzle,duplicate values at row:e")
     print(m)
     break;
for n in f:
    if f.count(n)>1:
     print("Error in Puzzle,duplicate values at row:f")
     print(n)
     break;
for o in g:
    if g.count(o)>1:
     print("Error in Puzzle,duplicate values at row:g")
     print(o)
     break;
for p in h:
    if h.count(p)>1:
     print("Error in Puzzle,duplicate values at row:h")
     print(p)
     break;
for q in z:
    if z.count(q)>1:
     print("Error in Puzzle,duplicate values at row:z")
     print(q)
     break;
#Comparing 'a' list elements with next list elements
print("Checking for matches in column elements")
for i in a:
    for j in b:
        if i==j and a.index(i)==b.index(j):
            print("matches found")
            print(i,j)
            break;
    for k in c:    
        if (i==k) and (a.index(i)==c.index(k)):
            print("matches found")
            print(i,k)
            break;
    for l in d:
        if (i==l) and (a.index(i)==d.index(l)):
            print("matches found")
            print(i,l)
            break;  
    for m in e:
        if (i==m) and (a.index(i)==e.index(m)):
            print("matches found")
            print(i,m)
            break;
    for n in f:
        if (i==n) and (a.index(i)==f.index(n)):
            print("matches found")
            print(i,n)
            break;
    for o in g:
        if (i==o) and (a.index(i)==g.index(o)):
            print("matches found")
            print(i,o)
            break;
    for p in h:
        if (i==p) and (a.index(i)==h.index(p)):
            print("matches found")
            print(i,p)
            break;
    for q in z:
        if (i==q) and (a.index(i)==z.index(q)):
            print("matches found")
            print(i,q)
            break;
#Comparing 'b' list elements with next list elements        
for j in b:
    for k in c:
        if (j==k) and (b.index(j)==c.index(k)):
            print("matches found")
            print(j,k)
            break;
    for l in d:
        if (j==l) and (b.index(j)==d.index(l)):
            print("matches found")
            print(j,l)
            break;
    for m in e:
        if (j==m) and (b.index(j)==e.index(m)):
            print("matches found")
            print(j,m)
            break;
    for n in f:
        if (j==n) and (b.index(j)==f.index(n)):
            print("matches found")
            print(j,n)
            break;
    for o in g:
        if (j==o) and (b.index(j)==g.index(o)):
            print("matches found")
            print(j,o)
            break;
    for p in h:
        if (j==p) and (b.index(j)==h.index(p)):
            print("matches found")
            print(j,p)
            break;
    for q in z:
        if (j==q) and (b.index(j)==z.index(q)):
            print("matches found")
            print(j,q)
            break;
#Comparing 'c' list elements with next list elements        
for k in c:
    for l in d:
        if (k==l) and (c.index(k)==d.index(l)):
            print("matches found")
            print(k,l)
            break;
    for m in e:
        if (k==m) and (c.index(k)==e.index(m)):
            print("matches found")
            print(k,m)
            break;
    for n in f:
        if (k==n) and (c.index(k)==f.index(n)):
            print("matches found")
            print(k,n)
            break;
    for o in g:
        if (k==o) and (c.index(k)==g.index(o)):
            print("matches found")
            print(k,o)
            break;
    for p in h:
        if (k==p) and (c.index(k)==h.index(p)):
            print("matches found")
            print(k,p)
            break;
    for q in z:
        if (k==q) and (c.index(k)==z.index(q)):
            print("matches found")
            print(k,q)
            break;
#Comparing 'd' list elements with next list elements 
for l in d:
    for m in e:
        if(l==m) and (d.index(l)==e.index(m)):
            print("matches found")
            print(l,m)
            break;
    for n in f:
        if(l==n) and (d.index(l)==f.index(n)):
            print("matches found")
            print(l,n)
            break;
    for o in g:
        if(l==o) and (d.index(l)==g.index(o)):
            print("matches found")
            print(l,o)
            break;
    for p in h:
        if(l==p) and (d.index(l)==h.index(p)):
            print("matches found")
            print(l,p)
            break;
    for q in z:
        if(l==q) and (d.index(l)==z.index(q)):
            print("matches found")
            print(l,q)
            break;
#Comparing 'e' list elements with next list elements
for m in e:
    for n in f:
        if(m==n) and (e.index(m)==f.index(n)):
            print("matches found")
            print(m,n)
            break;
    for o in g:
        if(m==o) and (e.index(m)==g.index(o)):
            print("matches found")
            print(m,o)
            break;
    for p in h:
        if(m==o) and (e.index(m)==h.index(p)):
            print("matches found")
            print(m,p)
            break;
    for q in z:
        if(m==q) and (e.index(m)==z.index(q)):
            print("matches found")
            print(m,q)
            break;
#Comparing 'f' list elements with next list elements
for n in f:
    for o in g:
        if(n==o) and (f.index(n)==g.index(o)):
         print("matches found")
         print(n,o)
         break;
    for p in h:
        if(n==p) and (f.index(n)==h.index(p)):
         print("matches found")
         print(n,p)
         break;
    for q in z:
        if(n==q) and (f.index(n)==z.index(q)):
         print("matches found")
         print(n,q)
         break;
#Comparing 'g' list elements with next list elements
for o in g:
    for p in h:
        if(o==p) and (g.index(o)==h.index(p)):
            print("matches found")
            print(o,p)
            break;
    for q in z:
            if(o==q) and (g.index(o)==z.index(q)):
                print("matches found")
                print(o,q)
                break;
#Comparing 'h' list elements with next list elements            
for p in h:
    for q in z:
        if(p==q) and (h.index(p)==z.index(q)):
            print("matches found")
            print(p,q)
            break;
