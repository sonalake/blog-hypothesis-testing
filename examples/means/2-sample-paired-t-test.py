from scipy.stats import truncnorm
from statsmodels.stats.weightstats import DescrStatsW as stats

# can we assume anything from our sample?
significance = 0.05

# we're checking if calls can be resolved in over 2 minutes
# so Ho == 120 seconds
null_hypothesis = 120

# Normally, in the real world, you would process an actual sample
# But for this test, we'll generate a random sample, where:
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
# note that this is, in effect, a sample t-test on the differences
# we want to see if v2 is slower than V1 so we get the differences and check the probability that they
# are larger than the null hypothesis here (of the default = 0.0)
(t_stat, p_value, degree_of_freedom) = stats(sample_v2 - sample_v1).ttest_mean(alternative='larger')

# report
print('t_stat: %0.5f, p_value: %0.5f' % (t_stat, p_value))

if p_value > significance:
    print("Fail to reject the null hypothesis - we have nothing else to say")
else:
    print("Reject the null hypothesis - suggest the alternative hypothesis is true")
