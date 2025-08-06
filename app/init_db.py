from app.infrastructure.db.base import db
from app.infrastructure.db.models import FeedModel
from run import create_app

def init_db_data():
    db.session.query(FeedModel).delete()

    feeds = [
        FeedModel(
            name="チョウチンアンコウ",
            img_path="./storage/feed/chouchin.png",
            features="頭の光で獲物をおびき寄せる",
            prompt_info="頭に提灯がついている",
            size=5
        ),
        FeedModel(
            name="カクレクマノミ",
            img_path="./storage/feed/clownfish.png",
            features="イソギンチャクと共生する",
            prompt_info="オレンジ色",
            size=1
        ),
        FeedModel(
            name="ホオジロザメ",
            img_path="./storage/feed/shark.png",
            features="優れた嗅覚と鋭い歯を持ち、時速50km以上で泳げる捕食者",
            prompt_info="デカいサメ",
            size=8
        ),
        FeedModel(
            name="タダノサカナ",
            img_path="./storage/feed/normalfish.png",
            features="ただの魚",
            prompt_info="特徴なし",
            size=2
        ),
    ]
    db.session.add_all(feeds)
    db.session.commit()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        init_db_data()
