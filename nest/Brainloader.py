import imp

def load_py_brain(path):
    """
    Load a python network file

    :param path: path to the .py file
    :param pop_meta_infos: A list of the populations meta info objects 
    """
    #logger.info("Loading brain model from python: " + path)
    brain_module = imp.load_source('__brain_model', path)
    populations = {}
    try:
        circuit = brain_module.circuit
        populations['circuit'] = circuit
    except AttributeError:
        pass

    try:
        populations.update(brain_module.__population_views)
    except AttributeError:
        raise AttributeError("The variable '__population_views' has not been declared in the brain file.")

    if not isinstance(populations, dict):
        raise ValueError("The variable '__population_views' is not a dictionary.")

    return populations
