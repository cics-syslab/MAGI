import pluggy

hookspec = pluggy.HookspecMarker("magi")
hookimpl = pluggy.HookimplMarker("magi")

class AddonSpec:
    def __init__(self):
        self.config = None
    @hookspec
    def generating(self):
        """Hook for generating functionality."""

    @hookspec
    def before_grading(self):
        """Hook for actions before grading."""

    @hookspec
    def grade(self):
        """Hook for grading functionality."""

    @hookspec
    def after_grading(self):
        """Hook for actions after grading."""

    @hookspec
    def generate_documentation(self):
        """Hook for generating documentation."""