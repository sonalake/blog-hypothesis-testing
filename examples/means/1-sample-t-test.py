from scipy.stats import truncnorm
from statsmodels.stats.weightstats import ttest_ind

# can we assume anything from our sample?
significance = 0.025

# we're checking if calls can be resolved in over 2 minutes
# so Ho == 120 seconds
null_hypothesis = 120

# Normally, in the real world, you would process a real sample
# But for this test, we'll generate a sample from this shape, where:
# - min/max is the range of available options
# - sample mean/dev are used to define the normal distribution
# - size is how large the sample will be
min, max = (0, 300)
sample_mean_v1, sample_dev_v1, sample_size_v1 = (121, 56, 500)
sample_mean_v2, sample_dev_v2, sample_size_v2 = (125, 16, 500)

########################
# here - for our test - we're generating a random string of durations to be our sample
# these are in a normal distribution between min/max, normalised around the mean
sample_v1 = truncnorm(
    (min - sample_mean_v1) / sample_dev_v1,
    (max - sample_mean_v1) / sample_dev_v1,
    loc=sample_mean_v1,
    scale=sample_dev_v1).rvs(sample_size_v1)

sample_v2 = truncnorm(
    (min - sample_mean_v2) / sample_dev_v2,
    (max - sample_mean_v2) / sample_dev_v2,
    loc=sample_mean_v2,
    scale=sample_dev_v2).rvs(sample_size_v2)

# Get the stat data
# note that we're comparing V2 to V1 - so the sample we expect to be larger goes first here
(t_stat, p_value, degree_of_freedom) = ttest_ind(sample_v2, sample_v1, alternative='larger')

# report
print('t_stat: %0.3f, p_value: %0.3f' % (t_stat, p_value))

if p_value > significance:
    print("Fail to reject the null hypothesis - we have nothing else to say")
else:
    print("Reject the null hypothesis - suggest the alternative hypothesis is true")
