# models/venue.py
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from base import Base

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    city = Column(String, nullable=False)

    concerts = relationship('Concert', back_populates='venue')

    def get_bands(self):
        return [concert.band for concert in self.concerts]

    def find_concert_on(self, date):
        return next((concert for concert in self.concerts if concert.date == date), None)

    def get_most_frequent_band(self, session):
        from sqlalchemy import func
        from models.concert import Concert
        result = session.query(Concert.band_id, func.count(Concert.id)).filter_by(venue_id=self.id).group_by(Concert.band_id).order_by(func.count(Concert.id).desc()).first()
        from models.band import Band
        return session.query(Band).get(result[0]) if result else None
