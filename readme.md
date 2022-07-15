### Project Goals

The project goal is to identify large drivers of churn and come up with a model that acts on those findings so we may take the next steps towards reducing churn.


### Project Description

There are probably many reasons for churn at telco, and some of them may be related to data that we don't have access to. I am conducting this project to dig into what data we do have and uncover some of these factors. If I can find the larger drivers of churn, we can find a path towards reducing that churn as a whole. This would be important towards the growth of the company and possibly even deciding what services and features to roll out at a later time.


### Initial Questions

What services churn more?

Which contract types churn more?

Is churn related to cost for service?

Who is likely to churn?

### Data Dictionary

| Variable                                      Meaning         
| -----------                                  -----------       
| fiber optic internet service | Customers who have fiber optic internet service                    
| monthly charges              | How customers pay monthly         
| contract type                | 1 month, 1 year or 2 year contract types         
| tenure                       | How long the customer has been subscribed, in months          
| tech support                 | If the customer has tech support service          
| dependents                   | Does the customer have dependents         
| relationship status          | does the customer have a partner          
                              


### Steps to Reproduce

1. You will need an env.py file that contains the hostname, username and password of the mySQL database that contains the telco table. Store that env file locally in the repository. Use a gitignore file to hide your env.

2. clone my repo (including the acquire.py and prepare.py)

3. libraries used are pandas, matplotlib, seaborn, stats, numpy, sklearn and math

4. Run my exploration / Presentation files to reproduce work

### The Plan

1.) Initial questions
2.) Data aquisition
3.) Data cleaning
4.) Exploration
5.) Modeling explored data
6.) drawing conclusions
7.) Making suggestion

### Key Findings

Churn seems to be influenced by many factors, but the following have strong correlation:
- internet type and internet options.
- contract length and tenure as a customer
- Age, relationship status and family type
- product cost

### Recommendations / Takeaways

- incentivize customers to choose longer contracts with special deals
- lower monthly costs in general to retain customers long term
- Market to large families, as they seem to be a target group for long term subscription