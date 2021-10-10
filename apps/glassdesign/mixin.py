import bisect
from decimal import Decimal, ROUND_HALF_DOWN

class GlassDesign():
    BETA_ALPHA_1 = [[0.272,0.362,0.476,0.603,0.711,0.740,0.748],
                [0.047,0.065,0.088,0.116,0.139,0.146,0.148]]

    BETA_ALPHA_2 =[[[2.988,1.720,1.322,1.075,0.888,0.732],
                    [0.132,0.128,0.118,0.106,0.092,0.077],
                    [1.720,1.206,1.024,0.866,0.729,0.603],
                    [0.128,0.124,0.115,0.103,0.090,0.075],
                    [1.322,1.024,0.801,0.694,0.592,0.492],
                    [0.118,0.115,0.107,0.097,0.084,0.070],
                    [1.075,0.866,0.694,0.563,0.483,0.403],
                    [0.106,0.103,0.097,0.087,0.076,0.064],
                    [0.888,0.729,0.592,0.483,0.397,0.331],
                    [0.092,0.090,0.084,0.076,0.066,0.056],
                    [0.732,0.603,0.492,0.403,0.331,0.272],
                    [0.077,0.075,0.070,0.064,0.056,0.047]]
                    ,[[3.158,1.501,1.087,0.824],
                    [0.169,0.156,0.133,0.107],
                    [1.683,1.200,0.925,0.713],
                    [0.164,0.153,0.130,0.105],
                    [1.286,0.968,0.778,0.610],
                    [0.153,0.143,0.122,0.099],
                    [1.042,0.794,0.654,0.517],
                    [0.138,0.129,0.111,0.090],
                    [0.860,0.656,0.546,0.435],
                    [0.120,0.113,0.097,0.079],
                    [0.708,0.540,0.451,0.360],
                    [0.101,0.095,0.082,0.066]]
                    ,[[3.226,1.587,1.184,0.942,0.767,0.628],
                    [0.188,0.176,0.155,0.133,0.112,0.093],
                    [1.636,1.288,1.023,0.831,0.683,0.561],
                    [0.183,0.172,0.152,0.130,0.110,0.091],
                    [1.230,1.051,0.872,0.721,0.598,0.492],
                    [0.171,0.161,0.143,0.123,0.104,0.086],
                    [1.010,0.870,0.739,0.620,0.517,0.426],
                    [0.154,0.146,0.130,0.112,0.095,0.079],
                    [0.831,0.723,0.622,0.525,0.439,0.363],
                    [0.134,0.128,0.114,0.098,0.083,0.069],
                    [0.684,0.596,0.515,0.436,0.365,0.302],
                    [0.113,0.107,0.096,0.083,0.070,0.058]]]

    BETA_ALPHA_3 = [[0.350,0.511,0.661,0.715,0.758,0.783,0.791,0.791],
                    [0.076,0.108,0.139,0.150,0.158,0.164,0.165,0.165]]

    BETA_ALPHA_4 =[[0.765,0.782,0.791,0.791],
                    [0.160,0.163,0.165,0.165]]
    
    E = 71600
    
    def __init__(self, a, b, t, w, *args):#tは複数の時リストで受ければよさそう
        self.a = a
        self.b = b
        self.BbyA = b/a
        self.t = t #単板でもリストで受ける
        self.w = w
        if args:
            self.a1 = args[0]
            self.b1 = args[1]
        
    def deci(self,x):
        return Decimal(x).quantize(Decimal('0.01'), rounding = ROUND_HALF_DOWN)
    
    def EqualThickness(self):
        t = self.t
        
        if len(t) == 1:
            equalthikness = t[0]
        else:
            totalthikness = sum(t)
            equalthikness = 0.866*totalthikness - 0.268    

        return equalthikness
        
    def Equation1(self):
        a = self.a
        b = self.b
        t = self.EqualThickness()
        w = self.w
        BbyA = self.BbyA
        BbyA_list = [1.0, 1.2, 1.5, 2.0, 3.0, 4.0, 5.0]
        E = GlassDesign.E
        
        if BbyA in BbyA_list:
            index = BbyA_list.index(BbyA)
        else: 
            index = bisect.bisect(BbyA_list, BbyA)
            if index>6:
                index = 6
        
        coeffA = GlassDesign.BETA_ALPHA_1[1][index]
        coeffB = GlassDesign.BETA_ALPHA_1[0][index]
        
        sigma = coeffB * w * pow(a,2) / pow(t,2)    
        delta = coeffA * w * pow(a,4) / (E * pow(t,3))    
        
        return self.deci(sigma), self.deci(delta)
    
    def Equation2(self):
        a = self.a
        b = self.b
        a1 = self.a1
        b1 = self.b1
        t = self.EqualThickness()
        w = self.w
        E = GlassDesign.E
        BbyA = self.BbyA
        b1byA = b1/a
        a1byA = a1/a
        BbyA_list = [1.0,1.4,2.0]
        a1byA_list = [0.01, 0.2, 0.4, 0.6, 0.8, 0.1]
        b1byA_list = [[0.01, 0.2, 0.4, 0.6, 0.8, 1.0],
                    [0.01, 0.4, 0.8, 1.2],
                    [0.01, 0.4, 0.8, 1.2, 1.6, 2.0]]

        #BbyAが[1,1.4,2]のどのインデックスかを二分探索法で判定
        if BbyA in [1,1.4,2]:
            index = BbyA_list.index(BbyA)
        else:
            index = bisect.bisect(BbyA_list, BbyA)
            if index > 2:
                index = 2

        #BbyAにネストされたb1ByAの列からインデックスを判定    
        if b1byA in b1byA_list[index]:
            index_b1byA = b1byA_list[index].index(b1byA)
        else:
            index_b1byA = bisect.bisect(b1byA_list[index], b1byA)
            if index_b1byA > len(b1byA_list[index])-1:
                index_b1byA = len(b1byA_list[index])-1


        #列の特定が済んだのであとは行を判定(a1byAの2倍or2倍+1がそれぞれベータ、アルファの行番号になる)
        if a1byA in a1byA_list:
            index_a1byA = a1byA_list.index(a1byA)
        else:
            index_a1byA = bisect.bisect(a1byA_list, a1byA)

        coeffA = GlassDesign.BETA_ALPHA_2[index][index_a1byA*2 + 1][index_b1byA]
        coeffB = GlassDesign.BETA_ALPHA_2[index][index_a1byA*2][index_b1byA]

        sigma = coeffB * w * a1 * b1 / pow(t,2)
        delta = coeffA * w * a1 * b1 * pow(a,2) / (E * pow(t,3))
        
        return self.deci(sigma), self.deci(delta)
    
    
    def Equation3(self):
        a = self.a
        b = self.b
        t = self.EqualThickness()
        w = self.w
        E = GlassDesign.E
        BbyA = self.BbyA
        BbyA_list = [0.5,0.7,1,1.2,1.5,2.0,3.0]
        
        if BbyA in BbyA_list:
            index_BbyA = BbyA_list.index(BbyA)
        else:
            index_BbyA = bisect.bisect(BbyA_list, BbyA)
        
        coeffA = GlassDesign.BETA_ALPHA_3[1][index_BbyA]
        coeffB = GlassDesign.BETA_ALPHA_3[0][index_BbyA]
        
        sigma = coeffB * w * pow(a,2) / pow(t,2)
        delta = coeffA * w * pow(a,4) / (E * pow(t,3))
        
        return self.deci(sigma), self.deci(delta)
    
    def Equation4(self):
        a = self.a
        b = self.b
        t = self.EqualThickness()
        w = self.w
        E = GlassDesign.E
        BbyA = self.BbyA
        BbyA_list = [0.5, 1.0, 2.0]
        
        if BbyA in BbyA_list:
            index_BbyA = BbyA_list.index(BbyA)
        else:
            index_BbyA = bisect.bisect(BbyA_list, BbyA)
        
        coeffA = GlassDesign.BETA_ALPHA_4[1][index_BbyA]
        coeffB = GlassDesign.BETA_ALPHA_4[0][index_BbyA]
        
        sigma = coeffB * w * pow(a,2) / pow(t,2)
        delta = coeffA * w * pow(a,4) / (E * pow(t,3))
        
        return self.deci(sigma), self.deci(delta)
    
    def Equation5(self, a1, a2, b, P):
        E = GlassDesign.E
        t = self.EqualThickness()
        sigma = 6 * a1 * a2 * P / ((a1 + a2) * b * pow(t,2))
        delta = 4 * P * a2 / (9 * E * b * pow(t,3) * (a1 + a2)) * pow(3 * pow(pow(a1 + a2,2)-pow(a2,2),3),0.5)
        return self.deci(sigma), self.deci(delta)
    
    def Equation6(self):
        a = self.a
        t = self.EqualThickness()
        w = self.w
        E = GlassDesign.E
        
        sigma = 0.916 * w * pow(a,2) / pow(t,2)
        delta = 0.294 * w * pow(a,4) / (E * pow(t,3))
        
        return self.deci(sigma), self.deci(delta)
    
    def Equation7(self):
        a = self.a
        t = self.EqualThickness()
        w = self.w
        E = GlassDesign.E
        
        sigma  = 1.212* w * pow(a,2) / pow(t,2)
        delta  = 0.756 * w * pow(a,4) / (E * pow(t,3))
        
        return self.deci(sigma), self.deci(delta)