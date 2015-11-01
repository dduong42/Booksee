def get_downloaded_file(content, default_path):
    return DownloadedFile(
        content,
        default_path,
        open,
    )


class DownloadedFile:
    def __init__(self, content, default_path, io_factory):
        self.content = content
        self.default_path = default_path
        self.io_factory = io_factory

    def write(self, f):
        f.write(self.content)

    def save(self, path=None):
        if path is None:
            path = self.default_path

        with self.io_factory(path, 'wb') as f:
            self.write(f)

    def __repr__(self):
        return '{}(default_path={})'.format(
            self.__class__.__name__, repr(self.default_path))
