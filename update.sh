#!/bin/bash
clear
echo -e "\e[94m╔══════════════════════════════════╗"
echo -e "\e[94m║\e[97m GPRAISE BOOSTER - UPDATE DB \e[94m║"
echo -e "\e[94m╚══════════════════════════════════╝\e[0m"
echo -e "\e[93m>> Pulling latest 200+ phones DB...\e[0m"
git pull origin main
if [ $? -eq 0 ]; then
  echo -e "\e[92m>> Update success! ✓\e[0m"
  echo -e "\e[93m>> New phones added, sensitivity improved!\e[0m"
else
  echo -e "\e[91m>> No git found, re-clone manually:\e[0m"
  echo -e "\e[97m git clone https://github.com/Gamerpraise/gpraise-gaming-booster\e[0m"
fi
sleep 1
echo -e "\e[93m>> Starting booster...\e[0m"
bash setup.sh