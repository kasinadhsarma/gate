N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film twenty four. Causality and game theory.'),
(N,'Confounders, adjustment and equilibria. Every idea runs as plain Python with comments.')],
"cause":[
(N,'Room one. Causal inference.'),
(R,'Patients who got the treatment did worse. Is the treatment harmful?'),
(S,'Not necessarily. Here sicker patients were more likely to be treated. Severity is a hidden cause of both treatment and outcome, a confounder. The naive difference is minus two point one, which says the treatment hurts.'),
(S,'But compare like with like. Within each severity group, the treatment effect is plus one point oh. The true effect is positive.'),
(S,'Correlation is not causation. Adjusting for confounders, or running a randomised experiment, is how we separate them. Structural causal models make those assumptions explicit.'),
(N,'Twist one. Compare like with like, or randomise, to find the causal effect.')],
"game":[
(N,'Room two. Game theory.'),
(R,'What if several learners interact, like drivers in traffic, or bidders in an auction?'),
(S,"A Nash equilibrium is a set of choices where nobody gains by switching alone. In the prisoner's dilemma, defect, defect is the only one, even though both cooperating would pay more."),
(S,"Some games have no pure equilibrium. In matching pennies, each player best responds to the other's history, and the frequencies settle near one half each. The equilibrium is mixed."),
(S,'Multi agent learning, auctions and generative adversarial networks all rest on this idea.'),
(N,"Twist two. In a game, each learner's best choice depends on the others.")],
"wk":[
(N,'Walkthrough. The naive comparison.'),
(S,'Treated outcomes average three and a half. Untreated average five and a half.'),
(S,'The difference is minus two, which looks harmful. But the groups were not alike to begin with.'),
(N,'Main logic. Check that groups are comparable before comparing outcomes.')],
"end":[
(N,'Film twenty four is complete. Causality and game theory.'),
(N,'Next: state space models, boosting and kernels.')],
}
