class Data:
    def __init__(self, dia=1, mes=9, ano=2001, horas=8, minutos=30, segundos=30):
        self._dia=dia
        self._ano = ano
        self._mes=mes
        self._horas=horas
        self._minutos = minutos
        self._segundos=segundos

    def __fix_mes(self,other, mod):
        self._mes+=mod
        if(self._mes < other.mes):
            self._mes=12+self._mes-other.mes
            self._ano-= other.ano+1
        else:
            self._mes=self._mes-other.mes
            self._ano-= other.ano

    def __fix_dia(self,other,mod):
        self._dia+=mod
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
            self._dia=self._dia-other.dia
            self.__fix_mes(other,0)  

    def __fix_horas(self,other,mod):
        self._horas += mod
        if(self._horas < other._horas):
            self.__fix_dia(other,-1)
            horas_o=abs(self._horas-other._horas)
            self._horas=24-horas_o
        else:
              self._horas=self._horas-other._horas
              self.__fix_dia(other,0)

    def __fix_minutos(self,other,mod):
        self._minutos += mod
        if(self._minutos < other._minutos):
            self.__fix_horas(other,-1)
            minutos_o=abs(self._minutos-other._minutos)
            self._minutos=60-minutos_o
        else:
            self._minutos=self._minutos-other._minutos
            self.__fix_horas(other,0) 

    def __fix_segundos(self,other):
        if(self._minutos < other._minutos):
            self.__fix_minutos(other,-1)
            segundos_o=abs(self._segundos-other._segundos)
            self._segundos=60-segundos_o
        else:
            self._segundos= self._segundos-other._segundos
            self.__fix_minutos(other,0)         
    
    def __sub__(self,other):
        if(self.__check_op(other) == True):
            self.__fix_segundos(other)
            if(self._ano > 1):
                print ("A diferença é de {} anos".format(self._ano),end=", ")
            else: 
                print ("A diferença é de {} ano".format(self._ano),end=", ")   
            if(self._mes > 1):
                print ("{} meses".format(self._mes),end=" e ")
            else: 
                print ("{} mes".format(self._mes),end=" e ")
            if(self._dia > 1):
                print ("{} dias".format(self._dia),end=" : ")
            else: 
                print ("{} dia".format(self._dia),end=" : ") 
            if(self._horas > 1):
                print ("{} horas".format(self._horas),end=" ")
            else: 
                print ("{} hora".format(self._horas),end=" ")
            if(self._minutos > 1):
                print ("{} minutos".format(self._minutos),end=" ")
            else: 
                print ("{} minuto".format(self._minutos),end=" ")
            if(self._segundos > 1):
                print ("{} segundos".format(self._segundos),end="\n")
            else: 
                print ("{} segundo".format(self._segundos),end="\n")             
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
    @property
    def horas(self):
        return self._horas
    @property
    def minutos(self):
        return self._minutos
    @property
    def segundos(self):
        return self._segundos
    @dia.setter
    def dia(self,dia):
        self._dia=dia  
    @mes.setter
    def mes(self,mes):
        self._mes=mes 
    @ano.setter
    def ano(self,ano):
        self._ano=ano
    @horas.setter
    def horas(self,horas):
        self._horas=horas 
    @minutos.setter
    def minutos(self,minutos):
        self._minutos=minutos 
    @segundos.setter
    def segundos(self,segundos):
        self._segundos=segundos  

    def __check_op(self,other):
        if(self._ano < other.ano):
            return False
        elif(self._ano == other.ano and self._mes < other._mes):
            return False
        elif (self._ano == other.ano and self._mes == other.mes and self._dia < other._dia):
            return False
        elif (self._ano == other.ano and self._mes == other.mes and self._dia == other.dia and self._horas < other._horas):
            return False  
        elif (self._ano == other.ano and self._mes == other.mes and self._dia == other.dia and self._horas == other._horas and self._minutos < other._minutos):
            return False
        elif (self._ano == other.ano and self._mes == other.mes and self._dia == other.dia and self._horas == other._horas and self._minutos == other._minutos and self._segundos < other._segundos):
            return False          
        else:
            return True

    def __str__(self):
        if (self._dia<10 and self._mes<10 ):
            return f'0{self._dia}/0{self._mes}/{self._ano} : {self._horas}:{self._minutos}:{self._segundos}'
        elif(self._dia>=10 and self._mes<10):
            return f'{self._dia}/0{self._mes}/{self._ano} : {self._horas}:{self._minutos}:{self._segundos}'
        elif (self._dia<10 and self._mes>=10):
            return f'0{self._dia}/{self._mes}/{self._ano} : {self._horas}:{self._minutos}:{self._segundos}'
        else:
            return f'{self._dia}/{self._mes}/{self._ano} : {self._horas}:{self._minutos}:{self._segundos}'               

                  

    
