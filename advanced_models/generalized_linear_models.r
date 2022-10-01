
species_df <- read.csv("example_data/forest_butterflies/butterfly_species.csv",
    sep = ";", h = TRUE, stringsAsFactors = TRUE)
sites_df <- read.csv("example_data/forest_butterflies/butterfly_sites.csv"
    , sep = ";", h = TRUE, stringsAsFactors = TRUE)

# We need to do some data managment, species and sites are grouped by "sites_ID"
sites_ID <- sites_df$sites_ID

richness <- NULL
count <- 1

for (i in levels(sites_ID)) {
    list1 <- species_df$Species[species_df$sites_ID == i]
    richness[count] <- length(list1)
    count <- 1 + count
}

names(sites_df)

analysis_df <- data.frame(richness, sites_df[c(12, 13, 15:17)])

library(lme4)

p_model1 <- glm(richness ~  A_mean_temp + A_rainfall + Olsoneconame
            + Ribeirovegtype + BSRs, data = analysis_df, family = poisson)

summary(p_model1)
anova(p_model1, test = "Chisq")
