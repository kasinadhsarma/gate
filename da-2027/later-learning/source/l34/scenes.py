from lhelp import *
import codes,math
def d_hash(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L34A)],30,150,690,15,20)
    cards(d,t,ts,[(2,"two sum [2,7,11,15] → 9","[0, 1]",TEAL),(2,"two sum [3,2,4] → 6","[1, 2]",TEAL),(3,"has duplicate","True",GOLD),(3,"best profit","5",GRN)],770,200,470,48,12,16)
    tw(d,sc,t,4,'TWIST #1 — remember what you have seen')
def d_prod(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L34B)],30,150,690,13,18)
    cards(d,t,ts,[(2,"product except self","[24, 12, 8, 6]",TEAL),(3,"3Sum of [-1,0,1,2,-1,-4]","[-1,-1,2], [-1,0,1]",GOLD)],770,200,470,48,12,16)
    tw(d,sc,t,4,'TWIST #2 — sort, then close in from both ends')
def d_tricks(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L34C)],30,150,690,15,20)
    cards(d,t,ts,[(2,"merged intervals","[1,6] [8,10] [15,18]",TEAL),(3,"palindrome","True",GOLD),(3,"anagram","True",GOLD),(3,"single number by XOR","4",GRN)],770,200,470,48,12,16)
    tw(d,sc,t,4,'TWIST #3 — normalise, compare, cancel')
def d_wk(d,t,sc):walk(d,sc,t,[(WK34,1,2)])
SCENES=[("title",mk_title('LeetCode 1','arrays · hashing · two pointers · XOR'),""),("hash",d_hash,'Room 1 · Hash maps'),("prod",d_prod,'Room 2 · Prefix products and pointers'),("tricks",d_tricks,'Room 3 · Intervals, palindromes, XOR'),("wk",d_wk,'Walkthrough · one Two Sum step'),("end",mk_end('LeetCode 1 — complete',['hash map', 'prefix sums', 'two pointers', 'XOR'],'next: strings, windows and lists'),"")]
