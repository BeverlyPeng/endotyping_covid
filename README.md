
# Machine Learning Analysis of Clinical Questionnaires Identifies Clusters, Severity Groups, and Trajectories of Post-Acute COVID Symptoms

Preprint: Peng et al. 2025 [https://www.biorxiv.org/content/10.1101/2025.04.10.648034v1](https://www.biorxiv.org/content/10.1101/2025.04.10.648034v1).

## Steps to run analysis

### ETL each cohort's symptom surveys. 

`data_qc/data_qc_{cohort}.ipynb`

### Run topic modeling. 

`Subphenotyping-for-PASC/Python code for training topic modeling/Main_train_topic_model.py`

- code from: Zhang, H., Zang, C., Xu, Z. et al. Data-driven identification of post-acute SARS-CoV-2 infection subphenotypes. Nat Med 29, 226–235 (2023). https://doi.org/10.1038/s41591-022-02116-3

- [Github link](https://github.com/HaoZhangXidian/Subphenotyping-for-PASC)

### Calculate optimal number of topics.

`get_num_topics.ipynb`

### Calculate optimal clustering method and number of clusters.

`get_n_clusters.ipynb`

### Interpret topic modeling results.

`{cohort}/results_*.ipynb`

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
