
# This script sets up '/etc/network/interfaces' and '/etc/rc.local' so that
# the Raspberry Pi always begins by trying to create and join a mesh ad-hoc
# network called 'bakery'.
if [ -e "/etc/network/interfaces" ]
then
    sudo mv "/etc/network/interfaces" "/etc/network/interfaces.commsav"
    sudo printf "Saving /etc/network/interfaces as /etc/network/interfaces.commsav\n"
fi
sudo touch "/etc/network/interfaces"
sudo printf "allow-hotplug wlan0\nauto wlan0\niface wlan0 inet dhcp\n\twpa-ssid=\"bakery\"\n" >> "/etc/network/interfaces"
if [ -e "/etc/rc.local" ]
then
    sudo mv "/etc/rc.local" "/etc/rc.local.commsav"
    sudo printf "Saving /etc/rc.local as /etc/rc.local.commsav\n"
fi
sudo touch "/etc/rc.local"
sudo printf "iwconfig wlan0 mode ad-hoc channel 11 essid \"bakery\"\n\nexit 0" >> "/etc/rc.local"

