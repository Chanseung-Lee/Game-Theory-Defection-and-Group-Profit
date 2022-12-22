# Game-Theory-Defection-and-Group-Profit

Link to the published research paper: To Be Added Soon!

This is the short code section that accompanies the collaborative research paper that's been accepted and published to the Applied Artificial Intelligence journal. The research paper has been accepted on December 8th, 2022.

Most research endeavors have been conducted analytically and mathematically, thus the final code segments are relatively concise due to the main purpose being simply to verify the conclusions from the research output. Details of the involved mathematics can be found on the published paper.

# Intro to the Research

The prisoner’s dilemma is a game theory framework illustrating two rational individuals making decisions in their own self-interest. Many social dilemma situations can be researched in the context of variations of this concept. Each player, regardless of the decision made by the other player, has an incentive to defect in one-shot interactions, or when the game is repeated for a finite number of times. Therefore, although the decision of cooperation by both players provides the more optimal payoff, the decision of defection is a rational decision, and it provides Nash equilibrium, despite the worse payoff. 

If two players repeat the same prisoner’s dilemma game in succession, however, and if it's given that both players remember the previous actions of all players, the game is called an iterated prisoner’s dilemma. In this version, the game is played repeatedly between the same players, who continuously have the opportunity to penalize the other for previous decisions. If information regarding the number of times the game is played is available to the players, then by backward induction the two rational players will betray each other repeatedly due to the same reasons as the single-shot variant. In an infinite or unknown length game there is no fixed optimum strategy.

<kbd><img src="https://github.com/Chanseung-Lee/Storage/blob/3a1fc6b0f730df3f686897c649ee973622e48c4f/rererere.JPG" alt="Image"></kbd>

Numerous studies have been conducted on optimizing an individual’s benefit in the setting of the iterated prisoner’s dilemma. Each study attempts to identify the best strategies to maximize the benefit of an individual by alternating between cooperation and defection. Prisoner’s dilemma tournaments have been held to compete and test algorithms for such cases. 
Each player has a tendency to be egotistical and defect to maximize his or her own benefit, not the profit of the group. However, without cooperation within the group, it’s easy to come to the conclusion that the collective society is doomed from the start. In human civilization, people cooperate with one another, even when it logically makes more sense to do otherwise at the time. It’s well-established that mutual cooperation can indeed be optimal in the iterated prisoner’s dilemma. Many theoretical mechanisms for the emergence and maintenance of cooperation in social dilemma games have been reported thus far.

<kbd><img src="https://github.com/Chanseung-Lee/Storage/blob/3a1fc6b0f730df3f686897c649ee973622e48c4f/ertr.JPG" alt="Image"></kbd>

In this paper, we look at the iterated prisoner’s dilemma issue from a different angle. We concentrate on the performance of the group as a whole, rather than on the performance of an individual. The goal is to maximize the group’s overall benefit, regardless of how each player performs.
Some members of a group cooperate, while others defect. Of course, some of the group members, as they cooperate and defect based on their individual strategies, will fare better than others. Given the present level of defection in a group, our focus is to analyze the effects of individual defection in terms of group benefit.

We look into whether pure angels that only choose to cooperate perform the best as a group, or if additional wickedness is required to maximize performance. How much defection, if necessary, is required to optimize a group’s advantages? In this study, we explore these problems, and seek to identify the effect of defection to maximize group benefit.


