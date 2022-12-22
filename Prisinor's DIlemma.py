import random
from matplotlib import pyplot as plt

# Class for one prisoner, contains the all-important profit value
class Prisoner:
  def __init__(self, profit, id):
    self.profit = profit
    self.id = id

  def get_profit(self):         #The classic get & set methods. Not needed, but useful!
      return self.profit

  def set_profit(self, n_profit):
      self.profit = n_profit


def decision(probability):     #Simple function to quickly calculate defection/cooperation based on d probability
    return random.random() < probability

def outcome(prisoner_a, prisoner_b, choice):    #function to adjust the profit values of two prisoners based on the choice
                                                #from the outcome matrix
    T = 7
    R = 3
    P = 2
    S = 1
    if choice == "CC":
        prisoner_a.profit = R
        prisoner_b.profit = R
    elif choice == "CD":
        prisoner_a.profit = S
        prisoner_b.profit = T
    elif choice == "DC":
        prisoner_a.profit = T
        prisoner_b.profit = S
    elif choice == "DD":
        prisoner_a.profit = P
        prisoner_b.profit = P
    else:
        print("Invalid choice detected")

def one_run(defect_prob):
    d = defect_prob  # probability of defection
    iter_count = 10000  # how many iterations of exchange will occur?
    jail_size = 500  # how many prisoners?

    jail = []  # list full of prisoners, stylishly named jail

    outcome_matrix = [[0 for _ in range(2)] for _ in range(2)]
    outcome_matrix[0][0] = "CC"
    outcome_matrix[0][1] = "CD"
    outcome_matrix[1][0] = "DC"
    outcome_matrix[1][1] = "DD"

    for i in range(jail_size):
        jail.append(Prisoner(0, i))  # add prisoners to jail up to max capacity, with incrementing id

    for x in range(iter_count):      #Perform iter_count number of exchanges, according to the given probability of defection
        index_a = random.randrange(jail_size)
        index_b = random.randrange(jail_size)

        prisoner_a = jail[index_a]
        prisoner_b = jail[index_b]

        if decision(d):
            a_choice = 1
        else:
            a_choice = 0

        if decision(d):
            b_choice = 1
        else:
            b_choice = 0

        final_choice = outcome_matrix[a_choice][b_choice]
        outcome(prisoner_a, prisoner_b, final_choice)

    total_profit = 0
    profits = []

    for prisoner in jail:       #Calculate total & average profit after the exchange iterations
        total_profit += prisoner.profit
        profits.append(prisoner.profit)

    avg_profit = (total_profit / jail_size)

    return avg_profit

def average(lst):
    return sum(lst) / len(lst)

def main():

    d_values = []
    avg_profits = []

    for z in range(100):            #Try d values of 0.01, 0.02, -> until 1.
        d_prob = z/100
        d_values.append(d_prob)

        avg_outputs = []
        for t in range(50):         #For each d, run through many iterations and take the average to reduce variance from randomness
            avg_output = one_run(d_prob)
            avg_outputs.append(avg_output)

        average_of_averages = average(avg_outputs)
        avg_profits.append(average_of_averages)

    plt.plot(d_values, avg_profits)
    plt.show()


if __name__ == "__main__":
    main()