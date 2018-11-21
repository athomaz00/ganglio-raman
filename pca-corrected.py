import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np



#TC = "Média das triplicatas TC - 2º set.xlsx"
#NAIVE = "Média dos espectros NAIVE.xlsx"
#NAIVEL = "Média triplicatas NAIVE+L.xlsx"
#STZ = "Média espectros STZ.xlsx"
#STZL = "Média espectros STZL.xlsx"
#TCL = "Média triplicatas TCL - 2º SET.xlsx"

TC = "output TC1A.xlsx"
NAIVE = "output NAIVE1A.xlsx"
NAIVEL = "output NL1A.xlsx"
STZ = "output STZ1A.xlsx"
STZL = "output STZL1A.xlsx"
TCL = "output TCL1A.xlsx"


specs = "PCA_Raman.xlsx"


dfTC = pd.read_excel(specs)




#TC_x = dfTC.loc[:,'cm-1':'int']





x_TC = dfTC.loc[:, 'cm-1':'int'].values
x_TC = StandardScaler().fit_transform(x_TC)




pca_TC = PCA(n_components=2)
principalComponents_TC = pca_TC.fit_transform(x_TC)
principalDf_TC = pd.DataFrame(data = principalComponents_TC
             , columns = ['principal component 1', 'principal component 2'])






dfNAIVE = pd.read_excel(NAIVE)









x_NAIVE = dfNAIVE.loc[:,'cm-1':'int'].values
x_NAIVE = StandardScaler().fit_transform(x_NAIVE)
pca_NAIVE = PCA(n_components=2)
principalComponents_NAIVE = pca_NAIVE.fit_transform(x_NAIVE)




dfNAIVEL = pd.read_excel(NAIVEL)









x_NAIVEL = dfNAIVEL.loc[:,'cm-1':'int'].values
x_NAIVEL = StandardScaler().fit_transform(x_NAIVEL)
pca_NAIVEL = PCA(n_components=2)
principalComponents_NAIVEL = pca_NAIVEL.fit_transform(x_NAIVEL)




dfSTZ = pd.read_excel(STZ)





x_STZ= dfSTZ.loc[:,'cm-1':'int'].values
x_STZ = StandardScaler().fit_transform(x_STZ)
pca_STZ = PCA(n_components=2)
principalComponents_STZ = pca_STZ.fit_transform(x_STZ)


dfSTZL = pd.read_excel(STZL)







x_STZL = dfSTZL.loc[:,'cm-1':'int'].values
x_STZL = StandardScaler().fit_transform(x_STZL)
pca_STZL = PCA(n_components=2)
principalComponents_STZL = pca_STZL.fit_transform(x_STZL)

dfTCL = pd.read_excel(TCL)






x_TCL = dfTCL.loc[:,'cm-1':'int'].values
x_TCL = StandardScaler().fit_transform(x_TCL)
pca_TCL = PCA(n_components=2)
principalComponents_TCL = pca_TCL.fit_transform(x_TCL)


plt.figure()
plt.scatter(pca_NAIVE.explained_variance_ratio_[0], pca_NAIVE.explained_variance_ratio_[1], label='NAIVE')
plt.scatter(pca_NAIVEL.explained_variance_ratio_[0], pca_NAIVEL.explained_variance_ratio_[1], label='NAIVEL')
plt.scatter(pca_TC.explained_variance_ratio_[0], pca_TC.explained_variance_ratio_[1], label='TC')
plt.scatter(pca_TCL.explained_variance_ratio_[0], pca_TCL.explained_variance_ratio_[1], label='TCL')
#plt.scatter(dfNAIVE['cm-1'], principalComponents_NAIVE[:,1])

#plt.scatter(dfTC['subtraído 8cm-1'], principalComponents_TC[:,1])
plt.scatter(pca_STZ.explained_variance_ratio_[0], pca_STZ.explained_variance_ratio_[1], label='STZ')
plt.scatter(pca_STZL.explained_variance_ratio_[0], pca_STZL.explained_variance_ratio_[1], label='STZL')

plt.legend()


plt.figure()
plt.scatter(np.max(principalComponents_NAIVE[:,0]), np.max(principalComponents_NAIVE[:,1]), label='NAIVE')
plt.scatter(np.max(principalComponents_NAIVEL[:,0]), np.max(principalComponents_NAIVEL[:,1]), label='NAIVEl')
plt.scatter(np.max(principalComponents_TC[:,0]), np.max(principalComponents_TC[:,1]), label='TC')
#plt.scatter(dfNAIVE['cm-1'], principalComponents_NAIVE[:,1])
plt.scatter(np.max(principalComponents_TCL[:, 0]), np.max(principalComponents_TCL[:, 1]), label='TCL')
#plt.scatter(dfTC['subtraído 8cm-1'], principalComponents_TC[:,1])
plt.scatter(np.max(principalComponents_STZ[:, 0]), np.max(principalComponents_STZ[:,1]), label='STZ')
plt.scatter(np.max(principalComponents_STZL[:, 0]), np.max(principalComponents_STZL[:, 1]), label='STZL')

plt.legend()
#
#
plt.figure()
plt.scatter(dfNAIVE['cm-1'], principalComponents_NAIVE[:,0], label='NAIVE')
plt.scatter(dfNAIVEL['cm-1'], principalComponents_NAIVEL[:,0], label='NAIVEl')
plt.scatter(dfTC['cm-1'], principalComponents_TC[:,0], label='TC')
plt.scatter(dfTCL['cm-1'], principalComponents_TCL[:, 0], label='TCL')
plt.scatter(dfSTZ['cm-1'], principalComponents_STZ[:,0], label='STZ')
plt.scatter(dfSTZL['cm-1'], principalComponents_STZL[:, 0], label='STZL')
plt.legend()
#
#
pc1 = [principalComponents_NAIVE[:,0][i]+principalComponents_STZ[:,0][i]+principalComponents_STZL[:,0][i] 
        + principalComponents_TCL[:,0][i]for i in range(1210)]

plt.figure()
plt.scatter(dfNAIVE['cm-1'], pc1)

pc2 = [principalComponents_NAIVE[:,1][i]+principalComponents_STZ[:,1][i]+principalComponents_STZL[:,1][i] 
        + principalComponents_TCL[:,1][i]for i in range(1210)]

plt.figure()
plt.scatter(dfNAIVE['cm-1'], pc2)
#
#
#
plt.figure()
plt.scatter(dfNAIVE['cm-1'], principalComponents_NAIVE[:,1], label='NAIVE')
plt.scatter(dfNAIVEL['cm-1'], principalComponents_NAIVEL[:,1], label='NAIVEl')
plt.scatter(dfTC['cm-1'], principalComponents_TC[:,1], label='TC')
plt.scatter(dfTCL['cm-1'], principalComponents_TCL[:, 1], label='TCL')
#plt.scatter(dfNAIVE['cm-1'], principalComponents_NAIVE[:,1])

#plt.scatter(dfTC['subtraído 8cm-1'], principalComponents_TC[:,1])
plt.scatter(dfSTZ['cm-1'], principalComponents_STZ[:,1], label='STZ')
plt.scatter(dfSTZL['cm-1'], principalComponents_STZL[:, 1], label='STZL')
plt.legend()
