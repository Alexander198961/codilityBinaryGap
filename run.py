class test:

	newstr="";
	def convert_to_bin(self, digit ):
		

		if  digit == 1 :
			self.newstr=" ".join((self.newstr , "1" ))
			return 0;
		
		rest=digit/2
		left=digit-rest*2
                str2=str(left)
		self.newstr=" ".join((self.newstr , str2 ))
		self.convert_to_bin(rest)
	
tester=test();


def solution(N):
	
	str=tester.convert_to_bin(N)
	list=tester.newstr.split(" ");
	size1=0;
	count=0
	for str in list[1:]:
		if  str == "1":
			if count > size1 :
				size1=count
			count=0	
		else:
			count=count+1
	return size1
