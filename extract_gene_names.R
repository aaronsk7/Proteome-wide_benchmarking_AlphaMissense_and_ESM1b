clinvar <- fread("~/alphamissense_analysis/variant_summary_07-10-2023.txt")
clinvar <- subset(clinvar, clinvar$Type == "single nucleotide variant")
clinvar <- subset(clinvar, clinvar$Assembly == "GRCh38")
clinvar <- subset(clinvar, clinvar$ClinicalSignificance == "Pathogenic" | clinvar$ClinicalSignificance == "Likely pathogenic" | clinvar$ClinicalSignificance == "Pathogenic/Likely pathogenic" | clinvar$ClinicalSignificance == "Benign" | clinvar$ClinicalSignificance == "Likely benign" | clinvar$ClinicalSignificance == "Benign/Likely benign")
clinvar <- clinvar[!grep(pattern = "=", clinvar$Name, fixed = TRUE),]
clinvar <- clinvar[grep(pattern = "(p.", clinvar$Name, fixed = TRUE),]
clinvar <- clinvar[!grep(pattern = "Ter", clinvar$Name, fixed = TRUE),]
gene_names <- as.data.table(unique(clinvar$GeneSymbol))
fwrite(gene_names, "~/alphamissense_analysis/clinvar_gene_list.csv", col.names = FALSE)