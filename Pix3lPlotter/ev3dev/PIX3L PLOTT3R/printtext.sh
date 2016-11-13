#!/bin/bash
convert -monochrome -background white -fill black  -pointsize 72 label:"$1" result.png
sudo python printmonochromenew.py result.png

