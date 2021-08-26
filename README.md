# Diversity--In--Tech

 

![alt text](https://raw.githubusercontent.com/iyesogie/Diversity--In--Tech/main/images%20/TItle.png)
)


According to Reveal, the United States requires an annual submission of employee gender, race/ethnicity,  and job type from all companies with more than 100 employees. (Rangarajan, 2018) Following submission this data was generally private. This project seeks to understand workplace diversity across tech companies in Silicon Valley in 2016 and the shifts in publicly sharing this data. 

Data 
In 2018, Reveal from The Center for Investigative Reporting published a dataset, and the accompanying methodology, of 2016 Equal Employment Opportunity Commission (EEO) data for 211 tech companies in Silicon Valley. Click here to learn more about Reveal’s methodology.

https://github.com/cirlabs/Silicon-Valley-Diversity-Data 

We used 4 sources for this analysis. 

EEO_2016.csv provides detailed information on gender, race/ethnicity, and job type the companies that said yes in 2016_EEO_Release_Status.csv

2016_EEO_Release_Status.csv provides a list of the 211 that completed the survey. It indicates if 2016 EEO data was publicly shared or not. 

Distributions_data_2016.csv provides percentages for gender, race/ethnicity, and job type for the 211 companies that completed. It does not provide data by name for the companies that did not release their 2016 EEO. 

Transformation & Load
We combined EEO_2016.csv and Distrubutions_data_2016.csv to create our database. Following the cleaning process, the database contained more than 4,000 rows. We then exported the database as a CSV file to create our visuals and analyze the results of three machine learning inquires.



Findings 

What are the top 10 companies committed to diversity and inclusion before 2018?

	Race
* 23 & Me, AirBnB, PayPal, Pinterest, Intuit, Lyft, LinkedIn, Sanmina-SCI, eBay, and Square. 


![alt text](https://raw.githubusercontent.com/iyesogie/Diversity--In--Tech/main/images%20/top%2010%20race.png)
)


	Gender 
* Apple, Intel, eBay, Twitter, Salesforce, MobileIron, Airbnb, 	   Adobe Systems, Intuit, 23 and Me

![alt text](https://raw.githubusercontent.com/iyesogie/Diversity--In--Tech/main/images%20/top%2010%20gender.png)

What is the breakdown of minorities in High Tech jobs?
* 59.01% white
* 26.47% asian 
* 7.20% Latino/Hispanic
* 5.12% Black
* 1.56% 2 or more races 
* 0.34% American Indian/Alaska Native
* 0.30% native Hawaiian/pacific islander 

![alt text](https://raw.githubusercontent.com/iyesogie/Diversity--In--Tech/main/images%20/minority%20pie%20chart.png)

What is the breakdown of minorities in management versus executives?
* There is more racial and ethnic diversity amongst persons in managerial positions than executives in Silicon Valley. 

![alt text](https://raw.githubusercontent.com/iyesogie/Diversity--In--Tech/main/images%20/excs%20v.%20managers.png)

Which companies did not share their 2016 EEO data publicly? 
* The following companies did not release their 2016 EEO data publicly:


![alt_text](https://raw.githubusercontent.com/iyesogie/Diversity--In--Tech/main/images%20/eeo%202016.png)


* A10 Networks 
* Abaxis 
* Accuray 
* Advanced Micro Devices 
* Aemetis 
* Aerohive Networks 
* Agilent Technologies 
* Align Technology 
* Anaplan
* AppDirect
* Applied Materials
* Applied Micro Circuits
* Apttus
* Arista Networks
* Automattic
* Aviat Networks
* Barracuda Networks
* Bio-Rad Laboratories
* Bloom Energy
* Box
* Brocade Communications
* C3 IoT
* Cadence Design Systems
* Callidus Software
* Carbon
* Cavium
* Chegg
* CloudFlare
* Coherent
* Coherus Biosciences
* Credit Karma
* Crowdstrike
* Cypress Semiconductor
* Depomed
* Docker
* Docusign




Machine Learning


Three machine learning models are used to classify data into private and public: KneighborsClassifier(KNN), Support Vector Machine Tuning Model(GridSearchCV), Deep Learning Model(Sequencital). Accuracy Score of testing data is 0.714, 0.783, and 0.857 separately. It seems Deep Learning Model shows the best accuray score for testing data.

![alt text](https://raw.githubusercontent.com/iyesogie/Diversity--In--Tech/main/images%20/ml%20gender%20and%20race.png)

![alt text](https://raw.githubusercontent.com/iyesogie/Diversity--In--Tech/main/images%20/ml%20race%20and%20job.png)


Sources 
Daley, S. (2021, May 5). Women in Tech Statistics Show the Industry Has a Long Way to Go. Built In. https://builtin.com/women-tech/women-in-tech-workplace-statistics 
Data. (2019, April 30). Inclusion Clearinghouse. https://inclusionclearinghouse.org/data/
Employers | U.S. Equal Employment Opportunity Commission. (2021). U.S. Equal Employment Opportunity Commission. https://www.eeoc.gov/employers 
Long, K. A. (2021, April 14). New Amazon data shows Black, Latino and female employees are underrepresented in best-paid jobs. The Seattle Times. https://www.seattletimes.com/business/amazon/new-amazon-data-shows-black-latino-and-female-employees-are-underrepresented-in-best-paid-jobs/ 
Rangarajan, M. B. S. (2018, November 29). How we created a baseline for Silicon Valley’s diversity problem. Reveal. https://revealnews.org/blog/how-we-created-a-baseline-for-silicon-valleys-diversity-problem/ 
Women in Tech Report. (2021). TrustRadius CAPTCHA. https://www.trustradius.com/buyer-blog/women-in-tech-report 






