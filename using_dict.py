#!/usr/bin/python
# Filename: using_dict.py

ab = {
    'Swaroop':'swaroop@sdfsdf.info',
    'Larry': 'larry@wall.org',
    'rry': 'lry@wall.org'
}
print "Swaroop's address is %s" % ab['Swaroop']

ab['Guido'] = 'guido@python.org'

del ab['rry']

print '\n There are %d contacts in the address-book\n' % len(ab)

for name, address in ab.items():
    print 'Contact %s at %s' % (name, address)


if 'Guido' in ab:
    print "\n Guido's address is %s" % ab['Guido']


