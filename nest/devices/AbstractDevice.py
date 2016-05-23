from collections import OrderedDict

class AbstractBrainDevice(object):
    """
    This class provides basic, shared functionality which are common for all brain device
    implementations.
    """

    default_parameters = {
        # Subclasses should override the field and set their parameters accordingly

        # The parameters which are specified here can be reset by specifying
        #   the respective parameters on construction.
    }

    fixed_parameters = {
        # Subclasses should override the field and set their parameters accordingly

        # The parameters which are specified here are not allowed to be reset by specifying
        #   the parameters on construction.
    }

    def __init__(self, *args, **params):
        super(AbstractBrainDevice, self).__init__()

        self._parameters = self.__class__.fixed_parameters.copy()
        self._parameters.update(self.get_parameter_defaults())
        self._update_parameters(params)

    def _update_parameters(self, params):
        """
        This method updates the device parameter dictionary with the provided parameter
        dictionary. The dictionary has to be validated before as this method assumes it to be
        correct.

        Overriding subclasses can provide additional configuration parameter adaption as this
        method is called before the brain simulator devices are constructed.

        :param params: The validated parameter dictionary
        """
        self._parameters.update(params)

    def get_parameters(self, *params):
        """
        This method allows to retrieve a dictionary containing device configuration parameters.
        It is possible to retrieve only a subset of the parameters and also to conduct a suitable
        parameter remapping using the subset parameter.

        The device specific parameters are build from the fixed parameters, the parameters which
        were specified on creation of the device or the default value if no the parameter was not
        specified.

        Given that the respective parameters are contained in the device configuration dictionary

        would return a dictionary as depicted below:

        .. code-block:: python

            get_parameters("param1", "param2")
            result = {"param1": value_of_param1, "param2": value_of_param2}

        Parameter remapping can be achieved by specifying a subset dictionary or by specifying
        single remappings as tuple. Both would return a dictionary as depicted below (the key
        "param1" is remapped to "p1", while "param2" is not changed):

        .. code-block:: python

            get_parameters({"p1": "param1", "param2": "param2"})
            get_parameter(("p1", "param1"), "param2")
            result = {"p1": value_of_param1, "param2": value_of_param2}

        :param params: keys of the parameters which should be returned. Each parameter can be
            provided as tuple (new_key, key) or multiple remappings can be provided as dictionary
            {new_key: key}.
        :return: a dictionary containing the desired configuration parameters
        """
        if not params:
            return self._parameters

        result = OrderedDict()
        for p in params:
            if isinstance(p, dict):
                for (k, v) in p.items():
                    result[k] = self._parameters[v]
            if isinstance(p, tuple):
                (k, v) = p
                result[k] = self._parameters[v]
            else:
                result[p] = self._parameters[p]
        return result

    @classmethod
    def get_parameter_defaults(cls):
        """
        The method returns a copy of the default parameter dictionary ("default_parameters"). It
        can be overridden in subclasses if a more flexible approach is necessary.

        :return: A dictionary containing device parameter defaults
        """
        return cls.default_parameters.copy()

