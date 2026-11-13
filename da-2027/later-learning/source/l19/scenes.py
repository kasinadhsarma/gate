from lhelp import *
import codes
def d_sieve(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L19A),(4,L19B)],30,150,690,15,20)
    pr={2,3,5,7,11,13,17,19,23,29}
    if ts[2]<=t<ts[4]:
        lab(d,1000,172,"1 .. 30  (primes stay)",WHITE,15)
        for n in range(1,31):
            r,c=divmod(n-1,6);x=830+c*56;y=195+r*50;k=(t-ts[2])
            gone=(n>1 and n not in pr and k>3+ (n%7)*0.6)
            cell(d,x,y,50,42,str(n),(60,60,90) if (gone or n==1) else (GOLD if n in pr and k>8 else TEAL),fs=16)
    if t>=ts[4]:
        lab(d,1000,185,"2^100 mod 1,000,000,007",WHITE,17);lab(d,1000,225,"= 976371285",GOLD,26)
        lab(d,1000,275,"100 in binary = 1100100",WHITE,17);lab(d,1000,310,"square, halve, multiply on 1-bits",GRY,15)
        lab(d,1000,380,"gcd(84, 36) = 12     lcm = 252",GRN,19)
    tw(d,sc,t,5,"TWIST #1 — keep everything as remainders")
def d_comb(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L19C)],30,150,690,15,20)
    if t>=ts[2]:
        lab(d,1000,200,"C(n, r) = n! · (r! · (n−r)!)^(−1)  mod p",WHITE,17)
        lab(d,1000,250,"inverse via Fermat:  x^(−1) = x^(p−2) mod p",GOLD,17)
    if t>=ts[3]:
        lab(d,1000,330,"C(10, 3) = 120",GRN,24);lab(d,1000,385,"C(20, 10) = 184,756",GRN,24)
    tw(d,sc,t,4,"TWIST #2 — division mod p = multiplication by a power")
def d_wk(d,t,sc):walk(d,sc,t,[(WK19,1,2)])
SCENES=[("title",mk_title("Number Theory and Counting","sieve · modular power · nCr mod p"),""),("sieve",d_sieve,"Room 1 · Primes and modpow"),("comb",d_comb,"Room 2 · Combinatorics"),("wk",d_wk,"Walkthrough · fast power"),("end",mk_end("Number theory — complete",["sieve","modpow","gcd / lcm","nCr mod p"],"next: advanced ML"),"")]
