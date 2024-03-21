"""'migrate'

Revision ID: 046d040aa82c
Revises: edb80efcf8b1
Create Date: 2024-03-20 12:19:04.423250

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '046d040aa82c'
down_revision = 'edb80efcf8b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_index('isbn')

    op.drop_table('books')
    op.drop_table('companies')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('origin', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('description', mysql.VARCHAR(length=1000), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('books',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('price', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('pages', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('description', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('company_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('publication_date', sa.DATE(), nullable=False),
    sa.Column('isbn', mysql.VARCHAR(length=30), nullable=True),
    sa.Column('genre', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name='books_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.create_index('isbn', ['isbn'], unique=True)

    # ### end Alembic commands ###
