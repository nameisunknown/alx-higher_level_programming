-- Import the database dump from hbtn_0d_tvshows to your MySQL server:
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql

-- This script uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT tv_genres.name FROM tv_genres 
WHERE tv_genres.name NOT IN (
    SELECT tv_genres.name FROM tv_genres JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id JOIN tv_shows
    ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = 'Dexter'
    )
ORDER BY tv_genres.name;
