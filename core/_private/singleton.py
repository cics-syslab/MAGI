def singleton(cls):
    """
    Decorator to ensure a class only allows one instance.
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


def overwrite_singleton(cls):
    """
    Decorator to overwrite the class definition with a singleton instance.
    """

    return cls()


def lazy_singleton(cls):
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

# class LazyInitSingletonBase:
#     _instance = None
#
#     class SingletonInner:
#         def __init__(self, child_instance):
#             self.outer_instance = child_instance
#             self.outer_instance.initialize(child_instance)
#
#     def initialize(self):
#         raise NotImplementedError("Subclasses should implement this method")
#
#     @classmethod
#     def _get_instance(cls):
#         if cls._instance is None:
#             cls._instance = cls.SingletonInner(cls)
#         return cls._instance
#
#     def __getattr__(self, name):
#         return getattr(self._get_instance().outer_instance, name)
#
#     def __setattr__(self, name, value):
#         if name in ["_instance", "SingletonInner"]:
#             super().__setattr__(name, value)
#         else:
#             setattr(self._get_instance().outer_instance, name, value)
#
#     def make_instance(self):
#         return self._get_instance().outer_instance
# def lazy_singleton(cls):
#     class Wrapper:
#         def __init__(self, *args, **kwargs):
#             self._initialized = False
#             self._init_args = args
#             self._init_kwargs = kwargs
#
#         def __getattr__(self, name):
#             if not self._initialized:
#                 self._initialize()
#             return getattr(self._inner_instance, name)
#
#         def __setattr__(self, key, value):
#             if key in ["_initialized", "_init_args", "_init_kwargs", "_inner_instance"]:
#                 super().__setattr__(key, value)
#                 return
#             if not self._initialized:
#                 self._initialize()
#             setattr(self._inner_instance, key, value)
#
#         def __delattr__(self, name):
#             if not self._initialized:
#                 self._initialize()
#             delattr(self._inner_instance, name)
#
#         def __str__(self):
#             if not self._initialized:
#                 self._initialize()
#             return str(self._inner_instance)
#
#         def __repr__(self):
#             if not self._initialized:
#                 self._initialize()
#             return repr(self._inner_instance)
#
#         def __call__(self, *args, **kwargs):
#             if not self._initialized:
#                 self._initialize()
#             return self._inner_instance(*args, **kwargs)
#
#         def _initialize(self):
#             self._inner_instance = cls(*self._init_args, **self._init_kwargs)
#             self._initialized = True
#
#     return Wrapper()
