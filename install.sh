#! /bin/bash

#安装依赖
sudo apt-get install xclip -y
sudo apt-get install libnotify-bin -y
sudo apt-get install notify-send -y
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
