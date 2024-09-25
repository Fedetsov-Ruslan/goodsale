from uuid import uuid4
import xml.etree.ElementTree as ET
from sqlalchemy.exc import SQLAlchemyError

from database.models import SKU


def orm_add_offer(offer:ET, session, category:list):
    old_price = float(offer.findtext('oldprice', 0.0))
    new_price = float(offer.findtext('price', 0.0))
    if old_price != 0:
        discount = round((old_price - new_price) / old_price * 100, 2)
    else:
        discount = 0
    params = {}
    for param in offer.findall('param'):
        param_name = param.get('name')
        param_value = param.text
        params[param_name] = param_value
    category_lvl_1 = category[0]
    if len(category) > 1:
        category_lvl_2 = category[1]
    if len(category) > 2:
        category_lvl_3 = category[2]
    if len(category) > 3:
        category_remaining = category[3:]
    offer_data = SKU(
        uuid=uuid4(),
        marketplace_id=int(offer.findtext('group_id', 0)),
        product_id=int(offer.get('id', 0)),
        title=offer.findtext('name'),
        description=offer.findtext('description'),
        brand=offer.findtext('vendor'),
        seller_id=int(offer.findtext('seller_id', 0)),
        seller_name=offer.findtext('seller_name'),
        first_image_url=offer.findtext('picture'),
        category_id=int(offer.findtext('categoryId', 0)),
        category_lvl_1=category_lvl_1,
        category_lvl_2=category_lvl_2,
        category_lvl_3=category_lvl_3,
        category_remaining=category_remaining,
        features=params,
        rating_count=int(offer.findtext('rating_count', 0)),
        rating_value=float(offer.findtext('rating_value', 0.0)),
        price_before_discounts=old_price,
        discount=discount,
        price_after_discounts=new_price,
        bonuses=int(offer.findtext('bonuses', 0)),
        sales=int(offer.findtext('sales', 0)),
        currency=offer.findtext('currencyId'),
        barcode=int(offer.findtext('barcode', 0)),
        similar_sku=[],
    )
    session.add(offer_data)
    try:
        session.commit()
    except:
        print("Значение выходит за пределы диапазона bigint")
        session.rollback()
    return offer_data


def orm_get_all(session):
    offset = 0
    batch_size = 1000
    while True:
        batch = session.query(SKU).limit(batch_size).offset(offset).all()
        if not batch:
            break
        yield from batch  
        offset += batch_size 


def orm_update_db_simular_sku(product_analog: dict, session):
    try:
        for product_uuid, similar_uuids in product_analog.items():

            product_record = session.query(SKU).filter(SKU.uuid == product_uuid).first()
            if product_record:
                product_record.similar_sku = similar_uuids 
                session.commit()
                print(f"Updated {product_uuid} with similar_sku: {similar_uuids}")
            else:
                print(f"Product with UUID {product_uuid} not found.")

    except SQLAlchemyError as e:
        session.rollback() 
        print(f"Error occurred: {e}")
        session.close() 
