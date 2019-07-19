# Hello, world!
#
# This is an example function named 'hello'
# which prints 'Hello, world!'.
#
# You can learn more about package authoring with RStudio at:
#
#   http://r-pkgs.had.co.nz/
#
# Some useful keyboard shortcuts for package authoring:
#
#   Build and Reload Package:  'Cmd + Shift + B'
#   Check Package:             'Cmd + Shift + E'
#   Test Package:              'Cmd + Shift + T'

setwd('/Users/csx/GitProject/sciMallNetworkScore/sciMallNetworkRPackege/')
library(rPython)

python.load( system.file( "../test.py", package = "rPython" ) )
python.call( "test")

hello <- function() {
  print("Hello, world!")
}


