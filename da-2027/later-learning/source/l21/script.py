N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film twenty one. Geometric deep learning.'),
(N,'Graph neural networks and equivariance. Every idea runs as plain Python with comments.')],
"gnn":[
(N,'Room one. Graph neural networks.'),
(R,'Images are grids and text is a line. What about a social network, or a molecule?'),
(S,"A graph neural network passes messages. In every layer each node collects its neighbours' features, averages them, and mixes the result with its own."),
(S,'Node zero starts with one, everyone else with zero. After the first layer, nodes one and two have each received a share. After the second layer, node three, two hops away, is no longer zero.'),
(S,'So the number of layers is how far information can travel. And the same weights work on any graph, of any size.'),
(N,'Twist one. A graph network is repeated neighbour averaging with learned weights.')],
"sym":[
(N,'Room two. Symmetry and equivariance.'),
(R,'What does equivariant mean?'),
(S,'Some changes should not change the answer. Rotate a molecule and the distances between atoms stay exactly the same. The code prints the same three distances before and after rotation.'),
(S,'Relabelling the points is another symmetry. A model that is permutation equivariant gives the same outputs, just reordered, which the code confirms with true.'),
(S,'Building the symmetry into the architecture means the model does not have to learn it from data. That is group equivariant learning, used for point clouds, molecules and physics.'),
(N,'Twist two. Build the symmetry in, and the model needs far less data.')],
"wk":[
(N,'Walkthrough. One message passing update, line by line.'),
(S,'Node zero keeps its own value of one. Its two neighbours both hold zero.'),
(S,'The update is half of its own value plus half of the neighbour average. That is zero point five.'),
(N,'Main logic. Mix yourself with your neighbours.')],
"end":[
(N,'Film twenty one is complete. Graph networks and equivariance.'),
(N,'Next: optimization and loss landscapes.')],
}
