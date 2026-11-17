library(stringr)

clinvar_mapped <- fread("~/alphamissense_analysis/clinvar_mapped_to_uniprot.csv")

clinvar_mapped <- dplyr::select(clinvar_mapped, uniprot, res_pos, ref, alt, ClinicalSignificance, ReviewStatus)
clinvar_mapped <- unique(clinvar_mapped)

columnnames <- c("uniprot", "res_pos", "ref", "alt", "am_score", "esm1b_score", "V7", "V8")

files <- list.files(path = "/work/am_comparison_project/alphamissense_analysis/Aaron/Tables", pattern = "table4", full.names = TRUE)

alpha_missense_analysis_data <- data.table()

for (i in files) {
  
  table <- fread(file = i, header = FALSE)
  colnames(table) <- columnnames
  table <- merge(clinvar_mapped, table, by=c("uniprot", "res_pos", "ref", "alt"))
  alpha_missense_analysis_data <- bind_rows(alpha_missense_analysis_data, table)
  
}

alpha_missense_analysis_data$pfam_id <- sapply(strsplit(alpha_missense_analysis_data$V7,"|", fixed = TRUE), `[`, 1)
alpha_missense_analysis_data$pfam_name <- sapply(strsplit(alpha_missense_analysis_data$V7,"|", fixed = TRUE), `[`, 2)

alpha_missense_analysis_data$membrane_domain <- sapply(strsplit(alpha_missense_analysis_data$V8,"|", fixed = TRUE), `[`, 1)
alpha_missense_analysis_data$sub_mem_domain <- sapply(strsplit(alpha_missense_analysis_data$V8,"|", fixed = TRUE), `[`, 2)

alpha_missense_analysis_data <- alpha_missense_analysis_data[, -10]
alpha_missense_analysis_data <- alpha_missense_analysis_data[, -9]

fwrite(alpha_missense_analysis_data, "/work/am_comparison_project/alphamissense_analysis/pfam&membrane_mapped_to_clinvar.txt")