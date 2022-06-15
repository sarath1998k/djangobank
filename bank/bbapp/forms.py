from django import forms
from .models import Branches,AccountDetails


class AccountForm(forms.ModelForm):

    class Meta:
        model = AccountDetails
        fields = (
            'first_name',
            'last_name',
            'dob',
            'email',
            'mobile_number',
            'address_line_1',
            'gender',
            'type',
            'district',
            'branch',
            'card',
                  )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)          #super implementation os init method
        self.fields['branch'].queryset = Branches.objects.none() #quersyset responsible for showing all the sub branch

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branches.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')