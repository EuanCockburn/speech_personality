#!/bin/bash

clear

echo "The script will now run, all commands are sudo commands"
echo "Now running sudo apt-get -f install"
sudo apt-get -f install

echo "Now installing autoconf"
sudo apt-get install autoconf

echo "Now Installing automake"
sudo apt-get install automake

echo "Installing m4"
sudo apt-get install m4

echo "Installing g++ and gcc"
sudo apt-get install g++
sudo apt-get install gcc

echo "Installing gnuplot"
sudo apt-get install gnuplot
~
~
~
