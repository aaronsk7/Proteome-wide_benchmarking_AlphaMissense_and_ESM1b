#!/home/proteinmechanic/local/anaconda3/bin/python

import os, sys, glob, subprocess
from tqdm import tqdm 
import numpy as np


# Make a table (table2) - per table1
# UP - Pos - Ref - Alt - AM - ESM

if os.path.isdir('Tables') == True:
        os.system('rm -r Tables')
        os.system('mkdir Tables')
else:
        os.system('mkdir Tables')


_base_ = '/home/proteinmechanic/Projects/Clean_AM_ESM1b/Merged_Tables/'
_base_C = os.getcwd()

d = glob.glob(_base_ + '*.table1')

for i in tqdm(d):
	_fn_ = i.split('/')[-1].split('.')[0]
	_f_ = open('Tables/' + _fn_ + '.table2','a')
	e = np.genfromtxt(i, dtype = str, delimiter = "\t")
	for j in e:
		pos = j[1]
		res = j[2]
		vals = j[5]
		valsA = vals.split('-E-')[0]
		valsE = vals.split('-E-')[1]
		A = {}
		for i in valsA.split(','):
			A[i.split('|')[0]] = i.split('|')[1]
		E = {}
		for i in valsE.split(','):
			E[i.split('|')[0]] = i.split('|')[1]
		# Run over AM as ESM has one for itself 
		for key in A.keys():
			_f_.write('\t'.join([_fn_,pos,res,key,A[key],E[key]]) + '\n')
	_f_.close()
	#break

# Now that the tables are in - for each table add pfam annotation 

_base_C = os.getcwd()
pfam = _base_C + '/Pfam/'

os.chdir(_base_C + '/Tables')
d = glob.glob('*.table2')

for i in tqdm(d):
	# open file for output
	_g_ = open(i.split('.')[0] + '.table3','a')
	# Load pfam if any for current ID
	pf = pfam + i.split('.')[0] + '.out'
	vals = []
	if os.path.isfile(pf) == True:
		with open(pf) as f:
			for line in f:
				vals.append(line.split('\n')[0])
	else:
		pass
	# Load table for ID
	e = np.genfromtxt(i, dtype = str, delimiter = '\t')
	if len(vals) > 0: # Some domain present so check for all residues
		for j in e:
			ann = []
			for k in vals:
				if k.split('|')[0] != "-":
					if int(j[1]) >= int(k.split('|')[3]) and int(j[1]) <= int(k.split('|')[4]):
						ann.append(k.split('|')[1] + '|' + k.split('|')[2])	
				else:
					pass
			if len(ann) > 0:
				ann = "-x-".join(ann)
			else:
				ann = "-"
			_g_.write("\t".join(j) + '\t' +  ann + '\n')
	else: # nothing present so just insert empty annotation 
		ann = "-"
		for j in e:
			_g_.write("\t".join(j) + '\t' +  ann + '\n')
	_g_.close()
	#break



# Now gen table4 with uniprot added 
_base_C = os.getcwd()
up = _base_C + '/Uniprot/'
os.chdir(_base_C + '/Tables')
d = glob.glob('*.table3')

for i in tqdm(d):
	# open file for output
	_g_ = open(i.split('.')[0] + '.table4','a')
	# Load up if any for current ID
	_up_ = up + i.split('.')[0] + '.featuresUP'
	vals = []
	if os.path.isfile(_up_) == True:
		with open(_up_) as f:
			for line in f:
				vals.append(line.split('\n')[0])
	else:
		pass
	e = np.genfromtxt(i, dtype = str, delimiter = '\t')
	if len(vals) > 0:
		for j in e:
			ann = []
			for k in vals:
				if int(j[1]) >= int(k.split('\t')[3]) and int(j[1]) <= int(k.split('\t')[4]):
					if len(k.split('\t')[8].split('Note=')) > 1:
						note_ann = k.split('\t')[8].split('Note=')[1].split(';')[0]
					else:
						note_ann = "-"
					ann.append(k.split('\t')[2] + '|' + note_ann)
				else:
					pass
			if len(ann) > 0:
				ann = "-x-".join(ann)
			else:
				ann = "-"
			_g_.write("\t".join(j) + '\t' +  ann + '\n')

	else: 	# nothing present so just insert empty annotation 
		ann = "-"
		for j in e:
			_g_.write("\t".join(j) + '\t' +  ann + '\n')
	_g_.close()

# Get the EC numbers 
_base_C = os.getcwd()
os.chdir(_base_C + '/Tables')
d = glob.glob('*.table4')
os.chdir(_base_C)

_g_ = open('Aaron_UP2EC.dat','a')
for i in tqdm(d): 
	_id_ = i.split('.')[0]
	val = subprocess.Popen('grep ' + _id_ + ' ECData/enzyme.out', shell = True, stdout = subprocess.PIPE).stdout.read().decode()
	if len(val) > 0:
		val = val.split('\n')[0:-1]
		for j in val:
			_g_.write(_id_ + '\t' + j.split('\t')[0] + '\n')

_g_.close()
