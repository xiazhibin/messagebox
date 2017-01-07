"""add user

Revision ID: 00ab3966a429
Revises: f960d0ab4ae3
Create Date: 2017-01-07 12:27:18.456870

"""

# revision identifiers, used by Alembic.
revision = '00ab3966a429'
down_revision = 'f960d0ab4ae3'

import sqlalchemy as sa
from alembic import op
from sqlalchemy import Table, MetaData

user_table = Table(
    'user', MetaData(),
    sa.Column('id', sa.Integer(), primary_key=True),
    sa.Column('nickname', sa.String()),
    sa.Column('role', sa.Integer())
)


def upgrade():
    _add_user(nickname='admin', role=0)
    _add_user(nickname='userA', role=8)
    _add_user(nickname='userB', role=8)
    _add_user(nickname='userC', role=8)


def _add_user(nickname, role):
    connection = op.get_bind()

    connection.execute(
        user_table.insert().values(nickname=nickname, role=role)
    )


def _delete_user(nickname):
    connection = op.get_bind()

    connection.execute(
        user_table.delete().where(user_table.c.nickname == nickname)
    )


def downgrade():
    _delete_user(nickname='admin')
    _delete_user(nickname='userA')
    _delete_user(nickname='userB')
    _delete_user(nickname='userC')
