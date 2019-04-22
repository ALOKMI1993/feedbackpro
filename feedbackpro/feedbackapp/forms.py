from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter name'
            }
        )
    )
    rating=forms.IntegerField(
        label='Rating',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Rating'
            }
        )
    )
    feedback=forms.CharField(
        label='Feedback',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Feedback'
            }
        )
    )
