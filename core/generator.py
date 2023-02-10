from core.components import generate
from managers import ModuleManager


def main():
    generate.generate_output()
    ModuleManager.generate()
    pass


if __name__ == "__main__":
    main()
