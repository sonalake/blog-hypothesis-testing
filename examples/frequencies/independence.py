from scipy.stats import chi2_contingency
import numpy as np

# can we assume anything from our sample
significance = 0.05

pivot = np.array([
    # town votes
    [200, 150, 50],
    # country votes
    [250, 300, 50]
])
########################
# Get the stat data
(chi_stat, p_value, degrees_of_freedom, expected) = chi2_contingency(pivot)

# report
print('chi_stat: %0.5f, p_value: %0.5f' % (chi_stat, p_value))

if p_value > significance:
    print("Fail to reject the null hypothesis - we have nothing else to say")
else:
    print("Reject the null hypothesis - suggest the alternative hypothesis is true")
