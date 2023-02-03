# import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp

# load data
heart = pd.read_csv('heart_disease.csv')
print(heart.head())

yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']
print(np.mean(heart.chol))
chol_hd = yes_hd.chol
#print(chol_hd)
mean = np.mean(chol_hd)
#print(mean)
tstat,pval=ttest_1samp(yes_hd.chol,mean)
#print(pval)
from scipy.stats import ttest_1samp
tstat, pval = ttest_1samp(chol_hd, 240)
#print(pval/2)
chol_hd2=no_hd['chol']
mean2 = np.mean(chol_hd2)
tstat,pval = ttest_1samp(chol_hd2,240)
#print(pval/2)

#print(heart.describe())
num_patients=len(heart)
print(num_patients)
num_highfbs_patients = np.sum(heart.fbs[heart.fbs == 1])
#print(num_highfbs_patients)
print(0.08 *303) 
from scipy.stats import binom_test
pval = binom_test(num_highfbs_patients, num_patients, .08, alternative='greater')
print(pval)



