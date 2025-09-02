import numpy as np

def tau_filter(x, tau, dt):
    """
    Apply a low-pass filter to a signal.

    This function filters the input signal `x` using an exponential smoothing
    low-pass filter with a time constant `tau`.

    Parameters
    ----------
    x : numpy.ndarray
        The input signal to be filtered.
    tau : float
        The time constant of the filter.
    dt : float
        The time step or sampling interval of the input signal.

    Returns
    -------
    numpy.ndarray
        The filtered output signal.
    """
    alpha = dt / (tau + dt)
    y = np.zeros(x.shape)
    y[0] = alpha * x[0]
    for i in range(1,x.size):
        y[i] = alpha * x[i] + (1-alpha) * y[i-1]
    return y