from django import forms
from django.core.exceptions import ValidationError
from django.forms import RadioSelect

widget = forms.NumberInput(attrs={'style': 'width:13ch',})

def wrap_boolean_check(v):
    return not (v is False or v is None or v == '' or v == 0)


    
    
class SelectionForm(forms.Form):
    minIx = forms.FloatField(label = '強軸断面二次モーメントの最小値で検索',required = False, initial = 0, widget = widget)
    minZx = forms.FloatField(label = '強軸断面係数の最小値で検索',required = False, initial = 0, widget = widget)

class RectangleForm(forms.Form):
    material = forms.ChoiceField(choices=(('steel', 'steel'), ('aluminum', 'aluminum')),widget=RadioSelect, initial = 'steel')
    height = forms.FloatField(label = "H(mm)", widget = widget)
    width = forms.FloatField(label = "B(mm)",widget = widget)
    Lb = forms.FloatField(label = "Lb(mm)",widget = widget)
    E = forms.FloatField(label = "E(ヤング係数)", initial = 205000,widget = widget)
    G = forms.FloatField(label = "G(横弾性係数)", initial = 79000,widget = widget)
    F = forms.FloatField(label = "F(基準強度)", initial = 235,widget = widget)
    M1 = forms.FloatField(label = "端部モーメント(大, N.mm)", widget = widget, required = True, initial = 0)
    M2 = forms.FloatField(label = "端部モーメント(小, N.mm)", widget = widget, required = True, initial = 0)
    doublecurve = forms.BooleanField(label = '曲げモーメントが複曲率', required = False,initial = 0, widget = forms.CheckboxInput(check_test=wrap_boolean_check))
    
    
    def clean(self):
        if self.cleaned_data['M1'] < self.cleaned_data['M2']:
            raise forms.ValidationError('M1はM2より大きい値にしてください')
        return self.cleaned_data['M1']
    
class RoundForm(forms.Form):
    material = forms.ChoiceField(choices=(('steel', 'steel'), ('aluminum', 'aluminum')),widget=RadioSelect, initial = 'steel')
    D = forms.FloatField(label = "D(mm)",widget = widget)
    Lb = forms.FloatField(label = "Lb(mm)",widget = widget)
    E = forms.FloatField(label = "E(ヤング係数)", initial = 205000,widget = widget)
    G = forms.FloatField(label = "G(横弾性係数)", initial = 79000,widget = widget)
    F = forms.FloatField(label = "F(基準強度)", initial = 235,widget = widget)
    M1 = forms.FloatField(label = "端部モーメント(大, N.mm)", widget = widget, required = True, initial=0)
    M2 = forms.FloatField(label = "端部モーメント(小, N.mm)", widget = widget, required = True, initial=0)
    doublecurve = forms.BooleanField(label = '曲げモーメントが複曲率', required = False,initial = 0, widget = forms.CheckboxInput(check_test=wrap_boolean_check))
    
    
class SquarePipeForm(forms.Form):
    material = forms.ChoiceField(choices=(('steel', 'steel'), ('aluminum', 'aluminum')),widget=RadioSelect, initial = 'steel')
    height = forms.FloatField(label = "H(mm)",widget = widget)
    width = forms.FloatField(label = "B(mm)",widget = widget)
    th = forms.FloatField(label = "th(mm)",widget = widget)
    tw = forms.FloatField(label = "tw(mm)",widget = widget)
    Lb = forms.FloatField(label = "Lb(mm)",widget = widget)
    E = forms.FloatField(label = "E(ヤング係数)", initial = 205000,widget = widget)
    G = forms.FloatField(label = "G(横弾性係数)", initial = 79000,widget = widget)
    F = forms.FloatField(label = "F(基準強度)", initial = 235,widget = widget)
    M1 = forms.FloatField(label = "端部モーメント(大, N.mm)", widget = widget, required = True, initial=0)
    M2 = forms.FloatField(label = "端部モーメント(小, N.mm)", widget = widget, required = True, initial=0)
    doublecurve = forms.BooleanField(label = '曲げモーメントが複曲率', required = False,initial = 0, widget = forms.CheckboxInput(check_test=wrap_boolean_check))   


class RoundPipeForm(forms.Form):
    material = forms.ChoiceField(choices=(('steel', 'steel'), ('aluminum', 'aluminum')),widget=RadioSelect, initial = 'steel')
    D = forms.FloatField(label = "D(mm)",widget = widget)
    t = forms.FloatField(label = "t(mm)",widget = widget)
    Lb = forms.FloatField(label = "Lb(mm)",widget = widget)
    E = forms.FloatField(label = "E(ヤング係数)", initial = 205000,widget = widget)
    G = forms.FloatField(label = "G(横弾性係数)", initial = 79000,widget = widget)
    F = forms.FloatField(label = "F(基準強度)", initial = 235,widget = widget)
    M1 = forms.FloatField(label = "端部モーメント(大, N.mm)", widget = widget, required = True, initial=0)
    M2 = forms.FloatField(label = "端部モーメント(小, N.mm)", widget = widget, required = True, initial=0)
    doublecurve = forms.BooleanField(label = '曲げモーメントが複曲率', required = False,initial = 0, widget = forms.CheckboxInput(check_test=wrap_boolean_check))
        
    def clean(self):
        data = super().clean()
        D = float(data['D'])
        t = float(data['t'])
        if D/2 <= t:
            raise ValidationError("厚みは半径以下にして下さい")
        return data

    
