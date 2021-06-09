import socket
import pickle
from _thread import *
from game import *

SERVER_ADDR = socket.gethostbyname(socket.gethostname())
PORT = 6000
games = {}
id_count = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((SERVER_ADDR, PORT))
except socket.error as e:
    print(e)

server.listen()
print("[ACTIVATED] Server is Activated.")

def threaded_client(conn, player, game_id):
    global id_count
    run = True
    conn.send(str.encode(str(player)))

    while True:
        try:
            reply = pickle.loads(conn.recv(4096))
            

            if game_id in games:
                game = games[game_id]

                if not reply:
                    break
                else:
                    if reply == "reset":
                        game.reset_game()
                    elif reply != "get":
                        game.play(player, reply)
                        print(game.players_scores)
                    

                print("Game Sended.")
                conn.sendall(pickle.dumps(game))
            else:
                break
        except socket.error as e:
            print(e)
            break
        
    print("[CONNECTION ERROR]")
    try:
        del games[game_id]
        print("Closing Game", game_id)
    except:
        pass
    id_count -= 1
    conn.close()
    
    

while True:
    conn, addr = server.accept()
    print("Connected to:", addr)
    id_count += 1

    player = 0
    game_id = (id_count - 1) // 2

    if id_count % 2 == 1:
        games[game_id] = Game(game_id, question_list)
        print("[NEW GAME] Creatin a New Game")
    else:
        games[game_id].ready = True
        player = 1
    
    start_new_thread(threaded_client, (conn, player, game_id))
