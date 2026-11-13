N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film twenty nine. Advanced linear algebra, part three.'),
(N,'Iterative solvers, tensors, Lie brackets and quadratic forms. Every idea runs as plain Python with comments.')],
"ncon":[
(N,'Room one. Numerical linear algebra.'),
(R,'Solving a big system exactly is slow. What do real programs do?'),
(S,'Iterative methods. Conjugate gradient solves a symmetric positive definite system using only matrix vector products. For a two by two system it needs two steps, and it matches the direct solver: zero point oh nine oh nine, zero point six three six four.'),
(S,'Conditioning matters. The Hilbert matrix of size six has a condition number of one point five times ten to the seven. A tiny rounding error in the input can become a big error in the answer.'),
(S,'Sparse solvers, steepest descent and preconditioners are all variations on these ideas.'),
(N,'Twist one. Iterate with cheap products, and watch the condition number.')],
"tens":[
(N,'Room two. Tensors, determinants, Lie brackets and quadratic forms.'),
(R,'What is a tensor, in practice?'),
(S,'A tensor generalises vectors and matrices to more indices. The tensor product of two vectors is their outer product, a rank one matrix, as printed. Libraries such as einsum write any contraction in one line.'),
(S,'The determinant is an alternating multilinear form. Swap two rows and the sign flips, from minus two to two.'),
(S,'The commutator of two matrices, X Y minus Y X, is the Lie bracket. It measures how much two transformations fail to commute, and underlies rotations and symmetries.'),
(S,'Finally, a quadratic form whose Hessian has all positive eigenvalues, here zero point seven nine three and two point two oh seven, is bowl shaped, so a stationary point is a minimum.'),
(N,'Twist two. Tensors, determinants and brackets describe structure. Positive eigenvalues describe a minimum.')],
"wk":[
(N,'Walkthrough. A conjugate gradient step size, line by line.'),
(S,'The residual is one, two. The matrix times the direction is six, seven.'),
(S,'The step size is residual dot residual over direction dot A direction. Five over twenty, point two five.'),
(N,'Main logic. Take the best step along the direction.')],
"end":[
(N,'Film twenty nine is complete. Numerical methods, tensors and quadratic forms.'),
(N,'Next: advanced probability and statistics.')],
}
