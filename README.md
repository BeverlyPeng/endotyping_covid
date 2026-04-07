# Machine Learning Analysis of Clinical Questionnaires Identifies Clusters, Severity Groups, and Trajectories of Post-Acute COVID Symptoms

Preprint: Peng et al. 2025. [https://www.biorxiv.org/content/10.1101/2025.04.10.648034v1](https://www.biorxiv.org/content/10.1101/2025.04.10.648034v1).

## Steps to run analysis

1. ETL each cohort's symptom surveys (data_qc/data_qc*.ipynb).

2. Run topic modeling (Subphenotyping-for-PASC/Python code for training topic modeling/Main_train_topic_model.py)

3. Calculate optimal number of topics (get_num_topics.ipynb).

4. Calculate optimal number of clusters and clustering method (get_n_clusters.ipynb).

5. Interpret topic modeling results (cohort_folder/results_*.ipynb). 

## Cohorts

- UCSF (N = 669): University of California, San Francisco, CA, USA

- ISMMS (N = 615): Icahn School of Medicine at Mount Sinai, New York, NY, USA

- Emory (N = 60): Emory University, Atlanta, GA, USA
  - combined with ISMSS lead to results in sinai_emory_n675

- Cardiff (N = 317): University Hospital of Wales, Cardiff, UK
