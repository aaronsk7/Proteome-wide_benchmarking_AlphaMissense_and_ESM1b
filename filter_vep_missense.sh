# filter_vep_observed.sh
# A. Kovacs

# Filter the vep observed files to syn
# and mis variants only


INPATH="/home/akovacs/alphamissense_analysis"
OUTPATH="/home/akovacs/alphamissense_analysis"

    grep -E 'missense' \
     "${INPATH}/clinvar_vep_output.txt" > \
     "${OUTPATH}/clinvar_vep_output_missense.txt"

