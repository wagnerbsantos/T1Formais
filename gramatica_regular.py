#   Trabalho 1   Formais
# Alunos: Bruno George de Moraes
#         Wagner Santos
#
import automato_finito

class GramaticaRegular:
	variaveis = set()
	transicoes = {}
	inicial: ''

	def __init__(self):
		self.variaveis = set()
		self.transicoes = {}
		self.inicial = ''

	def add_variavel(self, variavel):
		self.variaveis = self.variaveis.union((variavel,))

	def set_variavel_inicial(self, variavel):
		if variavel in self.variaveis:
			self.inicial = variavel

	def add_regras(self, v1, t, v2):
		if (v1 in self.variaveis):
			if (v1 not in self.transicoes.keys()):
				self.transicoes[v1] = [(t, v2)]
			else:
				if((t, v2) not in self.transicoes[v1]):
					self.transicoes[v1].append((t, v2))	

	def print(self):
		saida = ''
		for v in self.variaveis:
			if v == self.inicial:
				saida = saida + '->'
			saida = saida + '(' + v + ') -> '
			for prod in self.transicoes[v]:
				if prod[1] != '&':
					saida = saida + prod[0] + '(' +prod[1] + ') | '
				else:
					saida = saida + prod[0] + ' | '
			saida = saida[:-2] + '\n'
		return saida

	def alfabeto(self):
		lista = set()
		for v in self.variaveis:
			for prod in self.transicoes[v]:
				lista = lista.union(prod[0])
		return lista

	def to_afnd(self):
		af = automato_finito.AutomatoFinito()
		final = '_F_'
		af.estados = self.variaveis.union((final,))
		af.inicial = self.inicial
		af.finais.add(final)
		for v in self.variaveis:
			for e in self.transicoes[v]:
				if e[0] == '&' and e[1] == '&':
					af.finais.add(v)
				elif e[0] != '&' and e[1] == '&':
					af.transicoes[v, e[0]] = [final]
				else:
					af.transicoes[v, e[0]] = e[1]
		return af
