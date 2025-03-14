"""ahora es sin data y con url el archivo

Revision ID: 219d404ab85a
Revises: dd0b11410e96
Create Date: 2025-02-22 04:14:49.416665

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '219d404ab85a'
down_revision = 'dd0b11410e96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('archivo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('file_url', sa.String(length=255), nullable=False))
        batch_op.drop_column('data')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('archivo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data', postgresql.BYTEA(), autoincrement=False, nullable=False))
        batch_op.drop_column('file_url')

    # ### end Alembic commands ###
