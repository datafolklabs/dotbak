
from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import DotBakError
from .controllers.base import Base

# configuration defaults
CONFIG = init_defaults('dotbak')
CONFIG['dotbak']['suffix'] = '.bak'
CONFIG['dotbak']['timestamps'] = True

class DotBak(App):
    """DotBak primary application."""

    class Meta:
        label = 'dotbak'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Base
        ]


class DotBakTest(TestApp,DotBak):
    """A sub-class of DotBak that is better suited for testing."""

    class Meta:
        label = 'dotbak'


def main():
    with DotBak() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except DotBakError as e:
            print('DotBakError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
