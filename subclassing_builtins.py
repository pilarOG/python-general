# Taken from the Udemy course https://www.udemy.com/python-beyond-the-basics-object-oriented-programming/learn/v4/content

# Example of built-ins inheritance to specify behavior given polimorphic interfaces of magic methods

# Excelent example where the behavior of a list, MyList, is changed by modifying the way indexes work, forcing it to
# start index at 1 instead of 0 as in general Python lists.

class MyList(list):                             # Inherites from built-in list class
    def __getitem__(self, index):               # Redefines __getitem__ magic method, equivalent to x[y] syntax
        if index == 0: raise IndexError         # 0 indexing is now considered an error
        if index > 0: index -= 1                # Every other index is decreased by 1
        return list.__getitem__(self, index)    # The new index is used to actually use the original __getitem__ in the original built-in

    def __setitem__(self, index, value):
        if index == 0: raise IndexError
        if index > 0: index -= 1
        list.__setitem__(self, index, value)

    def __repr__(self):
        new = ''                                # (I added this extra) this magic method defines the behaviour of the print
        for n in self:                          # statement. It is redefined to print each element of your list
            new += n+'\n'
        return new


x = MyList(['a', 'b', 'c'])                     # Define instance of new class
print x                                         # New printing behaviour

x.append('spam')                                # Append works just fine, on the back using the new __setitem__

print x[1]                                      # Now index == 1 retrieves the first element in the list
print x[4]                                      # While index == 4 the just appended item
print x[0]                                      # And if we try to use zero we get an error
