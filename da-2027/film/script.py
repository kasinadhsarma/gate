# (speaker, text)  N=narrator R=Ramu S=Somu
SCENES = {
"title": [("N","Operation Gate. The Night Library. A film about data structures and algorithms, in twelve twists.")],
"s1": [
("N","Midnight. The great library holds one million shelves, and the Golden Algorithm book is missing."),
("R","Somu, I will check every shelf, one by one, starting from shelf number one."),
("S","That is linear search, Ramu. In the worst case it costs n steps. At one shelf per second, a million shelves is eleven days."),
("R","Eleven days! Fine, I am running. Shelf one, shelf two, shelf three."),
("N","Twist number six. The book was on the very last shelf."),
],
"s2": [
("S","Wait, Ramu. Look at the labels. The shelves are in sorted order. So walk to the middle shelf and ask one question."),
("R","Is my number bigger, or smaller?"),
("S","Exactly. If it is bigger, throw away the whole left half. Then ask again in the middle of what remains."),
("R","So every question cuts the problem in two. A million becomes half a million, then a quarter million."),
("S","After only twenty questions, one shelf is left. Twenty, because two to the twenty is just over a million. That is order log n."),
("N","Twist number seven. Binary search is magic, but only while the shelves stay sorted."),
],
"s3": [
("N","Then the lights flicker. A thief, the Shuffler, scrambles every shelf."),
("R","Now binary search is useless! I must sort a million books by hand."),
("S","Not by hand. Use divide and conquer. Split the pile in half, again and again, until every pile holds one book. A single book is already sorted."),
("R","And then?"),
("S","Then merge. Two sorted piles combine into one, by always taking the smaller front book. That is merge sort."),
("S","Bubble sort needs about half a trillion comparisons here. Merge sort needs about twenty million. The work is n per level, over log n levels."),
("N","Twist number eight. The cost of order is n log n, and no comparison sort can beat it."),
],
"s4": [
("R","Why search at all? Can the book simply tell me where it lives?"),
("S","That is hashing. Give every key a home address. Here the address is three times the key, mod ten."),
("S","Keys one, four, five and six find free homes. But key fourteen also hashes to slot two."),
("R","Slot two is taken!"),
("S","So it probes the next slot, then the next, until it finds an empty one. That is linear probing. Fourteen lands in slot four, and fifteen in slot six."),
("N","Twist number nine. The fuller the table, the longer the probes. At ninety percent full, expect ten probes. So tables grow before they fill."),
],
"s5": [
("N","In the basement, a ghost lives inside a Python function."),
("R","Somu, this function has a default empty list. I call it with one, then with two, then with three and a fresh list."),
("S","The default list is created only once, when the function is defined. Every call that skips it shares the same ghost list."),
("R","So the output is one, then one and two, and then just three."),
("N","Twist number ten. A name is a label on an object, not a box. Mutable defaults remember."),
],
"s6": [
("S","Now the city map. Roads are edges, junctions are vertices. Start at the library and send a ripple outward."),
("R","Everything one road away first, then two roads away. The ripple is a queue."),
("S","That is breadth first search. It finds the fewest roads, in time order V plus E."),
("R","And depth first search?"),
("S","It dives down one road as far as it can, then backs up. If a road leads back to a junction that is still open, we have found a back edge."),
("N","Twist number eleven. A back edge means a cycle. The city has a loop."),
],
"s7": [
("S","One last map. A morning routine, where some tasks must happen before others. No loops allowed, so it is a directed acyclic graph."),
("R","How do I order the tasks?"),
("S","Remove any task that has nothing waiting for it. Repeat. That is Kahn's topological sort. Four, five, two, zero, three, one."),
("N","If anything is left over, there was a cycle. Twist number twelve, hidden in plain sight."),
],
"s8": [
("R","Somu, one last riddle. The function mystery of four calls itself on n minus one and n minus two. How many calls?"),
("S","Draw the tree. Fifteen calls, for such a small input. The same questions are asked again and again."),
("R","Then remember the answers!"),
("S","That is memoisation. Fifteen calls collapse to five distinct problems, and exponential becomes linear. Fibonacci fifty finishes instantly."),
("N","The final twist. Most hard problems are easy problems asked too many times."),
],
"end": [
("N","The book was found. Search, sort, hash, remember, and walk the graph."),
("S","Linear is n. Binary is log n. Merge sort is n log n. Hash lookup is one on average. Breadth first search is V plus E."),
("R","Now I am ready, for GATE, and for Google."),
("N","Operation Gate. Next chapters, databases, machine learning and A I."),
],
}

