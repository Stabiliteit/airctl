import argparse
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from airctl.network_manager import NetworkManager


class AirctlCli:
    def __init__(self):
        self.console = Console()
        self.parser = self._create_arg_parser()

    def _create_arg_parser(self):
        parser = argparse.ArgumentParser(description="AIRCTL - a modern WiFi management tool for Linux")
        subparsers = parser.add_subparsers(dest="command")

        subparsers.add_parser("nm-status")
        subparsers.add_parser("disconnect")
        subparsers.add_parser("status").set_defaults(func=self._network_status)


        list_parser = subparsers.add_parser("list")
        list_parser.add_argument("--scan", action="store_true")
        list_parser.set_defaults(func=self._list_network)

        scan_parser = subparsers.add_parser("scan")
        scan_parser.add_argument("--delay", type=float, default=2.0)
        scan_parser.set_defaults(func=self._scan_network)

        connect_parser = subparsers.add_parser("connect")
        connect_parser.add_argument("--ssid")
        connect_parser.add_argument("--password", "-p")
        connect_parser.add_argument("--ifname", "-ifn")
        connect_parser.set_defaults(func=self._connect_network)

        toggle_parser = subparsers.add_parser("toggle")
        toggle_parser.add_argument("state", nargs="?", choices=["on", "off"])
        toggle_parser.set_defaults(func=self._toogle_wifi)

        forget_parser = subparsers.add_parser("forget")
        forget_parser.add_argument("--ssid")
        forget_parser.set_defaults(func=self._forget_network)

        info_parser = subparsers.add_parser("info")
        info_parser.add_argument("ssid")
        info_parser.set_defaults(func=self._network_info)

        return parser

    def run(self, argv=None):
        args = self.parser.parse_args(argv)
        return args.func(args)

    def _success(self, message):
        self.console.print(f"[bold green]{message}[/]")

    def _error(self, message):
        self.console.print(f"[bold red]{message}[/]")

    def _warning(self, message):
        self.console.print(f"[bold yellow]{message}[/]")

    def _network_status(self, args):
        status = NetworkManager.wifi_status()
        print(status)
        

    def _connect_network(self, args):
        print(args)

    def _scan_network(self, args):
        print(args)

    def _disconnect_network(self, args):
        print(args)

    def _forget_network(self, args):
        print(args)

    def _toogle_wifi(slef, args):
        print(args)

    def _network_info(self, args):
        print(args)

    def _list_network(self, networks):
        pass
