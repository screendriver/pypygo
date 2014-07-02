import os
import unittest
from unittest.mock import Mock
from unittest.mock import patch

import pypygo

@patch('pypygo.main.requests')
class TestMainFunctions(unittest.TestCase):

    def test_query_foo(self, mock_requests):
        side_effect = lambda cls: self._decode('foo_query.txt', cls)
        mock_response = Mock()
        mock_response.json.side_effect = side_effect 
        mock_requests.get.return_value = mock_response
        response = pypygo.query('foo')
        params = {'q': 'foo',
                  'format': 'json',
                  't': 'pypygo',
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
        side_effect = lambda cls: self._decode('foobar_query.txt', cls)
        mock_response = Mock()
        mock_response.json.side_effect = side_effect
        mock_requests.get.return_value = mock_response
        response = pypygo.query('foo')
        params = {'q': 'foo',
                  'format': 'json',
                  't': 'pypygo',
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

    def _decode(self, file_name, decoder):
        dirpath = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(dirpath, file_name)
        with open(filepath) as f:
            raw_json = ''.join(f.readlines())
            return decoder().decode(raw_json)


if __name__ == '__main__':
    unittest.main()
