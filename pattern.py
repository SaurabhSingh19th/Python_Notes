# Triangle Pattern : =>
# -------------------------------------------------------------------------------------------------------------------

# Left Justified Triangle
# for i in range(1, 6):
#     print(f"{'* '*i:<5}")

"""
*
* *
* * *
* * * *
* * * * *
"""


# Right Justified Triangle
# for i in range(1, 6):
#     print(f"{' *'*i:>10}")

"""
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""

# Equilateral Triangle
# for i in range(1, 6):
#     print(f"{'* ' * i : ^10}")

"""
    *     
   * *    
  * * *   
 * * * *  
* * * * * 
"""

# for i in range(1, 6):
#     print(f"{' *' * i : ^10}")

"""
*    
    * *   
   * * *  
  * * * * 
 * * * * *
"""


# Inverted Triangles (Left Justified)
# for i in range(6, 0, -1):
#     print(f"{'* ' * i: <6}")
"""
* * * * * * 
* * * * * 
* * * * 
* * * 
* *   
*   
"""

# Inverted Triangles (Right Justified)
# for i in range(6, 0, -1):
#     print(f"{'* '*i:>12}")
"""
* * * * * * 
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
"""


# Inverted Triangles (Centre)
# for i in range(6, 0, -1):
#     print(f"{'* '*i:^12}")

"""
 * * * * * *
  * * * * * 
   * * * *  
    * * *   
     * *    
      * 
"""


# Number Pattern in triangle: =>
# ------------------------------------------------------------------------------------------------------------------

# Left Justified

# pat = ''
# for i in range(1, 6):
#     pat += str(i) + " "
#     print(f'{pat:<5}')

"""
1    
1 2  
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""

# Number Pattern in triangle (Right Justified)
# pat = ''
# for i in range(1, 6):
#     pat += str(i) + " "
#     print(f'{pat:>10}')

"""
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5

"""
# Number Pattern in triangle (Centre)
# pat = ''
# for i in range(1, 6):
#     pat = pat + ' ' + str(i)
#     print(f'{pat:^10}')

"""
     1    
    1 2   
   1 2 3  
  1 2 3 4 
 1 2 3 4 5

"""


# Alphabet Pattern
# ------------------------------------------------------------------------------------------------------------------

# Left justification
# pat = ""
# for i in range(ord("a"), ord('d') + 1):
#     pat += chr(i) + " "
#     print(pat)

"""
a 
a b 
a b c 
a b c d 
"""

# Right Justification
# pat = ""
# for i in range(ord("a"), ord("d") + 1):
#     pat += chr(i) + " "
#     print(f'{pat:>8}')

"""
      a 
    a b 
  a b c 
a b c d  
"""

# Central
# pat = ""
# for i in range(ord("a"), ord("d") + 1):
#     pat += chr(i) + " "
#     print(f'{pat:^8}')

"""
   a    
  a b   
 a b c  
a b c d 
"""