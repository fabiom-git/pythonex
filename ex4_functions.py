# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:33:33 2013

----- Python -----
ex4) Functions

@author: FabioM-2013
"""

# definition of the Fibonacci function
def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b
# here, the end of the function

fib(2000)
funzione=fib

# function with return of values
def fib2(n):
    """Print a Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result #otherwise return Null

vall=fib2(200)

# ----- default parameters
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

# if ok IN ... ok deve trovarsi all'interno di un set
# esempi di chiamata:
#ask_ok('sì o no, prego: ','uffaaaa! riprova')   # non funziona
ask_ok('sì o no, prego: ',2,'uffaaaa! riprova') # OK


# ----- variable scope
i = 5
def f(arg=i):    # now i=5
    print arg

i = 6 
f() # the function still has i=5
# NB: with list, the list will be updated

# ----- Keyword Arguments -----
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    #function
    print voltage, state, action, type
    
# keyword arguments must follow positional arguments.
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# -----
def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
        
    print keywords.keys()
    print sorted(keywords.keys())
    
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]
        
# chiamata
cheeseshop('parmigiano','brutto...','bruttissimo...',key1='chiave1',key2='chiave2')
# item2-3 fan parte di arguments, mentre item3-4 sono evidentemente
# delle keyworkds key=...