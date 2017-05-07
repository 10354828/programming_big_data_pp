
import unittest

from CA4_Python_Script import read_file, get_commits, get_revisions_by_attribute, get_file_changes_by_action

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.txt')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0].author)
        self.assertEqual(1551925, commits[0].revision)
        
    def test_last_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[421].author)
        self.assertEqual(1491146, commits[421].revision)         
        
    def test_number_of_authors(self):
        commits = get_commits(self.data)
        authors = get_revisions_by_attribute(commits, "author")
        self.assertEqual(10, len(authors))
        self.assertEqual(191, authors['Thomas'])
        self.assertEqual(1, authors['murari.krishnan'])
        self.assertEqual(152, authors['Jimmy'])

    def test_day_in_week(self):
        commits = get_commits(self.data)
        daysinweek = get_revisions_by_attribute(commits, "dayinweek")
        self.assertEqual(5, len(daysinweek))
        self.assertEqual(118, daysinweek['Thu'])
        self.assertEqual(53, daysinweek['Mon'])
        self.assertEqual(76, daysinweek['Wed'])
    
    def test_week(self):
        commits = get_commits(self.data)
        weeks = get_revisions_by_attribute(commits, "weeknumber")
        self.assertEqual(20, len(weeks))
        self.assertEqual(50, weeks['28'])
        self.assertEqual(33, weeks['47'])
        self.assertEqual(4, weeks['38'])

    def test_number_files_actioned(self):
        commits = get_commits(self.data)
        file_changes = get_file_changes_by_action(commits) 
        total = 0
        index = 0
        while index < len(file_changes):
            total = total + file_changes[index]["Total Files Actioned"]
            index = index + 1
        self.assertEqual(3011, total)
        
    def test_files_actioned_by_author_by_type(self):
        commits = get_commits(self.data)
        file_changes = get_file_changes_by_action(commits)
        self.assertEqual(10, len(file_changes))
        # test author name 'Thomas'
        self.assertEqual(1359, file_changes[0]["Total Files Actioned"])
        self.assertEqual(87, file_changes[0]["Action Type A"])
        self.assertEqual(663, file_changes[0]["Action Type D"])
        self.assertEqual(609, file_changes[0]["Action Type M"])
        self.assertEqual(0, file_changes[0]["Action Type R"])
        # test author name 'Alan'
        self.assertEqual(30, file_changes[9]["Total Files Actioned"])
        self.assertEqual(9, file_changes[9]["Action Type A"])
        self.assertEqual(6, file_changes[9]["Action Type D"])
        self.assertEqual(15, file_changes[9]["Action Type M"])
        self.assertEqual(0, file_changes[9]["Action Type R"])  
   
        
if __name__ == '__main__':
    unittest.main()