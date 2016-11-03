# Before launching regression: Get all the columns names separated by a ' + '

variables <- colnames(table)[1]
for(i in 2:length(colnames(table))){
    variables <- paste(variables, ' + ', colnames(table)[i])
}
