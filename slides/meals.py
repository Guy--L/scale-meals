from sqlalchemy import create_engine, Column, String, Enum, ForeignKey, Table, ARRAY, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class MainCategory(Base):
    __tablename__ = 'main_category'
    
    category_id = Column(String, primary_key=True)
    category_name = Column(String, nullable=False)
    
class GroupCategory(Base):
    __tablename__ = 'group_category'
    
    group_category_id = Column(String, primary_key=True)
    categories = Column(ARRAY(String))
    
class CuisineType(Base):
    __tablename__ = 'cuisine_type'
    
    id = Column(String, primary_key=True)
    cusin_type = Column(String)
    
class OrderItem(Base):
    __tablename__ = 'order_item'
    
    order_item_id = Column(String, primary_key=True)
    ingredients = Column(ARRAY(String))
    order_id = Column(String)
    dishName = Column(String)
    meal_type = Column(Enum('b', 'd', 'l', name='meal_type'))  # 'b' for breakfast, 'd' for dinner, 'l' for lunch
    cuisine_type = Column(String, ForeignKey('cuisine_type.id'))
    dish_info = Column(String)
    preparation_time = Column(TIMESTAMP)
    main_category = Column(String, ForeignKey('main_category.category_id'))
    category = Column(String, ForeignKey('group_category.group_category_id'))

    cuisine_type_rel = relationship('CuisineType', backref='order_items')
    main_category_rel = relationship('MainCategory', backref='order_items')
    group_category_rel = relationship('GroupCategory', backref='order_items')

# Database connection
engine = create_engine('sqlite:///your_database.db')

# Create tables
Base.metadata.create_all(engine)

# Creating a session
Session = sessionmaker(bind=engine)
session = Session()

# Add some initial data if needed
main_category = MainCategory(category_id='1', category_name='Dish')
session.add(main_category)

group_category = GroupCategory(group_category_id='1', categories=['1'])
session.add(group_category)

cuisine_type = CuisineType(id='1', cusin_type='Italian')
session.add(cuisine_type)

order_item = OrderItem(
    order_item_id='1',
    ingredients=['Tomato', 'Cheese'],
    order_id='1',
    dishName='Pizza',
    meal_type='d',
    cuisine_type='1',
    dish_info='Classic Italian pizza with tomato and cheese',
    preparation_time='2023-05-10 12:00:00',
    main_category='1',
    category='1'
)
session.add(order_item)

# Commit the session
session.commit()
