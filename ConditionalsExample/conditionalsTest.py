import unittest
import conditions


class MyTestCase(unittest.TestCase):
    def test_check_validity_to_vote_true(self):
        result = conditions.check_validity_to_vote(2000)
        self.assertEqual('Congrats. You are allowed to vote', result)

    def test_check_validity_to_vote_false(self):
        result = conditions.check_validity_to_vote(2020)
        self.assertEqual('Sorry. You are too young to vote', result)

    def test_check_(self):
        result = conditions.check_validity_to_vote(2020)
        self.assertEqual('Sorry. You are too young to vote', result)


if __name__ == '__main__':
    unittest.main()
