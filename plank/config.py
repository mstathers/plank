import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # TODO autogen this from Makefile
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app/data/plank.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # TODO set this from the Makefile perhaps
    UPLOADED_IMG_DEST = "app/data/content/img"
    UPLOADED_IMG_URL = "/content/img/"
