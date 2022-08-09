import unittest

from db_controller import *


class TestConnectDB(unittest.TestCase):

    def test_connect_db(self):
        connector = connect_db()
        self.assertIsNotNone(connector)

    def test_insert_record(self):

        data_to_insert = ['2022-08-03', '15:33']
        connector = connect_db()
        insert_record(connector, data_to_insert)

        query = "SELECT * FROM DATE"
        data = connector.execute(query)
        data_in_db = data.fetchone()

        self.assertIsNotNone(data_in_db)

        connector.close()

    def test_query_next_date(self):

        connector = connect_db()
        first_insert = ['2022-08-03', '15:33']
        second_insert = ['2022-08-01', '18:33']
        insert_record(connector, first_insert)
        insert_record(connector, second_insert)

        # AssertEqual without pk
        expected_output = ('2022-08-01', '18:33', False)
        test_output_row = query_next_date(connector)
        test_output = (test_output_row[0][1], test_output_row[0][2], test_output_row[0][3])
        self.assertEqual(expected_output, test_output)

        connector.close()

    def test_update_notified(self):
        connector = connect_db()
        data_to_insert = ['2000-01-01', '12:34']
        insert_record(connector, data_to_insert)

        query = connector.execute("SELECT * FROM DATE WHERE date = '2000-01-01' AND time = '12:34'")
        row_not_updated = query.fetchone()
        self.assertFalse(row_not_updated[3])

        update_notified(connector, row_not_updated[0])

        query_after = connector.execute("SELECT * FROM DATE WHERE date = '2000-01-01' AND time = '12:34'")
        updated_row = query_after.fetchone()
        self.assertTrue(updated_row[0])

        connector.execute("DELETE FROM DATE WHERE date = '2000-01-01' AND time = '12:34'")
        connector.commit()
        connector.close()

    def test_all_notified(self):
        connector = connect_db()
        self.assertFalse(all_notified(connector))


if __name__ == '__main__':
    unittest.main()
