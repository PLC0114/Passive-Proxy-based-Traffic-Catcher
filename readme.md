# Startup steps

## 1.1 database setup
1. prepare a mongoDB server
2. change the connection parameters for the server in `config.Config`

## 1.2 mitmproxy setup
1. download mitmproxy
2. manually import its https certification(in `.mitmproxy` folder under system user directory)

## 1.3 run the script
1. install dependencies
2. `mitmdump -s ./main.py -p portnum` (portnum is any idle port number)
3. set proxy server address in your system using the same address `127.0.0.1:portnum`