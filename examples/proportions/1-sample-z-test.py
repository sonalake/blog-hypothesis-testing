from statsmodels.stats.proportion import proportions_ztest

# can we assume anything from our sample
significance = 0.05

# our sample - 82% are good
sample_success = 410
sample_size = 500

# our Ho is  80%
null_hypothesis = 0.80

# check our sample against Ho for Ha > Ho
# for Ha < Ho use alternative='smaller'
# for Ha != Ho use alternative='two-sided'
stat, p_value = proportions_ztest(count=sample_success, nobs=sample_size, value=null_hypothesis, alternative='larger')

# report
print('z_stat: %0.3f, p_value: %0.3f' % (stat, p_value))

if p_value > significance:
    print("Fail to reject the null hypothesis - we have nothing else to say")
else:
    print("Reject the null hypothesis - suggest the alternative hypothesis is true")
