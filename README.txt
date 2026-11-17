All R files run from and to a directory at the path "~/alphamissense_analysis". The scripts also write to directories within this directory located at: 
 "~/alphamissense_analysis/figs", ""~/alphamissense_analysis/results", ""~/alphamissense_analysis/sup_data" and "~/alphamissense_analysis/subcellular_location". 
Create these directories before running scripts
To run some scripts you will need the file HUMAN_9606_idmapping_selected.tab which can be downloaded from the uniprot website: https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/by_organism/

Order of execution to reproduce analysis:

1. Run fetchPfam.py, ExtractEC.py and GetCL.py to get pfam, membrane location and ec data information. You will need to use enzyme.dat to run ExtractEC.py which can be found in this repository

2. Run link_annotations.py to link am score, esm1b score, pfam ids, membrane location information and ec number to uniprot acc codes

2. Execute runvep_clinvar.sh on clinvar_vep_input.txt to get vepoutput

3. filter the output to only missense variants using filter_vep_missense.sh

4. Run extract_gene_names.R

5. Run markdown file map_clinvar_to_uniprot_with_vepout.Rmd so that clinvar is now linked to uniprot so that all of the previously mentioned annotations can be linked to ClinVar information

6. Run join_annotations_files.R to join annotations to ClinVar. To run both this and 

7. Finally run perform_analysis.Rmd to perform the entire analysis. Results can be found in results and figs directories. 
