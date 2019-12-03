def get_set_fif_epochs_ttsplit(data_path = 'fif/',  fif_list=fif_lst ):
        import mne
        

        data_path = 'fif/'
        #get all files in fif list and concatenate them into one raw object
        raws = mne.concatenate_raws([mne.io.read_raw_fif('fif/' + f, preload=False) for f in fif_lst])
        info = raws.info
        channels = raws.ch_names


        event_id = dict(Seizure=1, Nonseizure=0)
        events_from_annot, event_dict = mne.events_from_annotations(raws, event_id=event_id, chunk_duration=1)
        #get all events from the annotations previously set in the fif files and divide data into one second epochs labeled Seizure=1 or Nonseizure=0
        tmin, tmax = -0.5, 0.5
        epochs = mne.Epochs(raws, events_from_annot, event_id, tmin, tmax, proj=True,
                            decim=2, baseline=None, preload=True)

        

        # get MEG and EEG data
        
        picks = mne.pick_types(epochs.info, meg=False, eeg=True)

        #separate data and target
        X = epochs.get_data()[:, picks]
        y = epochs.events[:, 2]
        
        #reshape X for test train split
        X_2d = X.reshape(len(X), -1)

        #test train split with y stratified due to the our unbalanced classification problem,
        #so that the proportion of seizure and non-seizure categories are the same in the training and testing sets
        
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(
        X_2d, y, stratify=y)


return X_train, X_test, y_train, y_test
