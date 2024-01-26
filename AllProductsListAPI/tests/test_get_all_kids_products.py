import unittest

from AllProductsListAPI.requests.all_products_list_requests import get_request


class TestAPIallProducts(unittest.TestCase):

    def test_get_all_kids_products(self):
        response = get_request()
        products = response.get("products", [])
        no = 0
        expected_no = 13

        for product in products:
            usertype = product.get("category").get("usertype").get("usertype", "Unknown Category")
            if usertype == "Kids":
                no += 1
                print(no)
            else:
                print("The item is not for kids.")

        actual_no = no
        assert actual_no == expected_no, f"The number of articles for kids should be {expected_no}, instead the actual number of items for kids is {actual_no}"

