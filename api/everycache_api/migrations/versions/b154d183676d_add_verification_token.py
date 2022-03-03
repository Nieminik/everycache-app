"""Add user.verification_token

Revision ID: b154d183676d
Revises: 3b01865de320
Create Date: 2022-02-28 22:46:28.108505

"""

import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic
revision = "b154d183676d"
down_revision = "3b01865de320"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column(
            "verification_token",
            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
            nullable=True,
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "verification_token")
    # ### end Alembic commands ###
