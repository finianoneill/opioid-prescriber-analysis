# Opioid-prescriber-analysis


![Drug Overdose Kills ! Be safe ](https://i1.wp.com/thenypost.files.wordpress.com/2017/05/170522-drug-overdoses-feature.jpg?quality=90&strip=all&ssl=1)

**INTRODUCTION**

“Opioids” are the class of drugs which are naturally found in the poppy plant. They are often used and prescribed by physicians as pain relieving medicine. 
Centre for Disease control and prevention (CDC)Injury centre looks at the deaths and non-fatal overdoses for four categories of opiods:

•	Natural opioids which includes morphine and codeine and the semi-synthetic opioids which includes drugs like oxycodone,hydrocodone and hydromorphone and oxymorphone.

•	Methadone, a synthetic opioid.

•	Synthetic opioids other than methadone (drugs like tramadol and fentanyl).

•	Heroin, an illicit (illegally made) opioid synthesized from morphine that can be a white or brown powder, or a black sticky substance.

Opioids prescription has increased in the world and opioid sales in US has increased four times. According to CDC*in 2016 63,632 drug overdose deaths occurred in the United States.

**AIM:**

The main aim of this project is to determine the prescribing patterns of Opioids in USA in the year 2016.

**METHODOLOGY:**

“Opioid painkillers” are supposed to provide pain relief, but now a days there are many injuries and deaths because either they have been heavily marketed or inappropriately prescribed. With the use of analysis tools one can make useful inferences and predictions with the available data which will help the health care industries to improve the clinical outcomes.

**Source of information*

* The main source of information was from the website : https://www.cdc.gov/ and 
https://data.cms.gov/ .

* "Pip install sodapy" was done to access CDC and CMS APIs.

*Data type*

CDC Overdose API:
CDC data for overdose deaths had a column for “data_values” with multiple data types, and a separate column for “indicator” to say whether the “data_value” instance was referring to a percent, a whole number for total deaths, a whole number for overdose deaths, etc.
This data was transformed so that the “indicators”- total deaths, overdose deaths, opioid deaths, etc- are now column headers. The “data values” are grouped by state within each column category, so that it can be easily parsed to compare states across data categories or “indicators”. Column headers were renamed, data was sorted by highest # of drug overdose deaths, and filtered for 2016 data.
The data was available on the website and we used the API to access it (add API link).

*Technologies used*

* Google API
* SOCRATA
* PANDAS

*Cleaning of data*

The data was pretty huge which was cleaned on pandas by the dropna function where all the NaN values were dropped.

*Storing of the data*

MongoDb, API.


**ANALYSIS AND RESULTS**

The data was divided into two parts – “Opioids prescriber analysis” and the “Drug overdose deaths 2016”.

*Opioids prescriber analysis*

The data explored the Opioids prescriber based on the medicare data from the CMS. The result showed that there were 6,02,734 opioid overdose deaths in the US in 2016. The total number of deaths was maximum in the New York state (20,733) followed by Maryland (17,918) and North Carolina (16,343).

*Drug overdose deaths 2016*:

* NY had highest total # of overdose deaths at
24820.0, followed my MD: 20291 and NC: 21361.

* UT has the highest percentage of deaths caused by drug overdose at 3.79%, followed by NH: 3.77% and WV: 3.67%.

* Only 19 states report overdose details beyond total #of deaths and total # of overdose deaths. Of the available data, the following can be drawn.
* NY has the highest amount of reported overdose deaths in the categories of opioids, heroin, natural & semi-synthetic opioids, and synthetic opioids excluding methadone.
* NC has the highest amt of reported overdose deaths in the category of methadone.
* The NY data goes into deeper detail- with a “YC” state filter available referring to “NYC. Looking at NYC alone, it still falls before 90% of US states, and makes up  about 60% of the total NY data.

**LIMITATION OF PROJECT**

The study having limitations are inspirations to others or self analysis.
There were many limitations of the present study.

* *Time limit* . If time permits the present data can be compared with either any other country with low drug over dose deaths for detailed analysis of possible reasons.
* The age data was not available for studying the drug overdose deaths by age.
