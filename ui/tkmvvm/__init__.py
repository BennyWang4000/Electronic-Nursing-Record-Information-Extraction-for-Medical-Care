import sys
import os

if os.path.abspath(os.path.join(os.path.dirname(__file__))) not in sys.path:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import ui.tkmvvm.mvvm
import ui.tkmvvm.view
import ui.tkmvvm.model
import ui.tkmvvm.viewmodel