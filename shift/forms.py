from django import forms


LIBRARIES_CHOICES = (
    ('submit', 'submit'),
    ('cancel', 'cancel'),
    ('check', 'check'),
    ('calculate', 'calculate'),
)


class shiftForm(forms.Form):
    type = forms.ChoiceField(
        label='操作',
        widget=forms.Select,
        choices=LIBRARIES_CHOICES,
        required=True,
    )
    name = forms.CharField(label="名前", max_length=20, required=True)
    date = forms.DateField(label='日付', required=False)
    start_at = forms.TimeField(label='開始時間', required=False, initial=None)
    end_at = forms.TimeField(label='終了時間', required=False, initial=None)
