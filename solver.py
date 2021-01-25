import random
import requests
from flask import Flask, request

server = Flask(__name__)

def verify_text(input_string):
    list_open = []
    for c in input_string:
        if c in ["(", "[", "{"]:
            list_open.append(c)
        elif c in [")", "]", "}"]:
            if not list_open:
                return (f"INPUT: {input_string} -- RESULT: BAD INPUT : {c}\n")
            x = list_open.pop()
            if x == "(" and c !=")":
                return(f"INPUT: {input_string} -- RESULT: BAD INPUT : {c}\n")
            if x == "[" and c !="]":
                return(f"INPUT: {input_string} -- RESULT: BAD INPUT : {c}\n")
            if x == "{" and c !="}":
                return(f"INPUT: {input_string} -- RESULT: BAD INPUT : {c}\n")
    if not list_open:
        return(f"INPUT: {input_string} -- RESULT: OK!\n")
    return(f"INPUT: {input_string} -- RESULT: BAD INPUT : Need a close\n")

@server.route("/solve", methods = ['POST', 'GET'])
def solve_input():
    input_string = request.get_data().decode()
    if input_string == "":
        input_string = requests.get('http://localhost:5000/input').content.decode()
    res = verify_text(input_string)
    return res + "\n"

if __name__ == "__main__":
    print("Starting server solver")
    server.run(host="0.0.0.0", port = 5001)
