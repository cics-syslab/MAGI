from core.components import generate
from managers import AddonManager


def main():
    generate.generate_output()
    AddonManager.generate()


if __name__ == "__main__":
    main()
