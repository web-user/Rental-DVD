# django


1. `docker-compose up`

2. `docker exec -it <container-id> bash`

3. `python manage.py makemigrations`

   `python manage.py migrate`
   
   `python manage.py createsuperuser`
   
   `python manage.py collectstatic`

   `python manage.py loaddata products/fixtures/products.json`
   
    `# Run just one test case`
    
    `$ ./manage.py test animals.tests.AnimalTestCase`
    
    `# Run just one test method`
    
    `$ ./manage.py test animals.tests.AnimalTestCase.test_animals_can_speak`
   
   `curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"title":"xyz123","content":"xyz-123 vvv"}' \
  http://127.0.0.1:8085/rentaldvd/api/`
  
  http://127.0.0.1:8085/api/auth/register/