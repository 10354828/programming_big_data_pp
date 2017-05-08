# Name: Paul Prew
# Student Number: 10354828
# Programming for Big Data
# CA 4

# This is a python program that will execute to read in a sample text data file which is named 'changes_python.txt'.  
# This program works to scrub/clean the data, and differentiate the content into 422 separate objects, 
# which can be represented as rows on a spreadsheet.
# Where possible additional data was derived from the data e.g. week number was derived from the date. 
# The data was mostly extracted from the title row.  
# Additionally, for each row the number of files actioned for each revision number was calculated, and broken out by action type e.g. A, D, M, R.
# This extract provides a count of the total number of file changes, broken out by action type. 
# This also enables analysis on the number of file changed by author, and breakdown by action type.

# In the program the 'Commit' class is used to define the elements of the 'commit data' extracted from the file.
# Each of the 422 commits, are represented as instance objects of the 'Commit' class.

# Functions operate on these objects to perform analysis on the commit data, and return the result as dictionary files.  
# Dictionary files are used for the analysys outputs, as this facilitates export as CSV. 

# Visualisation of analysis was done using charts in R Studio, and Microsoft Excel.

# When the program executes, the user is asked to confirm the action, to begin data file read.
# If successful, a message printed to the console will acknowledge this, and also display the total number of commits in the extract 
# and the total number of lines in the file.
# The user is then asked to confirm next action, to perform analysis on the commit data. 
# The program will then execute the analysis and export the results to CSV files in the working directory.
# When above step is completed, a message printed to the console will confirm this.

# The user will now be asked if they wish to print the analysis results to the console.  If the user selects this option
# the results are printed on screen.


sep = 72*'-'
import datetime
import csv
import os

