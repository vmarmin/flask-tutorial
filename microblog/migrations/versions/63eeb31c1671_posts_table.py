"""posts table

Revision ID: 63eeb31c1671
Revises: 719a3eb99601
Create Date: 2020-01-08 14:35:36.647785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "63eeb31c1671"
down_revision = "719a3eb99601"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "post",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("body", sa.String(length=140), nullable=True),
        sa.Column("timestamp", sa.DateTime(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_post_timestamp"), "post", ["timestamp"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_post_timestamp"), table_name="post")
    op.drop_table("post")
    # ### end Alembic commands ###
