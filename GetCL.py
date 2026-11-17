#!/Users/proteinmechanic/opt/anaconda3/bin/python
import os, sys, glob, subprocess, requests
from tqdm import tqdm 

ignores = {
	"VARIANT": 0,
	"COMPBIAS":0,
	"MUTAGEN":0,
	"MOD_RES":0,
	"BINDING":0,
	"CROSSLNK":0,
	"VAR_SEQ":0,
	"HELIX":0,
	"TURN":0,
	"STRAND":0,
	"DISULFID":0,
	}

includes = {
	'Intramembrane':0,
	'Subcellular location[CC]':0,
	'Topological domain':0,
	'Transmembrane':0,
	'Motif':0
	}

def fetch_seqFeatures(ID):
	url = "https://www.ebi.ac.uk/proteins/api/proteins/"+ID
	url2 = "https://rest.uniprot.org/uniprotkb/" + ID + ".gff"
	response = requests.get(url2)
	res = response.text
	sub  = []
	for i in res.split('\n'):
		if len(i) > 1:
			_i_  = i.split('\t')
			if len(_i_) > 2:
				if _i_[2] in includes:
					sub.append(_i_)
	if len(sub) > 0:
		with open(ID + '.featuresUP','a') as f:
			for i in sub:
				f.write('\t'.join(i) + '\n')
	else:
		with open('Errors.featuresUP','a') as f:
			f.write(ID + ' has nothing' + '\n')
		
	'''
	if response.status_code == 200:
		res = response.json()
		for dct in res['features']:
			if dct['type'] not in ignores:
				print(dct)
	else:
		return 0
	'''
	
fetch_seqFeatures(sys.argv[1])
