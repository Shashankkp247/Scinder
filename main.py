from kivy.lang import Builder
from kivymd.app import MDApp

wrong = (1, 0, 0, 1) #Red
choosen = (1, 165/255, 0, 1) #Orange
correct = (0, 1, 0, 1) #Green

tot = 0
qnum = None

oname = ['a', 'b', 'c', 'd']

# Defining questions:
q = [
	'The endoplasmic reticulum with Ribosomes are called...',#Rough Endoplasmic reticulum
	'The cell was discovered by...',#Robert Hooke
	'Organelle which produces ATP is called',#Mitochondria
	'The Plastid resposible for color in plants is...',#Chromoplast
	'Blood is a...', # Colloid
	'Organelle which stores, modifies and packs products from ER is called...',#Golgi Appareteus
	'Who coined the term Protoplasm',#Purkinje
	'Food factory of the cell',#Chloroplast
	'Green Pigment in plants',#Chlorophyll
	'Which of the follwoing are one of the Equations of motion?'# v = u + at
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
	'0':['Spirogyra', 'Tough Endoplasmic Recticulum', 'Yeast', 'Rough Endoplasmic Reticulum'],
	'1':['Robert Hooke', 'Ludwig Van Beethoven', 'Guido Van Rossum', 'Robet Downey Jr.'],
	'2':['Nucleus', 'Mitochondria', 'Chlorophyll', 'Chloroplast'],
	'3':['Chromeplast', 'Corrosion', 'Chromoplast', 'Leucoplast'],
	'4':['Colloid', 'Solution', 'Element', 'Compound'],
	'5':['Stomach', 'Brain', 'Nucleus', 'Golgi Appareteus'],
	'6':['Robert Hooke', 'Purkinje', 'Schleiden & Shwann', 'Robert Brown'],
	'7':['Chromoplast', 'Leucoplast', 'Chloroplast', 'Plastid'],
	'8':['Chromosome', 'Chlorophyll', 'Sperms', 'Genes'],
	'9':['e = mc*c', 'a*a + b*b = c*c', 'a = (v - u)/t', 'v = u + at']
}

class Scinder(MDApp):
	def build(self):
		self.theme_cls.theme_style = 'Dark'
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

		try:
			self.root.ids['Q'].text = q[qnum]

			for i in range(4):
				self.root.ids[str(i)].text = opts[str(qnum)][i]
				self.root.ids[str(i)].text_color = (0, 0, 1, 1)
		except:
			self.root.ids['Q'].text = 'AN ERROR OCURRED: Master()'

	def success(self):

		#change the options blank
		for i in range(4):
			self.root.ids[str(i)].text = ''
		
		self.root.ids.Q.text = f'Score: {tot}\nAnswered wrong: {10 - tot}'



	def pressed(self, option):
		global qnum
		global tot
		global countdrac

		if int(ans[qnum]) == int(option):
			tot += 1
			self.root.ids[str(option)].text_color = correct
		else:
			self.root.ids[str(option)].text_color = wrong

		qnum += 1

	def state_check(self):
		global qnum
		print(qnum)
		if qnum != 10:
			self.master()
		else:
			self.success()

	def close(self):
		MDApp.get_running_app().stop() 
		


Scinder().run()