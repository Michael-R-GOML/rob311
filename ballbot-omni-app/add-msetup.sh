# check if the script is run as root
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# check if the file exists
if [ ! -f /etc/wpa_supplicant/wpa_supplicant-wlan0.conf ]; then
    echo "File not found, please verify that you are using the latest version of our Raspbian OS!"
    exit
fi

# check if the file is writable
if [ ! -w /etc/wpa_supplicant/wpa_supplicant-wlan0.conf ]; then
    echo "File not writable, please restart the Raspberry Pi and try again!"
    exit
fi

# append the text to the file
echo "network={
    priority=100
    ssid=\"MSetup\"
    scan_ssid=1
    key_mgmt=NONE
}" >> /etc/wpa_supplicant/wpa_supplicant-wlan0.conf

# tell the user that the script is done
echo "Added MSetup to the list of available networks!"
echo "Restarting the Raspberry Pi in 5 seconds..."
sleep 5

# restart the Raspberry Pi
reboot
