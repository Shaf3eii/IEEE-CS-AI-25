***
## Quantitative 
> This type of data represents **measurable quantities** and can be analyzed using mathematical calculations -> use numbers
##### Numerical Data - Two types:
- **Discrete (Counting):** Values are **countable and whole numbers** (no fractions or decimals).
- `e.g:`
	- 3 mice revive at 3 AM
	- 5 apples in a basked
- **Continuous (Measurement):** Values can take any number **within a range** and include decimals.
	- Measured: Interval from a to b
	- Distance 
	- Speed
	- Weight

## Qualitative 
>This type of data **describes qualities** or characteristics and is based on **observations** rather than numbers -> use words, color, soft / hard, low / high
##### Descriptive data - based on observations:
- `e.g:`
	- Color
	- Opinion
***
***
## Scales Data
#### Nominal Scale data (Categorical Data)
1. **Qualitative / Categorical**
2. **Names, Colors, Labels, Gender, etc**
3. **Order does not matter**
	- `e.g:`
		- **Colors** → "Red, Blue, Green"
		- **Gender** → "Male, Female, Other"
		- **Blood Type** → "A, B, AB, O"
		- **Nationality** → "Egyptian, American, Japanese"
#### Ordinal Scale data
1. **Ranking / Placement**
2. **The Order matter**
3. **Differences cannot be measured**
	- `e.g:`
		- **Movie Ratings** → "⭐, ⭐⭐, ⭐⭐⭐, ⭐⭐⭐⭐, ⭐⭐⭐⭐⭐"
		- **Placement in a Race** → "1st, 2nd, 3rd"
#### Interval Scale data
1. **The Order matter**
2. **Differences between values**
3. **Zero does not meat "Nothing"**
	- `e.g:`
		- **Temperature (°C, °F)** → 0°C doesn’t mean no temperature
> **Key Note:** Since there is **no true zero**, we **CANNOT** calculate ratios.

#### Ratio Scale data
1. **The Order matter**
2. **Differences & ratios are meaningful**
3. **Zero is meaning**
	- `e.g:`
		- **Weight (kg, lbs)** → 0 kg means "no weight"
		- **Speed (m/s, km/h)** → 0 km/h means "not moving"


| **Scale**    | **Order matters** | **Differences Measurable** | **True Zero** |
| ------------ | ----------------- | -------------------------- | ------------- |
| **Nominal**  | ❌                 | ❌                          | ❌             |
| **Ordinal**  | ✅                 | ❌                          | ❌             |
| **Interval** | ✅                 | ✅                          | ❌             |
| **Ratio**    | ✅                 | ✅                          | ✅             |
عاملة سيمتريك 
****
****
## Hypothesis Testing
- is a statistical method used to make decisions or draw conclusions based on sample data.
##### Two Hypotheses
- **Null Hypothesis$(H_0)$:**
	- No Effect
	- The default assumption that nothing has changed
	- We **assume $H₀$ is true** until proven otherwise
- **Alternative Hypothesis$(H_1)$:**
	- There is an effect
	- What we are trying to prove
	- If evidence **strongly contradicts $H₀$**, we reject it in favor of $H₁$.

###### Example

| Scenario | Null                                | Alternative                       |
| -------- | ----------------------------------- | --------------------------------- |
| A drug   | The drug has no impact              | The drug improves patients health |
| A coin   | The coin lands heads/ tails equally | The coin is biased                |

##### Steps in Hypothesis Testing
1. **State the hypotheses** $(H₀$ and $H₁)$.
2. **Choose a significance level (α)** (common values: **0.05, 0.01**).
3. **Select the test** (`e.g`, **Z-test, T-test, Chi-Square test**).
4. **Calculate the test statistic**.
5. **Find the p-value** (probability of getting results as extreme as observed)
6. Make a decision:
	1. **If p-value ≤ α** → **Reject H₀** (strong evidence for H₁).
	2. **else -> Fail to reject $H_0$** (Not enough evidence)

##### Key Concepts
- **Significance Level (α):**
	- The probability of rejecting H₀ when it is actually true.
	- Common choices: **0.05 (5%) or 0.01 (1%)**.
- **P-Value:**
	- The probability of obtaining a result **as extreme or more extreme** than the observed data, assuming H₀ is true
- **Types of Errors:**
	- **Type I Error (False Positive)** → Rejecting H₀ when it's actually true.
	- **Type II Error (False Negative)** → Failing to reject H₀ when H₁ is actually true.
- **Types of Tests:**
	- **One-Tailed Test** → Checking if the value is **greater or less** than a certain value.
	- **Two-Tailed Test** → Checking if the value is **different** (either higher or lower).

###### Conclusion 
- **What Does the Decision Mean?**
	- **Reject H₀** → There is strong evidence supporting H₁ (alternative hypothesis).
	- **Fail to reject H₀** → Not enough evidence to support H₁, but H₀ is not necessarily true.
***
***
## Confidence Interval
- is a range of values that likely contains the true population parameter (such as the mean) **with a certain level of confidence**.

###### Confidence Level
- The **confidence level** (`e.g`., 90%, 95%, 99%) represents how confident we are that the true parameter lies within the interval.
- `e.g` a **95% confidence interval** means:  
    **"If we repeated the study many times, 95% of the calculated confidence intervals would contain the true population mean."**

- **Higher confidence level → Wider interval (more certainty, less precision).**  
- **Lower confidence level → Narrower interval (more precision, less certainty).**

##### Formula for Confidence Interval (Mean)
 ![Task_5/images/MeanFormula.png]
- **$X$** = Sample mean
- Z = Z-score
- **σ** = Population standard deviation
- **n** = Sample size

- **Example:**
	- A sample of 50 students has an average test score of **75**, with a standard deviation of **10**. Find a **95% confidence interval** for the population mean.
	![Task_5/images/MeanExample.png]
	- We are **95% confident** that the true mean test score of all students is between **72.24 and 77.76**.

##### Formula for Confidence Interval (Proportion)
![Task_5/images/ProportionFormula.png]
- $P$ = Sample proportion (successes / total trials)
- $Z$ = Z-score
- $n$ = Sample size

- **Example:**
	- In a survey of **500** people, **40% (0.40)** support a new law. Find a **95% confidence interval**.
	![Task_5/images/ProportionExample.png]
	- We are **95% confident** that the true proportion of people who support the law is between **35.7% and 44.3%**.

***
***
## Regression Analysis
- is a **statistical method** used to model the relationship between a **dependent variable (outcome)** and one or more **independent variables (predictors)**.
	- Understand how variables are related
	- Make predictions واليعوذ بالله
	- Identify trends and patterns

##### Types of Regression Analysis
- **Simple Linear Regression (One Independent Variable):**
	- Used when there is **one predictor (X) and one outcome (Y)**.  
	![Task_5/images/LinearRegression.png]
	- $Y$ = Dependent variable (what we predict)
	- $X$ = Independent variable (predictor)
	- $β0$ = Intercept (value of Y when X = 0)
	- $β1​$ = Slope (rate of change in Y per unit increase in X)
	- $ϵ$ = Error term (random variation)

- **Multiple Linear Regression (More than One Independent Variable):**
	- Used when there are **multiple predictors (X1, X2, X3, ...)**.
	![Task_5/images/MultipleRegression.png]
	- شرحنا معناهم فوق 

- **Polynomial Regression (Curved Relationships):**
	- When data follows a **non-linear** pattern, we extend linear regression by adding powers of X:
	![Task_5/images/PolynomailRegression.png]
***
***
