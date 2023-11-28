# Jordan River Wines

### Insights / Sanity Check Conclusions

1. **Shape and data sufficiency: Check if there are sufficient rows of data for an ML problem**

   1. **INSIGHT:** Shape of the data is (1143, 12). i.e., dataset contains ~1150 observations, which is much greater than number of columns (12). Hence we can apply ML techniques rather than statistical rule-based approach.
2. **Datatypes: Check whether all the columns in the given dataset is numeric**

   1. **INSIGHT:** `Dtype` indicates that all columns are numeric
3. **Missing Values: Check whether there are missing values**

   1. **INSIGHT:** `Non-Null Count` indicates there are no missing values in the dataset
4. **Zero-variance: Check if there are any zero variance column in the dataset**

   1. **INSIGHT:** No zero-variance columns found in the dataset
5. **Range of numbers in each column: Check if the column values within the dataset are in the same magnitude**

   1. **INSIGHT:** Each column has numbers within the same magnitude or plottable in a graph
6. **Correlation: Check correlation between feature columns & target**

   1. **INSIGHT:** The columns `pH`, `free sulfur dioxide`, `residual sugar` have very weak correlation (0.00 - 0.20)
   2. **INSIGHT:** The columns `fixed acidity`, `citric acid`, `chlorides`, `total sulfur dioxide`, `density` have weak correlation (0.20 - 0.40)
   3. ***Note:*** *The barplots and correlation heatmap complement each other and reveal these findings
   4. ***Note:*** *absolute values of correlations were considered*
7. **Other Observations:**

   1. **INSIGHT:** Since (a) the target is given (b) target is continuous (number between 0..10), we can conclude that this is a supervised linear regression problem
   2. **INSIGHT:** The target variable, i.e., `quality` has discrete values which indicates that this can be solved using classification methods also. However we will continue with Linear Regression in this exercise.

   #### Checklist of STANDARD EDA items


   1. Strategy for missing data

      1. Action: No missing data, no action to be taken
   2. Convert categorical to numeric

      1. Action: No Categorical data, no action to be taken
   3. Dimensionality reduction/Drop the identified columns

      1. Action: Drop identified columns in Insights 6.1 and 6.2
   4. Check for Outliers, Normalize data in columns to fit a range ( *Optional* )

      1. Action: As per Insights 5.1 there are no Outliers

   #### Approach:

   We will follow a 3-step approach as outlined below:

   Step 1:

   1. First, we will process the complete dataset without dropping any columns.
   2. We will build the ML model with the complete data, test and validate the predictions.

   Step 2:

   1. As per Insights 6.1, we will drop the columns that show very weak correlations. These columns are - `pH`, `free sulfur dioxide`, `residual sugar`
   2. The dataset will thus have 9 features (including target)
   3. We will build the ML model with the remaining data, test and validate the predictions

   Step 3:

   1. As per Insights 6.2, we will next drop the columns that show weak correlations. These columns are - `fixed acidity`, `citric acid`, `chlorides`, `total sulfur dioxide`, `density`
   2. The dataset will thus have 4 features (including target)
   3. We will build the ML model with the remaining data, test and validate the predictions
