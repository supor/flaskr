# -*-coding:utf-8 -*-
from  flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

DATABASE = 'mysql://root:@localhost:3306/blog'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 123456
