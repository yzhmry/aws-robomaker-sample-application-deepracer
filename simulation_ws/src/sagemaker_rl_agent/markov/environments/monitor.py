class Monitor:
    def __init__(self, logfile):
        self._file = open(logfile, 'w')

    def add(self, *args, **kwargs):
        s = '\t'.join([str(i) for i in args])
        if s:
            self._file.write(s + '\n')

        s = '\t'.join(['{}={}'.format(k, v) for k, v in kwargs.items()])
        if s:
            self._file.write(s + '\n')

    def flush(self):
        self._file.close()
