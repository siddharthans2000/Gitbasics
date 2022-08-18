class Siddharthan:
	def _init_(self,name):
		self.name=name
		print("Yeah the Object is created {}".format(self.name))
	def function1(self,*args,**kwargs):
		print("Yes first Function is called")
	
	def function2(self,*args,**kwargs):
		print("2nd Function is called")

new=Siddharthan("Sidd")

new.function1()
new.function2()
