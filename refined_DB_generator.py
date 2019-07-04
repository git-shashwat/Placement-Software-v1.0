import pandas as pd
import re

def refinedDBcreator(parsedFileName, branchChoices, tenth_input_choice, twelth_input_choice, btech_input_choice, backlog_entry_choice, gapyear_entry_choice, gender_input):
    df = pd.read_excel(parsedFileName,converters={'University Roll Number': lambda x: str(x),'Residence No': lambda x: str(x),'Mobile Number': lambda x: str(x)})
    RDF = pd.DataFrame()

    # **** To check if list contains all branches or not

    if 'all' not in branchChoices:
        # **** CSE DF ****
        if 'cse' in branchChoices:
            RDF = RDF.append(df[(df['Class'].str.contains("CSE")) & (df['10th %'] >= tenth_input_choice) &(df['12th %'] >= twelth_input_choice) & (df['B.Tech %'] >= btech_input_choice) & (df['Backlogs'] <= backlog_entry_choice) & (df['Gap Year'] <= gapyear_entry_choice)])

        # **** ECE DF ****
        if 'ece' in branchChoices:
            RDF = RDF.append(df[(df['Class'].str.contains("ECE")) & (df['10th %'] >= tenth_input_choice) &(df['12th %'] >= twelth_input_choice) & (df['B.Tech %'] >= btech_input_choice) & (df['Backlogs'] <= backlog_entry_choice) & (df['Gap Year'] <= gapyear_entry_choice)])

        # **** EEE DF *****
        if 'eee' in branchChoices:
            RDF = RDF.append(df[(df['Class'].str.contains("EEE")) & (df['10th %'] >= tenth_input_choice) &(df['12th %'] >= twelth_input_choice) & (df['B.Tech %'] >= btech_input_choice) & (df['Backlogs'] <= backlog_entry_choice) & (df['Gap Year'] <= gapyear_entry_choice)])

        # **** IT DF ****
        if 'it' in branchChoices:
            RDF = RDF.append(df[(df['Class'].str.contains("IT")) & (df['10th %'] >= tenth_input_choice) &(df['12th %'] >= twelth_input_choice) & (df['B.Tech %'] >= btech_input_choice) & (df['Backlogs'] <= backlog_entry_choice) & (df['Gap Year'] <= gapyear_entry_choice)])
    else:
        RDF = RDF.append(df[(df['10th %'] >= tenth_input_choice) &(df['12th %'] >= twelth_input_choice) & (df['B.Tech %'] >= btech_input_choice) & (df['Backlogs'] <= backlog_entry_choice) & (df['Gap Year'] <= gapyear_entry_choice)])

    # ***** Female candidates only ****
    if gender_input == 'yes':
        RDF = RDF[(RDF['Gender'] == 'F')]

    # ***** Sorting on basis of secured packages *****
    RDF.sort_values('Package', inplace = True)
    RDF.groupby('Class')

    return RDF