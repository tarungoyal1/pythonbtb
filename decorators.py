# escape_unicode is a decorator that decorates f which is passed as an arg to it
def escape_unicode(f):
    # wrap simply uses extended arg syntax make f accepts any number of args
    def wrap(*args, **kwargs):
        # takes return value of f and assign to named ref x
        x = f(*args, **kwargs)
        # return non-ascii chars to escape seq
        return ascii(x)

    # here wrap is behaving just like f excepts it returns non-ascii chars to escape seq


    # decorator accepts callable (f) as an arg and returns new callable wrap
    return wrap

# we have decorated northern_city with our decorator @escape_unicode
@escape_unicode
def northern_city(name):
    return name

print(northern_city('I have £'))