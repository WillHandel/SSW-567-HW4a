import unittest
from unittest.mock import patch
from githubGetter import getGithubInfo

class testGithubGetter(unittest.TestCase):

    @patch('githubGetter.requests.get')
    def test_getGithubInfo(self, mock_get):
        mock_get.side_effect = [
            unittest.mock.Mock(json=lambda: [
                {"name": "repo1"},
                {"name": "repo2"}
            ]),
            # Mock the response for the commits of repo1
            unittest.mock.Mock(json=lambda: [{}] * 5),
            # Mock the response for the commits of repo2
            unittest.mock.Mock(json=lambda: [{}] * 3)
        ]

        result = getGithubInfo("WillHandel")
        expected = [
            "Repo: repo1, Number of commits: 5",
            "Repo: repo2, Number of commits: 3"
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()