# Utility function to get all the variable names separated by a ' + '
variables <- colnames(stores)[1]
for(i in 2:length(colnames(stores))){
    variables <- paste(variables, ' + ', colnames(stores)[i])
}
