****
****
## Employee Management Project Report
### 1. Introduction
- This document describes the steps taken to complete the Employee Management Project
	- The project involved creating and managing employee records, applying data validation, performing sorting and filtering, using conditional formatting.

### 2.Data Entry & Formatting 
- **Created an Employee Records sheet** with fields:
	- Employee ID, Name, Department, Job Title, Date of Joining, Salary, Email, Phone Number, Status (Active/Inactive).
- **Added 50 sample entries**.
- **Applied Formatting:**
	- Bold headers.
	- Applied borders.
	- Adjusted column widths for readability.

### 3.Data Validation
- **Created Drop-down Lists:**
	- Department: HR, IT, Finance, Admin, Marketing.
	- Job Title: Based on relevant job titles per department.
- **Applied Restrictions:**
	- Salary must be numeric and greater than 0.
	- Email must follow the format (example@example.com).
	- Date of Joining cannot be in the future.
	- Status can only be "Active" or "Inactive" using a drop-down list.

#### 4.Sorting & Filtering
- **Sorted Data:**
	- Sorted employees first by **Department** and then by **Date of Joining** (ascending).
- **Filtered Data:**
	- Applied a filter to show employees who joined **after a specific year** using the filter.

### 5.Conditional Formatting
- **Salary Highlighting:**
	- Applied conditional formatting to highlight employees earning below **$3,000** in **red**.
- **Recent Hires:**
	- Highlighted employees who joined in the last **6 months** in **green** using a formula based on the current date.

### 6.Functions & Lookups
- **Classification using IF Statement:**
	- Added a new column to classify employees as **"Senior"** or **"Junior"** using the formula:
		- `=IF(Salary>5000, "Senior", "Junior")`
- **VLOOKUP for Bonus Rate:**
	- Created a second sheet with bonus rates for each department.
	- Used VLOOKUP to pull the appropriate bonus rate based on the department using the formula:
		- `=VLOOKUP(Department, Sheet2!$A$2:$C$6, 2, FALSE)`

### Conclusion 
- عندي تعقيب صغير 👉😆👈