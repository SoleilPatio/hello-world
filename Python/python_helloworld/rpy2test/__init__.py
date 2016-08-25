import math






#----------------------------------------------

import rpy2.robjects as robjects

# Importing packages
# rpy2.robjects.packages.importr()

from rpy2.robjects.packages import importr
# import R's "base" package
base = importr('base')

# import R's "utils" package
utils = importr('utils')

# # import rpy2's package module
# import rpy2.robjects.packages as rpackages
# # select a mirror for R packages
# utils.chooseCRANmirror(ind=1) # select the first mirror in the list
# 
# 
# print( rpackages.isinstalled('ggplot2') )
# print( rpackages.isinstalled('hexbin') )
# 
# # R vector of strings
# from rpy2.robjects.vectors import StrVector
# utils.install_packages(StrVector(['ggplot2']))


#get r object
rpi = robjects.r["pi"]
print("R pi = %.20f" % rpi[0])
print("Python pi = %.20f" % math.pi)


robjects.r('''
        # create a function `f`
        plot(sin,-10,10)
        ''')

input("ENTER")
