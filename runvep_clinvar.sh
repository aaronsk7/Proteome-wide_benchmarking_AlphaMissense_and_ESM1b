#!/bin/bash

# runvep_observed.sh
# A. Kovacs

# Run VEP


    ~/ensembl-vep/vep --cache \
        --tab \
        --species homo_sapiens \
        --assembly GRCh38 \
        --fasta ~/.vep/homo_sapiens/110_GRCh38/Homo_sapiens.GRCh38.dna.toplevel.fa.gz \
	--use_transcript_ref \
	--numbers \
        --fork 4 \
        --buffer_size 60000 \
        -i "clinvar_vep_input.txt" \
        -o "clinvar_vep_output.txt"


