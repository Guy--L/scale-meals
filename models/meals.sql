CREATE TABLE main_category (
    category_id STRING PRIMARY KEY,
    category_name STRING NOT NULL
);

CREATE TABLE group_category (
    group_category_id STRING PRIMARY KEY,
    categories main_category[]
);

CREATE TABLE cuisine_type (
    id STRING PRIMARY KEY,
    cusin_type STRING
);

CREATE TABLE order_item (
    order_item_id STRING PRIMARY KEY,
    ingredients STRING[],
    order_id STRING,
    dishName STRING,
    meal_type ENUM('b', 'd', 'l'),  -- Assuming 'b' for breakfast, 'd' for dinner, 'l' for lunch
    cuisine_type STRING,
    dish_info STRING,
    preparation_time TIMESTAMP,
    main_category STRING,
    category STRING,
    FOREIGN KEY (cuisine_type) REFERENCES cuisine_type(id),
    FOREIGN KEY (main_category) REFERENCES main_category(category_id),
    FOREIGN KEY (category) REFERENCES group_category(group_category_id)
);