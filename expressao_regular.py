#   Trabalho 1   Formais
# Alunos: Bruno George de Moraes
#         Wagner Santos
#
import automato_finito
class ExpressaoRegular:
	syntaxTree = {}
	expr = ''
	nome = ''

	def __init__(self, expr = '', nome = ''):
		self.expr = expr
		self.nome = nome
		
	def add_expressao(self, expressao):                
		self.expr.append(expressao)

	def print(self):
		saida = '' + self.expr
		saida += '\n'
		return saida
	# AHO 3.9.3
	#def nullable

	#def rst_opN

	#def lastpos(N) 
	#def followpos(P)

	# AHO 3.9.5
	def to_afd(self):
		af = automato_finito.AutomatoFinito()
		#TODO
		return af
