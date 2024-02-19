"""Filling the data

Revision ID: ca0468d510ef
Revises: bc807a2875e2
Create Date: 2024-02-19 23:33:06.092150

"""
from typing import Sequence, Union
from models.models import BaseBoard
from alembic import op
import sqlalchemy as sa
import json


# revision identifiers, used by Alembic.
revision: str = 'ca0468d510ef'
down_revision: Union[str, None] = 'bc807a2875e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def make_data() -> list[dict]:
    json_data = json.load(open('hpg_boards.json', encoding='utf-8'))
    data = []
    for item in json_data[0]["fields"]:
        field = {
            "name": item["name"],
            "image": item["image"],
            "type": item["type"],
        }
        if "low" in item:
            field["low"] = item["low"]
        if "high" in item:
            field["high"] = item["high"]
        if "tags" in item:
            tags_string = ""
            for tag in item["tags"]:
                tags_string += tag + ","
            field["tags"] = tags_string
        if "points" in item:
            field["points"] = item["points"]
        if "games" in item:
            games_string = ""
            for game in item["games"]:
                games_string += game + ","
            field["games"] = games_string
        data.append(field)
    return data


def upgrade() -> None:
    data = make_data()
    for item in data:
        op.bulk_insert(BaseBoard.__table__, [item])


def downgrade() -> None:
    op.execute(BaseBoard.__table__.delete())
