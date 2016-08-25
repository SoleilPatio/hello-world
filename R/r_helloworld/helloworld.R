# TODO: Add comment
# 
# Author: clouds
###############################################################################

data <- read.csv("D:\\Users\\clouds\\Desktop\\test.csv")
data
ss<-subset( data, ¾Ç¦n == 11)
print(ss)
x<-rexp(100)
y<-rnorm(1000)
par(mfrow=c(2,3))
#hist(x)
#curve(100*dnorm(x),add=T,col="red")
plot(as.integer(ss),col="red")
#qqnorm(x)
#qqline(x)
#curve(100*dnorm(x),add=T,col="blue")
#acf(x)