def get_file_start_end_times():

    from datetime import time
    from datetime import datetime 
    
    with open('seizures.txt') as f:
    line_list = f.readlines()
    for elem in line_list:
        if elem[0:9] == 'File Name':
            elem2 = elem.split(":")[1]
            fn = elem2.split(".")[0].strip()
                    
    
    
        if elem[0:15] == 'File Start Time':
            fst = elem.split(":", 1)[1].strip()
            if fst[0:2] == '24':
                fstump = fst[2:9]
                z = '00'
                fst = z + fstump
                
            d[fn]['File Start Time'] = fst  
            
            std = datetime.strptime(fst, '%H:%M:%S')  
            
        if elem[0:13] == 'File End Time':
            fet = elem.split(":", 1)[1].strip()
            if fet[0:2] == '24':
                fetump = fet[2:9]
                z = '00'
                fet = z + fetump
            d[fn]['File End Time'] = fet    
            
            etd = datetime.strptime(fet, '%H:%M:%S')
            
            
            td = etd - std
            d[fn]['File length in seconds'] = td.total_seconds()  

    return d        