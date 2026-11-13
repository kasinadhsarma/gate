N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film twenty five. State space models, boosting and kernels.'),
(N,'Three more modern architectures and tools. Every idea runs as plain Python with comments.')],
"ssm":[
(N,'Room one. State space models.'),
(R,'Transformers are slow on very long inputs. What is the alternative?'),
(S,'A state space model keeps a small hidden state, updated once per input. The new state is a times the old state, plus b times the input. The output reads the state.'),
(S,'The code shows the neat part. The same model can be written as a convolution with a fixed kernel, and the two outputs match exactly. It prints true.'),
(S,'Cost matters. For a thousand steps, the recurrence does about a thousand updates. Attention compares every pair, about a million. Models such as Mamba make the state parameters depend on the input, to keep the linear cost with strong accuracy.'),
(N,'Twist one. A state space model is a recurrence you can also train as a convolution, with linear cost.')],
"boost":[
(N,'Room two. Gradient boosting.'),
(R,'How do many weak models become a strong one?'),
(S,'Start from the average. Then repeatedly fit a very simple model, a stump with one split, to the residual errors, and add a small step of it. Each round fixes what the previous ones missed.'),
(S,'The mean squared error falls from one point one four, to zero point three two, zero point one one five, and zero point oh three nine after the fourth round.'),
(S,'The weak models are trees, the sum of them is the ensemble, and a small learning rate keeps each step from overfitting. For tabular data, boosted trees are often the strongest baseline.'),
(N,'Twist two. Boosting adds simple models, one correction at a time.')],
"kern":[
(N,'Room three. Kernels and support vector machines.'),
(R,'How can a straight line separate points that no straight line can separate?'),
(S,'Map the points into a bigger space where a line works. The kernel trick says we never need to build that space. A kernel computes the dot product there directly. Here the explicit three dimensional map and the simple formula both give twenty five.'),
(S,'The exclusive or pattern cannot be split by any straight line in two dimensions. With the polynomial kernel, even a simple perceptron learns it. The code prints the right labels: one, one, minus one, minus one.'),
(S,'Support vector machines pair this trick with the widest possible margin.'),
(N,'Twist three. A kernel gives you a curved boundary at the price of a dot product.')],
"wk":[
(N,'Walkthrough. A fading memory, line by line.'),
(S,'The state starts at zero. Input one arrives, so the state becomes one.'),
(S,'With no more input the state decays by zero point eight each step. First zero point eight, then zero point six four.'),
(N,'Main logic. A little memory that fades.')],
"end":[
(N,'Film twenty five is complete. State space models, boosting and kernels.'),
(N,'Next: decision making with reinforcement learning.')],
}
