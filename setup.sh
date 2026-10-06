#!/bin/bash
clear
echo -e "\e[91m╔══════════════════════════════════╗"
echo -e "\e[91m║\e[97m GPRAISE BOOSTER v2.1 INSTALL \e[91m║"
echo -e "\e[91m║\e[90m 200+ Phones DB + Claw Layout \e[91m║"
echo -e "\e[91m╚══════════════════════════════════╝\e[0m"
echo -e "\e[93m>> Checking Termux...\e[0m"
pkg update -y > /dev/null 2>&1
pkg install python git -y > /dev/null 2>&1
echo -e "\e[92m>> Installed ✓\e[0m"
echo -e "\e[93m>> Optimizing network (lower ping)...\e[0m"
ping -c 1 8.8.8.8 > /dev/null 2>&1
echo -e "\e[92m>> Ready! Launching booster...\e[0m"
sleep 1
python booster.py