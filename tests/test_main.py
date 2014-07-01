import unittest
from unittest.mock import Mock
from unittest.mock import patch

import pypygo

@patch('pypygo.main.requests')
class TestMainFunctions(unittest.TestCase):

    def test_query_foo(self, mock_requests):
        def decode(cls):
            with open('foo_query.txt') as f:
                raw_json = ''.join(f.readlines())
                return cls().decode(raw_json)
        mock_response = Mock()
        mock_response.json.side_effect = decode
        mock_requests.get.return_value = mock_response
        response = pypygo.query('foo')
        params = {'q': 'foo',
                  'format': 'json',
                  'pretty': 0}
        self.assertEqual(response.abstract, 'no abstract')
        self.assertEqual(response.abstract_text, 'no abstract text')
        self.assertEqual(response.abstract_src, 'Wikipedia')
        self.assertFalse(response.image)
        self.assertEqual(response.type, 'disambiguation')
        self.assertEqual(len(response.related_topics), 2)
        self.assertListEqual(response.infobox, [])
        self.assertListEqual(response.results, [])
        mock_requests.get.assert_called_once_with('https://api.duckduckgo.com',
                                                  params=params)

    def test_query_foobar(self, mock_requests):
        def decode(cls):
            with open('foobar_query.txt') as f:
                raw_json = ''.join(f.readlines())
                return cls().decode(raw_json)
        mock_response = Mock()
        mock_response.json.side_effect = decode
        mock_requests.get.return_value = mock_response
        response = pypygo.query('foo')
        params = {'q': 'foo',
                  'format': 'json',
                  'pretty': 0}
        self.assertEqual(response.abstract, 'no abstract')
        self.assertEqual(response.abstract_text, 'no abstract text')
        self.assertEqual(response.abstract_src, 'Wikipedia')
        self.assertTrue(response.image)
        self.assertEqual(response.type, 'article')
        self.assertEqual(len(response.related_topics), 2)
        self.assertEqual(len(response.infobox.content), 2)
        self.assertEqual(len(response.infobox.meta), 2)
        self.assertEqual(len(response.results), 1)
        mock_requests.get.assert_called_once_with('https://api.duckduckgo.com',
                                                  params=params)

if __name__ == '__main__':
    unittest.main()
