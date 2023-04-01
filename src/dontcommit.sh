#!/bin/bash
patternArray=('phoenix' 'peacock' 'monkey-knife-fight' 'shrimp-cocktail' 'mandelbrot' 'mandelbrot-zoomed' 'spiral0' 'spiral1' 'seahorse' 'elephants' 'leaf' 'starfish')
for pattern in ${patternArray[@]}; do
  python src/main.py ${pattern}
  echo "Comparing" ${pattern}
  cmp ${pattern}.png backup/${pattern}.png
done