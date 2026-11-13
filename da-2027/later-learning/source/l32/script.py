N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film thirty two. Nonparametric methods, generalised models and learning theory.'),
(N,'Every idea runs as plain Python with comments.')],
"np":[
(N,'Room one. Nonparametric statistics and resampling.'),
(R,'What if I do not want to assume a distribution?'),
(S,'Kernel density estimation puts a small bump on every data point and adds them up. At zero, the estimate is zero point four oh seven, close to the true zero point three nine nine.'),
(S,'The bootstrap resamples the data with replacement, many times, and recomputes the statistic. The spread of the bootstrap medians, zero point one seven two, estimates the uncertainty of the median with no formula.'),
(S,'Importance sampling estimates a rare event by sampling where it happens, then correcting with weights. The probability that a normal exceeds three comes out as zero point oh oh one four, matching the true zero point oh oh one three five.'),
(N,'Twist one. Let the data speak: smooth it, resample it, or reweight it.')],
"glm":[
(N,'Room two. Generalised linear models and learning theory.'),
(R,'Linear regression predicts any number. What about yes or no, or counts?'),
(S,'A generalised linear model changes the link. Logistic regression models the probability of yes through a sigmoid, and Poisson regression models counts through an exponential. Here gradient ascent fits the logistic weights, five point three nine and minus two point four seven.'),
(S,'With many features, regularisation shrinks coefficients. From a least squares estimate of three, ridge shrinks it to one point five, and lasso, by soft thresholding, to two point five. For small coefficients, lasso sets them exactly to zero.'),
(S,'Learning theory asks how much data is enough. For a finite family of two to the twenty hypotheses, with error point one and confidence ninety five percent, the PAC bound says one hundred sixty nine samples. The VC dimension extends this to infinite families. Mixed models add random effects for clustered data.'),
(N,'Twist two. Match the model to the response, shrink to avoid overfitting, and use theory to size your data.')],
"wk":[
(N,'Walkthrough. Ridge and lasso on one coefficient.'),
(S,'The raw estimate is three, and the penalty strength is one.'),
(S,'Ridge divides by one plus lambda, giving one point five. Lasso subtracts half lambda, giving two point five.'),
(N,'Main logic. Ridge shrinks by a factor. Lasso subtracts, and can reach zero.')],
"end":[
(N,'Film thirty two is complete. Resampling, generalised models, shrinkage and PAC.'),
(N,'Last: calculus optimization.')],
}
