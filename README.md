# logistic_regression_affair

Project Description 📄

❄️ Built a linear regression model using statsmodel.api data fair to
predict Affair will happen or not based on other dependent variable.

#### Deployed Project Link: https://affair-prediction-api.herokuapp.com/

##### Jupyter Notebook: (https://github.com/shiv0112/logistic_regression_affair/blob/master/notebooks/logistic_regression.ipynb)

## Data:

Loaded from statsmodel.api

Data name: fair

```
:Number of observations: 6366
    Number of variables: 9
    Variable name definitions:

        rate_marriage   : How rate marriage, 1 = very poor, 2 = poor, 3 = fair,
                        4 = good, 5 = very good
        age             : Age
        yrs_married     : No. years married. Interval approximations. See
                        original paper for detailed explanation.
        children        : No. children
        religious       : How relgious, 1 = not, 2 = mildly, 3 = fairly,
                        4 = strongly
        educ            : Level of education, 9 = grade school, 12 = high
                        school, 14 = some college, 16 = college graduate,
                        17 = some graduate school, 20 = advanced degree
        occupation      : 1 = student, 2 = farming, agriculture; semi-skilled,
                        or unskilled worker; 3 = white-colloar; 4 = teacher
                        counselor social worker, nurse; artist, writers;
                        technician, skilled worker, 5 = managerial,
                        administrative, business, 6 = professional with
                        advanced degree
        occupation_husb : Husband's occupation. Same as occupation.
        affairs         : measure of time spent in extramarital affairs
```

I trained this model using Logistic Regression:

#### The Accuracy of the model:

![Alt text](https://github.com/shiv0112/logistic_regression_affair/blob/master/screenshots/accuracy.png)

#### Roc AUC curve

![Alt text](https://github.com/shiv0112/logistic_regression_affair/blob/master/screenshots/roc.png)

#### The comparison of Actual value and predicted value by our model

![Alt text](https://github.com/shiv0112/logistic_regression_affair/blob/master/screenshots/compare.png)

### Index page of Website:

![Alt text](https://github.com/shiv0112/logistic_regression_affair/blob/master/screenshots/1.png)

### Data Input from user:

![Alt text](https://github.com/shiv0112/logistic_regression_affair/blob/master/screenshots/2.png)

## Finally prediction displayed:

![Alt text](https://github.com/shiv0112/logistic_regression_affair/blob/master/screenshots/final.png)

### What I learnt from this project:

-->Classification using Logistic Regression

-->How we can use GridSearch CV to select best parameters for model

-->How to balanced and imbalanced dataset

-->How to make frontend using Flask framework
