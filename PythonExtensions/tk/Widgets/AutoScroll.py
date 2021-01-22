# ------------------------------------------------------------------------------
#  Created by Tyler Stegmaier.
#  Property of TrueLogic Company.
#  Copyright (c) 2020.
# ------------------------------------------------------------------------------

# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Nov 23, 2020 10:53:16 AM CST  platform: Windows NT
import platform

from .BaseWidgets import *
from .Frames import *
from .Themed import ScrollbarThemed
from ..Events import *
from ..Misc.Enumerations import *




__all__ = ['AutoScroll']

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(BaseTkinterWidget):
    __doc__ = """   Configure the scrollbars for a widget. 
      
    Example: 
    
        class ScrolledTreeView(AutoScroll, TreeViewThemed):
            __doc__ = "   A standard TreeViewThemed widget with scrollbars that will automatically show/hide as needed.   "
            @AutoScroll.create_container
            def __init__(self, master: FrameTypes, **kw):
                TreeViewThemed.__init__(self, master, **kw)
                AutoScroll.__init__(self, master)  
                ...
            ...
    """
    vsb: ScrollbarThemed
    hsb: ScrollbarThemed
    def __init__(self, master: BaseTkinterWidget, Color: Dict[str, str] = None):
        super().__init__(Color)
        self.master = master

        if hasattr(self, 'xview') and callable(self.xview):
            self.hsb = ScrollbarThemed(master, orientation=Orient.Horizonal, command=self.xview).Grid(column=0, row=1, sticky=AnchorAndSticky.EastWest)
            self.configure(xscrollcommand=self._autoscroll(self.hsb))

        if hasattr(self, 'yview') and callable(self.yview):
            self.vsb = ScrollbarThemed(master, orientation=Orient.Vertical, command=self.yview).Grid(column=1, row=0, sticky=AnchorAndSticky.NorthSouth)
            self.configure(yscrollcommand=self._autoscroll(self.vsb))

        self.Grid(column=0, row=0, sticky=AnchorAndSticky.All)

        master.Grid_RowConfigure(0, weight=1)
        master.Grid_ColumnConfigure(0, weight=1)

    @staticmethod
    def _autoscroll(sbar):
        """   Hide and show scrollbar as needed.   """
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1: sbar.hide()
            else: sbar.show()
            sbar.set(first, last)
        return wrapped

    def __str__(self): return str(self.master)

    @staticmethod
    def create_container(func):
        """   Creates a ttk Frame with a given master, and use this new frame to place the scrollbars and the widget.   """
        def wrapped(cls, master, **kw):
            container = Frame(master)
            container.Bind(Bindings.Enter, lambda e: AutoScroll._bound_to_mousewheel(e, container))
            container.Bind(Bindings.Leave, lambda e: AutoScroll._unbound_to_mousewheel(e, container))
            return func(cls, container, **kw)
        return wrapped

    # noinspection PyUnusedLocal
    @staticmethod
    def _bound_to_mousewheel(event: tkEvent, widget: BaseTkinterWidget):
        child = widget.winfo_children()[0]
        assert (isinstance(child, BaseTkinterWidget))
        if platform.system() == 'Windows' or platform.system() == 'Darwin':
            child.BindAll(Bindings.MouseWheel, lambda e: AutoScroll._on_mousewheel(e, child))
            child.BindAll(Bindings.ShiftMouseWheel, lambda e: AutoScroll._on_shiftmouse(e, child))
        else:
            child.BindAll(Bindings.Button4, lambda e: AutoScroll._on_mousewheel(e, child))
            child.BindAll(Bindings.Button5, lambda e: AutoScroll._on_mousewheel(e, child))
            child.BindAll(Bindings.ShiftButton4, lambda e: AutoScroll._on_shiftmouse(e, child))
            child.BindAll(Bindings.ShiftButton5, lambda e: AutoScroll._on_shiftmouse(e, child))

    # noinspection PyUnusedLocal
    @staticmethod
    def _unbound_to_mousewheel(event: tkEvent, widget: BaseTkinterWidget):
        assert (isinstance(widget, BaseTkinterWidget))
        if platform.system() == 'Windows' or platform.system() == 'Darwin':
            widget.unbind_all(Bindings.MouseWheel)
            widget.unbind_all(Bindings.ShiftMouseWheel)
        else:
            widget.unbind_all(Bindings.Button4)
            widget.unbind_all(Bindings.Button5)
            widget.unbind_all(Bindings.ShiftButton4)
            widget.unbind_all(Bindings.ShiftButton5)

    @staticmethod
    def _on_mousewheel(event, widget):
        if platform.system() == 'Windows':
            widget.yview_scroll(-1 * int(event.delta / 120), 'units')
        elif platform.system() == 'Darwin':
            widget.yview_scroll(-1 * int(event.delta), 'units')
        else:
            if event.num == 4:
                widget.yview_scroll(-1, 'units')
            elif event.num == 5:
                widget.yview_scroll(1, 'units')

    @staticmethod
    def _on_shiftmouse(event, widget):
        if platform.system() == 'Windows':
            widget.xview_scroll(-1 * int(event.delta / 120), 'units')
        elif platform.system() == 'Darwin':
            widget.xview_scroll(-1 * int(event.delta), 'units')
        else:
            if event.num == 4:
                widget.xview_scroll(-1, 'units')
            elif event.num == 5:
                widget.xview_scroll(1, 'units')
