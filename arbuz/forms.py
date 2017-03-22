from django import forms
from translator.views import *


class Base_Form:

    def Create_Fields(self):
        pass

    def Set_Widgets(self):
        pass

    def Exclude_Fields(self):
        pass

    def __init__(self, request):
        self.request = request

        self.Create_Fields()
        self.Set_Widgets()
        self.Exclude_Fields()



class Abstract_Model_Form(Base_Form, forms.ModelForm):

    def Edit_Instance(self):
        pass

    def __init__(self, request, *args, **kwargs):

        if 'instance' in kwargs:
            self.instance = kwargs['instance']
            self.Edit_Instance()

        forms.ModelForm.__init__(self, *args, **kwargs)
        Base_Form.__init__(self, request)



class Abstract_Form(Base_Form, forms.Form):

    def __init__(self, request, *args, **kwargs):
        forms.Form.__init__(self, *args, **kwargs)
        Base_Form.__init__(self, request)



class Abstract_Image_Form(Abstract_Form):

    def clean_image_base64(self):
        image_base64 = self.data['image_base64']

        if image_base64:
            image_base64 = Dynamic_Base.\
                Save_Image_From_Base64(image_base64)

            if not image_base64:
                raise forms.ValidationError(Text(self.request, 66))

        return image_base64

    def clean_url(self):
        image_url = self.data['url']

        if image_url:
            image_url = Dynamic_Base.\
                Save_Image_From_URL(image_url)

            if not image_url:
                raise forms.ValidationError(Text(self.request, 67))

        return image_url

    def clean_image(self):

        if self.data['url']:
            return 'url'

        if self.data['image_base64']:
            return 'image_base64'

        return ''

    def clean(self):

        if self.cleaned_data['image']:
            image = self.cleaned_data['image']
            self.cleaned_data['image'] = self.cleaned_data[image]

        return self.cleaned_data

    def Create_Fields(self):
        self.fields['image'] = forms.ImageField(required=False)
        self.fields['image_base64'] = forms.CharField(required=False)
        self.fields['url'] = forms.URLField(required=False)

    def Set_Widgets(self):

        image_base64_attr = {
            'hidden': 'true'
        }

        url_attrs = {
            'placeholder': Text(self.request, 97)
        }

        self.fields['image_base64'].widget = forms.TextInput(attrs=image_base64_attr)
        self.fields['url'].widget = forms.TextInput(attrs=url_attrs)
