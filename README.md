Concert Management System

Overview

This project is a basic concert management system using SQLAlchemy ORM with SQLite. It consists of three main models:

Band: Represents a musical band.
Concert: Represents a concert event where a band performs.
Venue: Represents a venue where concerts are held.
Models

Band

Represents a musical band.

Table Name: bands

Columns:

id (Integer, Primary Key, Index): Unique identifier for the band.
name (String, Non-nullable): Name of the band.
hometown (String, Nullable): Hometown of the band.
Relationships:

concerts: One-to-many relationship with Concert.
Methods:

get_venues(): Returns a list of venues where the band has performed.
schedule_concert(venue, date): Schedules a concert for the band.
generate_introductions(): Generates introductions for all concerts the band has performed.
find_most_active_band(session): Finds the most active band based on concert count.
Concert

Represents a concert event.

Table Name: concerts

Columns:

id (Integer, Primary Key, Index): Unique identifier for the concert.
date (String, Non-nullable): Date of the concert.
band_id (Integer, Foreign Key to bands.id, Non-nullable): The band performing.
venue_id (Integer, Foreign Key to venues.id, Non-nullable): The venue where the concert is held.
Relationships:

band: Many-to-one relationship with Band.
venue: Many-to-one relationship with Venue.
Methods:

is_hometown_show(): Returns True if the concert is in the band's hometown.
create_introduction(): Creates an introduction message for the concert.
Venue

Represents a venue where concerts are held.

Table Name: venues

Columns:

id (Integer, Primary Key, Index): Unique identifier for the venue.
title (String, Non-nullable): Name or title of the venue.
city (String, Non-nullable): City where the venue is located.
Relationships:

concerts: One-to-many relationship with Concert.
Methods:

get_bands(): Returns a list of bands that have performed at the venue.
find_concert_on(date): Finds a concert at the venue on a specific date.
get_most_frequent_band(session): Finds the band that has performed most frequently at the venue.
Setup

Install Dependencies:

Ensure you have Python 3.8+ and install the required packages using:

pip install sqlalchemy sqlite

Database Initialization:

Ensure you have a SQLite database set up. You can initialize the database schema using:

from sqlalchemy import create_engine from sqlalchemy.orm import sessionmaker from models.band import Band from models.concert import Concert from models.venue import Venue from base import Base

Create an SQLite database
engine = create_engine('sqlite:///concert_management.db') Base.metadata.create_all(engine)

Running Tests:

Ensure you have pytest installed:

pip install pytest

Run the tests using:

pytest

Repository

You can find the repository at the following locations:

GitHub Repository https://github.com/Thazar-r/week-3..3...3.git (HTTPS)
GitHub Repository git@github.com:Thazar-r/week-3..3...3.git (SSH)
License

This project is licensed under the MIT License - see the LICENSE file for details.


