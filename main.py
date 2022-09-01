from kivy.lang import Builder
from kivy.app import App
from kivy.core.audio import SoundLoader

import os, sys
from kivy.resources import resource_add_path, resource_find

wrong = (1, 0, 0, 1) #Red
choosen = (1, 165/255, 0, 1) #Orange
correct = (0, 1, 0, 1) #Green

tot = 0
qnum = None

oname = ['a', 'b', 'c', 'd']

# Defining questions:
q = [
	'The endoplasmic reticulum with\nRibosomes are called...',#Rough Endoplasmic reticulum
	'Cell was discovered by...',#Robert Hooke
	'Organelle which \nproduces ATP is called',#Mitochondria
	'The Plastid resposible for\ngiving color to flowers & fruits is...',#Chromoplast
	'Blood is a...', # Colloid
	'Cell Organelle which stores, \nmodifies and packs \nproducts from ER is called...',#Golgi Appareteus
	'Who coined the term Protoplasm',#Purkinje
	'Food factory of the cell',#Chloroplast
	'Green Pigment in plants',#Chlorophyll
	'Which of the follwoing \nare one of the\nEquations of motion?'# v = u + at
]

ans = {
	0:3,
	1:0,
	2:1,
	3:2,
	4:0,
	5:3,
	6:1,
	7:2,
	8:1,
	9:3
}

opts = {
	'0':['Spirogyra', 'Tough Endoplasmic \nRecticulum', 'Yeast', 'Rough Endoplasmic\n Reticulum'],
	'1':['Robert Hooke', 'Ludwig\nVan Beethoven', 'Guido Van Rossum', 'Robet Downey Jr.'],
	'2':['Nucleus', 'Mitochondria', 'Chlorophyll', 'Chloroplast'],
	'3':['Chromeplast', 'Corrosion', 'Chromoplast', 'Leucoplast'],
	'4':['Colloid', 'Solution', 'Element', 'Compound'],
	'5':['Stomach', 'Brain', 'Nucleus', 'Golgi Appareteus'],
	'6':['Robert Hooke', 'Purkinje', 'Schleiden & Shwann', 'Robert Brown'],
	'7':['Chromoplast', 'Leucoplast', 'Chloroplast', 'Plastid'],
	'8':['Chromosome', 'Chlorophyll', 'Sperms', 'Genes'],
	'9':['e = mc*c', 'a*a + b*b = c*c', 'a = (v - u)/t', 'v = u + at']
}

class Scinder(App):
	def build(self):
		music = SoundLoader.load('weeknd.wav')
		if music:
			music.play()
			music.loop = True


		self.start()

	def start(self):
		try:
			global qnum

			self.root.ids['Q'].text = q[0]

			for i in range(4):
				self.root.ids[str(i)].text = opts['0'][i]

			qnum = 0
		except:
			self.root.ids['Q'].text = 'AN ERROR OCURRED: Start()'

	def master(self):
		global qnum

		try:
			qnum += 1
			self.root.ids['Q'].text = q[qnum]

			for i in range(4):
				self.root.ids[str(i)].text = opts[str(qnum)][i]
				self.root.ids[str(i)].background_color = (135/255, 107/255, 105/255, 1)
		except:
			self.root.ids['Q'].text = 'AN ERROR OCURRED: Master()'

	def success(self):

		#change the options blank
		for i in range(4):
			self.root.ids[str(i)].text = ''
		self.root.ids.nex.text = ''
		self.root.ids[str(i)].background_color = (135/255, 107/255, 105/255, 1)
		self.root.ids.Q.text = f'Score: {tot}\nAnswered wrong: {10 - tot}'
		self.root.ids.ex.background_color = (1, 80/255, 0, 1)



	def pressed(self, option):
		global qnum
		global tot
		global countdrac
		global correct
		global wrong

		if int(ans[qnum]) == int(option):
			tot += 1
			self.root.ids[str(option)].background_color = (24/255, 181/255, 50/255, 1)
		else:
			self.root.ids[str(option)].background_color = (1, 0, 0, 1)

	def state_check(self):
		global qnum
		print(qnum)
		if qnum != 9:
			self.master()
		else:
			self.success()

	def close(self):
		App.get_running_app().stop() 
	
	def slid(self, *args):
		#print(args[1])
		self.root.ids.text = str(args[1])
		self.root.ids.font_size = str(int(args[1]))

if __name__ == '__main__':
	if hasattr(sys, '_MEIPASS'):
		resource_add_path(os.path.join(sys._MEIPASS))
	Scinder().run()