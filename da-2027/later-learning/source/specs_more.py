from mkfilm import make
def L(*xs):return [(x[0],x[2:]) for x in xs]
# ---------- L27 ----------
make("l27","Advanced Linear Algebra 1","vector spaces · linear maps · Gram-Schmidt",
L("N|Operation Gate. Later learning, film twenty seven. Advanced linear algebra, part one.","N|Abstract vector spaces, linear maps and inner products. Every idea runs as plain Python with comments."),
[dict(key="vs",chap="Room 1 · Vector spaces and maps",tw="anything you can add and scale is a vector",codes=[(2,"L27A")],
 lines=L("N|Room one. Abstract vector spaces and linear maps.","R|Vectors are arrows in R n. Why generalise?",
 "S|Because many things behave like vectors. Polynomials can be added and scaled, so they form a vector space. With basis one, x and x squared, the polynomial five plus three x plus four x squared is just the list five, three, four.",
 "S|The derivative becomes a matrix. Applying it gives three, eight, zero, meaning three plus eight x. Calculus has turned into matrix multiplication.",
 "S|The rank nullity theorem says rank plus nullity equals the number of columns. Our matrix has rank two, so nullity two, and the check prints true. And changing basis gives a similar matrix with the same eigenvalues, two and three.",
 "N|Twist one. Anything you can add and scale is a vector, and a linear map is then just a matrix."),
 vis='''
 if t>=ts[2]:
     lab(d,1000,175,"polynomial 5 + 3x + 4x²  =  [5, 3, 4]",WHITE,16)
     mat(d,800,215,[[0,1,0],[0,0,2],[0,0,0]],50,34,GOLD,18);lab(d,985,250,"×",WHITE,22);mat(d,1010,215,[[5],[3],[4]],50,34,TEAL,18)
 if t>=ts[3]:lab(d,1000,350,"= [3, 8, 0]   i.e.  3 + 8x",GRN,20)
 cards(d,t,ts,[(4,"rank + nullity","2 + 2 = 4 columns",GOLD),(4,"eigenvalues M and P⁻¹MP","2, 3  and  2, 3",GOLD)],770,400,470,44,10,16)
 '''),
 dict(key="ip",chap="Room 2 · Inner products and fields",tw="orthogonalise, and mind the field",codes=[(2,"L27B")],
 lines=L("N|Room two. Inner products and fields.","R|How do I build perpendicular directions from any set of vectors?",
 "S|Gram Schmidt. Take each vector and subtract its parts along the earlier directions, then normalise. The product of the result with its transpose is the identity, so the vectors are orthonormal. This is the heart of the QR decomposition.",
 "S|The field matters too. The same three vectors have rank three over the real numbers, but only rank two when arithmetic is done modulo two, because they add up to zero there.",
 "S|Finite fields like this are used in error correcting codes and cryptography.",
 "N|Twist two. Orthogonalise to simplify, and remember that the answer depends on the field."),
 vis='''
 if t>=ts[2]:
     lab(d,1000,175,"Q · Qᵀ",WHITE,16);mat(d,860,205,[[1,0,0],[0,1,0],[0,0,1]],60,40,GRN,22);lab(d,1000,350,"identity → orthonormal",GRN,17)
 cards(d,t,ts,[(3,"rank over the reals","3",TEAL),(3,"rank over GF(2)  (mod 2)","2",RED)],770,400,470,44,10,16)
 '''),],
L("N|Walkthrough. One Gram Schmidt step, line by line.","S|The vector is one, one. The earlier direction is one, zero.","S|The dot product is one, so we subtract one times the direction, leaving zero, one.","N|Main logic. Remove what you already have."),
"Advanced linear algebra 1 — complete",["polynomial space","rank-nullity","Gram-Schmidt","fields"],"next: decompositions","WK27","Walkthrough · Gram-Schmidt step",
L("N|Film twenty seven is complete. Vector spaces, linear maps and orthogonalisation.","N|Next: decompositions and canonical forms."))
# ---------- L28 ----------
make("l28","Advanced Linear Algebra 2","SVD · Jordan form · spectral theorem",
L("N|Operation Gate. Later learning, film twenty eight. Advanced linear algebra, part two.","N|Decompositions and canonical forms. Every idea runs as plain Python with comments."),
[dict(key="svd",chap="Room 1 · SVD",tw="keep the big singular values",codes=[(2,"L28A")],
 lines=L("N|Room one. The singular value decomposition.","R|Does every matrix have a nice decomposition, even a rectangular one?",
 "S|Yes, the SVD. Any matrix equals orthogonal, times diagonal, times orthogonal. The diagonal holds the singular values, here five and three. They measure how important each direction is.",
 "S|Keeping only the largest gives the best low rank approximation. The error is exactly the next singular value, three. The pseudo inverse, built from the SVD, projects onto the row space, which is how least squares works for any matrix.",
 "S|In machine learning this is used for compression, recommendation and PCA.",
 "N|Twist one. Keep the big singular values and you keep most of the matrix."),
 vis='''
 if t>=ts[2]:
     lab(d,1000,175,"singular values",WHITE,15);hbars(d,790,200,[("σ1",5),("σ2",3)],5,w=240,col=[GOLD,TEAL],lw=60)
 cards(d,t,ts,[(3,"rank-1 approximation error","3.0",RED),(3,"equals next singular value","3.0",GOLD)],770,320,470,44,10,16)
 '''),
 dict(key="jordan",chap="Room 2 · Canonical forms",tw="symmetric matrices always diagonalise",codes=[(2,"L28B")],
 lines=L("N|Room two. Canonical forms and the spectral theorem.","R|Can every matrix be diagonalised?",
 "S|No. The Jordan block with eigenvalue two repeated has only one eigenvector, so the rank of N is one. N squared is zero, which makes it nilpotent. Its powers are not just two to the n. The corner entry is n times two to the n minus one: thirty two and eighty for n equals five.",
 "S|Jordan form says every matrix over the complex numbers is block diagonal made of such pieces.",
 "S|Symmetric matrices are the nice case. The spectral theorem says they have real eigenvalues, two point three eight and four point six two here, and orthogonal eigenvectors. If all eigenvalues are positive, a Cholesky factor exists, which the code confirms.",
 "N|Twist two. Not every matrix diagonalises, but symmetric ones always do, with orthogonal eigenvectors."),
 vis='''
 if t>=ts[2]:
     lab(d,1000,175,"Jordan block J",WHITE,15);mat(d,900,200,[[2,1],[0,2]],60,40,GOLD,22)
 cards(d,t,ts,[(2,"eigenvectors","only 1",RED),(2,"J⁵ first row","[32, 80]",GOLD),(4,"eigenvalues of symmetric S","2.382, 4.618",GRN),(4,"Cholesky L·Lᵀ = S","True",GRN)],770,300,470,44,10,16)
 '''),],
L("N|Walkthrough. How much does one singular value explain?","S|Singular values are five and three. Their squares are twenty five and nine.","S|The first explains twenty five out of thirty four, about seventy three and a half percent.","N|Main logic. The share of squared singular values is the share of energy."),
"Advanced linear algebra 2 — complete",["SVD","low rank","Jordan form","spectral theorem"],"next: numerical methods and tensors","WK28","Walkthrough · energy share",
L("N|Film twenty eight is complete. SVD, Jordan form and the spectral theorem.","N|Next: numerical linear algebra and tensors."))
# ---------- L29 ----------
make("l29","Advanced Linear Algebra 3","numerical methods · tensors · Lie brackets",
L("N|Operation Gate. Later learning, film twenty nine. Advanced linear algebra, part three.","N|Iterative solvers, tensors, Lie brackets and quadratic forms. Every idea runs as plain Python with comments."),
[dict(key="ncon",chap="Room 1 · Numerical methods",tw="iterate cheaply; watch conditioning",codes=[(2,"L29A")],
 lines=L("N|Room one. Numerical linear algebra.","R|Solving a big system exactly is slow. What do real programs do?",
 "S|Iterative methods. Conjugate gradient solves a symmetric positive definite system using only matrix vector products. For a two by two system it needs two steps, and it matches the direct solver: zero point oh nine oh nine, zero point six three six four.",
 "S|Conditioning matters. The Hilbert matrix of size six has a condition number of one point five times ten to the seven. A tiny rounding error in the input can become a big error in the answer.",
 "S|Sparse solvers, steepest descent and preconditioners are all variations on these ideas.",
 "N|Twist one. Iterate with cheap products, and watch the condition number."),
 vis='''
 cards(d,t,ts,[(2,"CG after step 1","[0.25, 0.5]",TEAL),(2,"CG after step 2","[0.0909, 0.6364]",GOLD),(2,"direct solver","[0.0909, 0.6364]",GRN),(3,"condition number, Hilbert 6x6","1.5e7",RED)],770,200,470,48,12,16)
 '''),
 dict(key="tens",chap="Room 2 · Tensors and forms",tw="structure, brackets and minima",codes=[(2,"L29B")],
 lines=L("N|Room two. Tensors, determinants, Lie brackets and quadratic forms.","R|What is a tensor, in practice?",
 "S|A tensor generalises vectors and matrices to more indices. The tensor product of two vectors is their outer product, a rank one matrix, as printed. Libraries such as einsum write any contraction in one line.",
 "S|The determinant is an alternating multilinear form. Swap two rows and the sign flips, from minus two to two.",
 "S|The commutator of two matrices, X Y minus Y X, is the Lie bracket. It measures how much two transformations fail to commute, and underlies rotations and symmetries.",
 "S|Finally, a quadratic form whose Hessian has all positive eigenvalues, here zero point seven nine three and two point two oh seven, is bowl shaped, so a stationary point is a minimum.",
 "N|Twist two. Tensors, determinants and brackets describe structure. Positive eigenvalues describe a minimum."),
 vis='''
 cards(d,t,ts,[(2,"outer product rank","1",TEAL),(3,"det before / after row swap","-2  /  2",GOLD),(4,"Lie bracket [X, Y]","[[0,-1],[-1,0]]",PUR),(5,"Hessian eigenvalues","0.793, 2.207  → minimum",GRN)],770,200,470,48,12,16)
 '''),],
L("N|Walkthrough. A conjugate gradient step size, line by line.","S|The residual is one, two. The matrix times the direction is six, seven.","S|The step size is residual dot residual over direction dot A direction. Five over twenty, point two five.","N|Main logic. Take the best step along the direction."),
"Advanced linear algebra 3 — complete",["conjugate gradient","conditioning","tensors","Lie bracket"],"next: advanced probability and statistics","WK29","Walkthrough · CG step size",
L("N|Film twenty nine is complete. Numerical methods, tensors and quadratic forms.","N|Next: advanced probability and statistics."))
# ---------- L30 ----------
make("l30","Advanced Probability 1","Markov chains · random walks · limit theorems",
L("N|Operation Gate. Later learning, film thirty. Advanced probability, part one.","N|Stochastic processes, concentration and limit theorems. Every idea runs as plain Python with comments."),
[dict(key="mark",chap="Room 1 · Stochastic processes",tw="forget the start; spread like sqrt(time)",codes=[(2,"L30A")],
 lines=L("N|Room one. Stochastic processes.","R|How do I model something random that evolves over time?",
 "S|A Markov chain has a transition table. Sunny stays sunny ninety percent of the time, rainy stays rainy fifty percent. Start sunny, apply the table fifty times, and you reach the stationary distribution, zero point eight three three sunny and zero point one six seven rainy, whatever the start.",
 "S|A random walk adds up plus or minus one steps. After a hundred steps, the variance of the position is about a hundred, so the spread grows like the square root of the number of steps. Brownian motion is the continuous limit.",
 "S|Measure theory gives all of this a rigorous foundation, with sigma algebras and Lebesgue integrals.",
 "N|Twist one. A chain forgets its start, and a random walk spreads like the square root of time."),
 vis='''
 if t>=ts[2]:
     lab(d,1000,175,"stationary distribution",WHITE,15);hbars(d,790,200,[("sunny",0.833),("rainy",0.167)],1,w=240,col=[GOLD,TEAL],lw=80,fmt="{:.3f}")
 cards(d,t,ts,[(3,"random walk, 100 steps: variance","≈ 100",GRN)],770,330,470,44)
 '''),
 dict(key="conc",chap="Room 2 · Concentration and CLT",tw="bounds for the worst case, CLT for typical",codes=[(2,"L30B")],
 lines=L("N|Room two. Concentration and limit theorems.","R|How far can an average stray from its expected value?",
 "S|Take sample means of a hundred uniform numbers and ask how often they miss one half by more than point one. In simulation, only four in ten thousand do. Chebyshev's bound says at most zero point oh eight three, and Hoeffding's says at most zero point two seven one. Both are safe, but loose.",
 "S|The central limit theorem says the spread of the mean is sigma over root n. Simulated, zero point oh two eight nine. Predicted, zero point oh two eight nine.",
 "S|The law of large numbers says the mean converges. The modes of convergence, in probability, almost surely and in distribution, describe how.",
 "N|Twist two. Bounds guarantee the worst case. The central limit theorem describes the typical case."),
 vis='''
 if t>=ts[2]:
     lab(d,1000,175,"P(|mean - 0.5| >= 0.1)",WHITE,15);hbars(d,790,200,[("simulated",0.0004),("Chebyshev",0.083),("Hoeffding",0.271)],0.3,w=220,col=[GRN,GOLD,RED],lw=100,fmt="{:g}")
 cards(d,t,ts,[(3,"sd of the mean: simulated","0.0289",TEAL),(3,"sigma / sqrt(n)","0.0289",GOLD)],770,340,470,44,10,16)
 '''),],
L("N|Walkthrough. One step of a Markov chain, line by line.","S|We start sunny for certain. The new probability of sunny is staying sunny, point nine.","S|The new probability of rainy is point one. Repeating this many times gives the stationary distribution.","N|Main logic. Multiply the distribution by the table."),
"Advanced probability 1 — complete",["Markov chain","random walk","Chebyshev","CLT"],"next: information theory and estimation","WK30","Walkthrough · Markov step",
L("N|Film thirty is complete. Stochastic processes and limit theorems.","N|Next: information theory and estimation."))
# ---------- L31 ----------
make("l31","Advanced Statistics 1","information theory · maximum likelihood",
L("N|Operation Gate. Later learning, film thirty one. Information theory and estimation.","N|Entropy, KL divergence, maximum likelihood and the Cramér Rao bound. Every idea runs as plain Python with comments."),
[dict(key="info",chap="Room 1 · Information theory",tw="cross-entropy = entropy + KL",codes=[(2,"L31A")],
 lines=L("N|Room one. Information theory.","R|How do I measure surprise?",
 "S|Entropy is the average surprise in bits. A fair coin has one bit, the most possible. A biased coin, ninety ten, has only zero point four six nine.",
 "S|KL divergence measures how different two distributions are, and it is not symmetric: zero point seven three seven one way, zero point five three one the other.",
 "S|Cross entropy is entropy plus KL: one plus zero point seven three seven is one point seven three seven, which the code confirms. That is why minimising cross entropy loss shrinks the KL.",
 "S|Mutual information measures how much knowing one variable tells you about another. For two related bits it is zero point two seven eight bits.",
 "N|Twist one. Cross entropy equals entropy plus the KL you can still remove."),
 vis='''
 cards(d,t,ts,[(2,"entropy fair / biased coin","1.0  /  0.469",TEAL),(3,"KL(p‖q)  /  KL(q‖p)","0.737  /  0.531",GOLD),(4,"cross-entropy = H + KL","1.737 = 1 + 0.737",GRN),(5,"mutual information","0.278 bits",PUR)],770,200,470,48,12,16)
 '''),
 dict(key="mle",chap="Room 2 · Estimation",tw="best explanation, and how well anything can do",codes=[(2,"L31B")],
 lines=L("N|Room two. Estimation.","R|How do I pick the best value of a parameter from data?",
 "S|Maximum likelihood: choose the value that makes the observed data most probable. For coin flips with true rate point three, the sample mean is zero point two seven eight, and a grid search of the log likelihood peaks at zero point two eight, the same place.",
 "S|Fisher information measures how sharply the likelihood peaks. The Cramér Rao bound says no unbiased estimator can have a standard deviation below one over root Fisher information, here zero point oh two.",
 "S|The method of moments is an older alternative: match sample moments to theoretical ones.",
 "N|Twist two. Maximum likelihood is the best explanation of the data, and Fisher information says how well anything can do."),
 vis='''
 import math as m
 if t>=ts[2]:
     a=Ax(790,200,440,200,(0,1),(-400,0));lab(d,1000,182,"log-likelihood of the data",WHITE,15)
     X=[0.28*500*m.log(p)+(1-0.278)*500*m.log(1-p) for p in [0.01]]
     a.curve(d,lambda p:0.278*500*m.log(p)+(1-0.278)*500*m.log(1-p)-300+300,TEAL,4,xr=(0.03,0.97),ylim=(-400,0))
     a.dot(d,0.278,0.278*500*m.log(0.278)+(1-0.278)*500*m.log(1-0.278),GOLD,9);lab(d,a.px(0.278)+14,a.py(-300)-10,"peak = MLE 0.278",GOLD,14,"lm")
 cards(d,t,ts,[(3,"Cramér-Rao sd bound","0.02",GRN)],770,430,470,40)
 '''),],
L("N|Walkthrough. Entropy of a fair coin.","S|Each outcome has probability one half, and minus log base two of one half is one bit.","S|Averaging gives one bit in total.","N|Main logic. Entropy is average surprise."),
"Information and estimation — complete",["entropy","KL","MLE","Cramér-Rao"],"next: nonparametric methods, GLMs, learning theory","WK31","Walkthrough · entropy",
L("N|Film thirty one is complete. Information theory and maximum likelihood.","N|Next: nonparametric statistics, generalised models and learning theory."))
# ---------- L32 ----------
make("l32","Advanced Statistics 2","resampling · GLMs · regularisation · PAC",
L("N|Operation Gate. Later learning, film thirty two. Nonparametric methods, generalised models and learning theory.","N|Every idea runs as plain Python with comments."),
[dict(key="np",chap="Room 1 · Nonparametric and resampling",tw="let the data speak",codes=[(2,"L32A")],
 lines=L("N|Room one. Nonparametric statistics and resampling.","R|What if I do not want to assume a distribution?",
 "S|Kernel density estimation puts a small bump on every data point and adds them up. At zero, the estimate is zero point four oh seven, close to the true zero point three nine nine.",
 "S|The bootstrap resamples the data with replacement, many times, and recomputes the statistic. The spread of the bootstrap medians, zero point one seven two, estimates the uncertainty of the median with no formula.",
 "S|Importance sampling estimates a rare event by sampling where it happens, then correcting with weights. The probability that a normal exceeds three comes out as zero point oh oh one four, matching the true zero point oh oh one three five.",
 "N|Twist one. Let the data speak: smooth it, resample it, or reweight it."),
 vis='''
 cards(d,t,ts,[(2,"KDE at 0  /  true density","0.407  /  0.399",TEAL),(3,"bootstrap sd of the median","0.172",GOLD),(4,"P(Z > 3) by importance sampling","0.0014",GRN),(4,"true value","0.00135",GRY)],770,200,470,48,12,16)
 '''),
 dict(key="glm",chap="Room 2 · GLMs and learning theory",tw="match the model, shrink, size the data",codes=[(2,"L32B")],
 lines=L("N|Room two. Generalised linear models and learning theory.","R|Linear regression predicts any number. What about yes or no, or counts?",
 "S|A generalised linear model changes the link. Logistic regression models the probability of yes through a sigmoid, and Poisson regression models counts through an exponential. Here gradient ascent fits the logistic weights, five point three nine and minus two point four seven.",
 "S|With many features, regularisation shrinks coefficients. From a least squares estimate of three, ridge shrinks it to one point five, and lasso, by soft thresholding, to two point five. For small coefficients, lasso sets them exactly to zero.",
 "S|Learning theory asks how much data is enough. For a finite family of two to the twenty hypotheses, with error point one and confidence ninety five percent, the PAC bound says one hundred sixty nine samples. The VC dimension extends this to infinite families. Mixed models add random effects for clustered data.",
 "N|Twist two. Match the model to the response, shrink to avoid overfitting, and use theory to size your data."),
 vis='''
 cards(d,t,ts,[(2,"logistic weights  w, b","5.39, -2.47",TEAL),(3,"ridge  /  lasso on 3.0","1.5  /  2.5",GOLD),(4,"PAC sample bound","169",GRN)],770,200,470,48,12,16)
 '''),],
L("N|Walkthrough. Ridge and lasso on one coefficient.","S|The raw estimate is three, and the penalty strength is one.","S|Ridge divides by one plus lambda, giving one point five. Lasso subtracts half lambda, giving two point five.","N|Main logic. Ridge shrinks by a factor. Lasso subtracts, and can reach zero."),
"Advanced statistics 2 — complete",["KDE","bootstrap","GLM","PAC bound"],"next: calculus optimization","WK32","Walkthrough · ridge and lasso",
L("N|Film thirty two is complete. Resampling, generalised models, shrinkage and PAC.","N|Last: calculus optimization."))
# ---------- L33 ----------
make("l33","Calculus Optimization","critical points · second derivative · Lagrange",
L("N|Operation Gate. Later learning, film thirty three. Calculus optimization.","N|Finding the largest and smallest values, with and without constraints. Every idea runs as plain Python with comments."),
[dict(key="crit",chap="Room 1 · Critical points",tw="reduce, differentiate, test, check ends",codes=[(2,"L33A")],
 lines=L("N|Room one. Maximising a quantity.","R|A farmer has one hundred metres of fence. What rectangle has the biggest area?",
 "S|Follow the recipe. The objective is the area, width times height. The constraint says two widths plus two heights make one hundred, so the height is fifty minus the width. Now the area depends on one variable.",
 "S|Find where the first derivative is zero. The code bisects on the numerical derivative and lands at a width of twenty five, an area of six hundred twenty five. The second derivative is minus two, which is negative, so it is a maximum.",
 "S|Always check the endpoints too. Width zero and width fifty both give area zero, far worse.",
 "N|Twist one. Reduce to one variable, set the derivative to zero, test with the second derivative, and check the ends."),
 vis='''
 a=Ax(790,200,440,220,(0,50),(0,700))
 if t>=ts[2]:
     a.axes(d,(0,25,50),(0,300,600));a.curve(d,lambda w:w*(50-w),TEAL,4);lab(d,1000,182,"area = w (50 − w)",WHITE,15)
 if t>=ts[3]:
     a.dot(d,25,625,GOLD,9);d.line([a.P(15,625),a.P(35,625)],fill=GOLD,width=3);lab(d,a.px(25),a.py(625)-18,"f' = 0, f'' = −2",GOLD,14)
 if t>=ts[4]:a.dot(d,0,0,RED,8);a.dot(d,50,0,RED,8)
 '''),
 dict(key="lag",chap="Room 2 · Constraints",tw="parallel gradients at the optimum",codes=[(2,"L33B")],
 lines=L("N|Room two. Constrained optimisation and Lagrange multipliers.","R|What if I cannot easily solve the constraint for one variable?",
 "S|Use a Lagrange multiplier. To maximise x times y with x plus y equal ten, the gradient of the objective must be parallel to the gradient of the constraint. That gives y equals lambda and x equals lambda, so x and y are both five, and the product is twenty five.",
 "S|A brute force check agrees: the best product is twenty five at five. The same idea finds the closest point on the line y equals two x plus three to the origin: x minus one point two, y zero point six, a distance of one point three four two.",
 "S|In machine learning this idea appears everywhere: support vector machines, maximum entropy models and constrained training all rely on Lagrange multipliers.",
 "N|Twist two. At a constrained optimum, the objective can only be improved by breaking the constraint."),
 vis='''
 cards(d,t,ts,[(2,"max of x·y with x + y = 10","x = y = 5,  product 25",GOLD),(2,"multiplier λ","5",TEAL),(3,"brute-force check","(25.0, 5.0)",GRN),(3,"closest point to the origin","(−1.2, 0.6),  d = 1.342",PUR)],770,200,470,48,12,16)
 '''),],
L("N|Walkthrough. Checking a critical point, line by line.","S|The width is twenty five. The first derivative is fifty minus two w, which is zero.","S|The second derivative is minus two. Negative, so the point is a maximum.","N|Main logic. Zero slope, then negative curvature, means a peak."),
"Calculus optimization — complete",["objective","constraint","f' = 0","Lagrange"],"the Later Learning set is complete","WK33","Walkthrough · second derivative test",
L("N|Film thirty three is complete. That finishes the full Later Learning set.","N|Watch them in the order of the sheet. Every code block in every film was run, and the output on screen is the real output."))
