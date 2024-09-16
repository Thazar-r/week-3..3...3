# models/band.py
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from base import Base

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    hometown = Column(String, nullable=False)

    concerts = relationship('Concert', back_populates='band')

    def get_venues(self):
        return [concert.venue for concert in self.concerts]

    def schedule_concert(self, venue, date):
        from models.concert import Concert
        new_concert = Concert(band_id=self.id, venue_id=venue.id, date=date)
        return new_concert

    def generate_introductions(self):
        return [f"Hello {concert.venue.city}! We are {self.name} from {self.hometown}" for concert in self.concerts]

    @classmethod
    def find_most_active_band(cls, session):
        from sqlalchemy import func
        from models.concert import Concert
        result = session.query(cls).join(Concert).group_by(cls.id).order_by(func.count(Concert.id).desc()).first()
        return result
