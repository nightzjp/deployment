# -*- coding: utf-8 -*-

"""
@author: Mr_zhang
@software: PyCharm
@file: urls.py
@time: 2021/11/19 上午11:39
"""

from django.urls import path

from apps.websocket import views

websocket_urlpatterns = [
    path('ws/push', views.WebSocket.as_asgi())
]