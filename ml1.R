install.packages(c("dplyr","ggplot2","caTools","corrgram"))
library(dplyr)
library(ggplot2)
library(caTools)
library(corrgram)
library(rrcov)
data(fish)
df=fish
ggplot(data=df, aes(x=Weight, y=Height)) +
geom_point(aes(color=Species, size=10, alpha=0.7))
corrgram(df, lower.panel=panel.shade, upper.panel=panel.cor)
sampleSplit <- sample.split(Y=df$Weight, SplitRatio=0.7)
trainSet <- subset(x=df, sampleSplit==TRUE)
testSet <- subset(x=df, sampleSplit==FALSE)

model <- lm(formula=Weight ~ ., data=trainSet)
summary(model)
modelResiduals <- as.data.frame(residuals(model))


ggplot(modelResiduals, aes(residuals(model))) +
geom_histogram(fill="deepskyblue", color="black")
preds <- predict(model, testSet)
modelEval <- cbind(testSet$Weight, preds)
colnames(modelEval) <- c("Actual", "Predicted")
modelEval <- as.data.frame(modelEval)
rmse <- mean((modelEval$Actual - modelEval$Predicted)^2)
rmse <- sqrt(mse)
rmse
