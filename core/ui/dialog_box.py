import gi
from gi.repository import Gtk

gi.require_version("Gtk", "4.0")


class DialogBox:
    def __init__(self, parent, ssid: str, callback):
        self.parent = parent
        self.ssid = ssid
        self.callback = callback
        self._shown = False
        self._build_base()

    def _build_base(self):
        self.dialog_window = Gtk.Window(
            title=f"Connect to {self.ssid}",
            modal=True,
            transient_for=self.parent,
            default_width=300,
            default_height=150,
        )

        self.content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.content_box.set_margin_top(15)
        self.content_box.set_margin_bottom(15)
        self.content_box.set_margin_start(15)
        self.content_box.set_margin_end(15)

        self.dialog_window.set_child(self.content_box)

    def password(self):
        if self._shown:
            return
        self._shown = True

        label = Gtk.Label(label=f"Enter password for {self.ssid}")
        label.set_halign(Gtk.Align.START)

        entry = Gtk.PasswordEntry()
        entry.set_show_peek_icon(True)

        buttons = Gtk.Box(spacing=10)
        buttons.set_halign(Gtk.Align.END)
        buttons.set_margin_top(10)

        finished = False

        def finish(value):
            nonlocal finished
            if finished:
                return
            finished = True
            self.dialog_window.destroy()
            self.callback(value)

        cancel = Gtk.Button(label="Cancel")
        cancel.connect("clicked", lambda *_: finish(None))

        connect = Gtk.Button(label="Connect")
        connect.add_css_class("suggested-action")
        connect.connect("clicked", lambda *_: finish(entry.get_text()))

        entry.connect("activate", lambda *_: finish(entry.get_text()))

        self.dialog_window.connect(
            "close-request",
            lambda *_: finish(None),
        )

        buttons.append(cancel)
        buttons.append(connect)

        self.content_box.append(label)
        self.content_box.append(entry)
        self.content_box.append(buttons)

        self.dialog_window.present()
        entry.grab_focus()
