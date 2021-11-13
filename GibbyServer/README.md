# build
docker build -t gibby-server . 

# run a bash
docker run --rm -v /Users/jeffrey/Projects/ChessAI/GibbyServer:/home -it gibby-server  

# run python
docker run --rm -v /Users/jeffrey/Projects/ChessAI/GibbyServer:/home gibby-server python /home/src/main.py

# run server
docker run --rm -p 8888:8888 -v /Users/jeffrey/Projects/ChessAI/GibbyServer:/home gibby-server python /home/src/server.py

