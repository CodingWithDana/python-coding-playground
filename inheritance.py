# Good practice - recommended
# inherit from built-in list
class MyList(list):
    """ Defines MyList class that inherits from the built in list """
    # override append()

    def append(self, item):
        print("Adding:", item)
        super().append(item)


ml = MyList([1, 2, 3, 4])
print(f"This is the original list: {ml}")
ml.append(8)
print(f"This is the new list: {ml}")


# Bad practice - not recommended
def new_append(self, item):
    """Print a message and append item to the list (not recommended for global patching) """
    print("Adding:", item)
    return list.append(self, item)
