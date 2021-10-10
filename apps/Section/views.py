from django.shortcuts import render
from django.views.generic import TemplateView
from io import TextIOWrapper, StringIO
from .forms import SelectionForm, RectangleForm, RoundForm, SquarePipeForm, RoundPipeForm, HsectionForm, LsectionForm, CsectionForm, AnysectionForm
from .solver import  Rectangle_Ability, Round_Ability, SquarePipe_Ability, RoundPipe_Ability, H_Ability,L_Ability,C_Ability, BacklingAllowance
import math
import csv
from decimal import Decimal, ROUND_HALF_DOWN


from .models import  FB_data, R_data, I_data, H_data, LH_data, CT_data, C_data, RC_data, O_data, P_data, L_data



def my_customized_server_error(request, template_name='500.html'):
    import sys
    from django.views import debug
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)
# Create your views here.


def deci(x):
    return Decimal(x).quantize(Decimal('0.01'), rounding = ROUND_HALF_DOWN)

class IndexView(TemplateView):
    template_name = 'Section/index.html'
    fields=()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'SelectionForm' : SelectionForm(),
            'RectangleForm': RectangleForm(),
            'RoundForm': RoundForm(),
            'SquarePipeForm': SquarePipeForm(),
            'RoundPipeForm' : RoundPipeForm(),
            'HsectionForm' : HsectionForm(),
            'LsectionForm' : LsectionForm(),
            'CsectionForm' : CsectionForm(),
            'AnysectionForm': AnysectionForm(),
        })
        return context
    

    
    def post(self, request):
        context = self.get_context_data()
        lb = float(request.POST['Lb'])
        E = float(request.POST['E'])
        G = float(request.POST['G'])
        F = float(request.POST['F'])
        M1 = float(request.POST['M1'])
        M2 = float(request.POST['M2'])

        if "doublecurve" in request.POST:
            doublecurve = True
        else:
            doublecurve = False
        
        if "button_rectangle" in request.POST:
            context['RectangleForm'] = RectangleForm(request.POST)
            height = float(request.POST['height'])
            width = float(request.POST['width'])
            
            sectionability = Rectangle_Ability(height, width, lb, E, G, F, M1,M2,doublecurve)
            area, ability, torsionalconstant, compression, bend = sectionability.main()
            
        if "button_round" in request.POST:
            context['RoundForm'] = RoundForm(request.POST)
            D = float(request.POST['D'])
            Iw = 0
            sectionability = Round_Ability(D,lb, E, G, F,M1,M2,doublecurve)
            area, ability, torsionalconstant, compression, bend = sectionability.main()
            
        if "button_squarepipe" in request.POST:
            context['SquarePipeForm'] = SquarePipeForm(request.POST)
            height = float(request.POST['height'])
            width = float(request.POST['width'])
            th = float(request.POST['th'])
            tw = float(request.POST['tw'])
            Iw = 0
            sectionability = SquarePipe_Ability(height,width,th,tw,lb, E, G, F,M1,M2,doublecurve)
            area, ability, torsionalconstant, compression, bend = sectionability.main()
            
        if "button_roundpipe" in request.POST:
            context['RoundPipeForm'] = RoundPipeForm(request.POST)
            D = float(request.POST['D'])
            t = float(request.POST['t'])
            Iw = 0
            if D/2 > t:
                sectionability = RoundPipe_Ability(D,t,lb, E, G, F,M1,M2,doublecurve)
                area, ability, torsionalconstant, compression, bend = sectionability.main()
            else:
                area, ability , torsionalconstant, compression, bend = 0,[0,0,0,0],0,0,0
                
        if "button_hsection" in request.POST:
            context['HsectionForm'] = HsectionForm(request.POST)
            H = float(request.POST['H'])
            B = float(request.POST['B'])
            tw = float(request.POST['tw'])
            tf = float(request.POST['tf'])
            sectionability = H_Ability(H,B,tw,tf,lb, E, G, F,M1,M2,doublecurve)
            area, ability, torsionalconstant, compression, bend = sectionability.main()
            
        if "button_Lsection" in request.POST:
            context['LsectionForm'] = LsectionForm(request.POST)
            H = float(request.POST['H'])
            t = float(request.POST['t'])
            sectionability = L_Ability(H, t, lb, E, G, F,M1,M2,doublecurve)
            area, ability, torsionalconstant, compression, bend = sectionability.main()
            
        if "button_Csection" in request.POST:
            context['CsectionForm'] = CsectionForm(request.POST)
            H = float(request.POST['H'])
            B = float(request.POST['B'])
            th = float(request.POST['th'])
            tb = float(request.POST['tb'])
            sectionability = C_Ability(H, B, th,tb, lb, E, G, F,M1,M2,doublecurve)
            area, ability, torsionalconstant, compression, bend = sectionability.main()
            
        if "button_anysection" in request.POST:
            context['AnysectionForm'] = AnysectionForm(request.POST) 
            A = float(request.POST['A'])
            I = float(request.POST['I'])
            Z = float(request.POST['Z'])
            J = float(request.POST['J'])
            Iw= float(request.POST['Iw'])
            ability = [0,I,Z,0]
            BA = BacklingAllowance(A,ability, J,lb,E,G,F,Iw,M1,M2,doublecurve)
            area, ability, torsionalconstant, compression, bend = BA.main()
            
        context['area'] = deci(area)
        context['I_S'] = format(deci(ability[0]), '.2E')
        context['I_W'] = format(deci(ability[1]), '.2E')
        context['Z_S'] = format(deci(ability[2]), '.2E')
        context['Z_W'] = format(deci(ability[3]), '.2E')
        context['torsionalconstant'] = format(deci(torsionalconstant), '.2E')
        
        context['l_bend'] = deci(bend)
        context['s_bend'] = deci(bend*1.5)
        context['l_compression'] = deci(compression)
        context['s_compression'] = deci(compression*1.5)
        context['l_tension'] = deci(F/1.5)
        context['s_tension'] = F
        context['l_shear'] = deci(F/(math.sqrt(3)*1.5))
        context['s_shear'] = deci(F/math.sqrt(3))

        return render(request, 'Section/index.html', context)

