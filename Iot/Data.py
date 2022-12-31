class Data:
    def __init__(self, dia=1, mes=9, ano=2001, horas=0, minutos=0, segundos=0):
        self._dia=dia
        self._ano = ano
        self._mes=mes
        self._horas=horas
        self._minutos = minutos
        self._segundos=segundos

    def __fix_mes(self,other, mod):
        self._mes+=mod
        if(self._mes < other.mes):
            mes_o=abs(self._mes-other.mes)
            self._mes=12-mes_o
            self._ano-= other.ano+1
        else:
            self._mes-=other.mes
            self._ano-= other.ano

    def __fix_dia(self,other):
        if(self._dia < other.dia):
            self.__fix_mes(other,-1)
            dia_o=abs(self._dia-other.dia)
            if(self._mes==2 or self._mes==4 or self._mes==6 or self._mes==8 or self._mes==9 or self._mes==11 or self._mes==1 ):
                self._dia=31-dia_o
            elif(self._mes==3):
                self._dia=28-dia_o
            else:
                self._dia=30-dia_o
        else:
            self._dia-=other.dia 
            self.__fix_mes(other,0)  
    
    def __sub__(self,other):
        if(self.__check_op(other) == True):
            self.__fix_dia(other)
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
    @property
    def dia(self):
        return self._dia
    @property
    def ano(self):
        return self._ano
    @property
    def mes(self):
        return self._mes
    @dia.setter
    def dia(self,dia):
        self._dia=dia  
    @mes.setter
    def mes(self,mes):
        self._mes=mes 
    @ano.setter
    def ano(self,ano):
        self._ano=ano

    def __check_op(self,other):
        if(self._ano < other.ano):
            return False
        elif(self._ano == other.ano and self._mes < other.mes):
            return False
        elif (self._ano == other.ano and self._mes == other.mes and self._dia < other.dia):
            return False
        else:
            return True

    def __str__(self):
        if (self.dia<10 and self.mes<10):
            return f'0{self.dia}/0{self.mes}/{self.ano}'
        elif(self.dia>=10 and self.mes<10):
            return f'{self.dia}/0{self.mes}/{self.ano}'
        elif (self.get_dia()<10 and self.get_mes()>=10):
            return f'0{self.dia}/{self.mes}/{self.ano}'
        else:
            return f'{self.dia}/{self.mes}/{self.ano}'               

                  

    
