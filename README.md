# data_team
Recuruitment Task

Analizator 2000 - fully* automated script for:
- Un-taring provided data
- Getting and categorizing json files
- Reading json files content
- Getting informations from the data
- Ploting charts from the data
- Saving everything in files(.txt for informations and .png for generated charts)

*You just need to paste the .tar.gz file into the script location and after generating each plot rename it.


Used:
- pandas
- tarfile
- json
- matplotlib


Procedure of the program is following:
1) Tar class is taking the file name given by user and un-taring it using un_tar_file function
2) JsonOperations class is categorizing the data into two lists(json_fse and json_dd) using categorize_json function and saving it into raw_fse and raw_dd variables
3) Once data is categorized the function present_data is showing us which data we have received from the .tar.gz file
4) read function takes the raw categorized lists and fetches its content into dd_data and fse_data lists
5) At this point we are free to calculate the data by using one of the functions: 
    - txt_file_calculation(calcualtes mean value, sum, etc.)
    - bar_plot(generating bar plots)
    - pie_plot(generating pie plots)
