""" A EntryController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Entry import Entry


class EntryController(Controller):
    """Class Docstring Description
    """

    def __init__(self, request: Request):
        self.request = request


    def show(self):
        id = self.request.param("id")
        return Entry.where("id", id).get()

    def index(self):
       return Entry.all()

    def create(self):
        date = self.request.input("date")
        title = self.request.input("title")
        body = self.request.input("body")
        entry = Entry.create({"date": date, "title": title, "body": body})
        return entry

    def update(self):
        date = self.request.input("date")
        title = self.request.input("title")
        body = self.request.input("body")
        id = self.request.param("id")
        Entry.where("id", id).update({"date": date, "title": title, "body": body})
        return Entry.where("id", id).get()

    def destroy(self):
       id = self.request.param("id")
       entry = Entry.where("id", id).get()
       Entry.where("id", id).delete()
       return entry