
# Machine Learning Analysis of Clinical Questionnaires Identifies Clusters, Severity Groups, and Trajectories of Post-Acute COVID Symptoms

Preprint: Peng et al. 2025 [https://www.biorxiv.org/content/10.1101/2025.04.10.648034v1](https://www.biorxiv.org/content/10.1101/2025.04.10.648034v1).

| Folder Name | Description |
|----------|----------|
| cardiff_n317 | Cardiff cohort, n = 317: a case-control study of Long COVID | 
| sinai_emory_n675 | Sinai+Emory cohort, n = 675: combined Sinai and Emory (long COVID with MENSA assay data) 
| sinai_n615 | Sinai cohort, n = 615: walk-in clinic, preconditions provided | 
| ucsf_n222 | UCSF cohort subset, n = 222 | 
| ucsf_n669 | UCSF cohort, n = 669: longitudinal with balanced demographics | 

## Steps to run analysis

### Step 1: Processing each cohort's symptom surveys. 

`data_qc/data_qc_{cohort}.ipynb`

Ex. `data_qc/data_qc_ucsf.ipynb`

See data dictionary mapping symptoms across cohorts and organ systems in Supplementary Materials.xlsx Table 1.

### Step 2: Run topic modeling. 

`Subphenotyping-for-PASC/Python code for training topic modeling/Main_train_topic_model.py`

- Original code from: Zhang, H., Zang, C., Xu, Z. et al. Data-driven identification of post-acute SARS-CoV-2 infection subphenotypes. Nat Med 29, 226–235 (2023). https://doi.org/10.1038/s41591-022-02116-3

- Changed input dataset

- Iterated through 2-80 topics 10 times. 

### Step 3: Calculate optimal number of topics.

`get_num_topics.ipynb`

### Step 4: Calculate optimal clustering method and number of clusters.

`get_n_clusters.ipynb`

### Step 5: Interpret topic modeling results.

`{cohort}/results_*.ipynb`

Ex. ucsf_n669/results_ucsf_n669_22topics_15clusters_model.ipynb

See results in Supplementary Materials.xlsx Tables 2-5 (including cluster assignment, severity group, top 6 signature symptoms, top 3 organ systems).

```bash
├── Subphenotyping-for-PASC
│   ├── Python code for trianing topic modeling
│   │   ├── pydpm
│   │   ├── Main_train_topic_model.py
│   │   └── run.sh
├── cardiff_n317
│   └── similar structure as ucsf_n669
├── data_qc
├── legends
├── meta_analysis
├── sinai_emory_n675
│   └── similar structure as ucsf_n669
├── sinai_n615
│   └── similar structure as ucsf_n669
├── ucsf_n222
│   └── similar structure as ucsf_n669
├── ucsf_n669
│   ├── comorb
│   │   ├── proportion_auto.svg
│   │   ├── proportion_cancer.svg
│   │   └── ...
│   ├── individual
│   │   ├── individual_cluster1.svg
│   │   ├── individual_cluster2.svg
│   │   └── ...
│   ├── median
│   │   ├── median_cluster1.svg
│   │   ├── median_cluster2.svg
│   │   └── ...
│   ├── cluster_assignments_ucsf_n669_22topics_15clusters.csv
│   ├── cluster_by_symptom_col.png
│   ├── cluster_by_symptom_row.png
│   ├── clusters_minibatch_15.csv
│   ├── comorb_proportions_ucsf_n669.csv
│   ├── embedding.npy
│   ├── endotypes.png
│   ├── eq5d_cluster.svg
│   ├── eq5d_endotype.svg
│   ├── eq5d_severity_1st_2nd.svg
│   ├── eq5d_severity_mild_mod_severe.svg
│   ├── likelihood_avg_n669.svg
│   ├── likelihood_individual_n286.svg
│   ├── likelihood_individual_n669.svg
│   ├── pie_cluster_eq5d.svg
│   ├── pie_endotype_eq5d.svg
│   ├── proportion_sex.svg
│   ├── raw_surveys_ucsf_n669.csv
│   ├── results_ucsf_n669_22topics_15clusters_model.ipynb
│   ├── severity_curve.svg
│   ├── survey_bins.svg
│   ├── symptoms.png
│   ├── symptoms_over_time_decreasing.svg
│   ├── symptoms_over_time_increasing.svg
│   ├── symptoms_over_time_mountain.svg
│   ├── top3organs.csv
│   ├── top6symptoms.csv
│   ├── topic_coherence_avg_n669.svg
│   ├── topic_coherence_individual_n286.svg
│   ├── topic_coherence_individual_n669.svg
│   ├── UCSF_EQ5D_correlation_ML-severity.svg
│   ├── umap.svg
│   ├── umap_0to30.svg
│   ├── umap_31to90.svg
│   └── umap_90after.svg
├── LICENSE.txt
├── README.md
├── Supplementary Materials.xlsx
├── get_n_clusters.ipynb
├── get_num_topics.ipynb
├── organ_system_mapping.png
└── workflow.png
```

```
📦endotyping_covid
 ┗ 📂folder
   ┗📂folder
    ┣📂file
    ┣📂file
    ┣📂file
    ┗📂file
```

### Step 6: Run meta-analysis on all patients across 4 cohorts. 

`meta_analysis/results_meta.ipynb`

<img src="workflow.png" height="600">

## Cohorts

UCSF (N = 669): University of California, San Francisco, CA, USA

ISMMS (N = 615): Icahn School of Medicine at Mount Sinai, New York, NY, USA

Emory (N = 60): Emory University, Atlanta, GA, USA

- combined with ISMSS leads to results in sinai_emory_n675

* combined with ISMSS leads to results in sinai_emory_n675

Cardiff (N = 317): University Hospital of Wales, Cardiff, UK

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

* PolyBio Research Foundation (Balvi B43)
* Steven & Alexandra Cohen Foundation
* U.S. National Institues of Health (NIH) (K23AI157875, R01AI141003, 1R01NS136197, R01AI184931, P01AI168347, U01AI187057, P01AI125180-05S1, R01AI172254, P01AI078907, U01AI045969, U19AI109962, U54CA260563, T32HL116271, 5T32AI074492)
* NIH RECOVER (1OT2HL156812-01)
* UK National Institute for Health and Care Research (COV-LT2-0041)
* Intramural Research Program of the NIH
