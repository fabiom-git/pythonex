# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:59:08 2013

----- Python -----
ex5) modules

@author: fabio
"""

""" 
Supponiamo che in un file fibo.py siano definite
le funzioni in ex4) fib1(n) e fib2(n). E' possibile
includere le funzioni nello script corrente tramite 'import'
"""
import fibo

#chiamata
fibo.fib1(n)
fibo.fib2(n)

"""
Se si desiderano le funzioni allo stesso livello del main, utilizzare
'from'
"""
from fibo import *
#oppure singolarmente:
from fibo import fib1
#quindi la chiamata diventa:
fib1(n)

"""
I moduli possono essere precompilati nel corrispondente file .pyc,
usare modulo 'compileall'
"""

#----- sys()
#----- dir()
import fibo
dir(fibo) # visualizza i membri del modulo

# funzioni e variabili builtin
import __builtin__
dir(__builtin__)  

# livello corrente
dir()

"""
PACKAGES:

esempio da tutorial:
    
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
"""
# importazione di un modulo singolo (echo.py)
import sound.effects.echo

#chiamata di una funzione:
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

#oppure:
from sound.effects import echo

#import tra moduli dello stesso package
from . import echo               # importa echo, fratello del mod corrente
from .. import formats           # importa tutto formats, livello superiore
from ..filters import equalizer  # da filters (superiore) importa solo equalizer

