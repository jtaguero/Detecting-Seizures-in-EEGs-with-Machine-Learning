def downsample(X_train=X_train, y_train=y_train):
    # concatenate our training data back together
    X_stack = np.column_stack((X_train, y_train))

    # separate minority and majority classes
    a = y_train == 1
    seizures = X_stack[a,:]
    nonseizures = X_stack[~a,:]
    nonseizures_downsampled = resample(nonseizures,
                                    replace = False, # sample without replacement
                                    n_samples = int(10*len(seizures)), # match 10 * minority
                                    random_state = 27) # reproducible results

    # combine minority and downsampled majority
    downsampled = np.vstack((seizures, nonseizures_downsampled))

    y_down = downsampled[:,-1]
    X_down = np.delete(downsampled, -1, axis=1)
    
    return X_down, y_down