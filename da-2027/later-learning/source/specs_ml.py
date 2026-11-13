from mkfilm import make
def L(*xs):return [(x[0],x[2:]) for x in xs]
# ---------- L20 generative ----------
make("l20","Generative Models","diffusion · autoencoders · GANs · flows",
L("N|Operation Gate. Later learning, film twenty. Generative models.","N|Diffusion, autoencoders, GANs and normalizing flows. Every idea runs as plain Python with comments."),
[dict(key="diff",chap="Room 1 · Diffusion",tw="many small denoising steps",codes=[(2,"L20A")],
 lines=L("N|Room one. Diffusion models.","R|How can a model create a brand new image from nothing?",
 "S|Start from clean data and add a little noise at each step, until almost nothing of the original is left. That is the forward process. Each noisy value mixes the signal with noise.",
 "S|A diffusion model is trained to predict the noise that was added. If it predicts the noise correctly, the formula in the code recovers the clean value exactly. Two point zero, at every step.",
 "S|To generate, start from pure noise and remove the predicted noise step by step. The picture emerges.",
 "N|Twist one. Diffusion turns generation into many small denoising steps, each one easy to learn."),
 vis='''
 if t>=ts[2]:
     lab(d,1000,172,"signal kept  →  noisy value  →  recovered",WHITE,15)
     cards(d,t,ts,[(2,"step 1  (0.90 signal)","1.52  →  2.0",TEAL),(2,"step 2  (0.60)","0.82  →  2.0",TEAL),(3,"step 3  (0.30)","1.66  →  2.0",GOLD),(3,"step 4  (0.05)","-1.79  →  2.0",GOLD)],770,195)
 if t>=ts[4]:lab(d,1000,470,"generate: pure noise → remove noise, step by step",GRN,16)
 '''),
 dict(key="ae",chap="Room 2 · Autoencoders",tw="a bottleneck forces structure",codes=[(2,"L20B")],
 lines=L("N|Room two. Autoencoders.","R|What is a latent variable?",
 "S|An autoencoder squeezes the input through a narrow bottleneck, the latent code, and then tries to rebuild the input. Here two numbers pass through a single number.",
 "S|The data lies on a line, so one number is enough. Training lowers the reconstruction error from eight point four to essentially zero. The model discovered the line.",
 "S|Variational autoencoders go further and make the latent code a distribution, so we can sample new data from it.",
 "N|Twist two. A bottleneck forces the model to learn the structure of the data."),
 vis='''
 if t>=ts[2]:
     a=Ax(790,200,300,240,(-2.5,2.5),(-5,5));a.axes(d,(-2,0,2),(-4,0,4))
     for x in [-2,-1,-0.5,0.5,1,2]:a.dot(d,x,2*x,TEAL,6)
     lab(d,940,185,"data on a line",WHITE,14)
 if t>=ts[3]:
     lab(d,1140,215,"reconstruction error",WHITE,14);vbars(d,1100,235,150,[("before",8.438),("after",0.0)],9,bw=50,gap=20,col=[RED,GRN],fmt="{:g}")
 '''),
 dict(key="gan",chap="Room 3 · GANs and flows",tw="competition, or invertible steps",codes=[(2,"L20C")],
 lines=L("N|Room three. GANs and normalizing flows.","R|What is a GAN?",
 "S|Two networks play a game. A generator makes fakes, and a discriminator tries to tell real from fake. The best possible discriminator outputs the real density over the sum of both densities.",
 "S|When fakes match the data, it outputs zero point five, a coin flip, so it has been fooled. When the fakes are far away, it outputs zero point nine nine.",
 "S|Normalizing flows take a different route. They transform simple noise through an invertible function. By the change of variables rule, the density is the base density divided by the slope. Both numbers match at zero point one seven six, so the density is exact.",
 "N|Twist three. A GAN learns by competition. A flow keeps an exact density by using invertible steps."),
 vis='''
 if t>=ts[2]:
     import math as m
     def pdf(x,mu):return m.exp(-(x-mu)**2/2)/m.sqrt(2*m.pi)
     a=Ax(790,200,440,200,(-3,6),(0,1.05));a.axes(d,(-2,0,2,4,6),(0,0.5,1));lab(d,1000,182,"best discriminator D*(x)",WHITE,15)
     d.line([a.P(-3,0.5),a.P(6,0.5)],fill=TEAL,width=4)
     if t>=ts[3]:a.curve(d,lambda x:pdf(x,0)/(pdf(x,0)+pdf(x,3)),GOLD,4)
     lab(d,1160,a.py(0.5)-14,"fake = real: 0.5",TEAL,14,"rm")
 if t>=ts[4]:lab(d,1000,450,"flow:  p(x) = p(z) / |slope|",WHITE,16);lab(d,1000,485,"0.176 = 0.176",GOLD,22)
 '''),],
L("N|Walkthrough. One diffusion step, line by line.","S|Clean value two, signal fraction zero point six, noise one. The noisy value mixes the square roots of those fractions.","S|To undo it we subtract the noise part and divide by the same square root. We get two point zero back.","N|Main logic. Add noise with a known formula, then remove it with the same formula."),
"Generative models — complete",["diffusion","autoencoder","GAN","flow"],"next: geometric deep learning","WK20","Walkthrough · one diffusion step",
L("N|Film twenty is complete. Diffusion, autoencoders, GANs and flows.","N|Next: geometric deep learning."))
# ---------- L21 geometric ----------
make("l21","Geometric Deep Learning","graph networks · symmetry",
L("N|Operation Gate. Later learning, film twenty one. Geometric deep learning.","N|Graph neural networks and equivariance. Every idea runs as plain Python with comments."),
[dict(key="gnn",chap="Room 1 · Graph networks",tw="repeated neighbour averaging",codes=[(2,"L21A")],
 lines=L("N|Room one. Graph neural networks.","R|Images are grids and text is a line. What about a social network, or a molecule?",
 "S|A graph neural network passes messages. In every layer each node collects its neighbours' features, averages them, and mixes the result with its own.",
 "S|Node zero starts with one, everyone else with zero. After the first layer, nodes one and two have each received a share. After the second layer, node three, two hops away, is no longer zero.",
 "S|So the number of layers is how far information can travel. And the same weights work on any graph, of any size.",
 "N|Twist one. A graph network is repeated neighbour averaging with learned weights."),
 vis='''
 P={0:(900,260),1:(800,340),2:(1000,340),3:(1100,260)}
 if t>=ts[2]:
     for a,b in [(0,1),(0,2),(2,3)]:edge(d,P[a],P[b])
     L1={0:.5,1:.5,2:.25,3:0.0};L2={0:.438,1:.5,2:.25,3:.125};V={0:1.0,1:0.0,2:0.0,3:0.0}
     cur=V if t<ts[3] else (L1 if t<ts[3]+7 else L2)
     for n,(x,y) in P.items():node(d,x,y,str(n),GOLD if cur[n]>0 else TEAL,22,17);lab(d,x,y+38,f"{cur[n]:g}",WHITE,15)
     lab(d,1000,420,"start" if t<ts[3] else ("after layer 1" if t<ts[3]+7 else "after layer 2"),GRN,18)
 '''),
 dict(key="sym",chap="Room 2 · Equivariance",tw="build the symmetry in",codes=[(2,"L21B")],
 lines=L("N|Room two. Symmetry and equivariance.","R|What does equivariant mean?",
 "S|Some changes should not change the answer. Rotate a molecule and the distances between atoms stay exactly the same. The code prints the same three distances before and after rotation.",
 "S|Relabelling the points is another symmetry. A model that is permutation equivariant gives the same outputs, just reordered, which the code confirms with true.",
 "S|Building the symmetry into the architecture means the model does not have to learn it from data. That is group equivariant learning, used for point clouds, molecules and physics.",
 "N|Twist two. Build the symmetry in, and the model needs far less data."),
 vis='''
 import math as m
 if t>=ts[2]:
     pts=[(0,0),(3,0),(3,4)];s=26
     def draw(ox,oy,th,col,name):
         q=[(ox+s*(x*m.cos(th)-y*m.sin(th)),oy-s*(x*m.sin(th)+y*m.cos(th))) for x,y in pts]
         d.polygon(q,outline=col,width=4)
         for p in q:d.ellipse((p[0]-6,p[1]-6,p[0]+6,p[1]+6),fill=col)
         lab(d,ox+40,oy+25,name,col,14)
     draw(800,380,0,TEAL,"original")
     if t>=ts[2]+3:draw(1060,380,0.7,GOLD,"rotated")
     lab(d,1000,210,"distances: 3, 5, 4   |   3, 5, 4",GRN,18)
 if t>=ts[3]:lab(d,1000,470,"permute inputs → outputs permute: True",GRN,17)
 '''),],
L("N|Walkthrough. One message passing update, line by line.","S|Node zero keeps its own value of one. Its two neighbours both hold zero.","S|The update is half of its own value plus half of the neighbour average. That is zero point five.","N|Main logic. Mix yourself with your neighbours."),
"Geometric deep learning — complete",["message passing","hops","rotation","permutation"],"next: optimization and overfitting","WK21","Walkthrough · message passing",
L("N|Film twenty one is complete. Graph networks and equivariance.","N|Next: optimization and loss landscapes."))
# ---------- L22 optimisation ----------
make("l22","Optimization and Overfitting","loss landscapes · momentum · generalisation",
L("N|Operation Gate. Later learning, film twenty two. Optimization and overfitting.","N|Loss landscapes, momentum, and why more parameters can hurt. Every idea runs as plain Python with comments."),
[dict(key="opt",chap="Room 1 · Loss landscapes",tw="start point and step size decide the ending",codes=[(2,"L22A")],
 lines=L("N|Room one. Loss landscapes and optimisation.","R|Why is training deep networks hard if we just follow the slope?",
 "S|The loss is a landscape. In a long narrow valley, plain gradient descent zigzags and is slow. After sixty steps its loss is zero point three two. Momentum keeps a running push and reaches zero point zero two five.",
 "S|Make the learning rate too big and it overshoots every step and explodes, to a loss of five trillion.",
 "S|And the landscape is non convex. With two valleys, starting at minus two ends in the deeper valley, with value minus three point five. Starting at two ends in a shallower one, minus one point oh seven.",
 "N|Twist one. Where you start, and how big your steps are, decide where you end."),
 vis='''
 if t>=ts[2]:
     a=Ax(790,200,260,230,(-2.3,2.3),(-4,6));a.axes(d,(-2,0,2),(-4,0,4));a.curve(d,lambda x:x**4-3*x**2+x,TEAL,4);lab(d,920,182,"two valleys",WHITE,14)
     if t>=ts[4]:a.dot(d,-1.301,-3.514,GRN,8);a.dot(d,1.131,-1.07,GOLD,8)
     cards(d,t,ts,[(2,"plain GD, 60 steps","0.323",GOLD),(2,"with momentum","0.0255",GRN),(3,"learning rate too big","5e12",RED)],1070,200,180,44,10,13)
 '''),
 dict(key="over",chap="Room 2 · Overfitting",tw="predict new data, not old data",codes=[(2,"L22B")],
 lines=L("N|Room two. Overfitting and overparameterisation.","R|If more parameters fit the training data better, why not use a lot?",
 "S|Ten noisy points from a sine wave. A straight line has test error zero point two. A cubic does much better, zero point oh two. A degree nine polynomial fits the training points perfectly, but its test error, zero point oh two seven, is worse than the cubic.",
 "S|That is overfitting: memorising noise. Regularisation, early stopping and more data all fight it.",
 "S|Researchers have also observed that very large networks can still generalise even when they fit the training data perfectly. This is called double descent.",
 "N|Twist two. Fitting the training data is not the goal. Predicting new data is."),
 vis='''
 if t>=ts[2]:
     lab(d,1000,175,"error by polynomial degree",WHITE,15)
     lab(d,880,200,"train",TEAL,13);vbars(d,790,215,150,[("1",.203),("3",.009),("9",0.0)],0.25,bw=40,gap=20,col=TEAL,fs=13,fmt="{:g}")
     lab(d,1130,200,"test",RED,13);vbars(d,1040,215,150,[("1",.207),("3",.02),("9",.027)],0.25,bw=40,gap=20,col=RED,fs=13,fmt="{:g}")
     lab(d,1000,420,"degree 9: train 0, test worse than degree 3",GOLD,16)
 '''),],
L("N|Walkthrough. Gradient descent, line by line.","S|Start at four with learning rate point one. The slope of x squared is two x, so eight.","S|We subtract point one times eight, landing at three point two, then two point five six, then two point oh four eight. Each step shrinks by the same factor.","N|Main logic. Step against the slope."),
"Optimization — complete",["valleys","momentum","overfitting","double descent"],"next: Bayesian methods and uncertainty","WK22","Walkthrough · gradient step",
L("N|Film twenty two is complete. Landscapes, momentum and overfitting.","N|Next: Bayesian methods and uncertainty."))
# ---------- L23 bayes ----------
make("l23","Bayesian Methods and Uncertainty","MCMC · ensembles · variational inference",
L("N|Operation Gate. Later learning, film twenty three. Bayesian deep learning and uncertainty.","N|Sampling, ensembles and variational inference. Every idea runs as plain Python with comments."),
[dict(key="mcmc",chap="Room 1 · MCMC",tw="a random walk that visits by probability",codes=[(2,"L23A")],
 lines=L("N|Room one. Markov chain Monte Carlo.","R|How can I sample from a distribution I can only evaluate up to a constant?",
 "S|Metropolis sampling. From the current point, propose a nearby one. Always accept if it is more probable, and accept a downhill move with probability equal to the ratio. The chain wanders, spending time in proportion to the probability.",
 "S|Our target has two bumps, one at zero and a smaller one at four. After twenty thousand steps, the sample mean is one point eighteen, and thirty one percent of samples are above two. The exact values are one point three three and about thirty four percent. Close, but with sampling noise.",
 "S|That is why Bayesian methods rely on sampling. No formula is needed for the normalising constant.",
 "N|Twist one. MCMC trades exact formulas for a random walk that visits places in proportion to their probability."),
 vis='''
 import math as m
 if t>=ts[2]:
     a=Ax(790,200,440,200,(-4,8),(0,1.1));a.axes(d,(-4,0,4,8),());lab(d,1000,182,"target (unnormalised)",WHITE,15)
     a.curve(d,lambda x:m.exp(-x*x/2)+0.5*m.exp(-(x-4)**2/2),TEAL,4)
 cards(d,t,ts,[(3,"sample mean","1.18  (exact 1.33)",GOLD),(3,"share above 2","0.31  (exact ≈ 0.34)",GOLD)],770,430,470,40,8,16)
 '''),
 dict(key="unc",chap="Room 2 · Uncertainty",tw="turn one answer into a spread",codes=[(2,"L23B"),(4,"L23C")],
 lines=L("N|Room two. Uncertainty.","R|How does a model say, I am not sure?",
 "S|Train many versions on resampled data and compare their predictions. Inside the data the spread is only zero point oh nine. Far outside, at twelve, it is zero point seven eight. Disagreement is the uncertainty.",
 "R|And a faster, approximate Bayesian method?",
 "S|Variational inference picks the simple distribution q closest to the true posterior by minimising KL divergence. Against a two bump posterior, a narrow Gaussian on one bump scores zero point six nine. A wide one in the middle scores two point oh two, and a narrow one in the middle, five point four two. So it picks one bump and misses the other. That is its known bias, in return for speed.",
 "N|Twist two. Ensembles and variational inference both turn a single answer into a spread of answers."),
 vis='''
 if t>=ts[2] and t<ts[4]:
     lab(d,1000,175,"prediction spread (sd)",WHITE,15);hbars(d,790,200,[("inside data",0.09),("far outside",0.78)],0.8,w=240,col=[GRN,RED],lw=110,fmt="{:g}")
 if t>=ts[4]:
     lab(d,1000,175,"KL(q || p) for three choices of q",WHITE,15)
     cards(d,t,ts,[(4,"narrow on one bump","0.69",GRN),(4,"wide, in the middle","2.02",GOLD),(4,"narrow, in the middle","5.42",RED)],770,200,470,44,10,16)
 '''),],
L("N|Walkthrough. The accept step, line by line.","S|The current point has probability point two. The proposal has probability point one.","S|The ratio is one half, so we accept the move with probability one half.","N|Main logic. Uphill always, downhill sometimes."),
"Bayesian methods — complete",["Metropolis","ensemble","spread","variational"],"next: causality and game theory","WK23","Walkthrough · accept step",
L("N|Film twenty three is complete. MCMC, ensembles and variational inference.","N|Next: causality and game theory."))
# ---------- L24 causality, games ----------
make("l24","Causality and Game Theory","confounders · adjustment · Nash equilibrium",
L("N|Operation Gate. Later learning, film twenty four. Causality and game theory.","N|Confounders, adjustment and equilibria. Every idea runs as plain Python with comments."),
[dict(key="cause",chap="Room 1 · Causality",tw="compare like with like, or randomise",codes=[(2,"L24A")],
 lines=L("N|Room one. Causal inference.","R|Patients who got the treatment did worse. Is the treatment harmful?",
 "S|Not necessarily. Here sicker patients were more likely to be treated. Severity is a hidden cause of both treatment and outcome, a confounder. The naive difference is minus two point one, which says the treatment hurts.",
 "S|But compare like with like. Within each severity group, the treatment effect is plus one point oh. The true effect is positive.",
 "S|Correlation is not causation. Adjusting for confounders, or running a randomised experiment, is how we separate them. Structural causal models make those assumptions explicit.",
 "N|Twist one. Compare like with like, or randomise, to find the causal effect."),
 vis='''
 P={"Z":(900,230),"X":(800,340),"Y":(1000,340)}
 if t>=ts[2]:
     for a,b in [("Z","X"),("Z","Y"),("X","Y")]:arrow(d,P[a],P[b],GRY,3,12)
     for n,(x,y) in P.items():node(d,x,y,n,GOLD if n=="Z" else TEAL,24,18)
     lab(d,1000,190,"Z = severity (hidden)",GOLD,14);lab(d,800,385,"X treatment",TEAL,14);lab(d,1000,385,"Y outcome",TEAL,14)
 cards(d,t,ts,[(2,"naive difference","-2.1",RED),(3,"adjusted for severity","+1.0",GRN)],770,430,470,40,8,16)
 '''),
 dict(key="game",chap="Room 2 · Game theory",tw="best choices depend on the others",codes=[(2,"L24B")],
 lines=L("N|Room two. Game theory.","R|What if several learners interact, like drivers in traffic, or bidders in an auction?",
 "S|A Nash equilibrium is a set of choices where nobody gains by switching alone. In the prisoner's dilemma, defect, defect is the only one, even though both cooperating would pay more.",
 "S|Some games have no pure equilibrium. In matching pennies, each player best responds to the other's history, and the frequencies settle near one half each. The equilibrium is mixed.",
 "S|Multi agent learning, auctions and generative adversarial networks all rest on this idea.",
 "N|Twist two. In a game, each learner's best choice depends on the others."),
 vis='''
 if t>=ts[2]:
     lab(d,1000,175,"prisoner's dilemma (row, column)",WHITE,15)
     pay={(0,0):"3,3",(0,1):"0,5",(1,0):"5,0",(1,1):"1,1"};nm=["C","D"]
     for r in range(2):
         lab(d,800,235+r*80,nm[r],GOLD,18)
         for c in range(2):
             nash=(r,c)==(1,1)
             cell(d,830+c*130,205+r*80,120,70,pay[(r,c)],GRN if (nash and t>=ts[2]+4) else TEAL,fs=20)
     for c in range(2):lab(d,890+c*130,190,nm[c],GOLD,18)
     if t>=ts[2]+4:lab(d,1000,385,"Nash equilibrium: (D, D)",GRN,18)
 if t>=ts[3]:lab(d,1000,440,"matching pennies: both settle near 0.5",GOLD,17)
 '''),],
L("N|Walkthrough. The naive comparison.","S|Treated outcomes average three and a half. Untreated average five and a half.","S|The difference is minus two, which looks harmful. But the groups were not alike to begin with.","N|Main logic. Check that groups are comparable before comparing outcomes."),
"Causality and games — complete",["confounder","adjustment","Nash","mixed strategy"],"next: state space models, boosting, kernels","WK24","Walkthrough · naive comparison",
L("N|Film twenty four is complete. Causality and game theory.","N|Next: state space models, boosting and kernels."))
# ---------- L25 ----------
make("l25","SSMs, Boosting and Kernels","Mamba idea · gradient boosting · kernel trick",
L("N|Operation Gate. Later learning, film twenty five. State space models, boosting and kernels.","N|Three more modern architectures and tools. Every idea runs as plain Python with comments."),
[dict(key="ssm",chap="Room 1 · State space models",tw="a recurrence with linear cost",codes=[(2,"L25A")],
 lines=L("N|Room one. State space models.","R|Transformers are slow on very long inputs. What is the alternative?",
 "S|A state space model keeps a small hidden state, updated once per input. The new state is a times the old state, plus b times the input. The output reads the state.",
 "S|The code shows the neat part. The same model can be written as a convolution with a fixed kernel, and the two outputs match exactly. It prints true.",
 "S|Cost matters. For a thousand steps, the recurrence does about a thousand updates. Attention compares every pair, about a million. Models such as Mamba make the state parameters depend on the input, to keep the linear cost with strong accuracy.",
 "N|Twist one. A state space model is a recurrence you can also train as a convolution, with linear cost."),
 vis='''
 if t>=ts[2]:
     lab(d,1000,175,"output after each input",WHITE,15);vbars(d,790,200,120,[("1",.5),("2",.4),("3",.32),("4",1.256),("5",1.005)],1.3,bw=50,gap=22,col=TEAL,fs=13,fmt="{:g}")
 if t>=ts[3]:lab(d,1000,375,"recurrence == convolution: True",GRN,17)
 if t>=ts[4]:hbars(d,790,415,[("SSM",1000),("attention",1000000)],1000000,w=240,col=[GRN,RED],lw=90,fmt="{:,}")
 '''),
 dict(key="boost",chap="Room 2 · Gradient boosting",tw="each weak model fixes the last",codes=[(2,"L25B")],
 lines=L("N|Room two. Gradient boosting.","R|How do many weak models become a strong one?",
 "S|Start from the average. Then repeatedly fit a very simple model, a stump with one split, to the residual errors, and add a small step of it. Each round fixes what the previous ones missed.",
 "S|The mean squared error falls from one point one four, to zero point three two, zero point one one five, and zero point oh three nine after the fourth round.",
 "S|The weak models are trees, the sum of them is the ensemble, and a small learning rate keeps each step from overfitting. For tabular data, boosted trees are often the strongest baseline.",
 "N|Twist two. Boosting adds simple models, one correction at a time."),
 vis='''
 if t>=ts[2]:
     lab(d,1000,175,"mean squared error after each round",WHITE,15)
     vbars(d,800,200,170,[("1",1.142),("2",.32),("3",.115),("4",.039)],1.2,bw=70,gap=30,col=[RED,GOLD,GOLD,GRN],fmt="{:g}")
 '''),
 dict(key="kern",chap="Room 3 · Kernels and SVMs",tw="curved boundary for the price of a dot product",codes=[(2,"L25C")],
 lines=L("N|Room three. Kernels and support vector machines.","R|How can a straight line separate points that no straight line can separate?",
 "S|Map the points into a bigger space where a line works. The kernel trick says we never need to build that space. A kernel computes the dot product there directly. Here the explicit three dimensional map and the simple formula both give twenty five.",
 "S|The exclusive or pattern cannot be split by any straight line in two dimensions. With the polynomial kernel, even a simple perceptron learns it. The code prints the right labels: one, one, minus one, minus one.",
 "S|Support vector machines pair this trick with the widest possible margin.",
 "N|Twist three. A kernel gives you a curved boundary at the price of a dot product."),
 vis='''
 if t>=ts[2]:
     a=Ax(800,200,240,240,(-2,2),(-2,2));a.axes(d,(-1,1),(-1,1))
     for (x,y),c in [((1,1),GRN),((-1,-1),GRN),((1,-1),RED),((-1,1),RED)]:a.dot(d,x,y,c,9)
     lab(d,920,182,"XOR: no line separates",WHITE,14)
 cards(d,t,ts,[(2,"feature map dot","25.0",GOLD),(2,"kernel formula","25",GOLD),(3,"kernel perceptron on XOR","1, 1, -1, -1",GRN)],1060,210,190,50,10,13)
 '''),],
L("N|Walkthrough. A fading memory, line by line.","S|The state starts at zero. Input one arrives, so the state becomes one.","S|With no more input the state decays by zero point eight each step. First zero point eight, then zero point six four.","N|Main logic. A little memory that fades."),
"SSMs, boosting, kernels — complete",["state space","Mamba idea","boosting","kernel trick"],"next: reinforcement learning, decisions","WK25","Walkthrough · fading memory",
L("N|Film twenty five is complete. State space models, boosting and kernels.","N|Next: decision making with reinforcement learning."))
# ---------- L26 ----------
make("l26","RL: Decision Making","MDPs · value iteration · policy gradients",
L("N|Operation Gate. Later learning, film twenty six. Reinforcement learning and decision making.","N|Markov decision processes and policy gradients. Every idea runs as plain Python with comments."),
[dict(key="mdp",chap="Room 1 · MDPs",tw="a long plan as repeated one-step lookups",codes=[(2,"L26A")],
 lines=L("N|Room one. Markov decision processes.","R|How does an agent plan when its actions change the future?",
 "S|A Markov decision process has states, actions, rewards and a discount. The value of a state is the best immediate reward plus the discounted value of where you land. That is the Bellman equation.",
 "S|In the code, from state one, going gives ten. From state zero, going gives one plus point nine times ten, which is nine point nine, close to ten after rounding. Value iteration sweeps until the values stop changing.",
 "S|The best policy is read off the values: go, go.",
 "N|Twist one. Value iteration turns a long term plan into repeated one step lookups."),
 vis='''
 if t>=ts[2]:
     X=[820,1000,1180]
     for i in range(2):arrow(d,(X[i]+24,260),(X[i+1]-24,260),GRN,4,12)
     for i,n in enumerate(["s0","s1","end"]):node(d,X[i],260,n,GOLD if i==2 else TEAL,26,16)
     lab(d,910,235,"go: +1",GRN,14);lab(d,1090,235,"go: +10",GRN,14)
 cards(d,t,ts,[(3,"V(s1) after sweep 1","10.0",GOLD),(3,"V(s0) after sweep 2","10.0",GOLD),(4,"policy","go, go",GRN)],770,330,470,44,10,16)
 '''),
 dict(key="pg",chap="Room 2 · Policy gradients",tw="make rewarded actions more likely",codes=[(2,"L26B")],
 lines=L("N|Room two. Policy gradients.","R|What if there are too many states to keep a table of values?",
 "S|Learn the policy directly. A sigmoid policy gives the probability of picking arm one. After every pull, if the reward was one, nudge the preference towards the action that was taken.",
 "S|After two thousand pulls the policy picks the better arm with probability zero point nine seven. This is the REINFORCE method behind many robotics and language model training methods.",
 "S|Decision making for robotics adds sensors, safety limits and simulation, but the learning idea is the same.",
 "N|Twist two. Policy gradient makes rewarded actions more likely, without needing a value table."),
 vis='''
 if t>=ts[2]:
     lab(d,1000,175,"true win rates",WHITE,15);hbars(d,790,200,[("arm 0",0.3),("arm 1",0.7)],1,w=240,col=[RED,GRN],lw=80)
 if t>=ts[3]:
     lab(d,1000,320,"learned P(pick arm 1)",WHITE,15);hbars(d,790,345,[("start",0.5),("after",0.97)],1,w=240,col=[GRY,GRN],lw=80)
 '''),],
L("N|Walkthrough. One Bellman backup, line by line.","S|The next state is worth ten, and the reward is one.","S|The value is the reward plus point nine times ten. That is ten.","N|Main logic. Reward now plus discounted value later."),
"RL decisions — complete",["MDP","Bellman","value iteration","policy gradient"],"next: advanced linear algebra","WK26","Walkthrough · Bellman backup",
L("N|Film twenty six is complete. Markov decision processes and policy gradients.","N|Next: advanced linear algebra."))
