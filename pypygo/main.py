import json

import requests
from pypygo.models import Response, RelatedTopic, Result
from pypygo.models import Icon, Infobox, InfoboxContent, InfoboxMeta


def query(qry):
    params = {'q': qry,
              'format': 'json',
              't': 'pypygo',
              'pretty': 0}
    resp = requests.get('https://api.duckduckgo.com', params=params)
    return resp.json(cls=ResponseDecoder)


class ResponseDecoder(json.JSONDecoder):
    def decode(self, raw_json):
        jsn = super().decode(raw_json)
        related_topics = [RelatedTopic(t, Icon(t['Icon']))
                          for t in jsn['RelatedTopics']]
        raw_infbx = jsn['Infobox']
        if hasattr(raw_infbx, 'get'):
            infobox = Infobox([InfoboxContent(c)
                              for c in raw_infbx['content']],
                              [InfoboxMeta(m)
                              for m in raw_infbx['meta']])
        else:
            infobox = []
        results = [Result(r, Icon(r['Icon']))
                          for r in jsn['Results']]
        return Response(jsn, related_topics, infobox, results)