SCENES["title"]=[("N","Operation Gate. The Night Library. A film about mathematics, data structures and algorithms, in twelve twists.")]
SCENES["m1"]=[
("N","Before the library, there is the basement of numbers. Everything in computing starts with a few humble operations."),
("R","Add, subtract, multiply, divide. What else is there?"),
("S","Division has three faces. Seventeen sweets for five friends. Seventeen divided by five is three point four. Floor division gives three each. And the remainder, seventeen mod five, is two sweets left over."),
("S","They are tied by one identity. A equals b times the quotient, plus the remainder. Five times three, plus two, is seventeen."),
("R","What happens with minus seventeen?"),
("S","Python floors toward minus infinity. Minus seventeen floor five is minus four, and the remainder is three. Check it: five times minus four, plus three, is minus seventeen."),
("N","Twist number one. Floor means down, not toward zero. And power binds tighter than minus, so minus two squared is minus four."),
]
SCENES["m2"]=[
("R","Somu, I have two ropes, forty eight and eighteen metres. I want equal pieces with nothing left over. How long can each piece be?"),
("S","That is the G C D, the greatest common divisor. Some books call it the H C F, the highest common factor. It is the same thing."),
("S","Euclid's trick. Replace the pair by the smaller number and the remainder. Forty eight and eighteen becomes eighteen and twelve, then twelve and six, then six and zero. The answer is six."),
("R","Why does the remainder keep the same divisors?"),
("S","Anything that divides both a and b also divides a minus a multiple of b, which is the remainder. The pair shrinks, the common divisors stay."),
("S","Now the L C M, the least common multiple. Two buses leave every forty eight and eighteen minutes. They meet again after the L C M. And G C D times L C M equals a times b. So forty eight times eighteen, over six, gives one hundred forty four."),
("N","Twist number two. One G C D gives you the L C M for free, and Euclid needs only about log n steps."),
]
SCENES["m3"]=[
("R","Somu, how do I know whether a number is prime?"),
("S","Divide only up to its square root. If nothing divides it by then, no bigger factor can exist, because it would pair with a smaller one."),
("R","And all the primes up to fifty?"),
("S","Use the sieve of Eratosthenes. Write the numbers, cross out the multiples of two, then three, then five, then seven. What survives is prime. It costs n log log n."),
("S","Next, modular arithmetic. It is a clock. Add, subtract or multiply, then reduce. Seven times eight, mod five, equals two times three, mod five. Both are one."),
("S","For big powers, halve the exponent. Three to the thirteen needs only about log of thirteen steps, not twelve multiplications. That is fast exponentiation."),
("N","Twist number three. Cross out the multiples and the primes appear by themselves. Divide and conquer works even on powers."),
]
SCENES["m4"]=[
("R","Counting first. Five friends, and I pick two for a team."),
("S","If order matters, five times four is twenty. If order does not matter, divide by the two ways to order a pair. That gives ten. We say five choose two."),
("S","Probability is favourable outcomes over total outcomes. Two dice add to seven in six of thirty six ways. That is one sixth. A fair die averages three and a half, and expected values simply add."),
("R","Now a test for a rare disease. Ninety percent accurate. If I test positive, am I sick?"),
("S","Say one percent of people have the disease. The test catches ninety percent of the sick, but wrongly flags nine percent of the healthy. Test a thousand people. Ten are sick, nine of them test positive. Among nine hundred ninety healthy, about eighty nine also test positive."),
("S","So of about ninety eight positives, only nine are sick. About nine percent. That is Bayes theorem. Posterior equals likelihood times prior, over the evidence."),
("N","Twist number four. A positive test can still mean you are probably healthy."),
]
SCENES["m5"]=[
("N","Mathematics is not a separate subject. It is the machinery inside every algorithm."),
("S","Euclid's G C D is a loop. The sieve is an array. Fast power is divide and conquer. And hash tables run on probability."),
("R","Probability inside hashing?"),
("S","The birthday paradox. With only twenty three people, two share a birthday with probability over half. In the same way, three hundred keys in ten thousand slots collide with probability ninety nine percent."),
("S","And randomised quicksort. A random pivot makes the expected time n log n on every input, because the randomness lives in the pivot, not in the data."),
("N","Twist number five. Collisions arrive early. That is why hash tables resize, and why random pivots save quicksort."),
]

SCENES["mb"]=[
("N","Down in the basement, numbers wear different costumes. The costume is called the base."),
("R","Why does a computer count in twos?"),
("S","Because a switch has two states, on and off. In base two, each position is worth twice the one on its right: one, two, four, eight, sixteen. So forty five is thirty two, plus eight, plus four, plus one. That is one zero one one zero one."),
("S","To convert by hand, divide by two again and again and collect the remainders. Forty five gives one, zero, one, one, zero, one. Read them from the bottom up."),
("R","And hexadecimal?"),
("S","Group the bits in fours. One zero one one, then zero one one one, is B seven. That is one hundred eighty three. Octal groups the bits in threes. Hex and octal are just compact binary."),
("S","Adding in binary follows the school carry rule. One one zero one plus one carries to one one one zero. Negative numbers use two's complement: flip the bits and add one. Minus five, in eight bits, is one one one one one zero one one."),
("N","Bonus twist. Zero point one has no finite binary form, so zero point one plus zero point two is not exactly zero point three."),
]
