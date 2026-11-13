N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film twenty two. Optimization and overfitting.'),
(N,'Loss landscapes, momentum, and why more parameters can hurt. Every idea runs as plain Python with comments.')],
"opt":[
(N,'Room one. Loss landscapes and optimisation.'),
(R,'Why is training deep networks hard if we just follow the slope?'),
(S,'The loss is a landscape. In a long narrow valley, plain gradient descent zigzags and is slow. After sixty steps its loss is zero point three two. Momentum keeps a running push and reaches zero point zero two five.'),
(S,'Make the learning rate too big and it overshoots every step and explodes, to a loss of five trillion.'),
(S,'And the landscape is non convex. With two valleys, starting at minus two ends in the deeper valley, with value minus three point five. Starting at two ends in a shallower one, minus one point oh seven.'),
(N,'Twist one. Where you start, and how big your steps are, decide where you end.')],
"over":[
(N,'Room two. Overfitting and overparameterisation.'),
(R,'If more parameters fit the training data better, why not use a lot?'),
(S,'Ten noisy points from a sine wave. A straight line has test error zero point two. A cubic does much better, zero point oh two. A degree nine polynomial fits the training points perfectly, but its test error, zero point oh two seven, is worse than the cubic.'),
(S,'That is overfitting: memorising noise. Regularisation, early stopping and more data all fight it.'),
(S,'Researchers have also observed that very large networks can still generalise even when they fit the training data perfectly. This is called double descent.'),
(N,'Twist two. Fitting the training data is not the goal. Predicting new data is.')],
"wk":[
(N,'Walkthrough. Gradient descent, line by line.'),
(S,'Start at four with learning rate point one. The slope of x squared is two x, so eight.'),
(S,'We subtract point one times eight, landing at three point two, then two point five six, then two point oh four eight. Each step shrinks by the same factor.'),
(N,'Main logic. Step against the slope.')],
"end":[
(N,'Film twenty two is complete. Landscapes, momentum and overfitting.'),
(N,'Next: Bayesian methods and uncertainty.')],
}
