***
## Probability Distributions
- Probability distributions describe how the values of a random variable are distributed. They can be classified into **discrete** and **continuous** distributions.

### 1. Discrete Probability Distributions
- A discrete probability distribution applies to scenarios where the random variable takes **countable** values.

#### Common Discrete Distributions:
1. **Bernoulli Distribution:**
	- Models a single trial with two outcomes: success (1) or failure (0)
	- `e.g.` Coin toss (Heads = 1, Tails = 0).
2. **Binomial Distribution:**
	- Models the number of successes in **n** independent Bernoulli trials.
	- `e.g.` Number of heads in 10 coin tosses.
3. **Geometric Distribution:**
	- Models the number of trials until the first success in Bernoulli trials.
	- `e.g` Rolling a die until you get a 6.
4. **Poisson Distribution:**
	- Models the number of events occurring in a fixed interval of time or space when events happen at a constant rate.
	- `e.g.` Number of emails received per hour.

### 2. Continuous Probability Distributions
- A continuous probability distribution applies when the random variable can take **infinite values** within a given range.

#### Common Continuous Distributions:
1. **Uniform Distribution:**
	- All values in an interval $[a, b]$ are equally likely.
	- $F(X) = 1 / (b - a)$ , $a <= x <= b$
2. **Normal (Gaussian) Distribution**
	- Bell-shaped distribution commonly found in natural phenomena.
3. **Exponential Distribution:**
	- Models the time between independent events occurring at a constant rate.
	- `e.g.` Time between customer arrivals at a bank.
4. **Gamma Distribution:**
	- Generalized form of the exponential distribution, modeling waiting times for multiple events.
5. **Chi-Squared Distribution:**
	- arises from summing the squares of **k** independent standard normal variables:$$X=Z_1^2​+Z_2^2​+⋯+Z_k^2​$$
***
***
## Conditional Probability 
-  is the probability of an event **A** occurring **given that** another event **B** has already occurred. It is written as: $P(A|B)$ "the probability of A occurring given B has occurred."
- **Formula:** $P(A|B) = P(A∩B) / P(B)$ 
	- *Where* 
		- $P(A∣B) =$ Probability of A given B
		- $P(A∩B) =$ Probability of both A and B occurring
		- $P(B) =$ Probability of B occurring (must be greater than 0)
- **Multiplication Rule:**
	- Rearranging the **formula**, we get: $P(A∩B)=P(A∣B)⋅P(B)$ 
	- This helps in solving probability problems where two events happen together.

- **When to Use Conditional Probability?**
	- When events are dependent on each other.
	- Bayes' Theorem applications
	- Solving probability trees & real-world decision-making problems.

## Independent Events
- Two events **A** and **B** are **independent** if the occurrence of one **does not affect** the probability of the other.
- A and B are independent if: $P(A|B) = P(A)$ or $P(B∣A)=P(B)$ "B happened does not change the probability of A happening (and vice versa)"
- For two independent events **A** and **B**, the probability of both occurring together is:
	- $P(A∩B)=P(A)×P(B)$ -> **Multiplication Rule for Independent Events**.
	- If two events satisfy this formula, they are independent, otherwise, they are dependent

## Total Probability 
- finding the probability of an event **A** by considering all possible ways it can happen through different **mutually exclusive** events.
- It states that if $B_1, B_2, ..., B_n$ form a **partition** of the sample space (i.e., they are mutually exclusive and cover all possibilities), then:
	-  $P(A)=P(A∣B1​)P(B1​)+P(A∣B2​)P(B2​)+...+P(A∣Bn​)P(Bn​)$
	- more general: $P(A)=(i=1∑n​)P(A∣Bi​)P(Bi​)$
- **When to use:**
	-  When an event **A** depends on different possible scenarios $B_1, B_2, ..., B_n$
	- When breaking a complex probability into simpler conditional probabilities.
	- When using **Bayes’ Theorem** to update probabilities.

## Bayes' Theorem
- helps in finding the probability of an event **A**, given that another event **B** has already occurred. It updates our belief based on new evidence.
$$P(A∣B)=P(B∣A)P(A)/ P(B)​$$
- *where:*
	- **P(A∣B)** = Probability of **A happening given B**.
	- **P(B∣A)** = Probability of **B happening given A**.
	- **P(A)** = Probability of **A happening before any evidence**.
	- **P(B)** = Probability of **B happening**.
***
***
## Random Variables 
- is a variable that takes numerical values based on the outcome of a **random experiment**.
	- `e.g.`
		- Rolling a **6-sided die**, where the outcome (1 to 6) is a **random variable**.
		- Flipping a **coin**, where we assign **0 for heads** and **1 for tails**.

### Types of Random Variables
1. **Discrete Random Variable (Countable Outcomes)**
	- Takes a **finite** or **countable** number of values.
	- `e.g.`: Number of heads in 3 coin flips (**0, 1, 2, or 3**).
	- Common Distributions: **Binomial, Poisson**.
2. **Continuous Random Variable (Uncountable Outcomes)**
	- Takes an **infinite** number of values within a range.
	- `e.g.`: The **height of students** in a class (can be 170.2 cm, 170.25 cm, etc.).
	- Common Distributions: **Normal, Exponential, Uniform**.

### Probability Distributions
- Each random variable follows a **probability distribution**, which tells us how likely different values are.
- **Discrete Random Variable** → Probability Mass Function (PMF)
	- `e.g.`: **Rolling a fair die** → Each outcome (1-6) has a **1/6** probability.
- **Continuous Random Variable** → Probability Density Function (PDF)
	- `e.g.`: **Height of people** follows a **Normal Distribution (Bell Curve)**.
