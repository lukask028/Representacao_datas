# Crie uma classe para representar datas.
# 1. Represente uma data usando três atributos: o dia, o mês, e o ano.
# 2. Sua classe deve ter um construtor que inicializa os três atributos e verifica a validade dos valores
# fornecidos.
# 3. Forneça um construtor sem parâmetros que inicializa a data com a data atual fornecida pelo sistema
# operacional.
# 4. Forneça um método set um get para cada atributo.
# 5. Forneça o método toString para retornar uma representação da ata como string. Considere que a
# data deve ser formatada mostrando o dia, o mês e o ano separados por barra (/).
# 6. Forneça uma operação para avançar uma data para o dia seguinte

class Data:
    def __init__(self, dia : int, mes : int, ano : int):
        self._dia = dia;
        self._mes = mes;
        self._ano = ano;
       
    @property
    def dia(self):
        return self._dia;
        
    @dia.setter
    def dia(self, dia):
        self._dia = dia;  
        
    @property
    def mes(self):
        return self._mes;   
    
    @mes.setter
    def mes(self, mes):
        self._mes = mes;
        
    @property
    def ano(self):
        return self._ano;
        
    @ano.setter
    def ano(self, ano):
        self._ano = ano;   
        
    def __repr__(self):
            class_name = type(self).__name__
            attrs = f'({self._dia!r}, {self._mes!r} , {self._ano!r} )'
            return f'{class_name}{attrs}' 
        
    def verificaData(dia, mes, ano):
      
        if dia <= 0 or dia > 31:
            raise Exception("O dia não pode ser menor ou igual a 0, ou maior que 31.")
        
        if mes <= 0 or mes > 12:
            raise Exception("O mes não pode ser maior que 12, ou menor que 0.")
        
        if ano < 1950 or ano > 2050:
            raise Exception("O ano não pode ser menor que 1950, ou maior que 2050.")
        
        return Data(dia,mes,ano)      
   
    def avancaDia(dia, mes, ano):
        if dia == 31 and mes != 12:
            dia =+ 0
            mes += 1
            dia += 1
            
        
        if dia == 31 and mes == 12:
            dia += 0
            dia =+ 1
            mes += 0 
            mes =+ 1
            ano += 1
            
        if dia != 31:
            dia += 1
            
        return Data(dia,mes,ano) 
        
        
data1 = Data(15,5,2010)
datastr = str(data1)



print('Primeira data:', data1.dia,"/",data1.mes,"/", data1.ano)
dataverificada1 = Data.verificaData(data1.dia, data1.mes, data1.ano)
print('data verificada:', dataverificada1)
diaAvancado = Data.avancaDia(data1.dia, data1.mes, data1.ano)
print('data avancada:', diaAvancado)    