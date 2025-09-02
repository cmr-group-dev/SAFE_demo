import numpy as np

def get_random_safe_params(seed=None):
    """
    Generate random parameters for SAFE prediction.

    Parameters
    ----------
    seed : int, optional
        A seed to initialize the random number generator. If None, the
        generator is initialized with a random seed. Default is None.

    Returns
    -------
    safe : dict
        A dictionary of parameters for the general SAFE model.
        It contains the following keys:
        'tau1', 'tau2', 'tau3' : numpy.ndarray
            Time constants for the filters.
        'a1', 'a2', 'a3' : numpy.ndarray
            Weights for the filters.
        'stim_limit' : numpy.ndarray
            Stimulation limit.
        'g_scale' : numpy.ndarray
            Scaling factor.
    safe_cardiac : dict
        A dictionary of parameters for the cardiac-specific SAFE model.
        It contains the same keys as `safe`, but with different value ranges
        optimized for cardiac applications.
    """
    
    rng = np.random.default_rng(seed)
    
    
    safe = {}
    safe['tau1'] = rng.uniform(.0005, .0010, 3)
    safe['tau2'] = rng.uniform(.01, .02, 3)
    safe['tau3'] = rng.uniform(.0001, .0003, 3)

    safe['a1'] = rng.uniform(.2, .3, 3)
    safe['a2'] = rng.uniform(.45, .55, 3)
    safe['a3'] = np.ones(3) - safe['a2'] - safe['a1']

    safe['stim_limit'] = rng.uniform(20, 40, 3)
    safe['g_scale'] = rng.uniform(0.31, 0.35, 3)


    safe_cardiac = {}
    safe_cardiac['tau1'] = rng.uniform(.002, .003, 3)
    safe_cardiac['tau2'] = rng.uniform(.0015, .002, 3)
    safe_cardiac['tau3'] = rng.uniform(.001, .001, 3)

    safe_cardiac['a1'] = rng.uniform(.7, .8, 3)
    safe_cardiac['a2'] = np.ones(3) - safe['a1']
    safe_cardiac['a3'] = np.zeros(3)

    safe_cardiac['stim_limit'] = rng.uniform(14, 20, 3)
    safe_cardiac['g_scale'] = rng.uniform(0.30, 0.35, 3)


    return safe, safe_cardiac