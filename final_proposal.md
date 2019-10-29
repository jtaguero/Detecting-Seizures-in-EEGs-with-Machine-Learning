### Final Capstone Proposal

This project would use some available EEG data to attempt to classify short windows of EEG signal as either recording a seizure or not. One of the larger datasets I have found so far includes 664 .edf files of EEGs from the Children’s Hospital Boston of 22 pediatric subjects with intractable seizures. 129 of the files include one or more seizures with 198 seizures in total recorded. In addition there are annotations which specify the beginning and end of each recorded seizure.
 
I approached this problem using random forests for my previous project. I hope to compare at least a couple different models on the data. I will do more feature engineering this time using the Fourier transform and possibly wavelets to compare the results and relative merits of these approaches. I would also like to experiment with testing models trained on one subject's recordings on other subjects recorded during the study. I hope to develop a predictive model for this project as well though I am not sure exactly which model I will use for this. I will definitely be using the MNE library again for preprocessing and constructing the train and test sets. 

I think that recreating the wave forms should provide some nice visual examples from both classes of the small windows of EEG recording that we will be attempting to classify as to whether it records a seizure or not. 

There are many other datasets available of EEG and many of them also recorded seizures but this dataset is the best I've found so far. One of the larger datasets I have found so far includes 664 .edf files of EEGs from the Children’s Hospital Boston of 22 pediatric subjects with intractable seizures. 129 of the files include one or more seizures with 198 seizures in total recorded. In addition there are annotations which specify the beginning and end of each recorded seizure.It can be found here:

https://archive.physionet.org/pn6/chbmit/