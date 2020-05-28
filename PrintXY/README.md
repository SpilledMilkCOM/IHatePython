# PrintXY

## From Tim Sweeney's [Twitter post](https://twitter.com/TimSweeneyEpic/status/1265451572353552384):

### *Here's a neat test of programming language expressiveness: Can you write a function PrintXY taking an integer n>=0 that prints all strings of length n containing only the characters 'X' and 'Y'? Can you do it without recursion, and without assuming n<=64? Is it readable?*

Technically the `printXY(n)` function in the file `print.py` should do it with a single loop. Leveraging the base 2 (binary) nature of the problem and Python's ability to handle arbitrarily large integeters.

    >>> 2 ** 1000
    10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376

But how to do this purely with loops and **not** take advantage of this feature?  This breaks down if you want to add Z into the mix, you can no longer take advantage of the binary nature of the problem.  Hmmmm...  Maybe for another day...
