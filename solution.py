# import libraries
import codecademylib3
import pandas as pd
import numpy as np

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

# get cholesterol levels for patients with heart disease
chol_hd = yes_hd.chol

# calculate mean cholesterol level for patients with hd
print(np.mean(chol_hd))

# compare to cut-off for high cholesterol
from scipy.stats import ttest_1samp
tstat, pval = ttest_1samp(chol_hd, 240)
print(pval/2)

# get cholesterol levels for patients without heart disease
chol_no_hd = no_hd.chol

# calculate mean cholesterol level for patients w/o hd
print(np.mean(chol_no_hd))

# compare to cut-off for high cholesterol
from scipy.stats import ttest_1samp
tstat, pval = ttest_1samp(chol_no_hd, 240)
print(pval/2)

# calculate number of patients total
num_patients = len(heart)
print(num_patients)

# calculate number of patients with fbs>120
num_highfbs_patients = np.sum(heart.fbs)
print(num_highfbs_patients)

# calculate 8% of sample size
print(0.08*num_patients)

# run binomial test
from scipy.stats import binom_test
pval = binom_test(num_highfbs_patients, num_patients, .08, alternative='greater')
print(pval)