class HsectionForm(forms.Form):
    material = forms.ChoiceField(choices=(('steel', 'steel'), ('aluminum', 'aluminum')),widget=RadioSelect, initial = 'steel')
    H = forms.FloatField(label = "H(mm)",widget = widget)
    B = forms.FloatField(label = "B(mm)",widget = widget)
    tw = forms.FloatField(label = "tw(mm)",widget = widget)
    tf = forms.FloatField(label = "tf(mm)",widget = widget)
    Lb = forms.FloatField(label = "Lb(mm)",widget = widget)
    E = forms.FloatField(label = "E(ヤング係数)", initial = 205000,widget = widget)
    G = forms.FloatField(label = "G(横弾性係数)", initial = 79000,widget = widget)
    F = forms.FloatField(label = "F(基準強度)", initial = 235,widget = widget)
    M1 = forms.FloatField(label = "端部モーメント(大, N.mm)", widget = widget, required = True, initial=0)
    M2 = forms.FloatField(label = "端部モーメント(小, N.mm)", widget = widget, required = True, initial=0)
    doublecurve = forms.BooleanField(label = '曲げモーメントが複曲率', required = False,initial = 0, widget = forms.CheckboxInput(check_test=wrap_boolean_check))
    
    def clean(self):
        data = super().clean()
        H = float(data['H'])
        B = float(data['B'])
        tw = float(data['tw'])
        tf = float(data['tf'])
        if H < tf or B < tw:
            raise ValidationError("厚みは高さ,幅より小さくしてください")
        return data



class LsectionForm(forms.Form):
    material = forms.ChoiceField(choices=(('steel', 'steel'), ('aluminum', 'aluminum')),widget=RadioSelect, initial = 'steel')
    H = forms.FloatField(label = "B(mm)",widget = widget)
    t = forms.FloatField(label = "t(mm)",widget = widget)
    Lb = forms.FloatField(label = "Lb(mm)",widget = widget)
    E = forms.FloatField(label = "E(ヤング係数)", initial = 205000,widget = widget)
    G = forms.FloatField(label = "G(横弾性係数)", initial = 79000,widget = widget)
    F = forms.FloatField(label = "F(基準強度)", initial = 235,widget = widget)
    M1 = forms.FloatField(label = "端部モーメント(大, N.mm)", widget = widget, required = True, initial=0)
    M2 = forms.FloatField(label = "端部モーメント(小, N.mm)", widget = widget, required = True, initial=0)
    doublecurve = forms.BooleanField(label = '曲げモーメントが複曲率', required = False,initial = 0, widget = forms.CheckboxInput(check_test=wrap_boolean_check))
    
    def clean(self):
        data = super().clean()
        B = float(data['H'])
        t = float(data['t'])
        if B < t:
            raise ValidationError("厚みは高さより小さくしてください")
        return data


class CsectionForm(forms.Form):
    material = forms.ChoiceField(choices=(('steel', 'steel'), ('aluminum', 'aluminum')),widget=RadioSelect, initial = 'steel')
    H = forms.FloatField(label = "H(mm)",widget = widget)
    B = forms.FloatField(label = "B(mm)",widget = widget)
    th = forms.FloatField(label = "th(mm)",widget = widget)
    tb = forms.FloatField(label = "tb(mm)",widget = widget)
    Lb = forms.FloatField(label = "Lb(mm)",widget = widget)
    E = forms.FloatField(label = "E(ヤング係数)", initial = 205000,widget = widget)
    G = forms.FloatField(label = "G(横弾性係数)", initial = 79000,widget = widget)
    F = forms.FloatField(label = "F(基準強度)", initial = 235,widget = widget)
    M1 = forms.FloatField(label = "端部モーメント(大, N.mm)", widget = widget, required = True, initial=0)
    M2 = forms.FloatField(label = "端部モーメント(小, N.mm)", widget = widget, required = True, initial=0)
    doublecurve = forms.BooleanField(label = '曲げモーメントが複曲率', required = False,initial = 0, widget = forms.CheckboxInput(check_test=wrap_boolean_check))
    
    def clean(self):
        data = super().clean()
        H = float(data['H'])
        B = float(data['B'])
        th = float(data['th'])
        tb = float(data['tb'])
        if B < th or H < tb:
            raise ValidationError("厚みは高さ,幅より小さくしてください")
        return data



class AnysectionForm(forms.Form):
    material = forms.ChoiceField(choices=(('steel', 'steel'), ('aluminum', 'aluminum')),widget=RadioSelect, initial = 'steel')
    A = forms.FloatField(label = "面積(mm^2)",widget = widget)
    I = forms.FloatField(label = "断面二次モーメント(弱軸, mm^4)",widget = widget)
    Z = forms.FloatField(label = "断面係数(強軸, mm^3)",widget = widget)
    J = forms.FloatField(label = "サンブナンねじり定数(mm^4)",widget = widget)
    Iw= forms.FloatField(label = "曲げねじり定数(mm^4)", initial = 0,widget = widget, required = True)
    Lb = forms.FloatField(label = "Lb(mm)",widget = widget)
    E = forms.FloatField(label = "E(ヤング係数)", initial = 205000,widget = widget)
    G = forms.FloatField(label = "G(横弾性係数)", initial = 79000,widget = widget)
    F = forms.FloatField(label = "F(基準強度)", initial = 235,widget = widget)
    M1 = forms.FloatField(label = "端部モーメント(大, N.mm)", widget = widget, required = True, initial=0)
    M2 = forms.FloatField(label = "端部モーメント(小, N.mm)", widget = widget, required = True, initial=0)
    doublecurve = forms.BooleanField(label = '曲げモーメントが複曲率', required = False,initial = 0, widget = forms.CheckboxInput(check_test=wrap_boolean_check))