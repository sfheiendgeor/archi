from django import forms
from django.core.exceptions import ValidationError

widget = forms.NumberInput(attrs={'style': 'width:10ch',})


class Equation1Form(forms.Form):
    a = forms.FloatField(label = "a(mm, 短辺)", widget = widget)
    b = forms.FloatField(label = "b(mm, 長辺)",widget = widget)
    t1 = forms.FloatField(label = "t1(mm, 厚み)",widget = widget)
    t2 = forms.FloatField(label = "t2(mm)合わせガラス二層目",widget = widget , required = False)
    t3 = forms.FloatField(label = "t3(mm)合わせガラス三層目",widget = widget , required = False)
    t4 = forms.FloatField(label = "t4(mm)合わせガラス四層目",widget = widget , required = False)
    w = forms.FloatField(label = "W(N/m^2)",widget = widget)
    
    def clean(self):
        if self.cleaned_data['a'] > self.cleaned_data['b']:
            raise forms.ValidationError('aは短辺の寸法を入力して下さい')
        
    
class Equation2Form(forms.Form):
    a = forms.FloatField(label = "a(mm, 短辺)", widget = widget)
    b = forms.FloatField(label = "b(mm, 長辺)",widget = widget)
    t1 = forms.FloatField(label = "t1(mm, 厚み)",widget = widget)
    t2 = forms.FloatField(label = "t2(mm)合わせガラス二層目",widget = widget , required = False)
    t3 = forms.FloatField(label = "t3(mm)合わせガラス三層目",widget = widget , required = False)
    t4 = forms.FloatField(label = "t4(mm)合わせガラス四層目",widget = widget , required = False)
    a1 = forms.FloatField(label = "a1(mm, 短辺側矩形寸法)", widget = widget)
    b1 = forms.FloatField(label = "b1(mm, 長辺側矩形寸法)",widget = widget)
    w = forms.FloatField(label = "W(N/m^2)",widget = widget)
    
class Equation3Form(forms.Form):
    a = forms.FloatField(label = "a(mm, フリー辺)", widget = widget)
    b = forms.FloatField(label = "b(mm, 他辺)",widget = widget)
    t1 = forms.FloatField(label = "t1(mm, 厚み)",widget = widget)
    t2 = forms.FloatField(label = "t2(mm)合わせガラス二層目",widget = widget , required = False)
    t3 = forms.FloatField(label = "t3(mm)合わせガラス三層目",widget = widget , required = False)
    t4 = forms.FloatField(label = "t4(mm)合わせガラス四層目",widget = widget , required = False)
    w = forms.FloatField(label = "W(N/m^2)",widget = widget)
    
class Equation4Form(forms.Form):
    a = forms.FloatField(label = "a(mm, フリー辺)", widget = widget)
    b = forms.FloatField(label = "b(mm, 他辺)",widget = widget)
    t1 = forms.FloatField(label = "t1(mm, 厚み)",widget = widget)
    t2 = forms.FloatField(label = "t2(mm)合わせガラス二層目",widget = widget , required = False)
    t3 = forms.FloatField(label = "t3(mm)合わせガラス三層目",widget = widget , required = False)
    t4 = forms.FloatField(label = "t4(mm)合わせガラス四層目",widget = widget , required = False)
    w = forms.FloatField(label = "W(N/m^2)",widget = widget)
    
class Equation5Form(forms.Form):
    a1 = forms.FloatField(label = "a1(mm, 支点-荷重点距離(長))", widget = widget)
    a2 = forms.FloatField(label = "a2(mm, 支点-荷重点距離(短))",widget = widget)
    b = forms.FloatField(label = "b(mm, ガラス幅)",widget = widget)
    t1 = forms.FloatField(label = "t1(mm, 厚み)",widget = widget)
    t2 = forms.FloatField(label = "t2(mm)合わせガラス二層目",widget = widget , required = False)
    t3 = forms.FloatField(label = "t3(mm)合わせガラス三層目",widget = widget , required = False)
    t4 = forms.FloatField(label = "t4(mm)合わせガラス四層目",widget = widget , required = False)
    P = forms.FloatField(label = "P(N/m^2)",widget = widget)
    
class Equation6Form(forms.Form):
    a = forms.FloatField(label = "a(mm, 矩形寸法)", widget = widget)
    t1 = forms.FloatField(label = "t1(mm, 厚み)",widget = widget)
    t2 = forms.FloatField(label = "t2(mm)合わせガラス二層目",widget = widget , required = False)
    t3 = forms.FloatField(label = "t3(mm)合わせガラス三層目",widget = widget , required = False)
    t4 = forms.FloatField(label = "t4(mm)合わせガラス四層目",widget = widget , required = False)
    w = forms.FloatField(label = "W(N/m^2)",widget = widget)

class Equation7Form(forms.Form):
    a = forms.FloatField(label = "a(mm, 半径)", widget = widget)
    t1 = forms.FloatField(label = "t1(mm, 厚み)",widget = widget)
    t2 = forms.FloatField(label = "t2(mm)合わせガラス二層目",widget = widget , required = False)
    t3 = forms.FloatField(label = "t3(mm)合わせガラス三層目",widget = widget , required = False)
    t4 = forms.FloatField(label = "t4(mm)合わせガラス四層目",widget = widget , required = False)
    w = forms.FloatField(label = "W(N/m^2)",widget = widget)