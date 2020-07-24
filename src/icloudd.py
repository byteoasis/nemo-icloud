import dbus
import dbus.service
import click
import time
from pyicloud import PyiCloudService


class Time(dbus.service.Object):
    def __init__(self):
        self.bus = dbus.SessionBus()
        name = dbus.service.BusName('com.byteoasis.iCloud', bus=self.bus)
        super().__init__(name, '/Time')

    @dbus.service.method('com.byteoasis.Time', out_signature='s')
    def currenttime(self):
        """Use strftime to return a formatted timestamp
        that looks like 23-02-2018 06:57:04."""

        formatter = '%d-%m-%Y %H:%M:%S'
        return time.strftime(formatter)


if __name__ == '__main__':
    import dbus.mainloop.glib
    from gi.repository import GLib

    print('Py iCloud Services')
    api = PyiCloudService('email@example.com')
    # if api.requires_2fa:
    #     print
    #     "Two-factor authentication required. Your trusted devices are:"
    #
    #     devices = api.trusted_devices
    #     for i, device in enumerate(devices):
    #         print
    #         "  %s: %s" % (i, device.get('deviceName', "SMS to %s" %
    #                                     device.get('phoneNumber')))
    #
    #     device = click.prompt('Which device would you like to use?', default=0)
    #     device = devices[device]
    #     if not api.send_verification_code(device):
    #         print
    #         "Failed to send verification code"
    #         # sys.exit(1)
    #
    #     code = click.prompt('Please enter validation code')
    #     if not api.validate_verification_code(device, code):
    #         print
    #         "Failed to verify verification code"
    #         # sys.exit(1)

    print('Here are the files:')
    print(api.files.dir())

    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    loop = GLib.MainLoop()
    object = Time()
    loop.run()

