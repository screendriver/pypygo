class Response:
    def __init__(self, json, related_topics, infobox, results):
        self.abstract = json['Abstract']
        self.abstract_text = json['AbstractText']
        self.abstract_src = json['AbstractSource']
        self.abstract_url = json['AbstractURL']
        self.image = json['Image']
        self.heading = json['Heading']
        self.answer = json['Answer']
        self.answer_type = json['AnswerType']
        self.definition = json['Definition']
        self.definition_url = json['DefinitionURL']
        self.type = {'A': 'article',
                     'D': 'disambiguation',
                     'C': 'category',
                     'N': 'name',
                     'E': 'exclusive'}\
            .get(json['Type'], 'nothing')
        self.related_topics = related_topics
        self.infobox = infobox
        self.results = results


class RelatedTopic:
    def __init__(self, json, icon):
        self.result = json['Result']
        self.first_url = json['Result']
        self.text = json['Text']
        self.icon = icon


class Icon:
    def __init__(self, json):
        self.url = json['URL']
        self.height = json['Height']
        self.width = json['Width']


class Result:
    def __init__(self, json, icon):
        self.result = json['Result']
        self.first_url = json['FirstURL']
        self.text = json['Text']
        self.icon = icon


class Infobox:
    def __init__(self, content, meta):
        self.content = content
        self.meta = meta


class InfoboxContent:
    def __init__(self, json):
        self.data_type = json['data_type']
        self.value = json['value']
        self.label = json['label']
        self.wiki_order = json['wiki_order']


class InfoboxMeta:
    def __init__(self, json):
        self.data_type = json['data_type']
        self.value = json['value']
        self.label = json['label']