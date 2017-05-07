changes_file = 'changes_python.txt'
sep = 72*'-'
import datetime
import csv

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

    def get_commit_comment(commit):
        return 'svn merge -r' + str(commit.revision-1) + ':' + str(commit.revision) + ' by ' \
                + commit.author + ' with the comment ' + ','.join(commit.comment) \
                + ' and the changes ' + ','.join(commit.changes)

def get_attribute(data, attribute):
    result = {}
    for commit in data:
        value = getattr(commit, attribute)
        item = value
        result[item] = result.get(item, 0) + 1
    return result
 
def get_change_stats_by_author(data):
    all_authors = []
    for commit in data:
        new_author = {}
        author = commit.author
        match_found = False 
        if len(all_authors) > 0:
            for record in all_authors:
                if record['Author'] == author :
                    record['Commit Type A'] += commit.number_a
                    record['Commit Type D'] += commit.number_d
                    record['Commit Type M'] += commit.number_m
                    record['Commit Type R'] += commit.number_r
                    record['Total'] += commit.number_changes
                    match_found = True
                    break
                   
        if len(all_authors) == 0 or match_found == False :       
            new_author = {'Author': author, 'Commit Type A': commit.number_a, 'Commit Type D': commit.number_d, 'Commit Type M': commit.number_m, 
                'Commit Type R': commit.number_r, 'Total' : commit.number_changes }  
            all_authors.append(new_author)
     
    return all_authors
    
def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data  

def get_commits(data):
    commits = []
    current_commit = None
    index = 0   

    author = {}
    while True:
        try:
            # parse each of the commits and put them into a list of commits
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

def save_dict_as_csv (data,location):
    with open(location,'wb') as output_file:
        w = csv.writer(output_file)
        w.writerow(data.keys())
        w.writerow(data.values())      
    output_file.close()
    
def save_dict_list_as_csv(data, location) :          
    keys = data[0].keys()
    with open(location, 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
            
    output_file.close()
    
def print_dict_to_console(data,title):
    print title
    print "="*len(title)
    ls = list()
    for key, val in data.items():
        ls.append((val,key))
    ls.sort(reverse = True)
    for key, val in ls:
        print key, val
    return ls
   
data = read_file(changes_file)
results = get_commits(data)
save_commit_list_as_csv("Commit List.csv") 

authors = get_attribute(results, "author")
days = get_attribute(results, "dayinweek")
weeks = get_attribute(results, "weeknumber")
months = get_attribute(results, "month")
change_stats = get_change_stats_by_author(results)

filetoCSV = authors
save_dict_as_csv(filetoCSV,"Counts of Revisions By Author.csv") 

filetoCSV = days
save_dict_as_csv(filetoCSV,"Counts of Revisions By Day in Week.csv") 

filetoCSV = weeks
save_dict_as_csv(filetoCSV,"Counts of Revisions By Week Number.csv") 

filetoCSV = months
save_dict_as_csv(filetoCSV,"Counts of Revisions By Month.csv") 

filetoCSV = change_stats
save_dict_list_as_csv(filetoCSV,"Counts of Files Changed By Author By Type.csv") 

print authors
print days
print weeks
print months
console1 = print_dict_to_console(authors, "Revisions By Author")

title = "Revisions by Author By Change Type"
print title
print "=" * len(title)
for row in change_stats:
    print row

     
     
     