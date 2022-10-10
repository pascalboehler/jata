#
# gui.py
# jata
#
# Created by Pascal Boehler on 10.10.2022
# Copyright © 2020 Pascal Boehler. All rights reserved.
#

import time
import pytermgui as ptg

def macro_time(fmt: str) -> str:
    return time.strftime(fmt)

ptg.tim.define("!time", macro_time)

with ptg.WindowManager() as manager:
    manager.layout.add_slot("Body")
    manager.add(
        ptg.Window("[bold]The current time is:[/]\n\n[!time 75]%c", box="EMPTY")
    )