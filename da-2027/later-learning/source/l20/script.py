N,R,S="N","R","S"
SCENES={
"title":[
(N,'Operation Gate. Later learning, film twenty. Generative models.'),
(N,'Diffusion, autoencoders, GANs and normalizing flows. Every idea runs as plain Python with comments.')],
"diff":[
(N,'Room one. Diffusion models.'),
(R,'How can a model create a brand new image from nothing?'),
(S,'Start from clean data and add a little noise at each step, until almost nothing of the original is left. That is the forward process. Each noisy value mixes the signal with noise.'),
(S,'A diffusion model is trained to predict the noise that was added. If it predicts the noise correctly, the formula in the code recovers the clean value exactly. Two point zero, at every step.'),
(S,'To generate, start from pure noise and remove the predicted noise step by step. The picture emerges.'),
(N,'Twist one. Diffusion turns generation into many small denoising steps, each one easy to learn.')],
"ae":[
(N,'Room two. Autoencoders.'),
(R,'What is a latent variable?'),
(S,'An autoencoder squeezes the input through a narrow bottleneck, the latent code, and then tries to rebuild the input. Here two numbers pass through a single number.'),
(S,'The data lies on a line, so one number is enough. Training lowers the reconstruction error from eight point four to essentially zero. The model discovered the line.'),
(S,'Variational autoencoders go further and make the latent code a distribution, so we can sample new data from it.'),
(N,'Twist two. A bottleneck forces the model to learn the structure of the data.')],
"gan":[
(N,'Room three. GANs and normalizing flows.'),
(R,'What is a GAN?'),
(S,'Two networks play a game. A generator makes fakes, and a discriminator tries to tell real from fake. The best possible discriminator outputs the real density over the sum of both densities.'),
(S,'When fakes match the data, it outputs zero point five, a coin flip, so it has been fooled. When the fakes are far away, it outputs zero point nine nine.'),
(S,'Normalizing flows take a different route. They transform simple noise through an invertible function. By the change of variables rule, the density is the base density divided by the slope. Both numbers match at zero point one seven six, so the density is exact.'),
(N,'Twist three. A GAN learns by competition. A flow keeps an exact density by using invertible steps.')],
"wk":[
(N,'Walkthrough. One diffusion step, line by line.'),
(S,'Clean value two, signal fraction zero point six, noise one. The noisy value mixes the square roots of those fractions.'),
(S,'To undo it we subtract the noise part and divide by the same square root. We get two point zero back.'),
(N,'Main logic. Add noise with a known formula, then remove it with the same formula.')],
"end":[
(N,'Film twenty is complete. Diffusion, autoencoders, GANs and flows.'),
(N,'Next: geometric deep learning.')],
}
