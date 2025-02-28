***
***
## Types of Graphs and Charts And Their Uses
1. **Bar Chart**
	- `Comparing different categories`
	- Best for discrete data
		- `e.g.`
			- Sales by product type
			- Num of students in different classes 
		- *Variations:*
			- **Vertical Bar Chart** → Standard
			- **Horizontal Bar Chart** → For long category names
			- **Stacked Bar Chart** → Comparing parts of a whole
2. **Histogram**
	- `Showing frequency distribution`
	- Best for **continuous** data
		- `e.g.`
			- Age distribution of a population
			- Exam scores distribution
		- `Difference between bar chart:` 
			- **Bars touch each other** (because data is continuous)
3. **Pie Chart**
	- `Showing parts of a whole`
	- Best for **categorical** data with limited categories
		- `e.g.`
			- Market share of companies
			- Budget breakdown of expenses
4. **Line Graph**
	- `Showing changes/trends over time`
	- Best for **time-series data**
		- `e.g.`
			- Stock market trends
		- *Variations:*
			- **Multiple lines** → Comparing trends between groups
			- **Smoothed Line** → To reduce noise in data
5. **Scatter Plot**
	- Finding relationships between two variables
	- Best for **numerical data**
		- `e.g.`
			- Height vs. Weight of students
6. **Box Plot**
	- Summarizing data with quartiles & detecting outliers
	- Best for **skewed distributions**
		- `e.g.`
			- Exam score analysis
***
***
## Stem and Leaf plot
- **Steps to make stem and leaf plot:**
	1. Collect & Organize the Data
		- Let's say we have the following data set:  
			**15, 21, 23, 25, 31, 35, 37, 42, 43, 44, 47**
	2. Determine the Stems & Leaves
		- Stem: Leading digits (tens place)
		- Leaf: Last digit (ones place)

| Number | Stem | Leaf |
| ------ | ---- | ---- |
| 15     | 1    | 5    |
| 21     | 2    | 1    |
| 23     | 2    | 3    |
| 25     | 2    | 5    |
| 31     | 3    | 1    |
| 35     | 3    | 5    |
| 37     | 3    | 7    |
| 42     | 4    | 2    |
| 43     | 4    | 3    |
| 44     | 4    | 4    |
| 47     | 4    | 7    |
3. Draw the Stem and Leaf Plot 
```
Stem | Leaf
1    | 5
2    | 1 3 5
3    | 1 5 7
4    | 2 3 4 7
```

##### When to Use a Stem-and-Leaf Plot
- **Best for:**
	- Small to medium-sized datasets
	- Showing the **shape of distribution**
	- Identifying **minimum, maximum, & outliers**
- **Not Best for:**
	- Large datasets (use a histogram instead)

##### Advantages
- Keeps original data values
- Easy to make & interpret
- Shows data spread & clusters

***
***
## Box and Whisker Plot
- is a way to visualize the **distribution** of a dataset using **five-number summary** statistics.
- **Steps to make Box and Whisker Plot:**
	1. Collect & Organize the Data
		- Let's say we have the following data set:  
			- 5, 7, 8, 12, 15, 18, 21, 25, 30, 35, 40
		 - Arrange in **ascending order** (already sorted above).
	2. Find the Five-Number Summary
		- The five-number summary consists of:
			1. **Minimum (Min):** The smallest value in the dataset
			2. **First Quartile (Q1):** The **median** of the lower half of the data
			3. **Median (Q2):** The middle value of the dataset
			4. **Third Quartile (Q3):** The **median** of the upper half of the data
			5. **Maximum (Max):** The largest value in the dataset
		- Calculate these values
			- Min               --> 5
			- Q1                 --> 8
			- Median(Q2) --> 18
			- Q3                --> 30
			- Max              --> 40
    3. Draw the Box plot
	    1. **Draw a number line** that covers the range of data
	    2. **Plot the five-number summary** on the number line
	    3. **Create a box** from **Q1 to Q3**
	    4. Draw a vertical line at the median (Q2)
	    5. **Extend whiskers** from **Min to Q1** and **Q3 to Max**
	    6. **Identify any outliers** 
		    - To find **outliers**, use the **Interquartile Range (IQR)**:
			    - `IQR = Q3 − Q1`
			- **Lower Bound**: `Q1 − 1.5 × IQR`
			- **Upper Bound**: `Q3 − 1.5 × IQR`
			- Any data points outside this range are considered outliers.
```mathematica
`e.g.`

  Min   Q1  Median  Q3   Max  
   |-----|====|=====|-----|  
  5     8    18    30    40  

```

##### When to use Box Plot
- **Best For:**
	- Comparing **multiple datasets**
	- Identifying **skewness & outliers**
	- Understanding **data spread**
- **Not Best For:**
	- Small datasets
	- Showing exact data values (use a histogram instead)

##### Advantages
- Shows skewness & outliers
- Easy to compare multiple datasets
- Displays spread & variability clearly

***
***
## Dot Plot
- is a simple way to visualize the frequency of data points by placing dots above a number line.
- **Steps to Make a Dot Plot:**
	1. Collect & Organize the Data
		- Let's say we have the following data set:  
			- 2, 3, 3, 4, 4, 4, 5, 6, 6, 7, 8, 8, 9
	2. Draw a number line
		- Label the number line with **smallest to largest values** in the dataset.
		- 2   3   4   5   6   7   8   9
	3. Plot the Dots
		- For each **data value**, place a dot above its position on the number line.
```
2  ●  
3  ●●  
4  ●●●  
5  ●  
6  ●●  
7  ●  
8  ●●  
9  ●  
```


##### When to Use a Dot Plot
- **Best For:**
	- Small datasets (less than ~30 values).
	- Showing individual data points.
	- Comparing two groups of data.
- **Not Best For:**
	- Large datasets (use a histogram instead).
	- Continuous data (use a box plot).

##### Advantages
- Easy to create & interpret
- Displays exact data values
- Shows clusters & gaps clearly
***
***
## What is a Pie Chart?
- is a circular chart divided into slices that represent **proportions** of a whole.
- **Best For:**
	- Showing **percentage-based data** (`e.g.`, market share, survey results).
	- Comparing **parts of a whole**.
- **Not Best For:**
	- Large datasets with too many categories.
	- Exact comparisons (use a bar chart instead).
***
***
## What is a Bar Chart?
- uses rectangular bars to represent data values.
- **Best For:**
	- Comparing **discrete categories**
	- Showing trends over time with grouped bars.
- **Not Best For:**
	- Showing proportions (use a pie chart).
	- Large datasets with too many categories (use a histogram).
***
***
## Symmetry and Skewness
- describe the **shape** of a data distribution.
- **Symmetric Distribution:** Data is evenly spread around the center
- **Right-Skewed (Positive Skew):** Tail extends to the **right**
- **Left-Skewed (Negative Skew):** Tail extends to the **left**
***
***
## What is a Heatmap?
- is a graphical representation of data where values are shown as **colors**.
- **Best For:**
	- Visualizing **correlations** in large datasets.
	- Showing **patterns** in time-series or geographical data.
- **Not Best For:**
	- Small datasets (use a bar chart).
	- Precise values (use a table instead).
***
***
## What is a Violin Plot?
- A **Violin Plot** combines a **box plot** and a **density plot** to show the distribution of a dataset. It displays:
	- Median & Quartiles (like a box plot).
	- Density of data (like a KDE plot).
- **Best For:**
	- Comparing multiple distributions.
	- Showing the shape and spread of data.
- **Not Best For:**
	- Small datasets (use a box plot instead).
	- Data without much variation.
***
***
***
