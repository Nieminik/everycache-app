from enum import Enum

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_utils.types.choice import ChoiceType

from everycache_api.extensions import db, pwd_context


class User(db.Model):
    class Role(Enum):
        Admin = "admin"
        Default = "default"

    __tablename__ = "users"

    # base properties
    id_ = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, nullable=False, default=False)

    # own properties
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    _password = db.Column("password", db.String(255), nullable=False)
    role = db.Column(
        ChoiceType(Role),
        nullable=False,
        default=Role.Default.value,
    )
    verified = db.Column(db.Boolean, nullable=False, default=False)

    # relationships
    owned_caches = db.relationship("Cache", uselist=True, back_populates="owner")
    cache_visits = db.relationship("CacheVisit", uselist=True, back_populates="user")
    cache_comments = db.relationship(
        "CacheComment", uselist=True, back_populates="author"
    )

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: str):
        self._password = pwd_context.hash(value)

    def verify_password(self, password: str):
        return pwd_context.verify(password, self.password)