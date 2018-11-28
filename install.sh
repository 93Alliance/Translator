#! /bin/bash

#安装依赖
sudo apt-get install xclip -y
sudo apt-get install libnotify-bin -y
NOTIFY=$(which notify-send)
if [ -z $NOTIFY ]
then
    sudo apt-get install notify-send -y
fi

#将执行文件拷贝到系统环境下
sudo cp -f ./src/translate.py /usr/local/bin/translate
sudo chmod 775 /usr/local/bin/translate
sudo cp -f ./src/fanyi /bin/fanyi
sudo chmod 775 /bin/fanyi
sudo cp -f ./src/transword.py /usr/local/bin/transword
sudo chmod 775 /usr/local/bin/transword
sudo cp -f ./src/addword /bin/addword
sudo chmod 775 /bin/addword
mkdir ~/ydword
sudo chmod 777 ~/ydword

# Ubuntu系统可以自动添加快捷键
currentSystem=$(lsb_release -a | grep 'Distributor ID' 2> /dev/null)
currentSystem=$(echo ${currentSystem#*:})

if [ "$currentSystem" = "Ubuntu" || "$currentSystem" = "LinuxMint" ]
then
	gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom7/ name "fanyi"
	gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom7/ command "fanyi"
	gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom7/ binding "<Alt>period"
fi

