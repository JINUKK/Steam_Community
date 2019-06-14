from django import forms
from .models import Category, Document

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['category', 'title', 'text', 'attachment']

    def __init__(self, *args, **kwargs):
        # print(args)
        # print(kwargs)
        default_category = None
        if 'default_category' in kwargs:
            default_category = kwargs['default_category']
            del(kwargs['default_category']) # default_category라는 변수를 만들고 kwargs에서 값을 빼서 저장한 뒤 다시 지워줌
        super().__init__(*args, **kwargs)
        self.fields['category'].label = ""
        self.fields['title'].label = ""
        self.fields['text'].label = ""
        self.fields['attachment'].label = ""
        if default_category:
            self.fields['category'].queryset = Category.objects.filter(parent_category=default_category)
        self.fields['title'].widget.attrs = {'placeholder': "제목"}
