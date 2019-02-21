# data_team
Recuruitment Task

Analizator 2000 - automated script for:
- Un-taring provided package
- Getting and categorizing json files
- Reading json files content
- Getting specified pieces of data
- Ploting charts from the data
- Saving findings in newly created files (.png for generated charts or .txt for other outcome)

Libraries used:
- pandas
- tarfile
- json
- os
- matplotlib

Procedure:
1) Tar class takes in file name given by user and un-tares it.
2) JsonOperations class divides files into two lists(json_fse and json_dd) and saves it as raw_fse and raw_dd variables.
3) Once data is categorized function present_data shows lists of files received from the .tar.gz package.
4) read function takes the raw categorized lists, fetches its content and puts it into dd_data and fse_data lists.
5) At this point we are free to compute the data by using one of the functions: 
    - txt_file_calculation (calcualtes mean value, sum, etc.)
    - bar_plot (generates bar plots)
    - pie_plot (generates pie plots).
