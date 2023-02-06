from flask import Flask, render_template, url_for
from flask import request

 
application = Flask(__name__)

@application.route('/')
def hello_world():
    return render_template('index.html')

# use this GET API to calculate the length of the longest palindrome substring
# we assume that the input is just containing the digits and English letters
@application.route('/lengthPalindrome', methods=['POST'])
def get_length():
    if request.method == 'POST':
        input = request.form['input']
        n = len(input)
        # corner case: when the input is just one letter, we can directly return input
        if n < 2:
            return render_template('index.html', results=input)

        # initialize the dp table
        dp = [[False] * n for _ in range(n)]
        # base case: single letter must be palindrome
        for i in range(n):
            dp[i][i] = True
        
        maxLen = 1
        left = 0
        right = 0
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if j - i <= 2:
                    if input[i] == input[j]:
                        dp[i][j] = True
                else:
                    if input[i] == input[j]:
                        dp[i][j] = dp[i+1][j-1]
                
                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    left = i
                    right = j
    return render_template('index.html', results=input[left:right+1])




        
    

