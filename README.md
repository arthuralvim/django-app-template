django-app-template
===================

Similar to django-boot-template (https://github.com/arthuralvim/django-boot-template) but for app templating.


Usage
=====

You can build it directly:

    django-admin.py startapp --template=https://github.com/arthuralvim/django-app-template/archive/master.zip --extension=py,html APPNAME

or you can download it and pass the template path:

    git clone git@github.com:arthuralvim/django-app-template.git
    django-admin.py startapp --template=path/to/django-app-template/ --extension=py,html APPNAME

then you just have to add it to the Django's INSTALLED_APPS and routing.

Ex:

    INSTALLED_APPS += (
        'APPNAME',
    )

and

    urlpatterns += patterns('',
        url(r'^some_pattern/', include('APPNAME.urls', namespace='some_name')),
    )

License
=====

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE

Version 2, December 2004

Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE

TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

0. You just DO WHAT THE FUCK YOU WANT TO.
