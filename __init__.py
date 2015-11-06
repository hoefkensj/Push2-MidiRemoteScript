# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\midi-remote-scripts\Push2\__init__.py
from __future__ import absolute_import

def get_capabilities():
    from ableton.v2.control_surface import capabilities as caps
    return {caps.CONTROLLER_ID_KEY: caps.controller_id(vendor_id=10626, product_ids=[6503], model_name='Ableton Push 2'),
     caps.PORTS_KEY: [caps.inport(props=[caps.HIDDEN, caps.NOTES_CC, caps.SCRIPT]),
                      caps.inport(props=[]),
                      caps.outport(props=[caps.HIDDEN,
                       caps.NOTES_CC,
                       caps.SYNC,
                       caps.SCRIPT]),
                      caps.outport(props=[])],
     caps.TYPE_KEY: 'push2',
     caps.AUTO_LOAD_KEY: True}


def create_instance(c_instance):
    from .push2 import Push2
    from .push2_model import Root, Sender
    root = Root(sender=Sender(logger=c_instance, message_sink=c_instance.send_model_update, process_connected=c_instance.process_connected))
    return Push2(c_instance=c_instance, model=root)