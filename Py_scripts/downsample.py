def downsample(X_train=X_train, y_train=y_train, n):
    
    from sklearn.utils import resample, shuffle
    import numpy as np
    # concatenate our training data back together
    X_stack = np.column_stack((X_train, y_train))

    # separate minority and majority classes
    a = y_train == 1
    seizures = X_stack[a,:]
    nonseizures = X_stack[~a,:]
    nonseizures_downsampled = resample(nonseizures,
                                    replace = False, # sample without replacement
                                    n_samples = int(n*len(seizures)), # match 10 * minority
                                    random_state = 27) # reproducible results

    # combine minority and downsampled majority
    downsampled = np.vstack((seizures, nonseizures_downsampled))
    # shuffle samples so seizures are not all together
    shuff_down = shuffle(downsampled)
    #define new targets and features
    y_down = shuff_down[:,-1]
    X_down = np.delete(shuff_down, -1, axis=1)
    
    return X_down, y_down