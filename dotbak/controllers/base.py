
import os
from datetime import datetime
from cement import Controller, ex
from cement.utils import fs
from cement.utils.version import get_version_banner
from ..core.version import get_version
from ..core import exc

VERSION_BANNER = """
Lazily Backup Files and Directories %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'Lazily Backup Files and Directories'

        # text displayed at the bottom of --help output
        epilog = 'Usage: dotbak /path/to/file'

        # controller level arguments. ex: 'dotbak --version'
        arguments = [
            ### add a version banner
            ( [ '-v', '--version' ],
              { 'action'  : 'version',
                'version' : VERSION_BANNER } ),
            ( [ '-s', '--suffix' ],
              { 'action'  : 'store',
                'dest'    : 'suffix' ,
                'help'    : 'backup file/dir suffix (extension)' } ),
            ( [ 'path' ],
              { 'action'  : 'store',
                'help'    : 'path to file/dir to backup' } ),
        ]


    def _clean_path(self, path):
        RSTRIP = ['/', '\\']
        for char in RSTRIP:
            path = self.app.pargs.path.rstrip(char)
        res = fs.abspath(path)
        return res

    def _default(self):
        """Default action if no sub-command is passed."""

        path = self._clean_path(self.app.pargs.path)
        
        if self.app.pargs.suffix is not None:
            suffix = self.app.pargs.suffix
        else:
            suffix = self.app.config.get('dotbak', 'suffix')

        if self.app.config.get('dotbak', 'timestamps') is True:
            timestamp = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
            suffix = f'{suffix}-{timestamp}'

        if not os.path.exists(self.app.pargs.path):
            raise exc.DotBakError(f'Path does not exist: {path}')
        
        res = fs.backup(path, suffix=suffix)
        self.app.log.info(f'Copied {path} -> {res}')

