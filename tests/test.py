import unittest
from unittest.mock import patch
import app


class TestDocsMethods(unittest.TestCase):
    def setUp(self):
        self.dirs, self.docs = app.update_date()
        with patch('app.update_date', return_value=(self.dirs, self.docs)):
            with patch('app.input', return_value='q'):
                app.secretary_program_start()

    def test_get_doc_owner_name(self):
        right_name = self.docs[0]['name']
        with patch('app.input', return_value='2207 876234'):
            check_name = app.get_doc_owner_name()
        self.assertIs(check_name, right_name)

    def test_get_all_doc_owner_names(self):
        names_list = [self.docs[0]['name'], self.docs[1]['name'], self.docs[2]['name']]
        check = (app.get_all_doc_owners_names())
        self.assertIs(len(check), len(names_list))

    def test_get_doc_shelf(self):
        right_number = '2'
        with patch('app.input', return_value=f'{self.dirs["2"][0]}'):
            check = app.get_doc_shelf()
        self.assertIs(right_number, check)

    def test_delete(self):
        before_len = len(self.docs)
        with patch('app.input', return_value='11-2'):
            app.delete_doc()
        self.assertLess(len(self.docs), before_len)

    def test_add(self):
        before_len = len(self.docs)
        with patch('app.input', size_effect=['12345', 'passport', 'testUser', '1']):
            app.add_new_doc()
        self.assertGreater(len(self.docs), before_len)

    def test_move_doc_to_shelf(self):
        with patch('app.input', size_effect=['11-2', '3']):
            app.move_doc_to_shelf()
        self.test_delete()

    def test_add_new_shelf(self):
        with patch('app.input', return_value='testNum'):
            app.add_new_shelf()
        self.assertIs(len(app.directories), 4)


if __name__ == '__main__':
    unittest.main()