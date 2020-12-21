# Authentication to Apollo

class GroLogs(object):

    __version__ = '0.0.1'

    def __init__(self, target_directory, target_log, username = None, hostname = None):

        '''

        Initialize to find the target logs and readers

        '''

        if username == None and hostname == None:
            self.user, self.hostname = self._read_authentication()
        else:
            self.user = username
            self.hostname = hostname

        self.target_directory = target_directory
        self.target_log = target_log
        self.timings = {}
        self._read_loggers()

    def _read_authentication(self):


        """

        Read in the authentication file into apollo


        """

        from ruamel.yaml import YAML
        yaml = YAML()

        import os

        cwd = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(cwd, 'auth_apollo.yml')) as auth_file:

            try:
                auth_info = yaml.load(auth_file)
            except Exception as exc:
                print('Problems handling in reading in the authentication file')


        user = auth_info['username']
        hostname = auth_info['host']

        return user, hostname

    def _read_loggers(self):

        """

        Read the log files for GROMACS software to get step values


        """

        from fabric.connection import Connection

        with Connection(self.hostname, self.user) as portal:

            # Find the file paths
            file_paths_stream = portal.run('find ' + self.target_directory + ' -type f -name "' + self.target_log + '"', hide=True)
            file_paths = file_paths_stream.stdout.strip().split('\n')

            # Grep the logs
            for file_path in file_paths:

                stdout_stream = portal.run('tail -n 13 ' + file_path + '', hide=True)
                stdout = stdout_stream.stdout.strip().split('\n')[0].split('vol')[0].strip().split(' ')[-1]

                if str(stdout) == '0.0':
                    stdout = 'Completed'

                self.timings[file_path] = stdout

    def generate_table(self):

        '''

        Generate a stdout of table values

        '''

        from beautifultable import BeautifulTable

        table = BeautifulTable()

        table.column_headers = ["--- File Path ---", "Step", "Time (ns)"]

        for key, value in self.timings.items():

            row = []
            row.append(key.replace(self.target_log, ''))
            row.append(value)
            row.append(float(value) / 500000)

            table.append_row(row)

        print(table)

