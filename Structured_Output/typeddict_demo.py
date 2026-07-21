from typing import TypedDict

class ProductReview(TypedDict):
    Product_name : str
    rating : int
    review : str


new_review : ProductReview = {
    "Product_name" : "Wireless HeadPhone",
    "rating" : 5,
    "review" : "Excellint Procuct"
}

print(new_review)