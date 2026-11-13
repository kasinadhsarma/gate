N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film thirty five. LeetCode patterns, part two.'),
(N,'Sliding windows, stacks and linked lists. Every solution runs as plain Python.')],
"win":[
(N,'Room one. The sliding window.'),
(R,'Longest substring without repeating characters. Do I check every substring?'),
(S,'No. Keep a window that never repeats. Move the right edge one character at a time. If that character is already inside the window, jump the left edge just past its last position. The best length for abcabcbb is three, and for pwwkew also three.'),
(S,'Minimum window substring is the hard version. Count what you need. Expand until the window covers every needed letter, then shrink from the left while it stays valid, remembering the smallest. For ADOBECODEBANC and ABC the answer is BANC.'),
(N,'Twist one. A window grows on the right and shrinks on the left, so every element is touched twice at most.')],
"stack":[
(N,'Room two. Valid parentheses and reversing a list.'),
(R,'How do I check brackets match?'),
(S,'Use a stack. Push every opener. When a closer appears, the top of the stack must be its matching opener. Parentheses, brackets and braces in order are valid. A single bracket pair mismatch, or a crossed pair, is not.'),
(S,'To reverse a linked list, walk it once and flip each pointer to point backwards. One, two, three, four becomes four, three, two, one.'),
(N,'Twist two. A stack remembers the latest unmatched thing. Pointer flipping reverses in place.')],
"fs":[
(N,'Room three. Cycles and midpoints.'),
(R,'How do I know whether a linked list loops back?'),
(S,'Run two pointers. The slow one moves one step and the fast one moves two. If there is a cycle, the fast one must eventually catch the slow one, like a faster runner lapping a track. The code reports true.'),
(S,'The same trick finds the middle. When the fast pointer reaches the end, the slow one is halfway, at value three.'),
(N,'Twist three. Two speeds find loops and midpoints with no extra memory.')],
"wk":[
(N,'Walkthrough. A sliding window jump, line by line.'),
(S,'The last seen position of a is zero, and the left edge is at zero. We meet a again.'),
(S,'The new left edge is the larger of the old edge and the last position plus one. That gives one.'),
(N,'Main logic. Jump past the repeat, never backwards.')],
"end":[
(N,'Film thirty five is complete. Windows, stacks and linked lists.'),
(N,'Next: trees, graphs and dynamic programming.')],
}
