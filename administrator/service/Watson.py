from os.path import dirname, join
from watson_developer_cloud import VisualRecognitionV3
import json

class Watson():

    def __init__(self):
        """
            Construct an instance. Fetches
        """

        self.visual_recognition = VisualRecognitionV3(
            '2016-05-20',
            api_key='b4f3dd2ed8cc318ded9dca6db19dfc38f7287491')


    def createClassifier(self, name):
        """
            Cria o novo classificador
            :param name:
        """
        with open(join(dirname(__file__), '../../media/'+ name + '_positive'), 'rb') as positive, \
             open(join(dirname(__file__), '../../media/'+ name + '_negative'), 'rb') as negative:

            ret = json.dumps(self.visual_recognition.create_classifier(
            name, disease_positive_examples=positive, negative_examples = negative), indent=2)
            print(ret)


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
        path = 'https://belezanoardotnet.files.wordpress.com/2016/05/psoriaz-4_1.jpeg';
        return json.dumps(self.visual_recognition.classify(images_url=path))



    def listClassifiers(self):
        """

        """
        return json.dumps(self.visual_recognition.list_classifiers(), indent=2)



class Parser():
    def __init__(self):
        """
        """

    def parseResponseClassifier(self, response):
        return response