# Below defines the class 'Commit' which is used to define the elements of the 'commit data' extracted from the file.
class Commit:
    'class for commits'
   
    def __init__(self, revision = None, author = None, fulldatetime = None, fulldate = None, dateinmonth = None, dayinweek = None, weeknumber = None, month = None, year = None,
            comment_line_count = None, number_changes = None, number_a = None, number_d = None, number_m = None, number_r = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.fulldatetime = fulldatetime
        self.fulldate = fulldate
        self.dateinmonth = dateinmonth
        self.dayinweek = dayinweek
        self.weeknumber = weeknumber
        self.month = month
        self.year = year
        self.comment_line_count = comment_line_count
        self.number_changes = number_changes
        self.changes = changes
        self.number_a = number_a
        self.number_d = number_d
        self.number_m = number_m
        self.number_r = number_r
        self.comment = comment

        
# Below is a generic function that will accept as parameter an attribute from the commit data
# This allows this function to be called multiple times with different parameter values 
# e.g. revisions by author, revisions by day.
def get_revisions_by_attribute(data, attribute):
    result = {}
    for commit in data:
        value = getattr(commit, attribute)
        item = value
        result[item] = result.get(item, 0) + 1
    return result

# Below function will get the total number of file changes for all 422 commits,
# and break them out by file change action type i.e. A, D, M, R,
# and also by author    
def get_file_changes_by_action(data):
    all_authors = []
    for commit in data:
        new_author = {}
        author = commit.author
        match_found = False 
        if len(all_authors) > 0:
            for record in all_authors:
                if record['Author'] == author :
                    record['Action Type A'] += commit.number_a
                    record['Action Type D'] += commit.number_d
                    record['Action Type M'] += commit.number_m
                    record['Action Type R'] += commit.number_r
                    record['Total Files Actioned'] += commit.number_changes
                    match_found = True
                    break
                   
        if len(all_authors) == 0 or match_found == False :       
            new_author = {'Author': author, 'Action Type A': commit.number_a, 'Action Type D': commit.number_d, 'Action Type M': commit.number_m, 
                'Action Type R': commit.number_r, 'Total Files Actioned' : commit.number_changes }  
            all_authors.append(new_author)
     
    return all_authors
    
def read_file(changes_file):
    data = [line.strip() for line in open(changes_file, 'r')]
    return data  

def get_commits(data):
    commits = []
    current_commit = None
    index = 0   

    author = {}
    while True:
        try:
            current_commit = Commit()
            details = data[index + 1].split('|')
            current_commit.revision = int(details[0].strip().strip('r'))
            current_commit.author = details[1].strip()
            current_commit.fulldatetime = details[2].strip()    
            current_commit.dateinmonth = int(details[2][9:11])
            current_commit.month = int(details[2][6:8])
            current_commit.year = int(details[2][0:5])
            current_commit.fulldate = datetime.date(current_commit.year, current_commit.month, current_commit.dateinmonth)
            current_commit.weeknumber = current_commit.fulldate.strftime("%W")
            current_commit.dayinweek = details[2][28:31]
            current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
            current_commit.changes = data[index+2:data.index('',index+1)]
            current_commit.number_changes = len(current_commit.changes)-1 
            current_commit.number_a = 0
            current_commit.number_d = 0
            current_commit.number_m = 0
            current_commit.number_r = 0
            for i in range(current_commit.number_changes) :
                if current_commit.changes[i + 1].startswith("A /") :
                    current_commit.number_a = current_commit.number_a + 1
                elif current_commit.changes[i + 1].startswith("D /") :
                    current_commit.number_d = current_commit.number_d + 1
                elif current_commit.changes[i + 1].startswith("M /") :
                    current_commit.number_m = current_commit.number_m + 1
                elif current_commit.changes[i + 1].startswith("R /") :
                    current_commit.number_r = current_commit.number_r + 1
            index = data.index(sep, index + 1)
            current_commit.comment = data[index-current_commit.comment_line_count:index]
            commits.append(current_commit)
        except IndexError:
            break
    return commits

# this function saves the commit list (class instances) to a CSV log file
def save_commit_list_as_csv (location):    
    with open(location,"wb") as data_export:
        fnameWriter = csv.writer(data_export)
        fnameWriter.writerow(["Revision", "Author", "Full Date/Time", "Full Date", "Date in Month", "Day in Week", "Week Number", "Month", "Year", "Comment Line Count", "Number Changes", "Number A", 
            "Number D", "Number M", "Number R", "Comment"])
        for commit in results:
            fnameWriter.writerow([commit.revision, commit.author, commit.fulldatetime, commit.fulldate, commit.dateinmonth, commit.dayinweek, commit.weeknumber, commit.month,
            commit.year, commit.comment_line_count, commit.number_changes, commit.number_a, commit.number_d, commit.number_m, commit.number_r,
            commit.comment])
    data_export.close()

# this function saves the analysis results to the console, and is used where the result to save, is formatted as a single dictionary
# the function accepts as parameters: data, and location, so can be used many times 
def save_dict_as_csv (data,location):
    with open(location,'wb') as output_file:
        w = csv.writer(output_file)
        w.writerows(data.items())
    output_file.close()

# this function saves the analysis results to a CSV log file, and is used where the result to save, is formatted as a list of dictionaries
def save_dict_list_as_csv(data, location) :          
    keys = data[0].keys()
    with open(location, 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)    
    output_file.close()

# this function prints the analysis results to the console, and is used where the result to print, is formatted as a single dictionary
# the function accepts as parameters: data, and location, so can be used many times     
def print_dict_to_console(data,title):
    print ''
    print title
    print "="*len(title)
    ls = list()
    for key, val in data.items():
        ls.append((val,key))
    ls.sort(reverse = True)
    for key, val in ls:
        print key, val
    return ls

# this function prints the analysis results to the console, and is used where the result to print, is formatted as a list of dictionaries
def print_dict_list_to_console(data, title): 
    print ''
    print title
    print "=" * len(title)
    for row in data:
        print row

def export_analysis_data_to_CSV():
    filetoCSV = authors
    save_dict_as_csv(filetoCSV,"Python_Export_Counts of Revisions By Author.csv") 

    filetoCSV = days
    save_dict_as_csv(filetoCSV,"Python Export_Counts of Revisions By Day in Week.csv") 

    filetoCSV = change_files
    save_dict_list_as_csv(filetoCSV,"Python Export_Counts of Files Changed By Action Type.csv")         

    
# main program 
if __name__ == '__main__':       
    
    os.system('cls')
    
    print '\n***************************************\n'
    print "Analysis for sample text file"
    print "Text file is 'changes_python.txt'"
    print '\n***************************************\n'
    while True:
        try: 
            s_inp = raw_input("Enter any key to read data file and get commits: ")
            data = read_file('changes_python.txt')
            results = get_commits(data)
            # following line saves the commit list with 422 rows to a csv which acts as a log file
            save_commit_list_as_csv("Python Export_Commit List.csv") 
            print "\nFile read was successful, and data has been extracted"
            print "{} rows of commits extracted from {} lines"  .format(len(results), len(data))
            print "Results saved to csv log file in working directory"
            break
        
        except:
            print "\nError while reading file. Please try again."
            print "Ensure text file is saved as 'changes_python.txt and is saved in the working directory."
            continue    
    
    s_inp = raw_input("\nEnter any key to perform analysis on commit data: ")
    
    authors = get_revisions_by_attribute(results, "author")
    days = get_revisions_by_attribute(results, "dayinweek")
    change_files = get_file_changes_by_action(results)
    
    export_analysis_data_to_CSV()

    print "\nAnalysis on commit data is completed"
    print "Results saved as CSV files in working directory"
     
    print "\nEnter 'Y' to print analysis summary to console"
    print "Enter any other key to exit program"
    choice = raw_input()
    if choice.lower() == 'y' :
        print_dict_to_console(authors, "Revisions By Author")
        print_dict_to_console(days, "Revisions By Day in Week")
        print_dict_list_to_console(change_files, "Revisions By File Changes By Author")
    else :
        print "\nExited program"
    

   



     
     
     