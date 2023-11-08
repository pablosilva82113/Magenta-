#Turing complete
def vhex(h):
	return h in [
		"1","2","3","4","5","6",
		"7","8","9","A","B","C",
		"D","E","F","0"
	]
def nhex(x,a,b):
	if not x == 'x':
		return False
	return vhex(a) and vhex(b)

def ndecimal(n):
	return n.isdigit()
def sigmov(m):
	return m in ["SDer","SIzq","SAbj","SArr","SBom"]
"""
	senmov("Izq").
	senmov("Der").
	senmov("Arr").
	senmov("Abj").
"""
def senmov(m):
	return m in ["Izq","Der","Arr","Abj"]

"""
	senpas("Nad").
	senpas("Apa").
"""
def senpas(p):
	return p in ["Apa","Nad"]
"""
	senreg("RINT0").
	senreg("RINT1").
	senreg("RINT2").
	senreg("RINT3").
"""
def senreg(r):
	return r in [
		"RINT0","RINT1",
		"RINT2","RINT3"
	]
"""
	senopma("+").
	senopma("-").
	senopma("/").
	senopma("*").
"""
def senopma(op):
	return op in [
		"+","-",
		"/","*"
	]
"""
	sensalt("SALTAIGUAL").
	sensalt("SALTANIGUAL").
	sensalt("SALTAMAYOR").
	sensalt("SALTAMENOR").
	sensalt("SALTAMAYORI").
	sensalt("SALTAMENORI").
"""
def sensalt(s):
	return s in [
		"SALTAIGUAL","SALTANIGUAL",
		"SALTAMAYOR","SALTAMENOR",
		"SALTAMAYORI","SALTAMENORI",
	]

"""
insaccgral("Sck").
insaccgral(A) :- senmov(A).
insaccgral(A) :- senpas(A).
"""
def insaccgral(a):
	if a == "Sck" :
		return True
	elif senmov(a):
		return True
	elif senpas(a):
		return True
	return False
"""

senasig(R,"=",NH) :-senreg(R),nhex(NH).
senasig(RA,"=",RB) :-senreg(RA),senreg(RB).
senasig(RA,"=",RB,OP,RC) :-
	senreg(RA),
	senreg(RB),
	senopma(OP),
	senreg(RC).
senasig(RA,"=",RB,OP,NH) :-
	senreg(RA),
	senreg(RB),
	senopma(OP),
	nhex(NH).
senasig(RA,"=",NHA,OP,NHB) :-
	senreg(RA),
	nhex(NHA),
	senopma(OP),
	nhex(NHB).
senasig(RA,"=",NH,OP,RB) :-
	senreg(RA),
	nhex(NH),
	senopma(OP),
	senreg(RB).
"""

def shex(nh):
	nh = list(nh)
	if len(nh) != 3:
		return False
	else:
		x,a,b = nh
		return nhex(x,a,b)

def senasig(lasg):
	ln = len(lasg)
	if not (ln == 3 or ln == 5):
		return False
	if lasg[1] != '=':
		return False
	if ln == 3:
		R,I,RT = lasg
		if not senreg(R):
			return False
		if senreg(RT):
			return True
		elif shex(RT):
			return shex(RT)
		elif sigmov(RT):
			return True

	else: # ln = 5
		R,I,RB,OP,RC = lasg
		if not senreg(R):
			return False
		if not senopma(OP):
			return False
		if senreg(RB): # Registro
			# Evaluar a RC
			if senreg(RC):
				return True
			elif ndecimal(RC):
				return ndecimal(RC)
			else:
				return shex(RC)
		else: # nHex
				if shex(RB):
					# Evaluar a RC
					if senreg(RC):
						return True
					else:

						return shex(RC.isdigit())
				else:
					return False

"""
	inssalt(A,B,C,D) :- sensalt(A),senreg(B),nhex(C),nhex(D).
	inssalt(A,B,C,D) :- sensalt(A),nhex(B),senreg(C),nhex(D).
	inssalt(A,B,C,D) :- sensalt(A),nhex(B),nhex(C),nhex(D).
	inssalt(A,B,C,D) :- sensalt(A),senreg(B),senreg(C),nhex(D).
"""
def inssalt(A,B,C,D):
	if not sensalt(A):
		return False
	if not shex(D):
		return False
	# Si B es un Registro
	if senreg(B):
		if shex(C):
			return True
		elif senreg(C):
			return True
		return False
	elif shex(B):
		if shex(C):
			return True
		elif senreg(C):
			return True
		return False
	return False


def lienacodigo(L):
	l = len(L)
	if l == 1:
		return insaccgral(L[0])
	elif l == 3:
		return senasig(L)
	elif l == 4:
		A,B,C,D = L
		return inssalt(A,B,C,D)
	elif l ==5:
		return senasig(L)
	else:
		return False
	

