from django.forms import ModelForm

from administrator.model import Disease


class FormDisease(ModelForm):

    def setClassfierId(self, classifier_id):
        self.classifier_id = classifier_id


    def save(self, commit=True):
        disease = super(FormDisease, self).save(commit=False)
        disease.classifier_id = self.classifier_id
        if commit:
            disease.save()

        return disease

    class Meta:
        model = Disease.Disease
        fields = ['name', 'type', 'description']
