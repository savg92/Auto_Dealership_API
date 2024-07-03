# Auto Dealership API
This API serves an auto dealership, facilitating operations such as creating, reading, updating, and deleting cars, managing dealer locations, car features, and user accounts. Built with Django Rest Framework, it offers a comprehensive solution for dealership management.

## Installation
1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the requirements by running
```sh
pip install -r requirements.txt
```
4. Run the migrations using
```sh
python manage.py migrate
```
5. Run the server using
```sh
python manage.py runserver
```

## Features
- **Cars Management:** Add, list, retrieve, update, and delete cars in the dealership inventory.
- **Dealer Locations Management:** Manage dealership locations including adding, listing, updating, and deleting locations.
- **Features Management:** Handle car features including adding, listing, updating, and deleting features.
- **User Management:** Manage user accounts including registration, listing (for admins), updating, and deletion (for super admins).
- **Version Management:** Manage different versions of car features, ensuring the dealership can track changes over time.

## Advanced Usage
- **Authentication and Authorization:** Secure access to the API with user authentication and role-based permissions, ensuring that only authorized users can perform certain operations.

## Running the Server
Navigate to the project directory and run:
```sh
python manage.py runserver
```

### Seeding Data
For initial testing, you can seed the database with sample data by running:

```sh
python manage.py seed_data
```

### Read the API Documentation
The API documentation is available at:
- http://localhost:8000/api/docs/ for the Swagger UI documentation.
- http://localhost:8000/api/ for the Django Rest Framework browsable API.

### Project Structure
The project is structured as follows:

- api/: Contains the Django app including models, views, serializers, and URLs for the API.
- api/token: Contains the token authentication views.
- api/token/refresh: Contains the token refresh views.
- api/docs: Contains the Swagger UI documentation for the API.

### API Endpoints
The API offers the following endpoints:

- /cars: Manage cars in the dealership inventory.
- /locations: Manage dealership locations.
- /features: Manage car features.
- /users: Manage user accounts.
- /versions: Manage different versions of car features.

### API Documentation
The API documentation is available at:
- http://localhost:8000/api/ for the Django Rest Framework browsable API.
- http://localhost:8000/api/docs/ for the Swagger UI documentation.
You can view the API endpoints, make requests, and see the responses using the Swagger UI.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems.

### Conclusion
Ensure your API is properly set up and configured to meet the needs of your auto dealership, and enjoy streamlined management of your inventory, locations, and users.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgements
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Swagger UI](https://swagger.io/tools/swagger-ui/)

