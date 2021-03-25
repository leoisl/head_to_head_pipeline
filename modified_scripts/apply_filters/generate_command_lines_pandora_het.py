# configs
het_filters = [0.1, 0.3, 0.5, 0.7,  0.9]
technology = "nanopore"

for het_filter in het_filters:
    print(f"mkdir -p /hps/nobackup/iqbal/leandro/pandora_versions/pandora_workflow/het_filter_{het_filter}/{technology}/100x/random/compare_withdenovo_global_genotyping/")
    print(f"python apply_filters.py -i /hps/nobackup/iqbal/leandro/pandora_versions/precompiled_binaries/{technology}/pandora_compare_out_20_way_{technology}/pandora_multisample_genotyped.vcf "
          f"-o /hps/nobackup/iqbal/leandro/pandora_versions/pandora_workflow/het_filter_{het_filter}/{technology}/100x/random/compare_withdenovo_global_genotyping/pandora_multisample_genotyped_global.vcf "
          f"--min-frs {het_filter}")
    print(f"cp /hps/nobackup/iqbal/leandro/pandora_versions/precompiled_binaries/{technology}/pandora_compare_out_20_way_{technology}/pandora_multisample.vcf_ref.fa "
          f"/hps/nobackup/iqbal/leandro/pandora_versions/pandora_workflow/het_filter_{het_filter}/{technology}/100x/random/compare_withdenovo_global_genotyping/pandora_multisample.vcf_ref.fa")
    print(f"sed 's/pandora_output_pandora_paper_tag1/het_filter_{het_filter}/g' "
          f"/hps/nobackup/iqbal/leandro/pandora_versions/pandora_paper_roc/metadata/variant_calls_pandora_paper_tag1.{technology}.local_updates.csv > "
          f"/hps/nobackup/iqbal/leandro/pandora_versions/pandora_paper_roc/metadata/variant_calls_pandora_paper_tag1.{technology}.local_updates.het_filter_{het_filter}.csv")
    print(f"sed 's/variant_calls_pandora_paper_tag1.{technology}.csv/variant_calls_pandora_paper_tag1.{technology}.local_updates.het_filter_{het_filter}.csv/g' "
          f"/hps/nobackup/iqbal/leandro/pandora_versions/pandora_paper_roc/config.pandora_paper_tag1.{technology}.yaml | "
          f"sed 's/analysis_output_{technology}_pandora_paper_tag1/analysis_output_{technology}_pandora_paper_tag1_het_filter_{het_filter}/g' "
          f"> /hps/nobackup/iqbal/leandro/pandora_versions/pandora_paper_roc/config.pandora_paper_tag1.{technology}.het_filter_{het_filter}.yaml")

print("\n\n# To be run after, snakemake pipeline, one by one:")
for het_filter in het_filters:
    print(f"# bash scripts/submit_lsf.sh --configfile config.pandora_paper_tag1.{technology}.het_filter_{het_filter}.yaml "
          f"--singularity-prefix /hps/nobackup/iqbal/leandro/singularity_cache/ --until concat_all_plot_data")