class list(TemplateView):
    template_name = 'Section/list.html'
    fields=()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'SelectionForm' : SelectionForm(),
            'FBdata': FB_data.objects.order_by('H'),
            'Rdata' : R_data.objects.all(),
            'Idata' : I_data.objects.order_by('H','B'),
            'Hdata' : H_data.objects.order_by('H','B'),
            'LHdata': LH_data.objects.order_by('H','B'),
            'CTdata': CT_data.objects.order_by('H','B'),
            'Cdata' : C_data.objects.order_by('H','B'),
            'RCdata': RC_data.objects.order_by('H','B'),
            'Odata' : O_data.objects.order_by('H'),
            'Pdata' : P_data.objects.order_by('H','B'),
            'Ldata' : L_data.objects.order_by('H','B'),
        })
        return context
    
    def post(self,request):
        context = self.get_context_data()
        min = 0  
        if 'button_minfilter' in request.POST:
            minIx = float(request.POST['minIx'])
            minZx = float(request.POST['minZx'])
        context.update({
        'SelectionForm' : SelectionForm(request.POST),
        'Idata' : I_data.objects.filter(Ix__gte = minIx).filter(Zx__gte = minZx),
        'Hdata' : H_data.objects.filter(Ix__gte = minIx).filter(Zx__gte = minZx),
        'LHdata': LH_data.objects.filter(Ix__gte = minIx).filter(Zx__gte = minZx),
        'CTdata': CT_data.objects.filter(Ix__gte = minIx).filter(Zx__gte = minZx),
        'Cdata' : C_data.objects.filter(Ix__gte = minIx).filter(Zx__gte = minZx),
        'RCdata': RC_data.objects.filter(Ix__gte = minIx).filter(Zx__gte = minZx),
        'Odata' : O_data.objects.filter(Ix__gte = minIx).filter(Zx__gte = minZx),
        'Pdata' : P_data.objects.filter(Ix__gte = minIx).filter(Zx__gte = minZx),
        'Ldata' : L_data.objects.filter(Ix__gte = minIx).filter(Zx__gte = minZx),
        })
        return render(request, "Section/list.html" , context)

            
    def view(self, request):
        context = self.get_context_data()
        return render(request, 'Section/list.html',context)
    

