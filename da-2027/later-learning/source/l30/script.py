N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film thirty. Advanced probability, part one.'),
(N,'Stochastic processes, concentration and limit theorems. Every idea runs as plain Python with comments.')],
"mark":[
(N,'Room one. Stochastic processes.'),
(R,'How do I model something random that evolves over time?'),
(S,'A Markov chain has a transition table. Sunny stays sunny ninety percent of the time, rainy stays rainy fifty percent. Start sunny, apply the table fifty times, and you reach the stationary distribution, zero point eight three three sunny and zero point one six seven rainy, whatever the start.'),
(S,'A random walk adds up plus or minus one steps. After a hundred steps, the variance of the position is about a hundred, so the spread grows like the square root of the number of steps. Brownian motion is the continuous limit.'),
(S,'Measure theory gives all of this a rigorous foundation, with sigma algebras and Lebesgue integrals.'),
(N,'Twist one. A chain forgets its start, and a random walk spreads like the square root of time.')],
"conc":[
(N,'Room two. Concentration and limit theorems.'),
(R,'How far can an average stray from its expected value?'),
(S,"Take sample means of a hundred uniform numbers and ask how often they miss one half by more than point one. In simulation, only four in ten thousand do. Chebyshev's bound says at most zero point oh eight three, and Hoeffding's says at most zero point two seven one. Both are safe, but loose."),
(S,'The central limit theorem says the spread of the mean is sigma over root n. Simulated, zero point oh two eight nine. Predicted, zero point oh two eight nine.'),
(S,'The law of large numbers says the mean converges. The modes of convergence, in probability, almost surely and in distribution, describe how.'),
(N,'Twist two. Bounds guarantee the worst case. The central limit theorem describes the typical case.')],
"wk":[
(N,'Walkthrough. One step of a Markov chain, line by line.'),
(S,'We start sunny for certain. The new probability of sunny is staying sunny, point nine.'),
(S,'The new probability of rainy is point one. Repeating this many times gives the stationary distribution.'),
(N,'Main logic. Multiply the distribution by the table.')],
"end":[
(N,'Film thirty is complete. Stochastic processes and limit theorems.'),
(N,'Next: information theory and estimation.')],
}
