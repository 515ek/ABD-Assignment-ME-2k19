from mrjob.job import MRJob

class MRmyjob(MRJob):

	def mapper(self,_,line):
		#split the line with tab separated fields
		data = line.split(',')
		hofid = data[0].strip()
		category = data[7].strip()
		if category == 'Manager':
			yield hofid,None

	def reducer(self, key, list_of_values):
		
		yield "manager",key
	
if __name__ == '__main__':
	MRmyjob.run();