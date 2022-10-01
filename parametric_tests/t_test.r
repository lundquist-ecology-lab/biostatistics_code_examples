# One sample t assuming a population mean of 15
data <- c(13, 14, 13, 12, 14, 15, 16, 13, 14, 12)

t.test(data, mu = 15)

# Two sample t
group1 <- c(14, 12, 13, 12, 15, 12, 15, 15, 12, 13)
group2 <- c(12, 15, 14, 12, 13, 13, 14, 13, 12, 12)

# Test equal variances
var.test(group1, group2)

# If variances are equal (Student's t-test)
t.test(group1, group2, var.equal = TRUE)

# If variances are not equal (Welch's t-test)
t.test(group1, group2) # This is the default in R
