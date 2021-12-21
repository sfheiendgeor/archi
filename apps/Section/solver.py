import math
class BacklingAllowance():
    def __init__(self,area, ability,torsionalconstant, lb, E, G, F, Iw=None, M1=None, M2=None, doublecurve=False):
        self.area = area #断面積
        self.ability = ability #断面二次モーメントと断面係数のリスト [断面二次モーメント強, 弱, 断面係数強, 弱]
        self.torsionalconstant = torsionalconstant #サンブナンねじり定数
        self.lb = lb #座屈長
        self.E = E #ヤング係数
        self.G = G #横弾性係数
        self.F = F #基準強度
        if Iw == None:  #曲げねじり定数
            self.Iw = 0
        else:
            self.Iw = Iw
            

        if not M1==None and M2==None and  M1 >= M2:
            self.M1 = M2 #M1のほうが大きい
            self.M2 = M1 #M2が小さいほう
        else:   
            self.M1 = M1
            self.M2 = M2
        
        self.doublecurve = doublecurve #複曲率
        
    def SR(self): #細長比
        I_W = self.ability[1]
        i = (I_W/self.area)**0.5
        sr = self.lb/i
        return sr
    
    def LSR(self): #限界細長比
        lsr = math.pi*(self.E/0.6/self.F)**0.5
        return lsr
    
    def BacklingCompression(self): #圧縮座屈
        v = 1.5+2/3*((self.SR()/self.LSR())**2)
        
        if self.SR() <= self.LSR():
            fc = 1/v*(1-0.4*(self.SR()/self.LSR())**2)*self.F
        else:
            fc= 0.277*((self.LSR()/self.SR())**2)*self.F
        return round(fc,2)
    
    def BacklingBend(self): #曲げ座屈
        I_W = self.ability[1] #弱軸の断面二次モーメント
        Z_W = self.ability[2] #強軸の断面係数
        
        if self.M1 and self.M2: #支点間距離端部に最大曲げモーメントが発生する場合
            if self.doublecurve:
                M_ratio = -(self.M2/self.M1)
            else:
                M_ratio = self.M2/self.M1
            C = 1.75+1.05*M_ratio+0.3*M_ratio**2
            if C>=2.3:
                C = 2.3
            PLB = 0.6+0.3*M_ratio
        else:  #支点間距離内部に最大曲げモーメントが発生する場合
            C = 1.0    
            PLB = 0.3
        ELB = 1.29
        
        My = self.F*Z_W #降伏モーメント
        Me = C*(((math.pi**4)*(self.E**2)*I_W*self.Iw)/(self.lb**4) + (math.pi**2)*self.E*I_W*self.G*self.torsionalconstant/(self.lb)**2)**0.5 #弾性横座屈モーメント
        LambdaB = (My/Me)**0.5
        v = 1.5+2/3*(LambdaB/ELB)**2
        
        if LambdaB < PLB:
            fb = self.F/v
        elif PLB< LambdaB <= ELB:
            fb = (((1-0.4*(LambdaB-PLB)/(ELB-PLB))*self.F)/v)
        elif ELB < LambdaB:
            fb = 1/LambdaB**2*self.F/2.17
        
        return round(fb,2)
    
    def main(self):
        return self.area, self.ability, self.torsionalconstant, self.BacklingCompression(),self.BacklingBend()
    
    
    
    
    

#長方形    
class Rectangle_Ability():
    def __init__(self, height,width,lb, E, G, F, M1=None, M2=None,doublecurve = False):
        if height>width:
            self.L = height
            self.S = width
        else:
            self.L = width
            self.S = height

        self.lb = lb
        self.E = E #ヤング係数
        self.G = G #横弾性係数
        self.F = F #基準強度
        
        self.M1=M1
        self.M2=M2
        self.doublecurve = doublecurve
        
    def Area(self):
        area = self.L*self.S
        return area
    
    def ability(self):
        I_S = self.S*self.L**3/12 #SecondMoment_断面二次モーメント 
        I_W = self.S**3*self.L/12
        Z_S = I_S/(self.L/2)    #ElasticModulus＿断面係数
        Z_W = I_W/(self.S/2)
        return I_S, I_W, Z_S,Z_W
    
    def TorsionalConstant(self):
        Ix = self.L*self.S**3/16*(16/3-3.36*self.S/self.L*(1-1/12*(self.S/self.L)**4))

        return Ix
    
    def main(self):
        area = self.Area()
        ability = list(self.ability())
        torsionalconstant = self.TorsionalConstant()
        ba = BacklingAllowance(area, ability, torsionalconstant, self.lb, self.E, self.G, self.F, self.M1, self.M2, self.doublecurve)
        return ba.main()
    
