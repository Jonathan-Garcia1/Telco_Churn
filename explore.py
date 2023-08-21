import numpy as np
import pandas as pd

from pydataset import data
from scipy import stats

def chi2_internet_service(df):

    ct = pd.crosstab(df.churn, df.internet_service)
    
    chi2, p, dof, expected = stats.chi2_contingency(ct)
    
    print("Chi-Squared Value:", chi2)
    print("P-value:", format(p, '.4f'))
    
def chi2_internet_service_type(df):

    ct = pd.crosstab(df.churn, df.internet_service_type)
    
    chi2, p, dof, expected = stats.chi2_contingency(ct)
    
    print("Chi-Squared Value:", chi2)
    print("P-value:", format(p, '.4f'))
    
def chi2_payment_method(df):

    ct = pd.crosstab(df.churn, df.payment_method)

    chi2, p, dof, expected = stats.chi2_contingency(ct)

    print("Chi-Squared Value:", chi2)
    print("P-value:", format(p, '.4f'))

    if p < 0.05:
        print("There is a significant association between payment method and churn.")
    else:
        print("There is no significant association between payment method and churn.")


def ttest_churn_vs_tenure(df):
    churned_tenure = df[df['churn'] == 'Yes']['tenure']
    non_churned_tenure = df[df['churn'] == 'No']['tenure']

    t_statistic, p_value = stats.ttest_ind(churned_tenure, non_churned_tenure)

    print("T-Statistic:", t_statistic)
    print("P-Value:", format(p_value, '.4f'))
    print()

    if p_value < 0.05:
        print("There is a significant relationship between tenure and churn.")
    else:
        print("There is no significant relationship between tenure and churn.")

def ttest_monthly_charges(df):
    churned_charges = df[df['churn'] == 'Yes']['monthly_charges']
    non_churned_charges = df[df['churn'] == 'No']['monthly_charges']

    # Perform one-tailed t-test
    t_statistic, p_value = stats.ttest_ind(churned_charges, non_churned_charges, alternative='greater')

    print("One-tailed t-test results:")
    print(f"T-statistic: {t_statistic}")
    print(f"P-value: {p_value}")

    if p_value < 0.05:
        print("There is a significant relationship between monthly charges and churn.")
    else:
        print("There is no significant relationship between monthly charges and churn.")
        
        
