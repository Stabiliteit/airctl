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
        subparsers.add_parser("status")

        list_parser = subparsers.add_parser("list")
        list_parser.add_argument("--scan", action="store_true")

        scan_parser = subparsers.add_parser("scan")
        scan_parser.add_argument("--delay", type=float, default=2.0)

        connect_parser = subparsers.add_parser("connect")
        connect_parser.add_argument("--ssid")
        connect_parser.add_argument("--password", "-p")
        connect_parser.add_argument("--ifname", "-ifn")

        toggle_parser = subparsers.add_parser("toggle")
        toggle_parser.add_argument("state", nargs="?", choices=["on", "off"])

        forget_parser = subparsers.add_parser("forget")
        forget_parser.add_argument("--ssid")

        info_parser = subparsers.add_parser("info")
        info_parser.add_argument("ssid")

        return parser


