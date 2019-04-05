from mrjob.job import MRJob
from mrjob.step import MRStep
import sys  
class MRWordFrequencyCount(MRJob):
	def mapper1(self, _, lines):
		data = lines.split(',')
		players = data[0].strip()
		yield players,None

	def combiner(self, word, counts):
		
		yield word,None			
		
		
	def reducer1(self, key, counts):
		yield "total players",key

	def reducer2(self, key,word):
		yield key,len(list(word))
        
	def steps(self):
		return [ MRStep(mapper=self.mapper1,reducer=self.combiner),MRStep(reducer=self.reducer1),MRStep(reducer=self.reducer2)]



if __name__ == '__main__':
    MRWordFrequencyCount.run()