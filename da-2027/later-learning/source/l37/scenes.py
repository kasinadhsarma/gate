from lhelp import *
import codes,math
def d_bs(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L37S)],30,150,690,15,20)
    cards(d,t,ts,[(3,"search 0","index 4",GRN),(3,"search 3","-1",RED)],770,200,470,48,12,16)
    tw(d,sc,t,4,'TWIST #1 — one half is always sorted')
def d_bt(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L37BT)],30,150,690,15,20)
    cards(d,t,ts,[(2,"subsets of [1,2,3]","8",TEAL),(3,"combination sum, target 7","[2,2,3], [7]",GRN)],770,200,470,48,12,16)
    tw(d,sc,t,4,'TWIST #2 — choose, explore, undo')
def d_hard(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L38A)],30,150,690,15,20)
    cards(d,t,ts,[(2,"trapped water","6",TEAL),(3,"days to wait","[1,1,4,2,1,1,0,0]",GOLD),(3,"top 2 values","[6, 5]",GRN)],770,200,470,48,12,16)
    tw(d,sc,t,4,'TWIST #3 — a known pattern plus one invariant')
def d_design(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L38B)],30,150,690,13,17)
    cards(d,t,ts,[(2,"get 2, get 1, get 3","-1, 1, 3",TEAL),(3,"median of [1,3] and [2]","2",GOLD),(3,"median of [1,2] and [3,4]","2.5",GOLD),(3,"max subarray sum","6",GRN)],770,200,470,48,12,16)
    tw(d,sc,t,4,'TWIST #4 — two structures; best run ending here')
def d_wk(d,t,sc):walk(d,sc,t,[(WK37,1,2)])
SCENES=[("title",mk_title('LeetCode 4','binary search · backtracking · hard problems'),""),("bs",d_bs,'Room 1 · Modified binary search'),("bt",d_bt,'Room 2 · Backtracking'),("hard",d_hard,'Room 3 · Hard patterns'),("design",d_design,'Room 4 · Design and Kadane'),("wk",d_wk,'Walkthrough · Kadane step'),("end",mk_end('LeetCode 4 — complete',['binary search', 'backtracking', 'hard patterns', 'LRU'],'the Later Learning set is complete'),"")]
