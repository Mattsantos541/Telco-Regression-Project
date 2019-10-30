Project Name- Telco Regression Project




Project Intro/Objective

The purpose of this project is investigate WHY ARE OUR CUSTOMERS CHURNING? 
-Go beyond the contracts- Contract type is the biggest indicator of churn, but going beyond that with different features to narrow down that group for rish of churn.
-Does price affect ther liklihood of churn?
-Are there features that indicate a higher propensity to churn? like type of internet service, type of phone service, online security and backup, senior citizens, paying more than x% of customers with the same services, etc.?




Hypothesis:
We believe the biggest driver of churn is the contract type, as well as length of tenure.
Data Dictionary



Baseline- 

Using the variables: 
'tenure', 'contract_type', 'monthly_charges'- based on previous information 
to establish the baseline accuracy with a decision tree.  The accuracy of Decision Tree classifier on test set: 0.78

This model is better than 60%


MVP-

using the variables: 
tenure
online_secuirty
tech_support
monthly _charges
Toatl_charges

within the data set contsining just the month to moonth contracts, the decision tree clasifier increased the4 accuracy of the model by 1%

The acuracy of the MVP is 79%


