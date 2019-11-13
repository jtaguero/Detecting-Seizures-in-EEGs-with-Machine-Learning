def psd(sepochs=epochs):


    from mne.time_frequency import psd_array_welch
    from mne.time_frequency import psd_welch
    psds, freqs = psd_welch(epochs, fmin=1, fmax=40, n_fft=128, n_overlap=.5, n_per_seg=128, proj=False, n_jobs=1, reject_by_annotation=True, average='mean', verbose=None)
    psds /= np.sum(psds, axis=-1, keepdims=True)
    psds_rs = psds.reshape(len(psds), -1)
return psds_rs