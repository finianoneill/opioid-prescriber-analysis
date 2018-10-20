# Analysis of Opioid Prescription Patterns and Drug Overdose Deaths

![Drug Overdose Kills ! Be safe ](https://i1.wp.com/thenypost.files.wordpress.com/2017/05/170522-drug-overdoses-feature.jpg?quality=90&strip=all&ssl=1)

### Introduction

“Opioids” are the class of drugs which are naturally found in the poppy plant. They are often used and prescribed by physicians as pain relieving medicine. 

Centre for Disease control and prevention (CDC)Injury centre looks at the deaths and non-fatal overdoses for four categories of opiods:

* Natural opioids which includes morphine and codeine and the semi-synthetic opioids which includes drugs like oxycodone,hydrocodone and hydromorphone and oxymorphone.
* Methadone, a synthetic opioid.
* Synthetic opioids other than methadone (drugs like tramadol and fentanyl).
* Heroin, an illicit (illegally made) opioid synthesized from morphine that can be a white or brown powder, or a black sticky substance.

Opioid prescriptions and sales have increased substantially in the US. According to the CDC *in 2016 63,632 opioid drug overdose deaths occurred in the United States.*

Project Aim:  The main aim of our project is to determine the prescribing patterns of Opioids in USA in the year 2016.

### Methodology:

Selection of topic:

* Why this topic?
* Opioids are main cause of death in US
* Importance of data analytics in health care industry.

Opioid painkillers are supposed to provide pain relief, but there are many injuries and deaths because they have been inappropriately prescribed. With the use of analysis tools one can make useful inferences and predictions with the available data which will help the health care industries to improve the clinical outcomes.

Source of information:
The main source of information was from the website : https://www.cdc.gov/ and 
https://data.cms.gov/ .

Data Structure:

The data was available on the CMS and CDC websites and we used the available APIs to access the data:

* Socrata("data.cms.gov", "dLbTEKbMpc1G4L7fCsOvHvATT")
* Socrata("data.cdc.gov", "dLbTEKbMpc1G4L7fCsOvHvATT")

The technologies that were used in this project were Google API, SOCRATA, PANDAS, and MongoDB:

•	Cleaning of data
The data was pretty huge which was cleaned on pandas by the dropna function where all the NaN values were dropped.
•	Storing of the data
Add – MongoDb, API link.


### Analysis and Results
•	Graphs/Results and Analysis
The data was divided into two parts – “Opioids prescriber analysis” and the “Open payments”.

Opioids prescriber analysis 
The data explored the Opioids prescriber based on the medicare data from the CMS. 

•	The result showed that there were 602,734 opioid overdose deaths in the US in 2016.
•	The table below clearly shows that total deaths due to opioids overdose is 452,369 in the year 2016 in USA as a whole. The total number of deaths was maximum in the New York state (20,733) followed by Maryland (17,918) and North Carolina (16,343).

![Heat Map of Opioid Prescriptions](finian/Images/opioid_prescription_heat_map.png)

Open payments:

The data was cleaned by the dropna function which dropped all the NaN function.
The analysis shows that there are 5 main opioid manufacturers in the data.
   
State Colorado tops the list of the recipient state 