import os
import json
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from app.database import SessionLocal
from app.models import Tag, Dataset

load_dotenv()
current_dir_path = os.path.abspath(os.path.dirname(__file__))


class Seeder:
    def __init__(self):
        self.db: Session = SessionLocal()

    def seed_tags(self):
        with open(os.path.join(current_dir_path, "seeder_data/tags.json"), "r") as f:
            tags = json.load(f)

        for tag_name in tags:
            try:
                db_tag = Tag(name=tag_name)
                self.db.add(db_tag)
                self.db.commit()
                self.db.refresh(db_tag)
            except:
                print(f"🚨 Tag `{tag_name}` already exists, skipping...")
                continue

        print("✅ Seeding tags complete." + "\n")

    def seed_datasets(self):
        with open(
            os.path.join(current_dir_path, "seeder_data/datasets.json"), "r"
        ) as f:
            datasets = json.load(f)

        for dataset in datasets:
            try:
                selected_tags = (
                    self.db.query(Tag).filter(Tag.name.in_(dataset["tags"])).all()
                )

                db_dataset = Dataset(
                    name=dataset["name"],
                    description=dataset["description"],
                    tags=selected_tags,
                )
                self.db.add(db_dataset)
                self.db.commit()
                self.db.refresh(db_dataset)
            except:
                print(f"🚨 Dataset `{dataset['name']}` already exists, skipping...")
                continue

        print("✅ Seeding datasets complete." + "\n")

    def run_seed(self):
        print("🌱 Seeding database..." + "\n")

        self.seed_tags()
        self.seed_datasets()

        print("✨ Seeding database complete." + "\n")


if __name__ == "__main__":
    seeder = Seeder()
    seeder.run_seed()
