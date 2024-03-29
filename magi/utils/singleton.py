def singleton(cls: type):
    """
    Decorator to ensure a class only allows one instance.
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


def overwrite_singleton(cls: type):
    """
    Decorator to overwrite the class definition with a singleton instance.
    """

    return cls()


def lazy_singleton(cls: type):
    """
    Decorator to create a lazily-initialized singleton of the given class.

    Rather than immediately instantiating the class when called,
    this decorator defers instantiation until the instance's attributes
    or methods are first accessed.
    """

    class Wrapper:
        def __init__(self, *args, **kwargs):
            """Initialize the wrapper, but not the inner class."""

            self._initialized: bool = False  # Track if the inner instance has been initialized
            self._init_args = args  # Store args to use for initialization later
            self._init_kwargs = kwargs  # Store kwargs for initialization

        def __ensure_initialized(self):
            """Check if inner instance is initialized, if not, initialize it."""
            if not self._initialized:
                self.__initialize()

        def __initialize(self):
            """Actually initialize the inner instance of the class."""
            self._inner_instance = cls(*self._init_args, **self._init_kwargs)
            self._initialized = True

        def __getattr__(self, name):
            self.__ensure_initialized()
            return getattr(self._inner_instance, name)

        def __setattr__(self, key, value):
            """Override attribute setting. Only set on inner instance after initialization."""
            # Handle special attributes related to the Wrapper itself
            if key in ["_initialized", "_init_args", "_init_kwargs", "_inner_instance"]:
                object.__setattr__(self, key, value)
            else:
                self.__ensure_initialized()
                setattr(self._inner_instance, key, value)

        def __delattr__(self, name):
            self.__ensure_initialized()
            delattr(self._inner_instance, name)

        def __str__(self):
            self.__ensure_initialized()
            return str(self._inner_instance)

        def __repr__(self):
            self.__ensure_initialized()
            return repr(self._inner_instance)

        def __call__(self, *args, **kwargs):
            self.__ensure_initialized()
            # TODO: this probably needd to be changed to return self._inner_instance
            return self._inner_instance(*args, **kwargs)

    return Wrapper()
