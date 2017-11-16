#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 02:15:32 2017

@author: chuishunhui
"""
from django.conf.urls import url

from . import views




urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),

]