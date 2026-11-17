#!/Users/proteinmechanic/opt/anaconda3/bin/python
import os, sys, glob, subprocess, requests
from tqdm import tqdm 

def fetch_pfamN(ID):
	url = "https://www.ebi.ac.uk/interpro/api//entry/pfam/protein/UniProt/"+ID
	response = requests.get(url)
	if response.status_code == 200:
		res = response.json()
		pfam_ = ''
		res_ = []
		for dct in res['results']:
			val = dct['metadata']
			acc = val['accession']
			name = val['name']  
			val = dct['proteins']
			valS = str(val[0]['entry_protein_locations'][0]['fragments'][0]['start'])
			valE = str(val[0]['entry_protein_locations'][0]['fragments'][0]['end'])
			res_.append('|'.join([ID, acc, name, valS, valE]))
	#		pfam_ += '''{name:\"''' + name + '''\",begin:''' +  valS + ''',end:''' +  valE + '''},'''
	#	pfam_ = "[" + pfam_ + ']'
		return res_
	else:
		return ['-|-|-|-|-']
v = fetch_pfamN(sys.argv[1])
with open(sys.argv[1] + '.out','a') as f:
	for i in v:
		f.write(i + '\n')
