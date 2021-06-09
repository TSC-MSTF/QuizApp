import socket
import pickle


SERVER_ADDR = "192.168.1.100"
PORT = 6000
ADDR = (SERVER_ADDR, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

replys = []


def send(reply):
    try:
        client.send(pickle.dumps(reply))
        return pickle.loads(client.recv(4096))
    except socket.error as e:
        print(e)


def main():
    try:
        client.connect(ADDR)
        connection = True
    except socket.error as e:
        print(e)
        
    player = int(client.recv(2048).decode())
    if player == 0:
        print("Rakip Bekleniyor...\nOyuncu Numaran: ", player)
    else:
        print("Oyuncu Numaran:", player)
    

    
    run = True
    index = 0

    while run:
        try:
            game = send("get")

            if not game.ready:
                pass
            elif game.finish() == 0:
                for q in game.question_list:

                    
                    print(q.get_question())
                    q.print_options()

                    reply = input("Cevap: ")
                    if player == 0:
                        replys.append(reply)
                    else:
                        replys.append(reply)
                
                game = send(replys)
                print("Rakip Bekleniyor...")
            else:
                if game.finish() == 2:
                    if player == 0:
                        print(f"Senin Puanın: {game.players_scores[0]}\t\t", end = '')
                        print(f"Rakibinin Puanı: {game.players_scores[1]}")
                        print("Rakibin Cevapları".center(50))
                        for i in range(len(game.player2_replys)):
                            print(i + 1, game.player2_replys[i], end = ' ')
                    else:
                        print(f"Senin Puanın: {game.players_scores[1]}")
                        print(f"Rakibinin Puanı: {game.players_scores[0]}")
                        print("Rakibin Cevapları".center(50))
                        for i in range(len(game.player1_replys)):
                            print(f"({i + 1}), {game.player1_replys[i]}", end = ' ')

                    run = False
        except:
            run = False
    



main()
