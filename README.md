
## How to build container
docker build -t flask-regex-app .


## How to run container locally 
docker run -p 5000:5000 flask-regex-app


## How to access app locally
http://127.0.0.1:5000/


## TODOs
1. [x] Basic MVP code implemented
2. [ ] Improve better pattern and string text box sizes for visual improvement 
3. [ ] Improve matched output box 
4. [ ] Add most frequently used regex examples and python regex documentation link 
5. [ ] Deploy to aws lambda add security some request rate limiter per hour etc 

