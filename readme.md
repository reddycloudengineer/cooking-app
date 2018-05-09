models
    category
        id
        type
        name
    places
        id
        name
        city
        state
        country
        lat
        long -> None
        category_id -FK

api/ q=? restruant_name? category? place? city? zipcode? query?

search [zipcode, restrunate name, category, city]

api --> zipcode --> ListView of objects (GET)
    -->

admin --> register. category
      --> register. places

JWT --> google/ facebook/ twitter / JWT/ Basic authentication


#######part 2 #################

models:
    reviews:
        id
        places_id FK
        comment_text
        image_address
        rating

    #how to extend the exisitng user model in DRF
    user:
        id
        user_name
        email
        password
        zipcode
        address

Registration form -- user
api/login
api/register
api/forgotpassword


Review form --user

#pusht this github
#AWS -EC2 or S3  --Store the images


#create part 2
get - comments - filterset, viewset, views

c,d,p,post


git commands:

echo "# cooking-app" >> README.md
git init
git add .
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/reddycloudengineer/cooking-app.git
git push -u origin master

