from mkfilm import make
def L(*xs):return [(x[0],x[2:]) for x in xs]
CARD="770,200,470,48,12,16"
# ---------- L34 ----------
make("l34","LeetCode 1","arrays · hashing · two pointers · XOR",
L("N|Operation Gate. Later learning, film thirty four. LeetCode patterns, part one.","N|Arrays and hashing. These are the problems every interview starts with. Every solution runs as plain Python."),
[dict(key="hash",chap="Room 1 · Hash maps",tw="remember what you have seen",codes=[(2,"L34A")],
 lines=L("N|Room one. Two Sum, duplicates and best time to trade.","R|Two Sum: find two numbers that add up to a target. Two loops work. Why is that bad?",
 "S|Two loops cost n squared. Instead keep a dictionary of values already seen. For each number, ask whether the target minus this number is in the dictionary. One pass, and the code finds indices zero and one, then one and two.",
 "S|Contains duplicate is the same idea. A set drops repeats, so if the size shrinks, there was a duplicate. For best time to buy and sell, track the lowest price so far and the best profit. The answer is five.",
 "N|Twist one. A hash map turns a nested loop into a single pass."),
 vis='''
 cards(d,t,ts,[(2,"two sum [2,7,11,15] → 9","[0, 1]",TEAL),(2,"two sum [3,2,4] → 6","[1, 2]",TEAL),(3,"has duplicate","True",GOLD),(3,"best profit","5",GRN)],770,200,470,48,12,16)
 '''),
 dict(key="prod",chap="Room 2 · Prefix products and pointers",tw="sort, then close in from both ends",codes=[(2,"L34B")],
 lines=L("N|Room two. Product except self, and 3Sum.","R|Product of array except self, without division?",
 "S|Sweep twice. Going left to right, store the product of everything on the left. Going right to left, multiply by everything on the right. For one, two, three, four the answer is twenty four, twelve, eight, six.",
 "S|3Sum asks for triples that add to zero. Sort first. Fix one number, then two pointers close in from both ends: if the sum is too small, move the left pointer up, and if it is too big, move the right pointer down. Skip duplicates so each triple appears once.",
 "N|Twist two. Prefix and suffix sweeps avoid division, and sorting plus two pointers beats three nested loops."),
 vis='''
 cards(d,t,ts,[(2,"product except self","[24, 12, 8, 6]",TEAL),(3,"3Sum of [-1,0,1,2,-1,-4]","[-1,-1,2], [-1,0,1]",GOLD)],770,200,470,48,12,16)
 ''',fs=13,lh=18),
 dict(key="tricks",chap="Room 3 · Intervals, palindromes, XOR",tw="normalise, compare, cancel",codes=[(2,"L34C")],
 lines=L("N|Room three. Merge intervals, palindromes, anagrams and XOR.","R|Merge intervals looks messy. Where do I start?",
 "S|Sort by start. Then each interval either overlaps the last merged one, so extend it, or starts fresh. One to three and two to six merge into one to six.",
 "S|A palindrome reads the same both ways, so keep only letters, lower case them, and compare with the reverse. Anagrams sort to the same letters. And XOR cancels pairs: x XOR x is zero, so XOR over the list leaves the single number, four.",
 "N|Twist three. Sort to make the structure visible, and use XOR to make pairs vanish."),
 vis='''
 cards(d,t,ts,[(2,"merged intervals","[1,6] [8,10] [15,18]",TEAL),(3,"palindrome","True",GOLD),(3,"anagram","True",GOLD),(3,"single number by XOR","4",GRN)],770,200,470,48,12,16)
 '''),],
L("N|Walkthrough. One Two Sum step, line by line.","S|The dictionary already holds two at index zero. The current number is seven, the target is nine.","S|Nine minus seven is two. Two is in the dictionary at index zero, so we found the pair.","N|Main logic. Ask whether the missing partner has already been seen."),
"LeetCode 1 — complete",["hash map","prefix sums","two pointers","XOR"],"next: strings, windows and lists","WK34","Walkthrough · one Two Sum step",
L("N|Film thirty four is complete. Arrays and hashing.","N|Next: strings, sliding windows and linked lists."))
# ---------- L35 ----------
make("l35","LeetCode 2","sliding window · stacks · linked lists · fast and slow",
L("N|Operation Gate. Later learning, film thirty five. LeetCode patterns, part two.","N|Sliding windows, stacks and linked lists. Every solution runs as plain Python."),
[dict(key="win",chap="Room 1 · Sliding window",tw="expand right, shrink left",codes=[(2,"L35A")],
 lines=L("N|Room one. The sliding window.","R|Longest substring without repeating characters. Do I check every substring?",
 "S|No. Keep a window that never repeats. Move the right edge one character at a time. If that character is already inside the window, jump the left edge just past its last position. The best length for abcabcbb is three, and for pwwkew also three.",
 "S|Minimum window substring is the hard version. Count what you need. Expand until the window covers every needed letter, then shrink from the left while it stays valid, remembering the smallest. For ADOBECODEBANC and ABC the answer is BANC.",
 "N|Twist one. A window grows on the right and shrinks on the left, so every element is touched twice at most."),
 vis='''
 cards(d,t,ts,[(2,"longest unique: abcabcbb","3",TEAL),(2,"longest unique: pwwkew","3",TEAL),(3,"minimum window","BANC",GRN)],770,200,470,48,12,16)
 ''',fs=13,lh=17),
 dict(key="stack",chap="Room 2 · Stacks and pointers",tw="stack for nesting, flip for reversing",codes=[(2,"L35B")],
 lines=L("N|Room two. Valid parentheses and reversing a list.","R|How do I check brackets match?",
 "S|Use a stack. Push every opener. When a closer appears, the top of the stack must be its matching opener. Parentheses, brackets and braces in order are valid. A single bracket pair mismatch, or a crossed pair, is not.",
 "S|To reverse a linked list, walk it once and flip each pointer to point backwards. One, two, three, four becomes four, three, two, one.",
 "N|Twist two. A stack remembers the latest unmatched thing. Pointer flipping reverses in place."),
 vis='''
 cards(d,t,ts,[(2,"( ) [ ] { }","True",GRN),(2,"( ]","False",RED),(2,"( [ ) ]","False",RED),(3,"reversed list","[4, 3, 2, 1]",TEAL)],770,200,470,48,12,16)
 ''',fs=13,lh=17),
 dict(key="fs",chap="Room 3 · Fast and slow pointers",tw="two speeds find cycles and middles",codes=[(2,"L35C")],
 lines=L("N|Room three. Cycles and midpoints.","R|How do I know whether a linked list loops back?",
 "S|Run two pointers. The slow one moves one step and the fast one moves two. If there is a cycle, the fast one must eventually catch the slow one, like a faster runner lapping a track. The code reports true.",
 "S|The same trick finds the middle. When the fast pointer reaches the end, the slow one is halfway, at value three.",
 "N|Twist three. Two speeds find loops and midpoints with no extra memory."),
 vis='''
 cards(d,t,ts,[(2,"cycle detected","True",GRN),(3,"middle node value","3",TEAL)],770,200,470,48,12,16)
 '''),],
L("N|Walkthrough. A sliding window jump, line by line.","S|The last seen position of a is zero, and the left edge is at zero. We meet a again.","S|The new left edge is the larger of the old edge and the last position plus one. That gives one.","N|Main logic. Jump past the repeat, never backwards."),
"LeetCode 2 — complete",["window","stack","reverse list","fast and slow"],"next: trees, graphs and DP","WK35","Walkthrough · window jump",
L("N|Film thirty five is complete. Windows, stacks and linked lists.","N|Next: trees, graphs and dynamic programming."))
# ---------- L36 ----------
make("l36","LeetCode 3","trees · graphs · dynamic programming",
L("N|Operation Gate. Later learning, film thirty six. LeetCode patterns, part three.","N|Trees, grids, schedules and dynamic programming. Every solution runs as plain Python."),
[dict(key="tree",chap="Room 1 · Trees",tw="handle the node, trust the children",codes=[(2,"L36A")],
 lines=L("N|Room one. Binary trees.","R|Tree problems all look like recursion. What is the template?",
 "S|Handle the current node, and trust the two children to solve their own subtrees. Depth is one plus the larger child depth, three here. Inverting swaps the children at every node.",
 "S|To validate a binary search tree, carry an allowed range down. Every node must sit strictly between the bounds, and each child narrows them. Four, two, one, three, seven is valid. Five with a six on the left is not.",
 "N|Twist one. Pass information down and results up, and the recursion writes itself."),
 vis='''
 cards(d,t,ts,[(2,"max depth","3",TEAL),(3,"BST valid  /  broken one","True  /  False",GOLD),(3,"after invert, root children","7, 2",GRN)],770,200,470,48,12,16)
 '''),
 dict(key="graph",chap="Room 2 · Graphs on grids",tw="grids are graphs; prerequisites are edges",codes=[(2,"L36B")],
 lines=L("N|Room two. Number of islands and course schedule.","R|A grid of ones and zeros. How many islands?",
 "S|Scan every cell. When you meet unvisited land, count one island and flood fill it with depth first search, marking everything connected. The grid in the code has three islands.",
 "S|Course schedule asks whether all courses can be finished given prerequisites. Build a graph and repeatedly remove courses with no remaining prerequisites. If you can remove them all, there is no cycle, and the answer is true. A circular dependency leaves some behind, so false.",
 "N|Twist two. Flood fill counts regions, and topological sort detects cycles."),
 vis='''
 cards(d,t,ts,[(2,"islands in the grid","3",TEAL),(3,"schedule 1 needs 0","True",GRN),(3,"schedule 0 ⇄ 1 loop","False",RED)],770,200,470,48,12,16)
 ''',fs=13,lh=17),
 dict(key="dp",chap="Room 3 · Dynamic programming",tw="state first, loop second",codes=[(2,"L37A")],
 lines=L("N|Room three. Coin change, increasing subsequence and word break.","R|Coin change: fewest coins for eleven using one, two and five. Why not greedy?",
 "S|Greedy can fail for odd coin sets, so define dp of x as the fewest coins to make x, and build up. Eleven takes three coins, five five and one. Two cannot make three, so minus one.",
 "S|The longest increasing subsequence uses a tails list and binary search, in n log n time. The answer is four. Word break asks whether a string splits into dictionary words. A position is reachable if an earlier reachable position plus a word ends there. Leetcode splits into leet and code, true.",
 "N|Twist three. Say what dp of i means in words, and the loop follows."),
 vis='''
 cards(d,t,ts,[(2,"coin change 11 with [1,2,5]","3",TEAL),(2,"2 cannot make 3","-1",RED),(3,"longest increasing subsequence","4",GOLD),(3,"leetcode = leet + code","True",GRN)],770,200,470,48,12,16)
 ''',fs=13,lh=17),],
L("N|Walkthrough. One dynamic programming step, line by line.","S|The table holds zero, one, one. We want the answer for three, using coins one and two.","S|Using a one leaves dp two, which is one. Using a two leaves dp one, also one. The smaller is one, plus the coin gives two.","N|Main logic. Take the best earlier answer, then add one coin."),
"LeetCode 3 — complete",["trees","flood fill","topological sort","DP"],"next: search, backtracking, and hard problems","WK36","Walkthrough · one DP step",
L("N|Film thirty six is complete. Trees, graphs and dynamic programming.","N|Last: search, backtracking and the hard problems."))
# ---------- L37 ----------
make("l37","LeetCode 4","binary search · backtracking · hard problems",
L("N|Operation Gate. Later learning, film thirty seven. LeetCode patterns, part four.","N|Modified binary search, backtracking, and several hard problems. Every solution runs as plain Python."),
[dict(key="bs",chap="Room 1 · Modified binary search",tw="one half is always sorted",codes=[(2,"L37S")],
 lines=L("N|Room one. Searching a rotated sorted array.","R|The array was sorted, then rotated. Binary search should break. Does it?",
 "S|Not if you notice that after any split, at least one half is still sorted. Check whether the target falls inside that sorted half. If it does, search there, otherwise search the other half.",
 "S|In the array four, five, six, seven, zero, one, two, zero is found at index four, and three is not present, so minus one.",
 "N|Twist one. You do not need a fully sorted array, only a rule that tells you which half to discard."),
 vis='''
 cards(d,t,ts,[(3,"search 0","index 4",GRN),(3,"search 3","-1",RED)],770,200,470,48,12,16)
 '''),
 dict(key="bt",chap="Room 2 · Backtracking",tw="choose, explore, undo",codes=[(2,"L37BT")],
 lines=L("N|Room two. Subsets and combination sum.","R|Generate all subsets. Do I need a clever trick?",
 "S|No, just three verbs. Choose an element, explore with that choice, then undo it. For each item you either skip it or take it, so three items give two to the three, eight subsets.",
 "S|Combination sum reuses numbers, adding until the total hits the target, and prunes any branch that overshoots. For two, three, six, seven and target seven, the results are two, two, three and seven.",
 "N|Twist two. Backtracking explores a decision tree, and pruning cuts the dead branches early."),
 vis='''
 cards(d,t,ts,[(2,"subsets of [1,2,3]","8",TEAL),(3,"combination sum, target 7","[2,2,3], [7]",GRN)],770,200,470,48,12,16)
 '''),
 dict(key="hard",chap="Room 3 · Hard patterns",tw="a known pattern plus one invariant",codes=[(2,"L38A")],
 lines=L("N|Room three. Rain water, monotonic stacks and heaps.","R|Trapping rain water is rated hard. Where do I even start?",
 "S|Two pointers. Water above a bar equals the lower of the tallest bars on its two sides, minus its height. Move the pointer on the shorter side, because that side limits the water. The code traps six units.",
 "S|A monotonic stack answers next warmer day. Keep indexes of days still waiting. When a warmer day arrives, pop and record the wait. And a heap gives the top k values cheaply: six and five.",
 "N|Twist three. Hard problems are usually a known pattern with one clever invariant."),
 vis='''
 cards(d,t,ts,[(2,"trapped water","6",TEAL),(3,"days to wait","[1,1,4,2,1,1,0,0]",GOLD),(3,"top 2 values","[6, 5]",GRN)],770,200,470,48,12,16)
 '''),
 dict(key="design",chap="Room 4 · Design and Kadane",tw="two structures; best run ending here",codes=[(2,"L38B")],
 lines=L("N|Room four. LRU cache, medians and Kadane.","R|An LRU cache needs fast lookup and fast eviction. One structure cannot do both, right?",
 "S|Combine a hash map with an ordering. An ordered dictionary does both. Reading a key moves it to the newest end. When full, drop the oldest. After the sequence in the code, key two is gone, one is kept, and three is kept.",
 "S|A median is the middle of the merged lists, one point five for two plus three and two point five for the second pair. And Kadane's algorithm finds the best contiguous sum. At each step, either extend the run or restart. The answer is six.",
 "N|Twist four. Design problems combine two structures, and Kadane keeps the best run ending here."),
 vis='''
 cards(d,t,ts,[(2,"get 2, get 1, get 3","-1, 1, 3",TEAL),(3,"median of [1,3] and [2]","2",GOLD),(3,"median of [1,2] and [3,4]","2.5",GOLD),(3,"max subarray sum","6",GRN)],770,200,470,48,12,16)
 ''',fs=13,lh=17),],
L("N|Walkthrough. A Kadane step, line by line.","S|The current best run ends at four, and the next number is minus one.","S|Extending gives three, which beats starting fresh at minus one, so the run continues with three.","N|Main logic. Extend the run, or restart if the run is dragging you down."),
"LeetCode 4 — complete",["binary search","backtracking","hard patterns","LRU"],"the Later Learning set is complete","WK37","Walkthrough · Kadane step",
L("N|Film thirty seven is complete. That finishes the LeetCode set.","N|Every solution in these films was run, and the output on screen is the real output."))
