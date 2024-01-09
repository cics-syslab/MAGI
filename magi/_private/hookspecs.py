import pluggy

hookspec = pluggy.HookspecMarker("magi")
hookimpl = pluggy.HookimplMarker("magi")
@hookspec
def generating():
    pass

@hookspec
def before_grading():
    pass

@hookspec
def grade():
    pass

@hookspec
def after_grading():
    pass

@hookspec
def generate_documentation():
    pass