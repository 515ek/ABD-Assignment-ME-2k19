from mrjob.job import MRJob

class MRmyjob(MRJob):

	def mapper(self,_,line):
		#split the line with tab separated fields
		data = line.split(',')
		hofid = data[0].strip()
		year = data[1].strip()
		votes = data[5].strip()
		try:
			yield hofid,int(votes)
		except:
			yield hofid,0
		
	def reducer(self,key,list_of_values):
		yield key,sum(list_of_values)

if __name__ == '__main__':
	MRmyjob.run()