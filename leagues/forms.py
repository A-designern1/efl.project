from django import forms

from leagues.models import User, League, Team




class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class AddLeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = '__all__'

class AddTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

