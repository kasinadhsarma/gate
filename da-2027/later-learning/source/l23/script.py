N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film twenty three. Bayesian deep learning and uncertainty.'),
(N,'Sampling, ensembles and variational inference. Every idea runs as plain Python with comments.')],
"mcmc":[
(N,'Room one. Markov chain Monte Carlo.'),
(R,'How can I sample from a distribution I can only evaluate up to a constant?'),
(S,'Metropolis sampling. From the current point, propose a nearby one. Always accept if it is more probable, and accept a downhill move with probability equal to the ratio. The chain wanders, spending time in proportion to the probability.'),
(S,'Our target has two bumps, one at zero and a smaller one at four. After twenty thousand steps, the sample mean is one point eighteen, and thirty one percent of samples are above two. The exact values are one point three three and about thirty four percent. Close, but with sampling noise.'),
(S,'That is why Bayesian methods rely on sampling. No formula is needed for the normalising constant.'),
(N,'Twist one. MCMC trades exact formulas for a random walk that visits places in proportion to their probability.')],
"unc":[
(N,'Room two. Uncertainty.'),
(R,'How does a model say, I am not sure?'),
(S,'Train many versions on resampled data and compare their predictions. Inside the data the spread is only zero point oh nine. Far outside, at twelve, it is zero point seven eight. Disagreement is the uncertainty.'),
(R,'And a faster, approximate Bayesian method?'),
(S,'Variational inference picks the simple distribution q closest to the true posterior by minimising KL divergence. Against a two bump posterior, a narrow Gaussian on one bump scores zero point six nine. A wide one in the middle scores two point oh two, and a narrow one in the middle, five point four two. So it picks one bump and misses the other. That is its known bias, in return for speed.'),
(N,'Twist two. Ensembles and variational inference both turn a single answer into a spread of answers.')],
"wk":[
(N,'Walkthrough. The accept step, line by line.'),
(S,'The current point has probability point two. The proposal has probability point one.'),
(S,'The ratio is one half, so we accept the move with probability one half.'),
(N,'Main logic. Uphill always, downhill sometimes.')],
"end":[
(N,'Film twenty three is complete. MCMC, ensembles and variational inference.'),
(N,'Next: causality and game theory.')],
}
