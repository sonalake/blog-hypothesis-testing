from scipy.stats import chisquare

# can we assume anything from our sample
significance = 0.05

# what do we expect to see in proportions?
expected_proportions = [.05, .1, .15, .7]

# what counts did we see in our sample?
observed_counts = [27, 73, 82, 468]

########################
# how big was our sample
sample_size = sum(observed_counts)

# we derive our comparison counts here for  our expected proportions, based on the sample size
expected_counts = [float(sample_size) * x for x in expected_proportions]

# Get the stat data
(chi_stat, p_value) = chisquare(observed_counts, expected_counts)

# report
print('chi_stat: %0.5f, p_value: %0.5f' % (chi_stat, p_value))

if p_value > significance:
    print("Fail to reject the null hypothesis - we have nothing else to say")
else:
    print("Reject the null hypothesis - suggest the alternative hypothesis is true")
