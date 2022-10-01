## Testing SQL in R

## install.packages(c("DBI", "dplyr", "dbplyr", "RMySQL"))

install.packages("RMySQL")

library(DBI)

## Connect using con
con <- dbConnect(RMySQL::MySQL(),
                dbname = "mydatabase",
                host = "localhost",
                port = "portnumber",
                user = Sys.getenv("userid"),
                password = Sys.getenv("pwd")
            )

tables <- dbListTables(con)
str(tables)

## "userid" and "pwd" can be set in .Renviron in $HOME directory