#丸鋼
class Round_Ability(): 
    
    def __init__(self, D, lb, E, G, F, M1=None, M2=None, doublecurve = False):
        self.D = D
        self.lb = lb
        self.E = E #ヤング係数
        self.G = G #横弾性係数
        self.F = F #基準強度
        self.M1=M1 #区間端部のモーメント
        self.M2=M2 #区間端部のモーメント
        self.doublecurve = doublecurve
        
    def Area(self):
        area = ((self.D/2)**2)*math.pi
        return area
    
    def ability(self):
        #型を崩すと処理が使いまわせなくなるため強軸弱軸の形で書く
        I_S = math.pi*self.D**4/64   #SecondMoment_断面二次モーメント 
        I_W = math.pi*self.D**4/64
        Z_S = math.pi*self.D**3/32   #ElasticModulus_断面係数
        Z_W = math.pi*self.D**3/32
        return I_S, I_W, Z_S, Z_W
    
    
    def TorsionalConstant(self):
        Ix = math.pi*self.D**4/32
        return Ix
    
    def main(self):
        area = self.Area()
        ability = list(self.ability())
        torsionalconstant = self.TorsionalConstant()
        ba = BacklingAllowance(area, ability, torsionalconstant, self.lb, self.E, self.G, self.F, self.M1, self.M2, self.doublecurve)
        return ba.main()    
    
    
    
    
    
    
#角型鋼管  
class SquarePipe_Ability(): 
    def __init__(self, height, width, th, tw, lb, E, G, F, M1=None, M2=None, doublecurve = False):
        if height>width:
            self.L = height
            self.S = width
            self.tl = th
            self.ts = tw
        else:
            self.L = width
            self.S = height
            self.tl=tw
            self.ts=th

        self.lb = lb
        self.E = E #ヤング係数
        self.G = G #横弾性係数
        self.F = F #基準強度
        self.M1=M1 #区間端部のモーメント
        self.M2=M2 #区間端部のモーメント
        self.doublecurve = doublecurve
        
    def Area(self):
        area = self.L*self.S-(self.L-self.tl*2)*(self.S-self.ts*2)
        return area
    
    def ability(self):
        I_S = (self.S*self.L**3-(self.S-self.ts*2)*(self.L-self.tl*2)**3)/12 #SecondMoment_断面二次モーメント 
        I_W = (self.S**3*self.L-(self.S-self.ts*2)**3*(self.L-self.tl*2))/12
        Z_S = I_S/(self.L/2)    #ElasticModulus_断面係数
        Z_W = I_W/(self.S/2)
        return I_S, I_W, Z_S, Z_W
    
    
    def TorsionalConstant(self):
        Ix = (2*self.ts*self.tl*(self.L-self.tl)**2*(self.S-self.ts)**2)/(self.S*self.ts+self.L*self.tl-self.ts**2-self.tl**2)
        return Ix
    
    def main(self):
        area = self.Area()
        ability = list(self.ability())
        torsionalconstant = self.TorsionalConstant()
        ba = BacklingAllowance(area, ability, torsionalconstant, self.lb, self.E, self.G, self.F, self.M1, self.M2, self.doublecurve)
        return ba.main()
    
    
    
    
    
    
    
