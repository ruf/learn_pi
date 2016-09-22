#!/bin/bash
#
# generates an 8 bit color table (256 colors) for
# reference purposes, using the \033[48;5;${val}m
# ANSI CSI+SGR (see "ANSI Code" on Wikipedia)
#
# It is also possible (in these newfangled modern times) 
# to use a full 256 colors in most consoles. The color 
# table below can be used to determine the code for each
# color by adding the column and row number. In order to
# make use of these codes, we use the syntax 33[38;5;#m
# for the foreground (text) and 33[48;5;#m for the back-
# ground, or in a single statement like 33[38;5;#;48;5;#m
# to set both at once, where # is an 8-bit (0-255) color code.

echo -en "\n   +  "
for i in {0..15}; do
  printf "%2b " $i
done

for i in {0..15}; do
  let "i = i*16"
  printf "\n %3b  " $i
  for j in {0..15}; do
    let "val = i+j"
    echo -en "\033[48;5;${val}m   \033[m"
  done
done

echo -e "\n"
