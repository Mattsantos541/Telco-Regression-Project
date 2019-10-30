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
Totall_charges

within the data set containing just the month to month contracts, the decision tree clasifier increased the accuracy of the model by 1%

The acuracy of the MVP is 79%


Logistic Regression-

using the variables: 
tenure
online_secuirty
tech_support
monthly _charges
Total_charges

within the data set containing just the month to month contracts, the decision tree clasifier decreased the accuracy of the model 

The acuracy of the logistic regression is 71%


K-Nearest Neighbor-

using the variables: 

tenure
online_secuirty
tech_support
monthly _charges
Total_charges

within the data set containing just the month to month contracts, the decision tree clasifier decreased the accuracy of the model 

The acuracy of the logistic regression is 76%


DATA DICTIONARY:

Customer Id: Self Explanatory

Churn: 0:No 1: Yes

Gender: 0:Male 1:Female

Contract_Type_ID: 1: Month to Month 2: 1 Year 3: 2 Year

Senior Citizen: 0: No 1: Yes

internet_service_type_id: 1: DSL 2: Fiber Optic 3: None

family: 0:Partner and Dependents 1: Partner Only 2: Dependents Only 3: No Partner No Dependents

phone_services: 0: Phone Service and Multiple Lines: 1: Phone Service Only 2: No Phone Service

Streaming Services: 0: Streaming TV and Streaming Movies: 0 1: Streaming TV only 2: Streaming Movies only 3: No streaming services

Online Services: 0: Online Security and Online Backup 1: Online Security only 2: Online Backup 3: No Online Services

Tech Support: 0: No 1: Yes

Device Protection: 0: No 1: Yes

Paperless Billing: 0: No 1: Yes

Churn: 0: No 1: Yes



Google Slide link:
https://docs.google.com/presentation/d/1VAP2QB2HfpLBYQ444ktJxP3exuNvlGNyIP-0r7bHhD8/edit#slide=id.g657e12b098_0_1296









