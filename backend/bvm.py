class BMV:
    def __init__(self):
        self.Programa = []
        self.Mapa = [
            ['L','L','L','L','L','X','L','L'],
            ['L','L','L','L','L','X','L','L'],
            ['L','L','L','L','L','L','L','L'],
            ['L','L','L','L','L','X','L','L'],
            ['L','L','L','L','L','X','L','L'],
            ['L','L','L','L','L','X','L','B']

        ]
        self.X=0 #horizontal
        self.Y=0 #vertical
        #registros
        self.RINT0 = 0
        self.RINT1 = 0
        self.RINT2 = 0
        self.RINT3 = 0
        #self.Pila =[]
        self.NoLinnea = 0
        self.Salto = False
    

    def ejecutarCodigo(self,L):
            
            l = len(L)

            if l == 1:
                if L[0]=='Sck':
                    if self.Mapa[self.Y][self.X] == 'B':
                        self.Mapa[self.Y][self.X] = 'L'

                elif L[0]=='Izq':
                    self.X = self.X - 1
                    if self.X < 0:
                        print("Error: No se puede salir del mapa",self.X)
                        return False
                elif L[0]=='Der':
                    self.X = self.X + 1
                   
                    if self.X > 7:
                        print("Error: No se puede salir del mapa",self.X)
                        return False
                elif L[0]=='Arr':
                    self.Y = self.Y - 1
                    
                    if self.Y < 0:
                        print("Error: No se puede salir del mapa",self.Y)
                        return False
                elif L[0]=='Abj':
                    self.Y = self.Y + 1
                    if self.Y > 5:
                        print("Error: No se puede salir del mapa",self.Y)
                        return False
                    
                elif L[0]=='Apa':
                    print("Fin del programa")
                    return False
                
                elif L[0]=='Nad':
                    pass

            elif l == 3:
                registro,igual,valor = L

                if registro == 'RINT0':
                    if valor == 'SDer':
                        if self.X < 7 and self.Mapa[self.Y][self.X+1] !='X':
                            self.RINT0=0
                        else:
                            if self.X == 7 or self.Mapa[self.Y][self.X+1] =='X':
                                self.RINT0=1

                    elif valor == 'SIzq':
                        if  self.X > 0 and self.Mapa[self.Y][self.X - 1] != 'X':
                            self.RINT0=0
                        else:
                            if self.X == 0 or self.Mapa[self.Y][self.X - 1] == 'X':
                                self.RINT0=1
                            
                    elif valor == 'SAbj':
                        if self.Y < 5 and self.Mapa[self.Y + 1][self.X] != 'X':
                            self.RINT0=0
                        else:
                            if self.Y == 5 or self.Mapa[self.Y + 1][self.X] == 'X':
                                self.RINT0=1
                    elif valor == 'SArr':
                        if self.Y > 0 and self.Mapa[self.Y - 1][self.X] != 'X':
                            self.RINT0=0
                        else:
                            if self.Y == 0 or self.Mapa[self.Y - 1][self.X] == 'X':
                                self.RINT0=1
                    else:
                        valor = int('0'+valor,16)
                        self.RINT0 = valor

                elif registro == 'RINT1':
                    if valor == 'SDer':
                        if self.X < 7 and self.Mapa[self.Y][self.X + 1] != 'X':
                            self.RINT1 = 0
                        else:
                            if self.X == 7 or self.Mapa[self.Y][self.X + 1] == 'X':
                                self.RINT1 = 1

                    elif valor == 'SIzq':
                        if self.X > 0 and self.Mapa[self.Y][self.X - 1] != 'X':
                            self.RINT1 = 0
                        else:
                            if self.X == 0 or self.Mapa[self.Y][self.X - 1] == 'X':
                                self.RINT1 = 1

                    elif valor == 'SAbj':
                        if self.Y < 5 and self.Mapa[self.Y + 1][self.X] != 'X':
                            self.RINT1 = 0
                        else:
                            if self.Y == 5 or self.Mapa[self.Y + 1][self.X] == 'X':
                                self.RINT1 = 1
                    elif valor == 'SArr':
                        if self.Y > 0 and self.Mapa[self.Y - 1][self.X] != 'X':
                            self.RINT1 = 0
                        else:
                            if self.Y == 0 or self.Mapa[self.Y - 1][self.X] == 'X':
                                self.RINT1 = 1
                    else:
                        valor = int('0' + valor, 16)
                        self.RINT1 = valor

                elif registro == 'RINT2':
                    if valor == 'SDer':
                        if self.X < 7 and self.Mapa[self.Y][self.X + 1] != 'X':
                            self.RINT2 = 0
                        else:
                            if self.X == 7 or self.Mapa[self.Y][self.X + 1] == 'X':
                                self.RINT2 = 1

                    elif valor == 'SIzq':
                        if self.X > 0 and self.Mapa[self.Y][self.X - 1] != 'X':
                            self.RINT2 = 0
                        else:
                            if self.X == 0 or self.Mapa[self.Y][self.X - 1] == 'X':
                                self.RINT2 = 1

                    elif valor == 'SAbj':
                        if self.Y < 5 and self.Mapa[self.Y + 1][self.X] != 'X':
                            self.RINT2 = 0
                        else:
                            if self.Y == 5 or self.Mapa[self.Y + 1][self.X] == 'X':
                                self.RINT2 = 1
                    elif valor == 'SArr':
                        if self.Y > 0 and self.Mapa[self.Y - 1][self.X] != 'X':
                            self.RINT2 = 0
                        else:
                            if self.Y == 0 or self.Mapa[self.Y - 1][self.X] == 'X':
                                self.RINT2 = 1
                    else:
                        valor = int('0' + valor, 16)
                        self.RINT2 = valor

                elif registro == 'RINT3':
                    if valor == 'SDer':
                        if self.X < 7 and self.Mapa[self.Y][self.X + 1] != 'X':
                            self.RINT3 = 0
                        else:
                            if self.X == 7 or self.Mapa[self.Y][self.X + 1] == 'X':
                                self.RINT3 = 1

                    elif valor == 'SIzq':
                        if self.X > 0 and self.Mapa[self.Y][self.X - 1] != 'X':
                            self.RINT3 = 0
                        else:
                            if self.X == 0 or self.Mapa[self.Y][self.X - 1] == 'X':
                                self.RINT3 = 1

                    elif valor == 'SAbj':
                        if self.Y < 5 and self.Mapa[self.Y + 1][self.X] != 'X':
                            self.RINT3 = 0
                        else:
                            if self.Y == 5 or self.Mapa[self.Y + 1][self.X] == 'X':
                                self.RINT3 = 1
                    elif valor == 'SArr':
                        if self.Y > 0 and self.Mapa[self.Y - 1][self.X] != 'X':
                            self.RINT3 = 0
                        else:
                            if self.Y == 0 or self.Mapa[self.Y - 1][self.X] == 'X':
                                self.RINT3 = 1
                    else:
                        valor = int('0' + valor, 16)
                        self.RINT3 = valor

            elif l ==4:
                salto,reg,V1,lin  = L
                lin = int('0'+lin,16)
                print("lin",lin)
                
                if reg == 'RINT0':
                    v_1= self.RINT0
                elif reg == 'RINT1':
                    v_1= self.RINT1
                elif reg == 'RINT2':
                    v_1= self.RINT2
                elif reg == 'RINT3':
                    v_1= self.RINT3
                else:
                    v_1 = self.RINT0
                    v_1 = int('0'+v_1,16)
                
                
                if V1 == 'RINT0':
                    v_2= self.RINT0
                elif V1 == 'RINT1':
                    v_2= self.RINT1
                elif V1 == 'RINT2':
                    v_2= self.RINT2
                elif V1 == 'RINT3':
                    v_2= self.RINT3
                else:
                    v_2 = int('0'+V1,16)
                
                #tipo v1 y v2
                
                if salto =='SALTAIGUAL':
                    
                    if v_1 == v_2:
                        self.NoLinnea = lin
                        print("NoLinnea",self.NoLinnea)
                        self.Salto = True
                        return True
                    else:
                        self.Salto = False
                elif salto =='SALTANIGUAL':
                    if v_1 != v_2:
                        self.NoLinnea = lin
                        print("NoLinnea",self.NoLinnea)
                        self.Salto = True
                        return True
                    else:
                        self.Salto = False
                elif salto =='SALTAMAYOR':
                    if v_1 > v_2:
                        self.NoLinnea = lin
                        print("NoLinnea",self.NoLinnea)
                        self.Salto = True
                        return True
                    else:
                        self.Salto = False
                elif salto =='SALTAMENOR':
                    if v_1 < v_2:
                        self.NoLinnea = lin
                        print("NoLinnea",self.NoLinnea)
                        self.Salto = True
                        return True
                    else:
                        self.Salto = False

                elif salto =='SALTAMAYORI':
                    if v_1 >= v_2:
                        self.NoLinnea = lin
                        print("NoLinnea",self.NoLinnea)
                        self.Salto = True
                        return True
                    else:
                        self.Salto = False

                elif salto =='SALTAMENORI':
                    if v_1 <= v_2:
                        self.NoLinnea = lin
                        print("NoLinnea",self.NoLinnea)
                        self.Salto = True
                        return True
                    else:
                        self.Salto = False

            elif l == 5:
                Reg,igual,rb,op,rc = L
                #cuano rc es un entero como lo valido y lo convierto a hexadecimal
    
                if rb == 'RINT0':
                    rb = self.RINT0
                    
                elif rb == 'RINT1':
                    rb = self.RINT1
                    
                elif rb == 'RINT2':
                    rb = self.RINT2
                    
                elif rb == 'RINT3':
                    rb = self.RINT3
                    
                else:
                    rb = int('0'+rb,16)
                    
                #puede ser un entero o un registro o hexadecimal
                if rc == 'RINT0':
                    rc = self.RINT0
                    
                elif rc == 'RINT1':
                    rc = self.RINT1
                    
                elif rc == 'RINT2':
                    rc = self.RINT2
                  
                elif rc == 'RINT3':
                    rc = self.RINT3
                   
                elif rc.isdigit():
                    rc = int('0'+rc,16)
                    
                else:
                    rc = int('0'+rc,16)
                 
                
               

                #se realizan las operaciones y se convierte a hexadecimal
                if op == '+':
                    resultado = rb + rc
                    resultado = hex(resultado)
                    resultado = resultado[2:]
                    
                elif op == '-':
                    if rb > rc:
                        print("rb es mayor que rc")
                    resultado = rb - rc
                    resultado = hex(resultado)
                    resultado = resultado[2:]
                    
                elif op == '*':
                    resultado = rb * rc
                    resultado = hex(resultado)
                    resultado = resultado[2:]
                    
                elif op == '/':
                    if rc == 0:
                        print("Error: No se puede dividir entre 0")
                        return False
                    resultado = rb / rc
                    resultado = hex(resultado)
                    resultado = resultado[2:]
                    print("Soy un hexadecimal",resultado)

                if Reg == 'RINT0':
                    convertir_entero = int('0'+resultado,16)
                    self.RINT0 = resultado
                elif Reg == 'RINT1':
                    convertir_entero = int('0'+resultado,16)
                    self.RINT1 = resultado
                elif Reg == 'RINT2':
                    convertir_entero = int('0'+resultado,16)
                    self.RINT2 = resultado
                elif Reg == 'RINT3':
                    convertir_entero = int('0'+resultado,16)
                    self.RINT3 = convertir_entero
                    

        
    def depurar(self):
            print("self.X",self.X)
            print("self.Y",self.Y)
            print("self.RINT0",self.RINT0)
            print("self.RINT1",self.RINT1)
            print("self.RINT2",self.RINT2)
            print("self.RINT3",self.RINT3)
            print("########################################")
            
            antes = self.Mapa[self.Y][self.X]
            self.Mapa[self.Y][self.X] = 'R'
            for linea in self.Mapa:
                print(linea)
            self.Mapa[self.Y][self.X] = antes