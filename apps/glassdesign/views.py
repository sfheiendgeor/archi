from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import Equation1Form,Equation2Form,Equation3Form,Equation4Form,Equation5Form,Equation6Form,Equation7Form
from .mixin import  GlassDesign


class GlassdesignView(TemplateView):
    template_name = 'glassdesign/index.html'
    fields = ()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'Equation1Form': Equation1Form(),
            'Equation2Form': Equation2Form(),
            'Equation3Form': Equation3Form(),
            'Equation4Form' :Equation4Form(),
            'Equation5Form' :Equation5Form(),
            'Equation6Form' :Equation6Form(),
            'Equation7Form' :Equation7Form(),
        })
        return context
    
    
    def post(self,request):
        context = self.get_context_data()
        glasses = [request.POST['t1'],request.POST['t2'],request.POST['t3'],request.POST['t4']]
        glasses = [float(i) for i in glasses if i!= '']
            
        if 'button_Equation1' in request.POST:
            context['Equation1Form'] = Equation1Form(request.POST)
            a = float(request.POST['a'])
            b = float(request.POST['b'])
            w = float(request.POST['w'])/pow(10,6)
            GD = GlassDesign(a,b,glasses,w)
            sigma, delta =  GD.Equation1()
            
        if 'button_Equation2' in request.POST:
            context['Equation2Form'] = Equation2Form(request.POST)
            a = float(request.POST['a'])
            b = float(request.POST['b'])
            a1 = float(request.POST['a1'])
            b1 = float(request.POST['b1'])
            w = float(request.POST['w'])/pow(10,6)
            
            GD = GlassDesign(a,b,glasses,w,a1,b1)
            sigma, delta =  GD.Equation2()
            
        if 'button_Equation3' in request.POST:
            context['Equation3Form'] = Equation3Form(request.POST)
            a = float(request.POST['a'])
            b = float(request.POST['b'])
            w = float(request.POST['w'])/pow(10,6)
            
            GD = GlassDesign(a,b,glasses,w)
            sigma, delta =  GD.Equation3()
            
        if 'button_Equation4' in request.POST:
            context['Equation4Form'] = Equation4Form(request.POST)
            a = float(request.POST['a'])
            b = float(request.POST['b'])
            w = float(request.POST['w'])/pow(10,6)
            
            GD = GlassDesign(a,b,glasses,w)
            sigma, delta =  GD.Equation4()
            
        if 'button_Equation5' in request.POST:
            context['Equation5Form'] = Equation5Form(request.POST)
            a1 = float(request.POST['a1'])
            a2 = float(request.POST['a2'])
            b = float(request.POST['b'])
            P = float(request.POST['P'])
            
            GD = GlassDesign(a1,a2,glasses,P)
            sigma, delta =  GD.Equation5(a1,a2,b,P)
            
        if 'button_Equation6' in request.POST:
            context['Equation6Form'] = Equation6Form(request.POST)
            a = float(request.POST['a'])
            w = float(request.POST['w'])/pow(10,6)
            
            GD = GlassDesign(a,a,glasses,w)
            sigma, delta =  GD.Equation6()
            
        if 'button_Equation7' in request.POST:
            context['Equation7Form'] = Equation7Form(request.POST)
            a = float(request.POST['a'])
            w = float(request.POST['w'])/pow(10,6)
            
            GD = GlassDesign(a, a, glasses,w)
            sigma, delta =  GD.Equation7()
            
        context['sigma'] = sigma
        context['delta'] = delta
        
        return render(request, 'glassdesign/index.html' , context)