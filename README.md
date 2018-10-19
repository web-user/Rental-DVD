# Django


`docker-compose up -d --force-recreate`

`docker exec -it <container-id> bash`

`docker-compose run web python videostore/ makemigrations`

`docker-compose run web python videostore/y migrate`

`docker-compose run web python videostore/ createsuperuser`

`docker-compose run web python videostore/ collectstatic`

   
`# Run test`

`$ docker-compose run web python videostore/manage.py test`


```
curl --header "Content-Type: application/json" \
--request POST \
--data '{"title":"xyz123","content":"xyz-123 vvv"}' \
http://0.0.0.0:8084/rentaldvd/api/
```
  

`http://0.0.0.0:8084/`

`http://0.0.0.0:8084/api/`
`http://0.0.0.0:8084/api/1/`

`http://0.0.0.0:8084/api/auth/register/`
`http://0.0.0.0:8084/api/auth/login/`
  

 `docker-compose stop`