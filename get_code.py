#!/usr/bin/python
import urllib2
import re
import os
import subprocess
subprocess.call(['hg', 'clone', 'http://hg.tryton.org/3.0/trytond'])
subprocess.call(['hg', 'clone', 'http://hg.tryton.org/3.0/tryton'])
subprocess.call(['hg', 'clone', 'http://hg.savannah.gnu.org/hgweb/health'])

res = urllib2.urlopen("http://hg.tryton.org/3.0/modules/?sort=name")
content = res.read()
pattern = '<td><a href="/modules/(.*)/">'
list_modules = re.findall(pattern, content)
for module in list_modules:
    subprocess.call(['hg', 'clone', 'http://hg.tryton.org/3.0/modules/'+module,
        'trytond/trytond/modules/'+module])
thedir = 'health/tryton/'
dirs = [ name for name in os.listdir(thedir) if os.path.isdir(os.path.join(thedir, name)) and 'health' in name ]
for item in dirs:
    print item
    os.symlink('../../../health/tryton/'+item,'trytond/trytond/modules/'+item)
