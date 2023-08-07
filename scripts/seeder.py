import os
import json
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from app.database import SessionLocal
from app.models import Tag, Dataset, TagCategory, DatasetTag

load_dotenv()
current_dir_path = os.path.abspath(os.path.dirname(__file__))


class Seeder:
    def __init__(self):
        self.db: Session = SessionLocal()

    def seed_tag_categories(self):
        with open(
            os.path.join(current_dir_path, "seeder_data/tag_categories.json"), "r"
        ) as f:
            tag_categories = json.load(f)

        for tag_category in tag_categories:
            try:
                db_tag_category = TagCategory(
                    name=tag_category["name"],
                    hex_color=tag_category["hex_color"],
                    rank=tag_category["rank"],
                )
                self.db.add(db_tag_category)
                self.db.commit()
                self.db.refresh(db_tag_category)
            except:
                print(
                    f"🚨 Tag Category `{tag_category['name']}` already exists, skipping..."
                )
                continue

        print("✅ Seeding tag categories complete." + "\n")

    def seed_tags(self):
        with open(os.path.join(current_dir_path, "seeder_data/tags.json"), "r") as f:
            tags = json.load(f)

        for tag in tags:
            try:
                selected_tag_category = (
                    self.db.query(TagCategory)
                    .filter(TagCategory.name == tag["category"])
                    .first()
                )

                db_tag = Tag(name=tag["name"], tag_category=selected_tag_category)
                self.db.add(db_tag)
                self.db.commit()
                self.db.refresh(db_tag)
            except:
                print(f"🚨 Tag `{tag['name']}` already exists, skipping...")
                continue

        print("✅ Seeding tags complete." + "\n")

    def seed_datasets(self):
        with open(
            os.path.join(current_dir_path, "seeder_data/datasets.json"), "r"
        ) as f:
            datasets = json.load(f)

        for index, dataset in enumerate(datasets):
            try:
                selected_tags = (
                    self.db.query(Tag).filter(Tag.name.in_(dataset["tags"])).all()
                )

                dataset_tags = [
                    DatasetTag(tag_id=tag.id, is_filterable=index == 0)
                    for tag in selected_tags
                ]

                db_dataset = Dataset(
                    name=dataset["name"],
                    description=dataset["description"],
                    dataset_tags=dataset_tags,
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

        self.seed_tag_categories()
        self.seed_tags()
        self.seed_datasets()

        print("✨ Seeding database complete." + "\n")


if __name__ == "__main__":
    seeder = Seeder()
    seeder.run_seed()