#丸パイプ
class RoundPipe_Ability(): 
    def __init__(self, D, t, lb, E, G, F, M1=None, M2=None, doublecurve = False):
        self.D = D
        self.t = t
        self.lb = lb
        self.E = E #ヤング係数
        self.G = G #横弾性係数
        self.F = F #基準強度
        self.M1=M1 #区間端部のモーメント
        self.M2=M2 #区間端部のモーメント
        self.doublecurve = doublecurve
        
    def Area(self):
        area = ((self.D/2)**2-((self.D-2*self.t)/2)**2)*math.pi
        return area
    
    def ability(self):
        #型を崩すと処理が使いまわせなくなるため強軸弱軸の形で書く
        #現状強軸の値を使っていないので消してもよい
        D = self.D
        d = self.D-2*self.t

        I_S = math.pi*(D**4-d**4)/64   #SecondMoment_断面二次モーメント 
        I_W = math.pi*(D**4-d**4)/64
        Z_S = math.pi*(D**4-d**4)/(32*D)   #ElasticModulus_断面係数
        Z_W = math.pi*(D**4-d**4)/(32*D)
        return I_S, I_W, Z_S, Z_W
    
    
    def TorsionalConstant(self):
        Ix = math.pi*(self.D**4-(self.D-2*self.t)**4)/32
        return Ix
    
    def main(self):
        area = self.Area()
        ability = list(self.ability())
        torsionalconstant = self.TorsionalConstant()
        ba = BacklingAllowance(area, ability, torsionalconstant, self.lb, self.E, self.G, self.F, self.M1, self.M2, self.doublecurve)
        return ba.main()
    





#H鋼
class H_Ability(): 
    def __init__(self, H, B, tw, tf, lb, E, G, F, M1=None, M2=None, doublecurve = False):
        self.H = H
        self.B = B
        self.tw = tw
        self.tf = tf
        self.lb = lb
        self.E = E #ヤング係数
        self.G = G #横弾性係数
        self.F = F #基準強度
        self.M1=M1 #区間端部のモーメント
        self.M2=M2 #区間端部のモーメント
        self.doublecurve = doublecurve
        
    def Area(self):
        area = (self.B*self.tf)*2+(self.H-self.tf*2)*self.tw
        return area
    
    def ability(self):
        #型を崩すと処理が使いまわせなくなるため強軸弱軸の形で書く
        #現状強軸の値を使っていないので消してもよい
        H = self.H
        B = self.B
        h = self.H-2*self.tf #フランジの厚みを除いた高さ
        b = self.B-self.tw  #ウェブの厚みを除いた幅

        I_S = (B*H**3-b*h**3)/12 #SecondMoment_断面二次モーメント 
        I_W = (self.tf*2*B**3+h*self.tw**3)/12
        Z_S = I_S/(H/2)   #ElasticModulus_断面係数
        Z_W = I_W/(B/2)
        return I_S, I_W, Z_S, Z_W
    
    def TorsionalConstant(self):
        Ix = 1/3*(2*self.B*self.tf**3+(self.H-2*self.tf)*self.tw**3)
        return Ix
    
    def BendConstant(self):#曲げねじり定数を求める
        Iw = (self.H-self.tf)**2/12*self.tf*self.B**3*self.tw*self.B**3/(self.tf*self.B**3+self.tf*self.B**3)
        return Iw
        
    def main(self):
        area = self.Area()
        ability = list(self.ability())
        torsionalconstant = self.TorsionalConstant()
        bendconstant = self.BendConstant()
        ba = BacklingAllowance(area, ability, torsionalconstant, self.lb, self.E, self.G, self.F,bendconstant, self.M1, self.M2, self.doublecurve)
        return ba.main()
    
    
    