def upload(request):
    if 'csv' in request.FILES:
        filename = request.FILES['csv'].name
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        if  filename == 'FB.csv' :
            for row in csv_file:
                section = FB_data.objects.create()
                section.name = row[0]
                section.H = row[1]
                section.B = row[2]
                section.A = row[3]
                section.m = row[4]
                section.save()
                
        if filename == 'R.csv':
            for row in csv_file:
                section = R_data.objects.create()
                section.name = row[0]
                section.d = row[1]
                section.A = row[2]
                section.m = row[3]             
                section.save ()
                
        if filename == 'I.csv':
            for row in csv_file:
                section = I_data.objects.create()
                section.name = row[0]
                section.H = row[1] 
                section.B = row[2]
                section.t1 = row[3]
                section.t2 = row[4]
                section.r1 = row[5]
                section.r2 = row[6]
                section.A = row[7]
                section.m = row[8]
                section.Ix = row[9]
                section.Iy = row[10]
                section.rx = row[11]
                section.ry = row[12]
                section.Zx = row[13]
                section.Zy = row[14]
                
                section.save()
            
        if filename == 'H.csv':
            for row in csv_file:
                section = H_data.objects.create()
                section.name = row[0]
                section.H = row[1]
                section.B = row[1]
                section.t1 = row[3]
                section.t2 = row[4]
                section.r1 = row[5]
                section.A = row[6]
                section.m = row[7]
                section.Ix = row[8]
                section.Iy = row[9]
                section.rx = row[10]
                section.ry = row[11]
                section.Zx = row[12]
                section.Zy = row[13]
                
                section.save()
                
        if filename == 'LH.csv':
            for row in csv_file:
                section = LH_data.objects.create()
                section.name = row[0]
                section.H = row[1]
                section.B = row[2]
                section.t1 = row[3]
                section.t2 = row[4]
                section.A = row[5]
                section.m = row[6]
                section.Ix = row[7]
                section.Iy = row[8]
                section.rx = row[9]
                section.ry = row[10]
                section.Zx = row[11]
                section.Zy = row[12]
                
                section.save()
                
        if filename == 'CT.csv':
            for row in csv_file:
                section = CT_data.objects.create()
                section.name = row[0]
                section.H = row[1]
                section.B = row[2]
                section.t1 = row[3]
                section.t2 = row[4]
                section.r1 = row[5]
                section.A = row[6]
                section.m = row[7]
                section.Ix = row[8]
                section.Iy = row[9]
                section.rx = row[10]
                section.ry = row[11]
                section.Zx = row[12]
                section.Zy = row[13]
                
                section.save()
            
        if filename == 'C.csv':
            for row in csv_file:
                section= C_data.objects.create()
                section.name = row[0]
                section.H = row[1]
                section.B = row[2]
                section.t1 = row[3]
                section.t2 = row[4]
                section.r1 = row[5]
                section.r2 = row[6]
                section.A = row[7]
                section.m = row[8]
                section.Ix = row[9]
                section.Iy = row[10]
                section.rx = row[11]
                section.ry = row[12]
                section.Zx = row[13]
                section.Zy = row[14]
                
                section.save()
            
        if filename == 'RC.csv':
            for row in csv_file:
                section = RC_data.objects.create()
                section.name = row[0]
                section.H = row[1]
                section.B = row[2]
                section.C = row[3]
                section.t1 = row[4]
                section.A = row[5]
                section.m = row[6]
                section.Ix = row[7]
                section.Iy = row[8]
                section.rx = row[9]
                section.ry = row[10]
                section.Zx = row[11]
                section.Zy = row[12]
                
                section.save()
                
        if filename == 'O.csv':
            for row in csv_file:
                section = O_data.objects.create()
                section.name = row[0]
                section.H = row[1]
                section.t1 = row[2]
                section.A = row[3]
                section.m = row[4]
                section.Ix = row[5]
                section.Iy = row[6]
                section.rx = row[7]
                section.ry = row[8]
                section.Zx = row[9]
                section.Zy = row[10]
                section.save()
                
        if filename == 'P.csv':
            for row in csv_file:
                section = P_data.objects.create()
                section.name = row[0]
                section.H = row[1]
                section.B = row[2]
                section.t1 = row[3]
                section.A = row[4]
                section.m = row[5]
                section.Ix = row[6]
                section.Iy = row[7]
                section.rx = row[8]
                section.ry = row[9]
                section.Zx = row[10]
                section.Zy = row[11]
                section.save()
                
        if filename == 'L.csv':
            for row in csv_file:
                section = L_data.objects.create()
                section.name = row[0]
                section.H = row[1]
                section.B = row[2]
                section.t1 = row[3]
                section.t2 = row[4]
                section.r1 = row[5]
                section.A = row[6]
                section.m = row[7]
                section.Ix = row[8]
                section.Iy = row[9]
                section.rx = row[10]
                section.ry = row[11]
                section.Zx = row[12]
                section.Zy = row[13]
                section.save()

        return render(request, 'Section/upload.html')

    else:
        return render(request, 'Section/upload.html')
    

