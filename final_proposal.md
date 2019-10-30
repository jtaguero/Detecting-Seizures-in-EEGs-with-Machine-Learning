### Final Capstone Proposal

This project would use some available EEG data to attempt to classify short windows of EEG signal as either recording a seizure or not. I would like to extend this to a predictive model as well. Both CNN and RNN  have been used on such datasets. 
The article 'Deep learning for electroencephalogram (EEG) classification tasks: a review' in the Journal of Neural Engineering which is linked below details many approaches that have been used including the use of CNNs with spectrograms of the EEG used as the input and the less prevalent use of RNNs to analyze EEG data. It is claimed that 41% of the studies used calculated features which included, among other things, Fourier transforms, power spectral density and wavelets. The article can be found here:

['Deep learning for electroencephalogram (EEG) classification tasks: a review'](https://iopscience.iop.org/article/10.1088/1741-2552/ab0ab5/pdf)

 
I approached this problem using random forests for my previous project. I hope to compare at least a couple different models on the data. I will do more feature engineering this time using the Fourier transform and possibly wavelets to compare the results and relative merits of these approaches. I would also like to experiment with testing models trained on one subject's recordings on other subjects recorded during the study. I hope to develop a predictive model for this project as well though I am not sure exactly which model I will use for this. I will definitely be using the MNE library again for preprocessing and constructing the train and test sets. 

I think that recreating the wave forms should provide some nice visual examples from both classes of the small windows of EEG recording that we will be attempting to classify as to whether it records a seizure or not. I have already created many images that could be used . I would like to add an interactive graphic using Flask but that will be once I have everything else in place. 

There are many other datasets available of EEG and many of them also recorded seizures but this dataset is the best I've found so far. One of the larger datasets I have found so far includes 664 .edf files of EEGs from the Children’s Hospital Boston of 22 pediatric subjects with intractable seizures. 129 of the files include one or more seizures with 198 seizures in total recorded. In addition there are annotations which specify the beginning and end of each recorded seizure.It can be found here:

https://archive.physionet.org/pn6/chbmit/

Some of the problems with this project involve the raw data and the lack of an annotations channel as well as learning to effectively leverage the MNE library in this task. These problems have already been solved for the most part during my prior project with this dataset. The problems more specific to this iteration will probably have to do with attempting to train and compare multiple models on multiple subjects and attempting to test models on a different subject's data than the one they were trained on. There is also the possible challenge of attempting to build a predictive model based on this data which seems like it could be problematic. 

I see my next steps as being some feature engineering which will require creating some new pipeline sections to store output from Fourier transforms and similar new features as well as creating the training and testing sets from this data. After that I will probably begin building models on a couple of subjects records and testing them on the hold outs as well as on the other subject's data.