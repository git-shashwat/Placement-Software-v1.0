# Placement-Software-v1.0
I developed this project to ease out the working of my college’s placement cell by performing the following tasks on a Master Database Excel sheet which usually contains over **600+ records**: 

1. Students' placement record **Database Parsing** which includes:
* Setting homogenity in fields such as Enrollment Numbers, Date of Birth.
* Reducing data redundancy and Duplicacy particularly in contact details.
2. **Refining Parsed Database** based on the company profile:
* Based on the Company's Requirements such as B.Tech %, Backlogs, 12<sup>th</sup> % etc. , the parsed Database then undergoes a process of sorting and filtering of records.
* The Refined Database is then stored in a [Company_Name].xlsm format in the local directory for easy access later.
3. **Database Preview**: Once the records are refined, user can navigate to the *Preview* section of the software to take a look at the generated Database.

4. **Email Notifications** to selected/filtered students: User can access the *send e-mail* section of the software to send 
E-mails to the students to notify them about interview details from the software itself. 
***
## I used the following technologies to develop this software:
+ Python 3
+ Pandas
> For Dataframe operations.
+ Regular Expressions
> For Refining Dataframe entries
+ Tkinter
> Used to bind the complete application into a GUI.
***
# Preview
1. Upload Window
![upload window](https://user-images.githubusercontent.com/43851597/61184069-d14efb00-a666-11e9-8922-418c5cb751aa.gif)
2. Company Profile Window
![profile window](https://user-images.githubusercontent.com/43851597/61184102-5f2ae600-a667-11e9-8e74-24dd7631f1f9.gif)
3. Preview Window
![preview window](https://user-images.githubusercontent.com/43851597/61184154-0ad43600-a668-11e9-898f-871b116f79ba.gif)
4. E-mail Window
![email window](https://user-images.githubusercontent.com/43851597/61184196-98178a80-a668-11e9-88b6-ebea3d4fb4ef.gif)
