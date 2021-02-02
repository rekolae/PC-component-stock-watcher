from unittest import TestCase, mock

from pc_component_stock_watcher.run import main


class TestMain(TestCase):

    @mock.patch('builtins.print')
    def test_greetings(self, mock_print):
        main()
        mock_print.assert_called_once()
