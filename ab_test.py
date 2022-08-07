# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 10:39:47 2022

@author: user
"""


# 최소 샘플 사이즈 확인 

import statsmodels.api as sm
import pandas as pd
from scipy.stats import chi2_contingency

# =============================================================================
# 유의성 검증을 위한 최소한의 표본 크기
# =============================================================================

def get_least_sample_size(p1, p2, alpha, power): # 실험군 전환율, 대조군 전환율, 유의수준, 검정력
    effect_size = sm.stats.proportion_effectsize(p1, p2)
    analysis = sm.stats.TTestIndPower()
    result = analysis.solve_power(effect_size=effect_size,
                                  alpha=alpha, power=power, alternative='larger')
    print("검정력 {power}, 유의수준 {alpha} 에서 두 집단의 유의성 검정을 위한 최소 샘플 사이즈는 : {result}개 입니다".format(
        power=power, alpha=alpha, result=result))
    


def ab_test_chi(a_pos, total_a, b_pos, total_b): # 실험군 전환 수, 실험군 표본크기, 대조군 전환 수, 대조군 표본크기
    positive= [a_pos, b_pos]
    negative = [total_a- a_pos, total_b - b_pos]
    chi2, p, d_f, expected = chi2_contingency([positive, negative])
    print('카이제곱 통계량:', format(chi2, '.3f'))
    print('p-value: ', format(p, '.3f'))
    
    if p <= 0.05:
        print("A와 B 그룹의 차이는 유의미합니다")
    else: print("A와 B의 차이는 유의미한 차이가 아닙니다")




