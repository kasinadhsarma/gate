from lhelp import *
import codes,math
def d_tree(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L36A)],30,150,690,15,20)
    cards(d,t,ts,[(2,"max depth","3",TEAL),(3,"BST valid  /  broken one","True  /  False",GOLD),(3,"after invert, root children","7, 2",GRN)],770,200,470,48,12,16)
    tw(d,sc,t,4,'TWIST #1 — handle the node, trust the children')
def d_graph(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L36B)],30,150,690,13,17)
    cards(d,t,ts,[(2,"islands in the grid","3",TEAL),(3,"schedule 1 needs 0","True",GRN),(3,"schedule 0 ⇄ 1 loop","False",RED)],770,200,470,48,12,16)
    tw(d,sc,t,4,'TWIST #2 — grids are graphs; prerequisites are edges')
def d_dp(d,t,sc):
    ts=sc.ts;panel2(d,sc,t,[(2,L37A)],30,150,690,13,17)
    cards(d,t,ts,[(2,"coin change 11 with [1,2,5]","3",TEAL),(2,"2 cannot make 3","-1",RED),(3,"longest increasing subsequence","4",GOLD),(3,"leetcode = leet + code","True",GRN)],770,200,470,48,12,16)
    tw(d,sc,t,4,'TWIST #3 — state first, loop second')
def d_wk(d,t,sc):walk(d,sc,t,[(WK36,1,2)])
SCENES=[("title",mk_title('LeetCode 3','trees · graphs · dynamic programming'),""),("tree",d_tree,'Room 1 · Trees'),("graph",d_graph,'Room 2 · Graphs on grids'),("dp",d_dp,'Room 3 · Dynamic programming'),("wk",d_wk,'Walkthrough · one DP step'),("end",mk_end('LeetCode 3 — complete',['trees', 'flood fill', 'topological sort', 'DP'],'next: search, backtracking, and hard problems'),"")]
