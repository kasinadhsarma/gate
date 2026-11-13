from lhelp import *
import codes,math
def d_win(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L35A)],30,150,690,13,17)
    cards(d,t,ts,[(2,"longest unique: abcabcbb","3",TEAL),(2,"longest unique: pwwkew","3",TEAL),(3,"minimum window","BANC",GRN)],770,200,470,48,12,16)
    tw(d,sc,t,4,'TWIST #1 — expand right, shrink left')
def d_stack(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L35B)],30,150,690,13,17)
    cards(d,t,ts,[(2,"( ) [ ] { }","True",GRN),(2,"( ]","False",RED),(2,"( [ ) ]","False",RED),(3,"reversed list","[4, 3, 2, 1]",TEAL)],770,200,470,48,12,16)
    tw(d,sc,t,4,'TWIST #2 — stack for nesting, flip for reversing')
def d_fs(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L35C)],30,150,690,15,20)
    cards(d,t,ts,[(2,"cycle detected","True",GRN),(3,"middle node value","3",TEAL)],770,200,470,48,12,16)
    tw(d,sc,t,4,'TWIST #3 — two speeds find cycles and middles')
def d_wk(d,t,sc):walk(d,sc,t,[(WK35,1,2)])
SCENES=[("title",mk_title('LeetCode 2','sliding window · stacks · linked lists · fast and slow'),""),("win",d_win,'Room 1 · Sliding window'),("stack",d_stack,'Room 2 · Stacks and pointers'),("fs",d_fs,'Room 3 · Fast and slow pointers'),("wk",d_wk,'Walkthrough · window jump'),("end",mk_end('LeetCode 2 — complete',['window', 'stack', 'reverse list', 'fast and slow'],'next: trees, graphs and DP'),"")]
