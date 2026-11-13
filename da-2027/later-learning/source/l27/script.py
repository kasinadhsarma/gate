N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film twenty seven. Advanced linear algebra, part one.'),
(N,'Abstract vector spaces, linear maps and inner products. Every idea runs as plain Python with comments.')],
"vs":[
(N,'Room one. Abstract vector spaces and linear maps.'),
(R,'Vectors are arrows in R n. Why generalise?'),
(S,'Because many things behave like vectors. Polynomials can be added and scaled, so they form a vector space. With basis one, x and x squared, the polynomial five plus three x plus four x squared is just the list five, three, four.'),
(S,'The derivative becomes a matrix. Applying it gives three, eight, zero, meaning three plus eight x. Calculus has turned into matrix multiplication.'),
(S,'The rank nullity theorem says rank plus nullity equals the number of columns. Our matrix has rank two, so nullity two, and the check prints true. And changing basis gives a similar matrix with the same eigenvalues, two and three.'),
(N,'Twist one. Anything you can add and scale is a vector, and a linear map is then just a matrix.')],
"ip":[
(N,'Room two. Inner products and fields.'),
(R,'How do I build perpendicular directions from any set of vectors?'),
(S,'Gram Schmidt. Take each vector and subtract its parts along the earlier directions, then normalise. The product of the result with its transpose is the identity, so the vectors are orthonormal. This is the heart of the QR decomposition.'),
(S,'The field matters too. The same three vectors have rank three over the real numbers, but only rank two when arithmetic is done modulo two, because they add up to zero there.'),
(S,'Finite fields like this are used in error correcting codes and cryptography.'),
(N,'Twist two. Orthogonalise to simplify, and remember that the answer depends on the field.')],
"wk":[
(N,'Walkthrough. One Gram Schmidt step, line by line.'),
(S,'The vector is one, one. The earlier direction is one, zero.'),
(S,'The dot product is one, so we subtract one times the direction, leaving zero, one.'),
(N,'Main logic. Remove what you already have.')],
"end":[
(N,'Film twenty seven is complete. Vector spaces, linear maps and orthogonalisation.'),
(N,'Next: decompositions and canonical forms.')],
}
