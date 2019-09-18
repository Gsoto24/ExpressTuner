# ExpressTuner

The ExpressTuner is a project created to eliminate manual order re-processing 
through a point of sale (POS) system for customer subscriptions that failed to renew
due to credit card decline. In our department this process is referred to “Rolling” 
accounts. This version of the project has been stripped of sensitive information.

<b>Three</b> steps to using ExpressTuner.
<hr>


1) A service representative logs onto ExpressTuner and uploads a CSV file with
accounts that failed to renew due to credit card decline. ExpressTuner uses Python Auth
to validate the employee with the external POS.

![alt text](https://github.com/Gsoto24/ExpressTuner/blob/master/Screen%20Shot%202019-09-18%20at%202.33.52%20PM.png)


2) ExpressTuner automatically schedules dates in the future to re-attempt a charge on each account. 
A list of scheduled accounts in ExpressTuner can be exported to excel for further details, such as when an 
account is scheduled for a charge attempt, how many charge attempts have already been made, who uploaded the
account to ExpressTuner etc.

![alt text](https://github.com/Gsoto24/ExpressTuner/blob/master/Screen%20Shot%202019-09-18%20at%202.41.27%20PM.png)

3) On the date that accounts are scheduled, an attempt to successfully charge each customer is made by ExpressTuner. 
Successful charges as well as failures are recorded in the database and can be exported for further analysis.

![alt text](https://github.com/Gsoto24/ExpressTuner/blob/master/Screen%20Shot%202019-09-18%20at%202.38.09%20PM.png)

<hr>




