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
            default_width=400,
            default_height=200,
        )

        self.content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)
        self.content_box.set_margin_top(24)
        self.content_box.set_margin_bottom(24)
        self.content_box.set_margin_start(24)
        self.content_box.set_margin_end(24)

        self.dialog_window.set_child(self.content_box)

    def password(self):
        if self._shown:
            return
        self._shown = True

        header_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)

        title_label = Gtk.Label(label=f"Connect to {self.ssid}")
        title_label.set_halign(Gtk.Align.START)
        title_label.add_css_class("title-3")

        subtitle_label = Gtk.Label(label="Enter the network password")
        subtitle_label.set_halign(Gtk.Align.START)
        subtitle_label.add_css_class("dim-label")
        subtitle_label.set_opacity(0.7)

        header_box.append(title_label)
        header_box.append(subtitle_label)

        entry_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        entry_box.set_margin_top(8)

        entry_label = Gtk.Label(label="Password")
        entry_label.set_halign(Gtk.Align.START)
        entry_label.add_css_class("caption-heading")

        entry = Gtk.PasswordEntry()
        entry.set_show_peek_icon(True)
        entry.add_css_class("password-entry")

        entry_box.append(entry_label)
        entry_box.append(entry)

        buttons = Gtk.Box(spacing=12)
        buttons.set_halign(Gtk.Align.END)
        buttons.set_margin_top(16)

        finished = False

        def finish(value):
            nonlocal finished
            if finished:
                return
            finished = True
            self.dialog_window.destroy()
            self.callback(value)

        cancel = Gtk.Button(label="Cancel")
        cancel.set_size_request(100, -1)
        cancel.connect("clicked", lambda *_: finish(None))

        connect = Gtk.Button(label="Connect")
        connect.set_size_request(100, -1)
        connect.add_css_class("suggested-action")
        connect.connect("clicked", lambda *_: finish(entry.get_text()))

        entry.connect("activate", lambda *_: finish(entry.get_text()))

        self.dialog_window.connect(
            "close-request",
            lambda *_: finish(None),
        )

        buttons.append(cancel)
        buttons.append(connect)

        self.content_box.append(header_box)
        self.content_box.append(entry_box)
        self.content_box.append(buttons)

        self.dialog_window.present()
        entry.grab_focus()

    def confirmation(self):
        pass

    def error(self):
        pass
