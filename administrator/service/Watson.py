from os.path import dirname, join
from watson_developer_cloud import VisualRecognitionV3
import json
import logging
import requests
import urllib
logger = logging.getLogger()
class Watson():

    KEY_API = '5f1b04ca03706f380cda056c1a5768093a15a309'
    URI = 'https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classifiers/'

    def __init__(self):
        """
            Construct an instance. Fetches
        """

        self.visual_recognition = VisualRecognitionV3(
            '2016-05-20', api_key= self.KEY_API)


    def createClassifier(self, name):
        """
            Cria o novo classificador
            :param name:
        """
        with open(join(dirname(__file__), '../../media/'+ name + '_positive'), 'rb') as positive, \
             open(join(dirname(__file__), '../../media/'+ name + '_negative'), 'rb') as negative:

            ret = self.visual_recognition.create_classifier(
            name, disease_positive_examples=positive, negative_examples = negative)

            return ret


    def deleteClassifier(self, id):
        """
           deleteClassifier
           :param id :
        """
        self.visual_recognition.delete_classifier(classifier_id=id)


    def classifier(self, image):
        """
           :param image :
        """
        return json.dumps(self.visual_recognition.classify(images_url=image, owners=['me']))



    def listClassifiers(self):
        """

        """
        return json.dumps(self.visual_recognition.list_classifiers(), indent=2)


    def updateClassifier(self, name):
        return json.dumps({})



    def prepareRequest(self, classifier,data):

        requests.post(self.URI + classifier + '?api_key='+ self.KEY_API +'&version=2016-05-20', data)

        return requests.json()


class Parser():

    def __init__(self):
        """
        """

    def parseResponseClassifier(self, response):
        print response
        json_data = json.loads(response)
        print  json_data["images"][0]["classifiers"]
        #for key, value in json_data.images:
        #    print key, value

        return response