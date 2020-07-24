import dbus

bus = dbus.SessionBus()
time = bus.get_object('com.byteoasis.Time', '/Time')
curr = time.CurrentTime()
print('The current time is', curr)

#
# Devices
#
print('Devices')
print(api.devices)
print(api.devices[0])
print(api.iphone)
