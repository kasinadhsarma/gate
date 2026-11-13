N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film thirty seven. LeetCode patterns, part four.'),
(N,'Modified binary search, backtracking, and several hard problems. Every solution runs as plain Python.')],
"bs":[
(N,'Room one. Searching a rotated sorted array.'),
(R,'The array was sorted, then rotated. Binary search should break. Does it?'),
(S,'Not if you notice that after any split, at least one half is still sorted. Check whether the target falls inside that sorted half. If it does, search there, otherwise search the other half.'),
(S,'In the array four, five, six, seven, zero, one, two, zero is found at index four, and three is not present, so minus one.'),
(N,'Twist one. You do not need a fully sorted array, only a rule that tells you which half to discard.')],
"bt":[
(N,'Room two. Subsets and combination sum.'),
(R,'Generate all subsets. Do I need a clever trick?'),
(S,'No, just three verbs. Choose an element, explore with that choice, then undo it. For each item you either skip it or take it, so three items give two to the three, eight subsets.'),
(S,'Combination sum reuses numbers, adding until the total hits the target, and prunes any branch that overshoots. For two, three, six, seven and target seven, the results are two, two, three and seven.'),
(N,'Twist two. Backtracking explores a decision tree, and pruning cuts the dead branches early.')],
"hard":[
(N,'Room three. Rain water, monotonic stacks and heaps.'),
(R,'Trapping rain water is rated hard. Where do I even start?'),
(S,'Two pointers. Water above a bar equals the lower of the tallest bars on its two sides, minus its height. Move the pointer on the shorter side, because that side limits the water. The code traps six units.'),
(S,'A monotonic stack answers next warmer day. Keep indexes of days still waiting. When a warmer day arrives, pop and record the wait. And a heap gives the top k values cheaply: six and five.'),
(N,'Twist three. Hard problems are usually a known pattern with one clever invariant.')],
"design":[
(N,'Room four. LRU cache, medians and Kadane.'),
(R,'An LRU cache needs fast lookup and fast eviction. One structure cannot do both, right?'),
(S,'Combine a hash map with an ordering. An ordered dictionary does both. Reading a key moves it to the newest end. When full, drop the oldest. After the sequence in the code, key two is gone, one is kept, and three is kept.'),
(S,"A median is the middle of the merged lists, one point five for two plus three and two point five for the second pair. And Kadane's algorithm finds the best contiguous sum. At each step, either extend the run or restart. The answer is six."),
(N,'Twist four. Design problems combine two structures, and Kadane keeps the best run ending here.')],
"wk":[
(N,'Walkthrough. A Kadane step, line by line.'),
(S,'The current best run ends at four, and the next number is minus one.'),
(S,'Extending gives three, which beats starting fresh at minus one, so the run continues with three.'),
(N,'Main logic. Extend the run, or restart if the run is dragging you down.')],
"end":[
(N,'Film thirty seven is complete. That finishes the LeetCode set.'),
(N,'Every solution in these films was run, and the output on screen is the real output.')],
}
