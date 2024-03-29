# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model

from cms.utils.conf import get_cms_setting


PERMISSION_KEYS = [
    'add_page', 'change_page', 'change_page_advanced_settings',
    'change_page_permissions', 'delete_page', 'move_page',
    'publish_page', 'view_page',
]




def get_cache_key(user, key):
    username = getattr(user, get_user_model().USERNAME_FIELD)
    return "%s:permission:%s:%s" % (
        get_cms_setting('CACHE_PREFIX'), username, key)


def get_cache_permission_version_key():
    return "%s:permission:version" % (get_cms_setting('CACHE_PREFIX'),)


def get_cache_permission_version():
    from django.core.cache import cache
    try:
        version = int(cache.get(get_cache_permission_version_key()))
    except Exception:
        version = 1
    return int(version)


def get_permission_cache(user, key):
    """
    Helper for reading values from cache
    """
    from django.core.cache import cache
    return cache.get(get_cache_key(user, key), version=get_cache_permission_version())


def set_permission_cache(user, key, value):
    """
    Helper method for storing values in cache. Stores used keys so
    all of them can be cleaned when clean_permission_cache gets called.
    """
    from django.core.cache import cache
    # store this key, so we can clean it when required
    cache_key = get_cache_key(user, key)
    cache.set(cache_key, value,
              get_cms_setting('CACHE_DURATIONS')['permissions'],
              version=get_cache_permission_version())


def clear_user_permission_cache(user):
    """
    Cleans permission cache for given user.
    """
    from django.core.cache import cache
    for key in PERMISSION_KEYS:
        cache.delete(get_cache_key(user, key), version=get_cache_permission_version())


def clear_permission_cache():
    from django.core.cache import cache
    version = get_cache_permission_version()
    if version > 1:
        cache.incr(get_cache_permission_version_key())
    else:
        cache.set(get_cache_permission_version_key(), 2,
                  get_cms_setting('CACHE_DURATIONS')['permissions'])

class A:
    def __mul__(self, other, unexpected):  # Noncompliant. Too many parameters
        return 42
    def __add__(self):  # Noncompliant. Missing one parameter
        return 42
A() * 3  # TypeError: __mul__() missing 1 required positional argument: 'unexpected'
A() + 3  # TypeError: __add__() takes 1 positional argument but 2 were given