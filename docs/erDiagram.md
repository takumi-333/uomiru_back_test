erDiagram
    USERS {
        string id PK
        string hashed_pass "NOT NULL"
    }

    FISH {
        int id PK "AUTO_INCREMENT"
        int size "NOT NULL"
        string img_path "NOT NULL"
        string user_id "UNIQUE, FK"
    }

    FEED {
        int id PK "AUTO_INCREMENT"
        string img_path "NOT NULL"
        string features
        string metadata
        int size
    }

    USERS ||--|| FISH : "has"
