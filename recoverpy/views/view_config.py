from py_cui import PyCUI

from recoverpy.utils.saver import SAVER


class ConfigView:
    def __init__(self, master: PyCUI):
        self.master = master
        self.create_ui_content()

    def create_ui_content(self):
        """Handle the creation of the UI elements."""
        self.master.add_text_box(
            title="Save Path",
            row=0,
            column=1,
            row_span=1,
            column_span=8,
            padx=0,
            pady=0,
            initial_text=SAVER.save_path,
        )
        self.master.add_button(
            "Save",
            1,
            8,
            row_span=1,
            column_span=1,
            padx=0,
            pady=0,
            command=None,
        ).set_color(1)
        self.master.add_text_box(
            title="Log Path",
            row=2,
            column=1,
            row_span=1,
            column_span=8,
            padx=0,
            pady=0,
            initial_text=SAVER.save_path,
        )
        self.master.add_button(
            "Save",
            3,
            8,
            row_span=1,
            column_span=1,
            padx=0,
            pady=0,
            command=None,
        ).set_color(1)
        self.master.add_label(
            title="Enable Logging",
            row=4,
            column=4,
            row_span=1,
            column_span=2,
            padx=0,
            pady=0,
        )
        self.master.add_button(
            "Yes",
            5,
            3,
            row_span=1,
            column_span=1,
            padx=0,
            pady=0,
            command=None,
        ).set_color(1)
        self.master.add_button(
            "No",
            5,
            6,
            row_span=1,
            column_span=1,
            padx=0,
            pady=0,
            command=None,
        ).set_color(1)

        self.master.add_button(
            "Save & Exit",
            9,
            1,
            row_span=1,
            column_span=3,
            padx=0,
            pady=0,
            command=None,
        ).set_color(1)
        self.master.add_button(
            "Cancel",
            9,
            6,
            row_span=1,
            column_span=3,
            padx=0,
            pady=0,
            command=None,
        ).set_color(1)
