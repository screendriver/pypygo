import requests
import simplejson
from pypygo.models import (Response,
                           RelatedTopic,
                           Result,
                           Icon,
                           Infobox,
                           InfoboxContent,
                           InfoboxMeta)


def query(qry):
    params = {'q': qry,
              'format': 'json',
              'pretty': 0}
    resp = requests.get('https://api.duckduckgo.com', params=params)
    return resp.json(cls=ResponseDecoder)


class ResponseDecoder(simplejson.JSONDecoder):
    def decode(self, json):
        json = super().decode(json)
        related_topics = [RelatedTopic(t, Icon(t['Icon']))
                          for t in json['RelatedTopics']]
        infobox = Infobox([InfoboxContent(c)
                           for c in json['Infobox']['content']],
                          [InfoboxMeta(m)
                           for m in json['Infobox']['meta']])
        results = [Result(r, Icon(r['Icon']))
                          for r in json['Results']]
        return Response(json, related_topics, infobox, results)