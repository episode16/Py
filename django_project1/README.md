# Product management system in Django
A simple product management system developed using Django. Allows you to add products with details such as name, price, description and quantity.

## Usage
Once your project is set up, you can add a product by going to `/products/create`. Here you can enter the name, price, description and quantity of the product. After filling out the form, click the submit button to save the product in the database.

# Technical details
The project uses Django ORM to interact with the database. The `Product` model contains fields for `name`, `price`, `description` and `quantity`. The Django REST Framework is used to process requests.