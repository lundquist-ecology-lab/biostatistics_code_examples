df <- read.csv("example_data/iris.csv", stringsAsFactors = TRUE)

# Box plots
boxplot(Petal.Width ~ Species, data = df)

# Strip plot
library(lattice)
stripplot(Petal.Width ~ Species, data = df, jitter = TRUE)

# ANOVA
model <- lm(Petal.Width ~ Species, data = df)
summary(aov(model))
# OR
anova(model)

# Tukey HSD
TukeyHSD(aov(model))

# Check assumptions
par(mfrow = c(2, 2))
plot(model) ## QQ plots and others

# Shapiro-Wilk test for normality
shapiro.test(df$Petal.Width)

# Bartlett test for homogenety of variances
bartlett.test(Petal.Width ~ Species, data = df)

# Levene's test for homogeneity of variances
library(car)
leveneTest(Petal.Width ~ Species, data = df)