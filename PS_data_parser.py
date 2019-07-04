import pandas as pd
import re

def dataParser(name):
    df = pd.read_excel(name)
    numRows = df.shape[0]

    # Dropping Unneccessary columns
    df = df.drop(columns=['Class Serial Number','First Name\t', 'Second Name\t', 'Last Name\t',
       "Father's Name\t", "Mother's Name",
       'Any Sibling (Studying in IPU College) If Yes then give details\t',
       "Preparing for GATE/GRE/GMAT/CAT etc give details, if any\t",'10th Board Name',
       'Year of Passing-10th\t', '10th School City\t', '10th School State\t','12th Board Name', 'Year of Passing-12th\t',
       '12th School City\t', '12th School State\t', 'Diploma %',
       'Diploma Board Name\t', 'Year of Passing - Diploma\t',
       'Graduation Degree\t', 'Branch', '1st Semester%\t', '2nd Semester%\t',
       '3rd Semester%\t', '4th Semester%', '5th Semester %', '6th Semester %',
       '7th Semester %', '8th Semester %','Address', 'Address\t', 'Address Line 1\t', 'Address Line 2\t',
       'City\t\t', 'State', 'Pin Code\t', 'College Name'])

    # Creating homogenity among university roll numbers
    # Length of each roll number is now equal to 11

       # Filling NaN with 0
    df['Residence No\t'].fillna('0',inplace = True)
    df['Residence No\t'] = df['Residence No\t'].replace('','0')
    df['Residence No\t'] = df['Residence No\t'].replace('-','0')
    df['Gap Year'].fillna(0, inplace = True)
#     df['Gap Year'] = df['Gap Year'].replace('',0)
    df['10th %\t'].fillna(0, inplace = True)
#     df['10th %\t'] = df['10th %\t'].replace('',0)
    df['12th %'].fillna(0, inplace = True)
#     df['12th %'] = df['12th %'].replace('',0)
    df['B.Tech %\t'].fillna(0, inplace = True)
#     df['B.Tech %\t'] = df['B.Tech %\t'].replace('',0)
    df['Backlogs\t'].fillna(0, inplace = True)
#     df['Backlogs\t'] = df['Backlogs\t'].replace('',0)
    df['CGPA'].fillna(0, inplace = True)
#     df['CGPA'] = df['CGPA'].replace('',0)
    df['Package'].fillna(0, inplace = True)
#     df['Package'] = df['Package'].replace('',0)

    for i in range(numRows):
       df.iloc[i,1] = str(df.iloc[i,1])
       df.iloc[i,1] = re.sub('[\'`~!@#$%^&*()-+=(a-zA-Z){}|\:;",./?]',' ',df.iloc[i,1])
       df.iloc[i,1] = df.iloc[i,1].split()[0]
       if(len(df.iloc[i,1]) < 11):
              while(len(df.iloc[i,1]) != 11):
                     df.iloc[i,1] = '0' + df.iloc[i,1]
       elif(len(df.iloc[i,1]) > 11):
              sObject = slice(1,12)
              df.iloc[i,1] = df.iloc[i,1][sObject]     

       # Name-> letters converted to uppercase()
       df.iloc[i,2] = df.iloc[i,2].upper()

      # Gender-> converted to 'M' and 'F' to avoid redundancy
       df.iloc[i,3] = df.iloc[i,3].upper()
       if df.iloc[i,3] == "MALE":
              df.iloc[i,3] = 'M'
       else:
              df.iloc[i,3] = 'F'        
       # DOB -> converted to general format of yyyy-mm-dd
       df.iloc[i,4] = str(df.iloc[i,4])
       sObject = slice(11)
       df.iloc[i,4] = df.iloc[i,4][sObject]
       df.iloc[i,4] = re.sub('[/_]','-', df.iloc[i,4])
       pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
       if(pattern.match(df.iloc[i,4]) != None):
              date_entity = df.iloc[i,4].split('-')
              df.iloc[i,4] = date_entity[2] + '-' + date_entity[1] + '-' + date_entity[0]
       df.iloc[i,4] = df.iloc[i,4][sObject]

       # Mobile Numbers -> Multiple entries removed, each number has 10 digits.
       df.iloc[i,6] =str(df.iloc[i,6])
       df.iloc[i,6] = df.iloc[i,6].split(',')[0]
       df.iloc[i,6] = df.iloc[i,6].replace(' ','')
       df.iloc[i,6] = df.iloc[i,6].replace('\u202c','')
       if len(df.iloc[i,6]) > 10:
              while(len(df.iloc[i,6]) != 10):
                     df.iloc[i,6] = df.iloc[i,6][1:]

       # Telephone Numbers
       df.iloc[i,7] = str(df.iloc[i,7])
       df.iloc[i,7]= re.sub('[\'`~!@#$%^&*()-+=(a-zA-Z){}|\:;",./?]',' ',df.iloc[i,7])
       df.iloc[i,7] = df.iloc[i,7].replace(' ','')
       df.iloc[i,7] = df.iloc[i,7].replace('-','')
       if len(df.iloc[i,7]) == 8:
              df.iloc[i,7] = "011" + df.iloc[i,7]
       elif len(df.iloc[i,7]) > 11:
              while(len(df.iloc[i,7]) != 11):
                     df.iloc[i,7] = df.iloc[i,7][1:]

       # Email
       df.iloc[i,5] = df.iloc[i,5].split(',')[0]

    return df

