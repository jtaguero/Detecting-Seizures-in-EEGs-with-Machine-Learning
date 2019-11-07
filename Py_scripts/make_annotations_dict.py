def make_annotations_dict(d):
    import mne

    anno_nm_lst = [n for n in range(138)]
    anno_lst = [n for n in range(138)]
    idx = 0
    for elem in d.keys():
        
        df = d[elem]
        numb = df[list(df)[0]]
        duration = [df[list(df)[i]] for i in range(3, df[list(df)[0]]*3 + 1, 3)]
        onset = [df[list(df)[i]] for i in range(1, 3*numb + 1, 3)]
        description1=['Seizure']*numb
        onset3 = [0.0]
        onset2 = [onset[i] + duration[i] for i in range(numb)]
        onset2 = onset3 + onset2
        duree = [onset[i] - onset2[i] for i in range(numb)]    

        duration2 = [df[list(df)[-1]] - onset2[-1]]
        
        
        description2 = ['Nonseizure']*(numb + 1)
        onset = onset2 + onset
        duration = duree + duration2 + duration
        
        description = description2 + description1

        
        anno = elem 
        
        anno_nm_lst[idx] = anno
        anno = mne.Annotations(onset=onset,
                                duration=duration,
                                description=description)

        
        
        anno_lst[idx] = anno
        idx += 1

    annotations_dict = {anno_nm_lst[i]: anno_lst[i] for i in range(138)}

return annotations_dict