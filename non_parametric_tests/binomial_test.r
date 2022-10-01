# Six-sided die flipped 24 times and lands on three exactly 6 times
binom.test(x = 6, n = 24, p = 1/6, alternative = "greater")

# Flip coin 30 times and it lands on heads exactly 19 times
binom.test(x = 19, n = 30, p = 1/2, alternative = "greater")
