"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup


ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
    Get("/", "EntryController@index").name("index"),
        Get("/@id", "EntryController@show").name("show"),
        Post("/", "EntryController@create").name("create"),
        Put("/@id", "EntryController@update").name("update"),
        Delete("/@id", "EntryController@destroy").name("destroy"),
    ], prefix="/entry", name="entry")
]
