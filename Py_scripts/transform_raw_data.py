def transform_raw_data(subject='chb01', annotations_dict=annotations_dict):
    import mne
    from mne.channels.montage import get_builtin_montages
    
    for rec in records_loc_lst:
        #for all records matching the subject read them into an mne raw object and set the channels

        if rec[0:5] == subject:
                data_path = 'chb-mit-scalp-eeg-database-1.0.0/'
                fname = data_path + rec
                data = mne.io.read_raw_edf(fname, preload=True)
                data = data.filter(1., 40., fir_design='firwin', n_jobs=1)
                info = data.info
                info['ch_names'] = ['AF7', 'FT7', 'TP7', 'PO7', 'AF3', 'FC3', 'CP3', 'PO3', 'AF4', 'FC4', 'CP4', 'PO4', 'AF8', 'FT8', 'TP8', 'PO8', 'FCz', 'CPz', 'T7', 'FT9', 'FT10', 'T8', 'TP8']
                
                for i in range(len(info['chs'])):
                    info['chs'][i]['ch_name'] = info['ch_names'][i]
                    
                montage = mne.channels.read_montage("standard_1020")
                data.set_montage(montage)    

                #if rec in annotations_dict set the annotations for the seizures in the raw object
                    
                rec_name = rec.split('/')[1].split('.')[0]
                if rec_name in annotations_dict:
                    anno = annotations_dictionary[rec_name]
                    data.set_annotations(anno)
            
                    event_id = dict(Seizure=1, Nonseizure=0)
                    events_from_annot, event_dict = mne.events_from_annotations(data, chunk_duration=1)

                 #if rec not in annotations_dict set the annotations as all nonseizure in the raw object    
                    
                if rec_name not in annotations_dictionary:
                    events = mne.make_fixed_length_events(data, id=0, start=0, stop=None, duration=1.0, first_samp=True, overlap=0.0)
                    
                    
                    mapping = {0: 'Nonseizure', 1: 'Seizure'}
                    onsets = events[:, 0] / data.info['sfreq']
                    durations = np.ones_like(onsets)  # assumes instantaneous events
                    descriptions = [mapping[event_id] for event_id in events[:, 2]]
                    annot_from_events = mne.Annotations(onset=onsets, duration=durations,
                                                        description=descriptions)
                    data.set_annotations(annot_from_events)    
                    
                
            #save raw files with annotations set as fif files  
                
            fif_lst = []
            fif = '_raw.fif'
            file_nm = rec_name + fif
            fif_lst.append(file_nm)
            data.save(file_nm, picks='all', fmt='single')
        
    return fif_lst    