print(7+3, 7-3, 7*3, 7/2, 7//2, 7%2, 2**10)
print(-7//2, -7%2, 7//-2, 7%-2, divmod(-7,2))
print(0.1+0.2, 0.1+0.2==0.3, abs((0.1+0.2)-0.3)<1e-9)
print(bin(13), int("1101",2), 13>>1, 13<<2, 13&6, 13|6, 13^6)
print(2+3*4**2, (2+3)*4**2, -2**2, 2**3**2)
print(5>3>1, 5>3>4, not 0, 3 and 0, 3 or 0, [] or "x")
print(10**20+1, 2**100)
print(round(2.5), round(3.5), round(-2.5), int(-2.7), int(2.7))
a=[1,2,3]; b=a; c=a[:]; b.append(4); print(a,c,a is b, a is c)
x=10; y=x; y+=1; print(x,y)
t=(1,[2,3]); t[1].append(4); print(t)
print(sum(range(1,101)), sum(i*i for i in range(1,6)))
def gcd(a,b):
    while b: a,b=b,a%b
    return a
print(gcd(48,18))
print(sorted("banana"), "banana".count("a"), "banana"[::-1], "banana"[1:4])
n=29; print(all(n%i for i in range(2,int(n**0.5)+1)))
def power(b,e):
    if e==0:return 1
    h=power(b,e//2)
    return h*h if e%2==0 else h*h*b
print(power(3,13), 3**13)
print([i for i in range(10) if i%3==0], {i:i*i for i in range(4)}, {x%3 for x in range(10)})
import sys
d={}; 
for w in "to be or not to be".split(): d[w]=d.get(w,0)+1
print(d)
print(1/3, round(1/3,4), 10/4, 10//4, 10%4, 2**-1, 7.0//2)
print(len(str(2**100)), bin(255).count("1"), 255 .bit_length())
