# Machine-Learning-Projects
Some Data Science projects I will be pursuing.

### Proposal One

This project would use some available EEG data to attempt to classify short windows of EEG signal as either recording a seizure or not. One of the larger datasets I have found so far includes 664 .edf files of EEGs from the Children’s Hospital Boston of 22 pediatric subjects with intractable seizures. 129 of the files include one or more seizures with 198 seizures in total recorded. In addition there are annotations which specify the beginning and end of each recorded seizure.
 
I would like to approach this problem using random forests. I hope to compare at least a couple different models on the data and I will do some EDA and attempt to recreate a wave form graphic from the recorded data. Using the MNE library I have put the first file in a data frame and begun to examine the data.

I think that recreating the wave forms should provide some nice visual examples from both classes of the small windows of EEG recording that we will be attempting to classify as to whether it records a seizure or not. 

There are many other datasets available of EEG and many of them also recorded seizures but this dataset is the best I've found so far. It can be found here:

https://archive.physionet.org/pn6/chbmit/


### Proposal Two 

This project would examine, compare and attempt to create predictive models based on imdb and Rotten Tomatoes movie ratings and other data such as budget, viewer votes and popularity. I have already webscraped 10,000 records for imdb and begun building a webscraper to obtain some corresponding data from Rotten Tomatoes for the top films of 2018.

I will need to do some EDA and try out some different models. I'm not completely sure which methods I would focus on here.


### Proposal Three

This project would be aimed at classifying pitches and possibly combinations of pitches correctly from recorded examples. I would like to pursue musical transcription as a machine learning application as a continuing project and this would be at least a first step. I have identified some publicly available datasets of musical recordings and samples including labels for the notes and their time of occurence. I am considering sampling individual notes and possibly relatively simple combinations of notes to create data sets as well. This would serve to focus the scope of the project toward correctly classifying notes. My thought is this might be able to operate in conjunction with some other models that would identify the beginnings and ends of individual notes in time.
