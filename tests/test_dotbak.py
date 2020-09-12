
import os
from pytest import raises
from dotbak.core import exc
from dotbak.main import DotBakTest


def test_dotbak_default(tmp):
    with DotBakTest(argv=[tmp.file]) as app:
        app.run()
        assert app.exit_code == 0
        assert os.path.exists(f'{tmp.file}.bak')

def test_dotbak_suffix(tmp):
    with DotBakTest(argv=['--suffix=.notbak', tmp.file]) as app:
        app.run()
        assert app.exit_code == 0
        assert os.path.exists(f'{tmp.file}.notbak')

def test_dotbak_missing_source(tmp):
    os.remove(tmp.file)
    with DotBakTest(argv=[tmp.file]) as app:
        with raises(exc.DotBakError):
            app.run()
