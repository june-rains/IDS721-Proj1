# IDS721-Proj1
[![Python Flask](https://github.com/june-rains/IDS721-Proj1/actions/workflows/main.yml/badge.svg)](https://github.com/june-rains/IDS721-Proj1/actions/workflows/main.yml)

***This is my study for AWS + Flask project***

The repository contains a RESTful API built with Flask for find the Longest Palindrome Substring in a string, You can use the following endpoints:

`[GET] /` - Access the index page.  
`[POST] /lengthPalindrome` - enter a string, and then find the longest palindrome substring in it

**Note**: <i> Yes, it is Leetcode 5, to keep the API simple, nothing fancy :)</i>

## Overall WorkFlow
![IDS721-Proj1-WorkFlow](https://user-images.githubusercontent.com/71317967/216917868-db0e3436-e9eb-46a2-9e19-90370f83a473.jpg)


## Local Run

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask --app application.py run
```

## AWS Elastic BeanStalk URL
you can also use this [link](http://flaskapp-env.eba-7rppqvxb.us-east-1.elasticbeanstalk.com/) to call my Flask API 

## Demo Video


