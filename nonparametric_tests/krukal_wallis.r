df <- read.csv("example_data/iris.csv")

kruskal.test(Petal.Width ~ Species, data = df)
