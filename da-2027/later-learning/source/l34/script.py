N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film thirty four. LeetCode patterns, part one.'),
(N,'Arrays and hashing. These are the problems every interview starts with. Every solution runs as plain Python.')],
"hash":[
(N,'Room one. Two Sum, duplicates and best time to trade.'),
(R,'Two Sum: find two numbers that add up to a target. Two loops work. Why is that bad?'),
(S,'Two loops cost n squared. Instead keep a dictionary of values already seen. For each number, ask whether the target minus this number is in the dictionary. One pass, and the code finds indices zero and one, then one and two.'),
(S,'Contains duplicate is the same idea. A set drops repeats, so if the size shrinks, there was a duplicate. For best time to buy and sell, track the lowest price so far and the best profit. The answer is five.'),
(N,'Twist one. A hash map turns a nested loop into a single pass.')],
"prod":[
(N,'Room two. Product except self, and 3Sum.'),
(R,'Product of array except self, without division?'),
(S,'Sweep twice. Going left to right, store the product of everything on the left. Going right to left, multiply by everything on the right. For one, two, three, four the answer is twenty four, twelve, eight, six.'),
(S,'3Sum asks for triples that add to zero. Sort first. Fix one number, then two pointers close in from both ends: if the sum is too small, move the left pointer up, and if it is too big, move the right pointer down. Skip duplicates so each triple appears once.'),
(N,'Twist two. Prefix and suffix sweeps avoid division, and sorting plus two pointers beats three nested loops.')],
"tricks":[
(N,'Room three. Merge intervals, palindromes, anagrams and XOR.'),
(R,'Merge intervals looks messy. Where do I start?'),
(S,'Sort by start. Then each interval either overlaps the last merged one, so extend it, or starts fresh. One to three and two to six merge into one to six.'),
(S,'A palindrome reads the same both ways, so keep only letters, lower case them, and compare with the reverse. Anagrams sort to the same letters. And XOR cancels pairs: x XOR x is zero, so XOR over the list leaves the single number, four.'),
(N,'Twist three. Sort to make the structure visible, and use XOR to make pairs vanish.')],
"wk":[
(N,'Walkthrough. One Two Sum step, line by line.'),
(S,'The dictionary already holds two at index zero. The current number is seven, the target is nine.'),
(S,'Nine minus seven is two. Two is in the dictionary at index zero, so we found the pair.'),
(N,'Main logic. Ask whether the missing partner has already been seen.')],
"end":[
(N,'Film thirty four is complete. Arrays and hashing.'),
(N,'Next: strings, sliding windows and linked lists.')],
}
