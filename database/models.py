from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    Text,
    Float,
    JSON,
    ARRAY,
    TIMESTAMP,
    Index)
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class SKU(Base):
    __tablename__ = 'sku'
    __table_args__ = (
        {'schema': 'public'}, 
 
    )

    uuid = Column(PG_UUID(as_uuid=True), primary_key=True)
    marketplace_id = Column(Integer, nullable=False)
    product_id = Column(BigInteger, nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text)
    brand = Column(Text)
    seller_id = Column(Integer)
    seller_name = Column(Text)
    first_image_url = Column(Text)
    category_id = Column(Integer)
    category_lvl_1 = Column(Text)
    category_lvl_2 = Column(Text)
    category_lvl_3 = Column(Text)
    category_remaining = Column(Text)
    features = Column(JSON)
    rating_count = Column(Integer)
    rating_value = Column(Float)
    price_before_discounts = Column(Float)
    discount = Column(Float)
    price_after_discounts = Column(Float)
    bonuses = Column(Integer)
    sales = Column(Integer)
    inserted_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
        )
    currency = Column(Text)
    barcode = Column(BigInteger)
    similar_sku = Column(ARRAY(PG_UUID(as_uuid=True)))
    

    def __str__(self):
        return (f"<SKU("
                f"uuid={self.uuid}, "
                f"product_id={self.product_id}, "
                f"title={self.title})>")
