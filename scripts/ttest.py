import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity as cos
from scipy import stats


tokens1 = np.zeros((5, 1280))
tokens2 = np.zeros((5, 1280))
tokens3 = np.zeros((5, 1280))

token_sim1 = np.zeros(25)
token_sim2 = np.zeros(25)


for i in range(5):
    token1 = np.load("../outputs/tokens/va__" + str(i) + ".npy")
    token_mean1 = np.mean(token1, axis=0).reshape(1,-1)
    tokens1[i,:] = token_mean1

    token2 = np.load("../outputs/tokens/constable__" + str(i) + ".npy")
    token_mean2 = np.mean(token2, axis=0).reshape(1,-1)
    tokens2[i,:] =  token_mean2
    
    token3 = np.load("../outputs/tokens/va__" + str(i) + ".npy")
    token_mean3 = np.mean(token3, axis=0).reshape(1,-1)
    tokens3[i,:] =  token_mean3

n = 0
for token1 in tokens1:
    for token2 in tokens2:    
        token_sim1[n] = cos(token1.reshape(1,-1), token2.reshape(1,-1))
        n += 1

m = 0
for token1 in tokens1:
    for token3 in tokens3:    
        token_sim2[m] = cos(token1.reshape(1,-1), token3.reshape(1,-1))
        m += 1


print(token_sim1)
print(np.mean(token_sim1))
print(np.mean(token_sim2))
print(np.std(token_sim1))

stat, pval = stats.ttest_ind(token_sim1, token_sim2, equal_var=False)

print(stat) # t-statistic = -1.3466880839479145
print(pval) # p-value = 0.1796437807913805





#################### Entire Images ######################

# images (constable-lionel, constable-valenciennes)
# t-statistic = 3.8956330323592088
# p-value = 0.00035514124078366623

# images (constable-constable, constable-valenciennes)
# t-statistic = 6.64540617839588
# p-value = 1.4515943320644916e-07

# images (valenciennes-valenciennes, constable-valenciennes)
# t-statistic = -14.900780735569638
# p-value = 1.5732859370314718e-19

# images (constable-constable, constable-lionel)
# t-statistic = 3.3552582810550686
# p-value = 0.0016750030168162999

# images (lionel-lionel, constable-lionel)
# t-statistic = -11.770151783499507
# p-value = 9.368822359293797e-13









#################### Gray Sky Images ######################

# sky images (constable-lionel, constable-valenciennes)
# t-statistic = -4.370225400435966
# p-value = 0.00012049956338692179

# sky images (constable-constable, constable-valenciennes)
# t-statistic = 6.697453028984675
# p-value = 2.5699725177758415e-07

# sky images (valenciennes-valenciennes, constable-valenciennes)
# t-statistic = -14.445496209374216
# p-value = 2.3170879468867697e-16

# sky images (constable-constable, constable-lionel)
# t-statistic = 8.461603847547272
# p-value = 8.692209890301477e-11

# sky images (lionel-lionel, constable-lionel)
# t-statistic = -7.625480398861246
# p-value = 2.061509247942312e-09

#################### Sky Images ######################

# sky images (constable-lionel, constable-valenciennes)
# t-statistic = -1.3466880839479145
# p-value = 0.1796437807913805

# sky images (constable-constable, constable-valenciennes)
# t-statistic = 11.403320710678114
# p-value = 1.7609310077522645e-23

# sky images (valenciennes-valenciennes, constable-valenciennes)
# t-statistic = -11.032811714261365
# p-value = 2.412445378751111e-22

# sky images (constable-constable, constable-lionel)
# t-statistic = 13.461210548070426
# p-value = 1.1442919949383959e-29

# sky images (lionel-lionel, constable-lionel)
# t-statistic = -13.011434207490906
# p-value = 5.30569665169081e-28