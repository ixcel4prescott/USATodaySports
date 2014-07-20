Python 2.7.4 (default, Apr 19 2013, 18:32:33) 
[GCC 4.7.3] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.environ['DJANGO_SETTINGS_MODULE'="mysite.settings"
	   
SyntaxError: invalid syntax
>>> os.environ['DJANGO_SETTINGS_MODULE']= 'mysite.settings'
>>> from polls.model import Poll, Choice

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    from polls.model import Poll, Choice
ImportError: No module named model
>>> from polls.models import Poll, Choice
>>> Polls.objects.all()

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    Polls.objects.all()
NameError: name 'Polls' is not defined
>>> Poll.objects.all()
[]
>>> 
from django.utils import timezone
>>> p = Poll(question="What's new?", pub_date=timezone.now())
>>> p.id
>>> p.save()
>>> p.id
1L
>>> p.question
"What's new?"
>>> p.pub_date
datetime.datetime(2013, 7, 17, 0, 58, 57, 952743, tzinfo=<UTC>)
>>> p.question = "what's up?"
>>> p.save()
>>> Poll.objects.all()
[<Poll: Poll object>]
>>> ================================ RESTART ================================
>>> from polls.models import Poll,Choice

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    from polls.models import Poll,Choice
  File "polls/models.py", line 12
    def __unicode__(self):
      ^
SyntaxError: invalid syntax
>>> from polls.models import Poll,Choice

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    from polls.models import Poll,Choice
  File "polls/models.py", line 1, in <module>
    from django.db import models
  File "/usr/local/lib/python2.7/dist-packages/django/db/__init__.py", line 11, in <module>
    if settings.DATABASES and DEFAULT_DB_ALIAS not in settings.DATABASES:
  File "/usr/local/lib/python2.7/dist-packages/django/conf/__init__.py", line 53, in __getattr__
    self._setup(name)
  File "/usr/local/lib/python2.7/dist-packages/django/conf/__init__.py", line 46, in _setup
    % (desc, ENVIRONMENT_VARIABLE))
ImproperlyConfigured: Requested setting DATABASES, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
>>> import os
>>> os.environ['DJANGO_SETTINGS_MODULE']= 'mysite.settings'
>>> from polls.models import Poll,Choice

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    from polls.models import Poll,Choice
  File "polls/models.py", line 1, in <module>
    from django.db import models
  File "/usr/local/lib/python2.7/dist-packages/django/db/__init__.py", line 40, in <module>
    backend = load_backend(connection.settings_dict['ENGINE'])
  File "/usr/local/lib/python2.7/dist-packages/django/db/__init__.py", line 34, in __getattr__
    return getattr(connections[DEFAULT_DB_ALIAS], item)
  File "/usr/local/lib/python2.7/dist-packages/django/db/utils.py", line 93, in __getitem__
    backend = load_backend(db['ENGINE'])
  File "/usr/local/lib/python2.7/dist-packages/django/db/utils.py", line 27, in load_backend
    return import_module('.base', backend_name)
  File "/usr/local/lib/python2.7/dist-packages/django/utils/importlib.py", line 35, in import_module
    __import__(name)
  File "/usr/local/lib/python2.7/dist-packages/django/db/backends/mysql/base.py", line 33, in <module>
    from django.db import utils
ImportError: cannot import name utils
>>> ================================ RESTART ================================
>>> from polls.models import Poll,Choice

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    from polls.models import Poll,Choice
  File "polls/models.py", line 1, in <module>
    from django.db import models
  File "/usr/local/lib/python2.7/dist-packages/django/db/__init__.py", line 11, in <module>
    if settings.DATABASES and DEFAULT_DB_ALIAS not in settings.DATABASES:
  File "/usr/local/lib/python2.7/dist-packages/django/conf/__init__.py", line 53, in __getattr__
    self._setup(name)
  File "/usr/local/lib/python2.7/dist-packages/django/conf/__init__.py", line 46, in _setup
    % (desc, ENVIRONMENT_VARIABLE))
ImproperlyConfigured: Requested setting DATABASES, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
>>> ================================ RESTART ================================
>>> import os
>>> os.environ['DJANGO_SETTINGS_MODULE']= 'mysite.settings'
>>> from polls.models import Poll,Choice
>>> Poll.objects.all()
[<Poll: what's up?>]
>>> Poll.objects.filter(id=1)
[<Poll: what's up?>]
>>> Poll.objects.filter(question__startswith='What')
[]
>>> Poll.objects.filter(question__startswith='what')
[<Poll: what's up?>]
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Poll.objects.get(pub_date__year=current_year)
<Poll: what's up?>
>>> Poll.objects.get(id=2)

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    Poll.objects.get(id=2)
  File "/usr/local/lib/python2.7/dist-packages/django/db/models/manager.py", line 143, in get
    return self.get_query_set().get(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/django/db/models/query.py", line 389, in get
    (self.model._meta.object_name, kwargs))
DoesNotExist: Poll matching query does not exist. Lookup parameters were {'id': 2}
>>> Poll.objects.get(pk=1)
<Poll: what's up?>
>>> p=Poll.objects.get(pk=1)
>>> p.was_published_recently()
True
>>> 
