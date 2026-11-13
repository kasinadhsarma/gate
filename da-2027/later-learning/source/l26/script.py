N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film twenty six. Reinforcement learning and decision making.'),
(N,'Markov decision processes and policy gradients. Every idea runs as plain Python with comments.')],
"mdp":[
(N,'Room one. Markov decision processes.'),
(R,'How does an agent plan when its actions change the future?'),
(S,'A Markov decision process has states, actions, rewards and a discount. The value of a state is the best immediate reward plus the discounted value of where you land. That is the Bellman equation.'),
(S,'In the code, from state one, going gives ten. From state zero, going gives one plus point nine times ten, which is nine point nine, close to ten after rounding. Value iteration sweeps until the values stop changing.'),
(S,'The best policy is read off the values: go, go.'),
(N,'Twist one. Value iteration turns a long term plan into repeated one step lookups.')],
"pg":[
(N,'Room two. Policy gradients.'),
(R,'What if there are too many states to keep a table of values?'),
(S,'Learn the policy directly. A sigmoid policy gives the probability of picking arm one. After every pull, if the reward was one, nudge the preference towards the action that was taken.'),
(S,'After two thousand pulls the policy picks the better arm with probability zero point nine seven. This is the REINFORCE method behind many robotics and language model training methods.'),
(S,'Decision making for robotics adds sensors, safety limits and simulation, but the learning idea is the same.'),
(N,'Twist two. Policy gradient makes rewarded actions more likely, without needing a value table.')],
"wk":[
(N,'Walkthrough. One Bellman backup, line by line.'),
(S,'The next state is worth ten, and the reward is one.'),
(S,'The value is the reward plus point nine times ten. That is ten.'),
(N,'Main logic. Reward now plus discounted value later.')],
"end":[
(N,'Film twenty six is complete. Markov decision processes and policy gradients.'),
(N,'Next: advanced linear algebra.')],
}
