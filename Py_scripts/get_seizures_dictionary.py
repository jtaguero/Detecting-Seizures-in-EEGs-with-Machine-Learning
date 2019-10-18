def get_seizures_dictionary():

    d = {}
    with open('seizures.txt') as f:
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
