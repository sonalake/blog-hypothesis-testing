from scipy.stats import chisquare

# can we assume anything from our sample
significance = 0.05

# what counts did we see in our samples?
observed_counts_A = [32, 65, 97, 450]
observed_counts_B = [27, 73, 82, 468]

########################

# Get the stat data
(chi_stat, p_value) = chisquare(observed_counts_A, observed_counts_B)

# report
print('chi_stat: %0.5f, p_value: %0.5f' % (chi_stat, p_value))

if p_value > significance:
    print("Fail to reject the null hypothesis - we have nothing else to say")
else:
    print("Reject the null hypothesis - suggest the alternative hypothesis is true")
