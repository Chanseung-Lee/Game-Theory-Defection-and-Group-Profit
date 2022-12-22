# Game-Theory-Defection-and-Group-Profit

Link to the published research paper: To Be Added Soon!

This is the short code section that accompanies the collaborative research paper that's been accepted and published to the Applied Artificial Intelligence journal. The research paper has been accepted on December 8th, 2022.

***Most research endeavors have been conducted analytically and mathematically***, thus the final code segments are relatively simple in comparison due to their main purpose being simply to verify the conclusions from the research output. Details of the involved mathematics can be found on the published paper!

# Introduction
The prisoner’s dilemma is a game theory framework illustrating two rational individuals making decisions in their own self-interest. Two players simultaneously take a choice between two options: to cooperate, or to defect. If two players repeat the same prisoner’s dilemma game in succession, however, and if it's given that both players remember the previous actions of all players, the game is called an iterated prisoner’s dilemma. In this version, the game is played repeatedly between the same players, who continuously have the opportunity to penalize the other for previous decisions. If information regarding the number of times the game is played is available to the players, then by backward induction the two rational players will betray each other repeatedly due to the same reasons as the single-shot variant. In an infinite or unknown length game there is no fixed optimum strategy.

In this paper, we look at the iterated prisoner’s dilemma issue from a unique angle. We concentrate on the performance of the group as a whole, rather than on the performance of an individual. The goal is to maximize the group’s overall benefit, regardless of how each player performs.
Some members of a group cooperate, while others defect. Of course, some of the group members, as they cooperate and defect based on their individual strategies, will fare better than others. Given the present level of defection in a group, our focus is to analyze the effects of individual defection in terms of group benefit.

We look into whether pure angels that only choose to cooperate perform the best as a group, or if additional greed is required to maximize performance. How much defection, if necessary, is required to optimize a group’s advantages? In this study, we explore these problems, and seek to identify the effect of defection to maximize group benefit.

# Summary of Rsearch Nodes


<kbd><img src="https://github.com/Chanseung-Lee/Storage/blob/3a1fc6b0f730df3f686897c649ee973622e48c4f/rererere.JPG" alt="Image"></kbd>

The entries of Fig. 1 represent the payoffs that each player gains. If both players (player X and player Y) cooperate, they both receive payoff R for reward. If both players defect, they receive P for punishment. If only one player defects and the other player cooperates, the defector receives T for temptation, and the cooperator gets S for sucker. 

To make the payoff table more realistic, we assume that T>R>P>S. Regardless of what the other player does, the payoff of playing defect is greater than the payoff of playing cooperate, while the payoff of mutual cooperation is higher than the payoff of mutual defection. Thus, rational players will end up in the less desirable outcome of mutual defection. Because T>R and P>S, mutual defection is the only Nash equilibrium of the single-shot game.

<kbd><img src="https://github.com/Chanseung-Lee/Storage/blob/3a1fc6b0f730df3f686897c649ee973622e48c4f/ertr.JPG" alt="Image"></kbd>

The elements that are highlighted through research are as follows:

- When there is no defection (everybody cooperates), the average balance (AVG) is R. The proof is trivial, because from the definition of AVG, AVG=R when d=0.

- When there is no cooperation (everybody defects), the average balance is P. The proof is trivial, because from the definition of AVG, AVG=P when d=1.

- When T+S<P+R, the average profit monotonically decreases as d increases. Therefore, when d=0, the profit is maximized.

- When the value of P approaches R, meaning the reward for cooperating is not sufficiently greater than the punishment of mutual defection, the value of F becomes close to 1/2. In this case, the value of AVG approaches (T+S+2R)/4.

Putting it all together, the optimal value of d that maximizes the group benefit is as follows:

<kbd><img src="https://github.com/Chanseung-Lee/Storage/blob/62b0f18977df276bdb8ad63d2f143d042b791583/rr3.JPG" alt="Image"></kbd>



