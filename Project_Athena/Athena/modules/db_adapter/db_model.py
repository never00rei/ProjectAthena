# coding: utf-8
from sqlalchemy import ARRAY, Boolean, Column, ForeignKey, Text, text, TEXT
from sqlalchemy.dialects.postgresql.base import INET, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class ServiceCheck(Base):
    __tablename__ = 'service_check'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    service_id = Column(ForeignKey('services.id'))
    check_type = Column(Text, nullable=False)
    check_url = Column(Text)
    check_ip = Column(INET)
    is_active = Column(Boolean, server_default=text("true"))

    service = relationship('Service')


class Service(Base):
    __tablename__ = 'services'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    service_name = Column(Text, nullable=False)
    service_description = Column(Text, nullable=False)
    keywords = Column(ARRAY(TEXT()))


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True, server_default=text("uuid_generate_v4()"))
    slack_user_id = Column(Text, nullable=False)
    slack_team_id = Column(Text, nullable=False)
    slack_real_name = Column(Text, nullable=False)
    slack_username = Column(Text, nullable=False, unique=True)
    active = Column(Boolean, server_default=text("true"))
    is_owner = Column(Boolean, server_default=text("false"))
    is_admin = Column(Boolean, server_default=text("false"))
    can_manage_integrations = Column(Boolean, server_default=text("false"))
    can_manage_services = Column(Boolean, server_default=text("false"))
    can_manage_users = Column(Boolean, server_default=text("false"))