#Lアングル
class L_Ability(): 
    def __init__(self, H, t, lb, E, G, F, M1=None, M2=None,doublecurve = False):
        self.H = H
        self.t = t
        self.lb = lb
        self.E = E #ヤング係数
        self.G = G #横弾性係数
        self.F = F #基準強度
        self.M1=M1 #区間端部のモーメント
        self.M2=M2 #区間端部のモーメント
        self.doublecurve = doublecurve
        
    def Area(self):
        h = self.H
        t = self.t
        area = h*t+(h-t)*t
        return area
    
    def ability(self):
        #型を崩すと処理が使いまわせなくなるため強軸弱軸の形で書く
        H = self.H
        t = self.t
        area = self.Area()
        g = (t**2*H/2+(H-t)*t*((H-t)/2+t))/area
        #断面二次モーメント
        #ひし形の断面二次モーメントの引き算＞＞＞軸の移動で求める
        #大きいひし形のそれぞれの断面二次モーメント
        Ilerge = H**4/12
        Ismall = (H-t)**4/12
        #弱軸方向の引き算
        I_W_temp = Ilerge-(Ismall+(t**2/2)*(H-t)**2)#大きいほうの中心を軸とした断面二次モーメント
        g_diff = H/(2**0.5)-g*(2**0.5) #重心位置から大きいほうのひし形の重心までの距離
        I_W = I_W_temp-g_diff**2*(H**2-(H-t)**2)

        #強軸の計算
        I_S = Ilerge-Ismall
        
        #辺に平行な軸の計算
        I_M = 1/3 * (t*(H-g)**3 + H*g**3 - (H-t) * (g - t)**3 )

        Z_S = I_S/(H/2**0.5)#ElasticModulus_断面係数
        Z_W = I_W/(g_diff+3/2**0.5)
        Z_M = I_M/(H-g)
        return I_M, I_W, Z_M, Z_W
    
    def TorsionalConstant(self):
        H = self.H
        t = self.t
        J = 2/3*H*t**3
        return J
    
    def BendConstant(self):#曲げねじり定数を求める
        H = self.H
        t = self.t
        Iw = (H*t)**3/18
        return Iw
        
    def main(self):
        area = self.Area()
        ability = list(self.ability())
        torsionalconstant = self.TorsionalConstant()
        bendconstant = self.BendConstant()
        ba = BacklingAllowance(area, ability, torsionalconstant, self.lb, self.E, self.G, self.F,bendconstant, self.M1, self.M2, self.doublecurve)
        return ba.main()
    
    
#みぞ形鋼
class C_Ability(): 
    def __init__(self, H, B, th, tb, lb, E, G, F, M1=None, M2=None,doublecurve = False):
        self.H = H
        self.B = B
        self.th = th
        self.tb = tb
        self.lb = lb
        self.E = E #ヤング係数
        self.G = G #横弾性係数
        self.F = F #基準強度
        self.M1=M1 #区間端部のモーメント
        self.M2=M2 #区間端部のモーメント
        self.doublecurve = doublecurve
        
    def Area(self):
        H = self.H
        B = self.B
        th = self.th
        tb = self.tb
        area = (H-2*tb)*th+2*B*tb
        return area
    
    def ability(self):
        #型を崩すと処理が使いまわせなくなるため強軸弱軸の形で書く
        #現状強軸の値を使っていないので消してもよい
        H = self.H
        B = self.B
        th = self.th
        tb = self.tb
        area = self.Area()
        #弱軸の重心を求める
        
        g_w = (H*th**2/2 - tb*th**2 + B**2*tb)/area
        I_W = ((H-2*tb)*th**3/12 + (g_w-th/2)**2 * ((H-2*tb)*th))  +  2*(tb*B**3/12 + (B/2-g_w)**2 * (B*th))
        I_S = (th*(H-2*tb)**3/12) + 2*(B*tb**3/12 + (H/2-tb/2)**2 * B*tb)
        Z_W = I_W/(B-g_w)
        Z_S = I_S/(H/2)
        return I_S, I_W, Z_S, Z_W
    
    def TorsionalConstant(self):
        H = self.H
        B = self.B
        th = self.th
        tb = self.tb

        J = (2*B*tb**3 + H*th**3)/3
        return J
    
    def BendConstant(self):#曲げねじり定数を求める
        H = self.H
        B = self.B
        th = self.th
        tb = self.tb
        
        Iw = (tb*B**3*H**2)/12 * (3*tb*B+2)/(6*tb*B+th*H)
        return Iw
        
    def main(self):
        area = self.Area()
        ability = list(self.ability())
        torsionalconstant = self.TorsionalConstant()
        bendconstant = self.BendConstant()
        ba = BacklingAllowance(area, ability, torsionalconstant, self.lb, self.E, self.G, self.F,bendconstant, self.M1, self.M2, self.doublecurve)
        return ba.main()
    
    
