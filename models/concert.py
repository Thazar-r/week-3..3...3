# models/concert.py
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, nullable=False)
    band_id = Column(Integer, ForeignKey('bands.id'), nullable=False)
    venue_id = Column(Integer, ForeignKey('venues.id'), nullable=False)

    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    def is_hometown_show(self):
        return self.band.hometown == self.venue.city

    def create_introduction(self):
        return f"Hello {self.venue.city}! We are {self.band.name} from {self.band.hometown}"
