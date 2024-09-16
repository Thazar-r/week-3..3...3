# tests/test_models.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.band import Band
from models.venue import Venue
from models.concert import Concert
from base import Base

DATABASE_URL = 'sqlite:///test_concerts.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Create tables for testing
Base.metadata.create_all(engine)

def test_band_methods():
    band = session.query(Band).first()
    assert band
    venues = band.get_venues()
    assert len(venues) >= 0
    introductions = band.generate_introductions()
    assert len(introductions) >= 0

def test_venue_methods():
    venue = session.query(Venue).first()
    assert venue
    bands = venue.get_bands()
    assert len(bands) >= 0
    concert = venue.find_concert_on('2024-09-16')
    assert concert is None
    frequent_band = venue.get_most_frequent_band(session)
    assert frequent_band is None

def test_concert_methods():
    concert = session.query(Concert).first()
    assert concert
    assert concert.is_hometown_show() is not None
    introduction = concert.create_introduction()
    assert introduction
