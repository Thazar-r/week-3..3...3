import os
from dotenv import load_dotenv
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.engine import Engine
from sqlalchemy import event

# Load environment variables from .env file
load_dotenv()

# Set up database connection
db = SQLAlchemy()
migrate = Migrate()

def get_engine():
    # Use the Flask application config to create the SQLAlchemy engine
    return db.get_engine()

def run_migrations_online():
    # Create an engine using Flask app's configuration
    connectable = get_engine()
    
    # Apply the correct configuration settings for migration
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=db.metadata,
            url=current_app.config['SQLALCHEMY_DATABASE_URI']
        )
        
        # Begin the migration environment
        with context.begin_transaction():
            context.run_migrations()

def run_migrations_offline():
    # Configure migration environment for offline mode
    url = current_app.config['SQLALCHEMY_DATABASE_URI']
    context.configure(
        url=url,
        target_metadata=db.metadata,
        literal_binds=True
    )
    
    # Run migrations
    with context.begin_transaction():
        context.run_migrations()

def configure_migrations():
    # Determine whether we're running online or offline migrations
    if current_app.config.get('SQLALCHEMY_DATABASE_URI'):
        run_migrations_online()
    else:
        run_migrations_offline()

# Use Flask-Migrate to apply migrations
def run_migrations():
    from alembic import context
    
    # Run the migration configuration
    configure_migrations()

if __name__ == '__main__':
    run_migrations()
