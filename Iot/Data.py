class Data:
    def __init__(self, dia, mes, ano):
        self._dia=dia
        self._ano = ano
        self._mes=mes
        
    def print_data(self):
        if (self.get_dia()<10 and self.get_mes()<10):
            print("0{}".format(self.get_dia()),"0{}".format(self.get_mes()),self.get_ano(),sep="/")
        elif(self.get_dia()>=10 and self.get_mes()<10):
            print(self.get_dia(),"0{}".format(self.get_mes()),self.get_ano(),sep="/")
        elif (self.get_dia()<10 and self.get_mes()>=10):
            print("0{}".format(self.get_dia()),self.get_mes(),self.get_ano(),sep="/")
        else:
            print(self.get_dia(),self.get_mes(),self.get_ano(),sep="/")                 

    def fix_mes(self,other, mod):
        self._mes+=mod
        if(self._mes < other.get_mes()):
            mes_o=abs(self._mes-other.get_mes())
            self._mes=12-mes_o
            self._ano-= other.get_ano()+1
        else:
            self._mes-=other.get_mes()
            self._ano-= other.get_ano()

    def fix_dia(self,other):
        if(self._dia < other.get_dia()):
            self.fix_mes(other,-1)
            dia_o=abs(self._dia-other.get_dia())
            if(self._mes==2 or self._mes==4 or self._mes==6 or self._mes==8 or self._mes==9 or self._mes==11 or self._mes==1 ):
                self._dia=31-dia_o
            elif(self._mes==3):
                self._dia=28-dia_o
            else:
                self._dia=30-dia_o
        else:
            self._dia-=other.get_dia() 
            self.fix_mes(other,0)  
    
    def __sub__(self,other):
        if(self.check_op(other) == True):
            self.fix_dia(other)
            if(self._ano > 1):
                print ("A diferença é de {} anos".format(self._ano),end=", ")
            else: 
                print ("A diferença é de {} ano".format(self._ano),end=", ")   
            if(self._mes > 1):
                print ("{} meses".format(self._mes),end=" e ")
            else: 
                print ("{} mes".format(self._mes),end=" e ")
            if(self._dia > 1):
                print ("{} dias".format(self._dia),end="\n")
            else: 
                print ("{} dia".format(self._dia),end="\n") 
            return self                  
        else:
            print("****Operação inválida*****") 
            exit  
    
    def get_dia(self):
        return self._dia

    def get_ano(self):
        return self._ano
    
    def get_mes(self):
        return self._mes

    def check_op(self,other):
        if(self._ano < other.get_ano()):
            return False
        elif(self._ano == other.get_ano() and self._mes < other.get_mes()):
            return False
        elif (self._ano == other.get_ano() and self._mes == other.get_mes() and self._dia < other.get_dia()):
            return False
        else:
            return True  

    
