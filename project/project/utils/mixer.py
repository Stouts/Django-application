from __future__ import absolute_import

from mixer.backend.django import mixer


@mixer.middleware('auth.user')
def set_password(user):
    user.set_password(user.password)
    return user
