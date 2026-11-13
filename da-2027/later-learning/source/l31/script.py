N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film thirty one. Information theory and estimation.'),
(N,'Entropy, KL divergence, maximum likelihood and the Cramér Rao bound. Every idea runs as plain Python with comments.')],
"info":[
(N,'Room one. Information theory.'),
(R,'How do I measure surprise?'),
(S,'Entropy is the average surprise in bits. A fair coin has one bit, the most possible. A biased coin, ninety ten, has only zero point four six nine.'),
(S,'KL divergence measures how different two distributions are, and it is not symmetric: zero point seven three seven one way, zero point five three one the other.'),
(S,'Cross entropy is entropy plus KL: one plus zero point seven three seven is one point seven three seven, which the code confirms. That is why minimising cross entropy loss shrinks the KL.'),
(S,'Mutual information measures how much knowing one variable tells you about another. For two related bits it is zero point two seven eight bits.'),
(N,'Twist one. Cross entropy equals entropy plus the KL you can still remove.')],
"mle":[
(N,'Room two. Estimation.'),
(R,'How do I pick the best value of a parameter from data?'),
(S,'Maximum likelihood: choose the value that makes the observed data most probable. For coin flips with true rate point three, the sample mean is zero point two seven eight, and a grid search of the log likelihood peaks at zero point two eight, the same place.'),
(S,'Fisher information measures how sharply the likelihood peaks. The Cramér Rao bound says no unbiased estimator can have a standard deviation below one over root Fisher information, here zero point oh two.'),
(S,'The method of moments is an older alternative: match sample moments to theoretical ones.'),
(N,'Twist two. Maximum likelihood is the best explanation of the data, and Fisher information says how well anything can do.')],
"wk":[
(N,'Walkthrough. Entropy of a fair coin.'),
(S,'Each outcome has probability one half, and minus log base two of one half is one bit.'),
(S,'Averaging gives one bit in total.'),
(N,'Main logic. Entropy is average surprise.')],
"end":[
(N,'Film thirty one is complete. Information theory and maximum likelihood.'),
(N,'Next: nonparametric statistics, generalised models and learning theory.')],
}
