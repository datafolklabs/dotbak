
import os
import re
from glob import glob
from pytest import raises
from dotbak.core import exc
from dotbak.main import DotBakTest


def test_dotbak_default(tmp):
    with DotBakTest(argv=[tmp.file]) as app:
        app.run()
        assert app.exit_code == 0

        ### FIXME: regex is way too loose for a proper test
        res = glob(f'{tmp.file}.bak-*')

        assert len(res) > 0

def test_dotbak_default_without_timestamps(tmp):
    with DotBakTest(argv=[tmp.file]) as app:
        app.config.set('dotbak', 'timestamps', False)
        app.run()
        assert app.exit_code == 0
        assert os.path.exists(f'{tmp.file}.bak')

def test_dotbak_suffix(tmp):
    with DotBakTest(argv=['--suffix=.notbak', tmp.file]) as app:
        app.config.set('dotbak', 'timestamps', False)
        app.run()
        assert app.exit_code == 0
        assert os.path.exists(f'{tmp.file}.notbak')

def test_dotbak_missing_source(tmp):
    os.remove(tmp.file)
    with DotBakTest(argv=[tmp.file]) as app:
        with raises(exc.DotBakError):
            app.run()
