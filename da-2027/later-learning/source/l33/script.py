N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film thirty three. Calculus optimization.'),
(N,'Finding the largest and smallest values, with and without constraints. Every idea runs as plain Python with comments.')],
"crit":[
(N,'Room one. Maximising a quantity.'),
(R,'A farmer has one hundred metres of fence. What rectangle has the biggest area?'),
(S,'Follow the recipe. The objective is the area, width times height. The constraint says two widths plus two heights make one hundred, so the height is fifty minus the width. Now the area depends on one variable.'),
(S,'Find where the first derivative is zero. The code bisects on the numerical derivative and lands at a width of twenty five, an area of six hundred twenty five. The second derivative is minus two, which is negative, so it is a maximum.'),
(S,'Always check the endpoints too. Width zero and width fifty both give area zero, far worse.'),
(N,'Twist one. Reduce to one variable, set the derivative to zero, test with the second derivative, and check the ends.')],
"lag":[
(N,'Room two. Constrained optimisation and Lagrange multipliers.'),
(R,'What if I cannot easily solve the constraint for one variable?'),
(S,'Use a Lagrange multiplier. To maximise x times y with x plus y equal ten, the gradient of the objective must be parallel to the gradient of the constraint. That gives y equals lambda and x equals lambda, so x and y are both five, and the product is twenty five.'),
(S,'A brute force check agrees: the best product is twenty five at five. The same idea finds the closest point on the line y equals two x plus three to the origin: x minus one point two, y zero point six, a distance of one point three four two.'),
(S,'In machine learning this idea appears everywhere: support vector machines, maximum entropy models and constrained training all rely on Lagrange multipliers.'),
(N,'Twist two. At a constrained optimum, the objective can only be improved by breaking the constraint.')],
"wk":[
(N,'Walkthrough. Checking a critical point, line by line.'),
(S,'The width is twenty five. The first derivative is fifty minus two w, which is zero.'),
(S,'The second derivative is minus two. Negative, so the point is a maximum.'),
(N,'Main logic. Zero slope, then negative curvature, means a peak.')],
"end":[
(N,'Film thirty three is complete. Four LeetCode films come next.'),
(N,'Watch them in the order of the sheet. Every code block in every film was run, and the output on screen is the real output.')],
}
