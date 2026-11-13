N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film twenty eight. Advanced linear algebra, part two.'),
(N,'Decompositions and canonical forms. Every idea runs as plain Python with comments.')],
"svd":[
(N,'Room one. The singular value decomposition.'),
(R,'Does every matrix have a nice decomposition, even a rectangular one?'),
(S,'Yes, the SVD. Any matrix equals orthogonal, times diagonal, times orthogonal. The diagonal holds the singular values, here five and three. They measure how important each direction is.'),
(S,'Keeping only the largest gives the best low rank approximation. The error is exactly the next singular value, three. The pseudo inverse, built from the SVD, projects onto the row space, which is how least squares works for any matrix.'),
(S,'In machine learning this is used for compression, recommendation and PCA.'),
(N,'Twist one. Keep the big singular values and you keep most of the matrix.')],
"jordan":[
(N,'Room two. Canonical forms and the spectral theorem.'),
(R,'Can every matrix be diagonalised?'),
(S,'No. The Jordan block with eigenvalue two repeated has only one eigenvector, so the rank of N is one. N squared is zero, which makes it nilpotent. Its powers are not just two to the n. The corner entry is n times two to the n minus one: thirty two and eighty for n equals five.'),
(S,'Jordan form says every matrix over the complex numbers is block diagonal made of such pieces.'),
(S,'Symmetric matrices are the nice case. The spectral theorem says they have real eigenvalues, two point three eight and four point six two here, and orthogonal eigenvectors. If all eigenvalues are positive, a Cholesky factor exists, which the code confirms.'),
(N,'Twist two. Not every matrix diagonalises, but symmetric ones always do, with orthogonal eigenvectors.')],
"wk":[
(N,'Walkthrough. How much does one singular value explain?'),
(S,'Singular values are five and three. Their squares are twenty five and nine.'),
(S,'The first explains twenty five out of thirty four, about seventy three and a half percent.'),
(N,'Main logic. The share of squared singular values is the share of energy.')],
"end":[
(N,'Film twenty eight is complete. SVD, Jordan form and the spectral theorem.'),
(N,'Next: numerical linear algebra and tensors.')],
}
