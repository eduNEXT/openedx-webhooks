# coding=utf-8
from __future__ import unicode_literals

from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

from openedx_webhooks import db


class OAuth(db.Model, OAuthConsumerMixin):
    pass
