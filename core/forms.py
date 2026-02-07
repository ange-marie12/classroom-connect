from django import forms

class StudentEnrollmentForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2026)), required=True)

class CourseCreationForm(forms.Form):
    course_name = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    start_date = forms.DateField(widget=forms.SelectDateWidget(), required=True)
    end_date = forms.DateField(widget=forms.SelectDateWidget(), required=True)

class CourseManagementForm(forms.Form):
    course_id = forms.IntegerField(required=True)
    status = forms.ChoiceField(choices=[('active', 'Active'), ('inactive', 'Inactive')], required=True)
    update_info = forms.CharField(widget=forms.Textarea, required=False)