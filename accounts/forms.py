from django import forms

from accounts.models import User


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'role', 'phone_number', 'email', 'is_staff', 'phone_number',
            'is_phone_verified', 'sub_domain', 'timezone', 'country', 'currency_symbol', 'notification_method',
            'enable_calendar_module'
        )

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
