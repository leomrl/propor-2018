# propor-2018


The goal of this repository is to centralize all efforts and progress about detecting textual content similarity between Portuguese and Brazilian locales.

## Dataset

### Raw

OpenSubtitles.pt-pt_br.pt_br
OpenSubtitles.pt-pt_br.pt

### Final (classeds added, sentences double quoted and some noisy removal)

OpenSubtitlesPT.csv

## Noisy Removal

Removed punctuation.
Removed lines containing words: DIVX, divx, Subtitle, Traduzido, Legendas.

## Algorithm

weka.classifiers.bayes.NaiveBayesMultinomialText

### Options

Default

## Results

5 Fold Cross Validation:

=== Summary ===

```
Correctly Classified Instances      322228               59.2077 %
Incorrectly Classified Instances    222005               40.7923 %
Kappa statistic                     0.1842
Mean absolute error                 0.4397
Root mean squared error             0.4872
Relative absolute error             87.9329 %
Root relative squared error         97.4365 %
Total Number of Instances           544233   
```

=== Detailed Accuracy By Class ===

                  TP Rate  FP Rate  Precision  Recall   F-Measure  MCC      ROC Area  PRC Area  Class
                  0.539    0.354    0.603      0.539    0.569      0.185    0.646     0.657     PT_PT
                  0.646    0.461    0.583      0.646    0.613      0.185    0.646     0.632     PT_BR
    Weighted Avg. 0.592    0.408    0.593      0.592    0.591      0.185    0.646     0.644     

=== Confusion Matrix ===

```
      a      b   <-- classified as
 146568 125545 |      a = PT_PT
  96460 175660 |      b = PT_BR
```
