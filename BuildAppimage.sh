#!/bin/bash
# Set the version the the current version of your project
export VERSION=1
cd Appimage
unlink rootdir/usr/bin/main;
unlink rootdir/AppRun;
cp ../Binary/main rootdir/usr/bin/;
ln -s "$(pwd)"/rootdir/usr/bin/main rootdir/AppRun 
../.dependencies/appimagetool.AppImage ../Appimage/rootdir/