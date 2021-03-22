from random import *
class Pergunta:
	def __init__(self):
		self.level = [
		['Seu Pet toma dano de dragao?', 'dragao'],
		['Seu Pet toma dano de fantasma?', 'fantasma'],
		['Seu Pet toma dano de pedra?', 'pedra'],
		['Seu Pet toma dano de inseto?', 'inseto'],
		['Seu Pet toma dano de psiquico?', 'psiquico'],
		['Seu Pet toma dano de voador?', 'voador'],
		['Seu Pet toma dano de terra?', 'terra'],
		['Seu Pet toma dano de veneno?', 'veneno'],
		['Seu Pet toma dano de lutador?', 'lutador'],
		['Seu Pet toma dano de gelo?', 'gelo'],
		['Seu Pet toma dano de grama?', 'grama'],
		['Seu Pet toma dano de eletrico?', 'eletrico'],
		['Seu Pet toma dano de agua?', 'agua'],
		['Seu Pet toma dano de fogo?', 'fogo'], 
		['Seu Pet toma dano de normal?', 'normal'],
		]

	def texto(self):
		string = self.level[0]
		del self.level[0]
		return string
