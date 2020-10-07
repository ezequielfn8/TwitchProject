--Twich SQL/Data Visualization Project (CodeCademy)
--In this project, you will be working with two training tables that contain Twitch users’ stream (video) viewing data and chat room usage data.

--1. Start by getting a feel for the stream table and the chat table:
--Select all columns from the first 20 rows.
--What columns do the tables have?
SELECT * FROM stream
WHERE subscriber = "true"
LIMIT 20;
--The columns are time, device_id, login, channel, country, player, game, stream_format and subscriber.

--2. What are the unique games in the stream table?
SELECT DISTINCT game FROM stream
WHERE game IS NOT NULL;
--The unique games in the stream table are LoL, DayZ, Dota2, Heroes of the Storm, CS GO, Heartstone, The Binding of Isaac, Agar.io, Gaming Takl Shows, Rocket League, World of Tanks, ARK: Survival Evolved,
-- SpeedRunners, Breaking Point, Duck Game, Devil May Cry 4, Block N Load, Fallout, Batman, Reign of Kings, The Witcher 3, Skyrim, Super Mario Bros 1 and 3, H1Z1, The Last of Us, Depth, Mortal Kombat X, Senran Kagura,
-- The Sims 4, You Must Build a Boat, Choice Chamber, Music, Risk of Rain, GTA V, Besiege, Hektor, Bridge Constructor, Lucius, BlackJack and Cities:Skylines

--3. What are the unique channels in the stream table?
SELECT DISTINCT channel FROM stream;
--The unique channels are frank, george, estelle, morty, kramer, jerry, helen, newman, elaine and susan.

--4. What are the most popular games in the stream table?
SELECT game, COUNT (*) FROM stream
WHERE game IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;
--The most popular games are LoL, Dota 2 and CS GO.

--5. These are some big numbers from the game League of Legends (also known as LoL).
--Where are these LoL stream viewers located?
SELECT country, COUNT (*) FROM stream
WHERE game = "League of Legends"
AND country IS NOT NULL
GROUP BY country
ORDER BY 2 DESC
LIMIT 10;
--Most of the viewers are located in the United States, Canada, Germany and Great Britain.

--6. The player column contains the source the user is using to view the stream (site, iphone, android, etc).
--Create a list of players and their number of streamers.
SELECT player, COUNT(*) FROM stream
GROUP BY 1
ORDER BY 2 DESC;
--The players which are most used by streamers are site, iphone and android.

--7. Create a new column named genre for each of the games.
--Group the games into their genres: Multiplayer Online Battle Arena (MOBA), First Person Shooter (FPS), Survival, and Other.
SELECT CASE
WHEN game = "League of Legends" OR
game = "Dota2" OR
game = "Heroes of the Strom" THEN "MOBA"
WHEN game = "Counter-Strike: Global Offensive" OR
game = "DayZ" OR 
game = "Survival Evolved" THEN "FPS"
ELSE "Other" 
END AS "Genre", COUNT(*) FROM stream
GROUP BY game
ORDER BY COUNT (*) DESC;

--8. How does view count change in the course of a day?
-- Before we get started, let’s run this query and take a look at the time column from the stream table:

SELECT time FROM stream
LIMIT 10;

--9. SQLite comes with a strftime() function - a very powerful function that allows you to return a formatted date.
-- It takes two arguments: strftime(format, column)
--Let’s test this function out:
SELECT time, strftime ('%S', time) as "second"
FROM stream
GROUP BY 1
LIMIT 20;

--10. Okay, now we understand how strftime() works. Let’s write a query that returns three columns:
--The hours of the time column
--The view count for each hour
--Lastly, filter the result with only the users in your country using a WHERE clause.
SELECT strftime ('%H', time), COUNT (*) FROM stream
WHERE country = "AR"
GROUP BY 1;

-- 11. The stream table and the chat table share a column, device_id.
--Let’s join the two tables on that column.

SELECT * FROM stream
JOIN chat2
ON stream.device_id = chat2.device_id
LIMIT 10;

