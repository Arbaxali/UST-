import numpy as np




#Import the FAA (Federal Aviation Authority) dataset
import pandas as pd
exer = pd.read_csv(r'C:\Users\arbazalx\OneDrive - Intel Corporation\Desktop\javasc\flames website\faa_ai_prelim.csv')
print(exer)



print(exer.shape)



print(exer.head())

print(exer.columns)




#Create a new dataframe with only the required columns
analyze_dataframe = exer[['ACFT_MAKE_NAME','LOC_STATE_NAME','ACFT_MODEL_NAME','RMK_TEXT',
                                       'FLT_PHASE','EVENT_TYPE_DESC','FATAL_FLAG']]





#View the type of the object
print(type(analyze_dataframe))



print("Check if the dataframe contains all the required attributes ")
print(analyze_dataframe.head())



print("Replace all Fatal Flag missing values with the required output")
print(analyze_dataframe['FATAL_FLAG'].replace('N/A',np.nan))



print("Verify if the missing values are replaced")
print(analyze_dataframe.head())




print("Check the number of observations")
print(analyze_dataframe.shape)



print("Drop the unwanted values/observations from the dataset")
final_dataset = analyze_dataframe.dropna(subset = ['ACFT_MAKE_NAME'])





print("Check the number of observations now to compare it with the original dataset and see how many values have been dropped")
print(final_dataset.shape)



print("Group the dataset by aircraft name")
aircraftType = final_dataset.groupby('ACFT_MAKE_NAME')




print("View the number of times each aircraft type appears in the dataset (Hint: use the size() method)")
aircraftType.size()





print("Group the dataset by fatal flag")
fatalAccident = final_dataset.groupby('FATAL_FLAG')



print("View the total number of fatal and non-fatal accidents ")
print(fatalAccident.size())



print("K Create a new dataframe to view only the fatal accidents (Fatal Flag values = Yes)")
accidents_with_fatality = fatalAccident.get_group('Yes')
print(accidents_with_fatality)




