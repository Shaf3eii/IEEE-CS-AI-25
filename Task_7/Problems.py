"""
    Write a Python function that takes in a list of values and returns the probability distribution of those values. Assume the values are discrete.

    Input:
    data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1] 

    Output:
    {1: 0.3, 2: 0.2, 3: 0.2, 4: 0.2, 5: 0.1}
"""

data = list(map(int, input().split()))
distribution = { }

for i in data: 
    distribution[i] = distribution.get(i, 0) + 1

sz = len(data)
for key in distribution:
    distribution[key] /= sz

print(distribution)




"""
    Write a Python function that calculates the conditional probability of event B given event A, given two lists of events A and B.

    Input:
    event_a = [1, 0, 1, 0, 1]
    event_b = [1, 1, 0, 0, 1]

    Output:
    0.5
"""

# event B given event A -> P(B|A) = P(B ∩ A) / P(A)
event_a = list(map(int, input().split()))
event_b = list(map(int, input().split()))


length = min(len(event_a), len(event_b))

takato3 = sum(event_a[i] == event_b[i] == 1 for i in range(length))

print(takato3 / sum(event_a) if sum(event_a) > 0 else 0)




"""
    Write a Python function that implements Bayes' theorem to calculate the probability of event A given event B, given the prior probability of A and B, and the conditional probability of B given A.

    Input:
    prior_a = 0.3
    prior_b = 0.6
    conditional_b_given_a = 0.8

    Output:
    0.4
"""

# P(A)   -> 0.3
# P(B)   -> 0.6
# P(B|A) -> 0.8
# P(A|B) -> ?
# P(A|B) -> P(B|A) * P(A) / P(B)

prior_a = float(input("Enter the prior probability of event A: "))
prior_b = float(input("Enter the prior probability of event B: "))
conditional_b_given_a = float(input("Enter the conditional probability of B: "))

print(conditional_b_given_a * prior_a / prior_b)