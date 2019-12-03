def get_records_lists():
    
    records_loc_lst = []
    #create list of file locations from text file included in dataset
    with open('Data/RECORDS') as f:
        line_list = f.read().splitlines()
        for elem in line_list:
            if len(elem) > 1:
                records_loc_lst.append(elem)
            
            
    records_w_seizures = []
    #create list of files containing seizures from text file included in dataset
    with open('Data/RECORDS-WITH-SEIZURES') as f:
        line_list = f.readlines()
        for elem in line_list:
            
            if len(elem) > 1:
                records_w_seizures.append(elem.split("/")[1].split('.')[0])
                #make correction
    records_w_seizures[34] = 'chb07_19'            

    records_lst = []
    #create list of records
    for rec in records_loc_lst:
        rec_name = rec.split('/')[1].split('.')[0]
        records_lst.append(rec_name)

    return    records_loc_lst, records_w_seizures, records_lst 



def get_seizures_dictionary():
    #create seizure dictionary with all seizure information from text files. 
    # This dictionary will beused to create the annotations added to the f
    # iles to create our labelled sets of seizure and non-seizre periods

    d = {}
    with open('Data/seizures.txt') as f:
        line_list = f.readlines()
        for elem in line_list:
            if elem[0:9] == 'File Name':
                elem2 = elem.split(":")[1]
                fn = elem2.split(".")[0].strip()
                d[fn]={}
                
            if elem[0:26] == 'Number of Seizures in File':
                numb = int(elem.split(":")[1])
                d[fn]['Number of Seizures in File'] = numb
                
            
            if (elem[0:18]   ==  'Seizure Start Time') or (elem[0:20]   ==  'Seizure 1 Start Time'):
                    elem2 = elem.split(":")[1]
                    elem3 = int(elem2.split()[0])
                    d[fn]['Seizure 1 Start Time'] = elem3


            if (elem[0:16]   ==  'Seizure End Time') or (elem[0:18]   ==  'Seizure 1 End Time'):
                    elem2 = elem.split(":")[1]
                    elem3 = int(elem2.split()[0])
                    d[fn]['Seizure 1 End Time'] = elem3
                    d[fn]['Seizure 1 Duration'] = elem3 - d[fn]['Seizure 1 Start Time']    


            if elem[0:20]   ==  'Seizure 2 Start Time':
                elem2 = elem.split(":")[1]
                elem3 = int(elem2.split()[0])
                d[fn]['Seizure 2 Start Time'] = elem3


            if elem[0:18]   ==  'Seizure 2 End Time':
                elem2 = elem.split(":")[1]
                elem3 = int(elem2.split()[0])
                d[fn]['Seizure 2 End Time'] = elem3
                d[fn]['Seizure 2 Duration'] = elem3 - d[fn]['Seizure 2 Start Time']  

            if elem[0:20]   ==  'Seizure 3 Start Time':
                elem2 = elem.split(":")[1]
                elem3 = int(elem2.split()[0])
                d[fn]['Seizure 3 Start Time'] = elem3


            if elem[0:18]   ==  'Seizure 3 End Time':
                elem2 = elem.split(":")[1]
                elem3 = int(elem2.split()[0])
                d[fn]['Seizure 3 End Time'] = elem3
                d[fn]['Seizure 3 Duration'] = elem3 - d[fn]['Seizure 3 Start Time']  

            if elem[0:20]   ==  'Seizure 4 Start Time':
                elem2 = elem.split(":")[1]
                elem3 = int(elem2.split()[0])
                d[fn]['Seizure 4 Start Time'] = elem3


            if elem[0:18]   ==  'Seizure 4 End Time':
                elem2 = elem.split(":")[1]
                elem3 = int(elem2.split()[0])
                d[fn]['Seizure 4 End Time'] = elem3
                d[fn]['Seizure 4 Duration'] = elem3 - d[fn]['Seizure 4 Start Time']   


            if elem[0:20]   ==  'Seizure 5 Start Time':
                elem2 = elem.split(":")[1]
                elem3 = int(elem2.split()[0])
                d[fn]['Seizure 5 Start Time'] = elem3


            if elem[0:18]   ==  'Seizure 5 End Time':
                elem2 = elem.split(":")[1]
                elem3 = int(elem2.split()[0])
                d[fn]['Seizure 5 End Time'] = elem3
                d[fn]['Seizure 5 Duration'] = elem3 - d[fn]['Seizure 5 Start Time'] 
            
    return d 
            
def make_annotations_dict(d):
    import mne
    #use seizure dictionary to create dictionary of mne annotations objects for use in epoching and labeling data

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
        #create mne annotations object from data taken from seizures dictionary for each file containing a seizure
        anno_nm_lst[idx] = anno
        anno = mne.Annotations(onset=onset,
                                duration=duration,
                                description=description)

        
        
        anno_lst[idx] = anno
        idx += 1

    annotations_dict = {anno_nm_lst[i]: anno_lst[i] for i in range(138)}

    return annotations_dict            



if __name__ == "__main__":

    recs_l, rec_wsl, rec_wos = get_records_lists()

    d = get_seizures_dictionary()

    annotations_dict = make_annotations_dict(d)



