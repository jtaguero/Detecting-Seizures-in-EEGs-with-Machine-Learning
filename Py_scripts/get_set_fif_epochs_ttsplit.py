def get_set_fif_epochs_ttsplit(data_path = 'fif/',  fif_list=fif_lst ):
        import mne
        

        data_path = 'fif/'

        raws = mne.concatenate_raws([mne.io.read_raw_fif('fif/' + f, preload=False) for f in fif_lst])
        info = raws.info
        channels = raws.ch_names


        event_id = dict(Seizure=1, Nonseizure=0)
        events_from_annot, event_dict = mne.events_from_annotations(raws, event_id=event_id, chunk_duration=1)

        tmin, tmax = -0.5, 0.5
        epochs = mne.Epochs(raws, events_from_annot, event_id, tmin, tmax, proj=True,
                            decim=2, baseline=None, preload=True)

        

        # get MEG and EEG data
        
        picks = mne.pick_types(epochs.info, meg=False, eeg=True)
        X = epochs.get_data()[:, picks]
        y = epochs.events[:, 2]
        X.shape, y.shape

        X_2d = X.reshape(len(X), -1)

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(
        X_2d, y, stratify=y)


return X_train, X_test, y_train, y_test
