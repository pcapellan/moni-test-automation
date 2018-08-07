import os.path
import sys


def setup_behave():
    """
    Apply tweaks, extensions and patches to "behave".
    """
    from behave.configuration import Configuration
    # -- DISABLE: Timings to simplify issue.features/ tests.
    Configuration.defaults["show_timings"] = False


def behave_main0():
    from behave.__main__ import main as behave_main
    setup_behave()
    return behave_main()


if __name__ == "__main__":
    os.environ["BEHAVE_TERM_STYLE"] = "blue"
    sys.exit(behave_main0())