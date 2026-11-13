N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film thirty six. LeetCode patterns, part three.'),
(N,'Trees, grids, schedules and dynamic programming. Every solution runs as plain Python.')],
"tree":[
(N,'Room one. Binary trees.'),
(R,'Tree problems all look like recursion. What is the template?'),
(S,'Handle the current node, and trust the two children to solve their own subtrees. Depth is one plus the larger child depth, three here. Inverting swaps the children at every node.'),
(S,'To validate a binary search tree, carry an allowed range down. Every node must sit strictly between the bounds, and each child narrows them. Four, two, one, three, seven is valid. Five with a six on the left is not.'),
(N,'Twist one. Pass information down and results up, and the recursion writes itself.')],
"graph":[
(N,'Room two. Number of islands and course schedule.'),
(R,'A grid of ones and zeros. How many islands?'),
(S,'Scan every cell. When you meet unvisited land, count one island and flood fill it with depth first search, marking everything connected. The grid in the code has three islands.'),
(S,'Course schedule asks whether all courses can be finished given prerequisites. Build a graph and repeatedly remove courses with no remaining prerequisites. If you can remove them all, there is no cycle, and the answer is true. A circular dependency leaves some behind, so false.'),
(N,'Twist two. Flood fill counts regions, and topological sort detects cycles.')],
"dp":[
(N,'Room three. Coin change, increasing subsequence and word break.'),
(R,'Coin change: fewest coins for eleven using one, two and five. Why not greedy?'),
(S,'Greedy can fail for odd coin sets, so define dp of x as the fewest coins to make x, and build up. Eleven takes three coins, five five and one. Two cannot make three, so minus one.'),
(S,'The longest increasing subsequence uses a tails list and binary search, in n log n time. The answer is four. Word break asks whether a string splits into dictionary words. A position is reachable if an earlier reachable position plus a word ends there. Leetcode splits into leet and code, true.'),
(N,'Twist three. Say what dp of i means in words, and the loop follows.')],
"wk":[
(N,'Walkthrough. One dynamic programming step, line by line.'),
(S,'The table holds zero, one, one. We want the answer for three, using coins one and two.'),
(S,'Using a one leaves dp two, which is one. Using a two leaves dp one, also one. The smaller is one, plus the coin gives two.'),
(N,'Main logic. Take the best earlier answer, then add one coin.')],
"end":[
(N,'Film thirty six is complete. Trees, graphs and dynamic programming.'),
(N,'Last: search, backtracking and the hard problems.')],
}
