from django import forms
from .models import Category, Document, Comment

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['app_name', 'app_image', 'app_price', 'app_link', 'app_release_date', 'category', 'title', 'text', 'attachment']

    def __init__(self, *args, **kwargs):
        # print(args)
        # print(kwargs)
        default_category = None
        if 'default_category' in kwargs:
            default_category = kwargs['default_category']
            del(kwargs['default_category']) # default_category라는 변수를 만들고 kwargs에서 값을 빼서 저장한 뒤 다시 지워줌
        super().__init__(*args, **kwargs)
        self.fields['app_name'].widget = forms.HiddenInput()
        self.fields['app_image'].widget = forms.HiddenInput()
        self.fields['app_price'].widget = forms.HiddenInput()
        self.fields['app_link'].widget = forms.HiddenInput()
        self.fields['app_release_date'].widget = forms.HiddenInput()
        self.fields['category'].label = ""
        self.fields['title'].label = ""
        self.fields['text'].label = ""
        self.fields['attachment'].label = ""
        if default_category:
            qs = Category.objects.filter(parent_category=default_category)
            if qs:
                self.fields['category'].queryset = qs
            else:
                self.fields['category'].queryset = Category.objects.filter(parent_category=default_category.parent_category)
        self.fields['title'].widget.attrs = {'placeholder': "제목"}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = ""
        self.fields['text'].widget.attrs = {'class': "form-control", 'placeholder': "댓글을 남겨주세요."}

