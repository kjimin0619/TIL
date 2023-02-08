#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.metrics import *

# In[2]:


def get_clf_eval(y_test, pred=None, pred_proba=None):
    confusion = confusion_matrix( y_test, pred) # 혼돈행렬
    accuracy = accuracy_score(y_test , pred) # 정확도
    precision = precision_score(y_test , pred) # 정밀도
    recall = recall_score(y_test , pred) # 재현율
    # f1 스코어 추가
    f1 = f1_score(y_test,pred)
    # ROC-AUC 추가 
    roc_auc = roc_auc_score(y_test, pred_proba)
    print('오차 행렬')
    print(confusion)
    # ROC-AUC print 추가
    print('정확도: {0:.4f}, 정밀도: {1:.4f}, 재현율: {2:.4f},          F1: {3:.4f}, AUC:{4:.4f}'.format(accuracy, precision, recall, f1, roc_auc))

# 정밀도 재현율 시각화
def precision_recall_curve_plot(y_test, pred_proba_c1):
    precisions, recalls, thresholds = precision_recall_curve(y_test, pred_proba_c1)
    
    plt.figure(figsize = (8,6))
    threshold_boundry = thresholds.shape[0]
    plt.plot(thresholds, precisions[0:threshold_boundry], linestyle='--',label='precision')
    plt.plot(thresholds, recalls[0:threshold_boundry],label='recall')
    
    start, end = plt.xlim()
    plt.xticks(np.round(np.arange(start, end, 0.1),2))
    plt.xlabel('Threshold value'); plt.ylabel('Precision and Recall value')
    plt.legend(); plt.grid()
    plt.show()