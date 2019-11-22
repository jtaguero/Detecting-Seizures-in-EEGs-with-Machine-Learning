## Final Capstone Proposal

## Objective

This project used some available EEG data to attempt to classify short windows of EEG signal as either recording a seizure or not. I would like to extend this to a predictive model as well. Both CNN and RNN have been used on such datasets. 
The article 'Deep learning for electroencephalogram (EEG) classification tasks: a review' in the Journal of Neural Engineering which is linked below details many approaches that have been used including the use of CNNs with spectrograms of the EEG used as the input and the less prevalent use of RNNs to analyze EEG data. It is claimed that 41% of the studies used calculated features which included, among other things, Fourier transforms, power spectral density and wavelets. The article can be found here:

['Deep learning for electroencephalogram (EEG) classification tasks: a review'](https://iopscience.iop.org/article/10.1088/1741-2552/ab0ab5/pdf)

## My approach to the problem
 
I approached this problem using balanced random forests due to the unbalanced nature of this classification problem. The recorded seizures makes up less than .5 % of the dataset. I did some feature engineering using the Welch power spectral density, a version of the fast Fourier transform. I would like to work further with Fourier transforms and wavelets to compare their relative merits for this problem. I also experimented with testing models trained on one subject's recordings on other subjects recorded during the study. I hope to develop a predictive model for this project as well probably using CNN or RNN. I will definitely be using the MNE library again for preprocessing and constructing the train and test sets. 
 

## The Data

There are many other datasets available of EEG and many of them also recorded seizures but this dataset is the best I've found so far. One of the larger datasets I have found so far includes 664 .edf files of EEGs from the Children’s Hospital Boston of 22 pediatric subjects with intractable seizures. 129 of the files include one or more seizures with 198 seizures in total recorded. In addition there are annotations which specify the beginning and end of each recorded seizure.It can be found here:

https://archive.physionet.org/pn6/chbmit/

## Challenges

Some of the problems with this project involve the raw data and the lack of an annotations channel as well as learning to effectively leverage the MNE library in this task. These problems have already been solved for the most part during my prior project with this dataset. The problems more specific to this iteration had to do with attempting to train and compare multiple models on multiple subjects which necessitated increasingly large EC2 instances on AWS. There is also the possible challenge of attempting to build a predictive model based on this data which seems like it could be problematic. 

## Next steps
Building a predictive model with CNN or RNN hopefully in conjunction with a classifier trained to detect the pre-ictal phase which precedes a seizure.
