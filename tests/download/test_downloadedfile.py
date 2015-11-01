from unittest import TestCase
from unittest.mock import Mock

from booksee.download.downloadedfile import DownloadedFile


class DownloadedFileTestCase(TestCase):
    def test_write(self):
        f = Mock()
        f.write = Mock()

        downloaded_file = DownloadedFile(
            content=b'content',
            default_path='my_path',
            io_factory=Mock(),
        )
        downloaded_file.write(f)
        f.write.assert_called_once_with(b'content')

    def test_save_without_arg(self):
        f = Mock()
        f.write = Mock()

        ctx = Mock()
        ctx.__enter__ = Mock(return_value=f)
        ctx.__exit__ = Mock(return_value=False)

        io_factory = Mock(return_value=ctx)

        downloaded_file = DownloadedFile(
            content=b'content',
            default_path='my_path',
            io_factory=io_factory,
        )
        downloaded_file.save()
        io_factory.assert_called_once_with('my_path', 'wb')
        f.write.assert_called_once_with(b'content')

    def test_save_with_arg(self):
        f = Mock()
        f.write = Mock()

        ctx = Mock()
        ctx.__enter__ = Mock(return_value=f)
        ctx.__exit__ = Mock(return_value=False)

        io_factory = Mock(return_value=ctx)

        downloaded_file = DownloadedFile(
            content=b'content',
            default_path='my_path',
            io_factory=io_factory,
        )
        downloaded_file.save('new_path')
        io_factory.assert_called_once_with('new_path', 'wb')
        f.write.assert_called_once_with(b'content')
