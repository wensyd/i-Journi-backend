# i-Journi - Capstone Project
#### By Wensy DeSousa

## Project Summary

I-Journi is a journal application with a masonite backend. The backend has an index, show, create, update, and delete routes. The backend also uses a Postgres database and is deployed as a Heroku application. 

## Schema


{
    table.increments("id")
    table.string("date")
    table.string("title")
    table.string("body", length= 3000)
    table.timestamps()
}

## Route Table

List your routes in a table

| url | method | action |
|-----|--------|--------|
| /entry | get | get all entries (index)|
| /entry/:id | get | get a particular entry (show)|
| /entry/new | get | return form to create a new entry (new)|
| / | post | get post request to /entry, create new and redirect to index (create)|
| /entry/:id/edit | get | edit a particular entry (edit)|
| /entry/:id | put | put request to /entry/:id (update)|
| /entry/:id | delete | deletes a particular entry (destroy)|

## User Stories

-user can view all entries on main page (index).
-user can select entry and it redirects to show page for that particular entry. 
-user can edit entry, title, and body of each entry.
-user can delete entry.
-user can update entry.
-user can create new entry. 


## List of Technologies

-Python 
-Masonite
-JS
-Postgres

## Challenges

- The biggest challenge was the naming to match when creating the seed files. Another challenge I ran into was not being able to create a new entry. This was resolved by viewing the preview error in postman and it showed there was an error with the middleware, which was fixed by exempting the CSFR middleware routes. 
