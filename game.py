class Question:
    def __init__(self, question, options, correct):
        self.question = question
        self.options = options
        self.correct = correct
    
    def get_question(self):
        return self.question
    
    def get_options(self):
        return self.options
    
    def print_options(self):
        for o in self.options:
            print(o)
    
    def get_correct(self):
        return self.correct

    def check_correct(self, reply):
        if reply.lower() == self.get_correct().lower():
            return 20
        else:
            return 0

class Game:
    def __init__(self, id, question_list):
        self.player1_replied = 0
        self.player2_replied = 0
        self.ready = False
        self.players_scores = [0, 0]
        self.question_list = question_list
        self.id = id
        self.player1_replys = []
        self.player2_replys = []
    
    def reset_game(self):
        self.player1_replied = 0
        self.player2_replied = 0
        self.players_scores = [0, 0]
        self.player1_replys = []
        self.player2_replys = []

    
    def finish(self):
        return self.player1_replied + self.player2_replied
    
    def play(self, player, reply):
        
        if player == 0:
            self.player1_replys = reply
            index = 0
            for r in self.player1_replys:
                self.players_scores[player] += question_list[index].check_correct(r)
                print(r, question_list[index].get_correct)
                index += 1
            self.player1_replied = 1
        else:
            self.player2_replys = reply
            index = 0
            for r in self.player2_replys:
                self.players_scores[player] += question_list[index].check_correct(r)
                index += 1
            self.player2_replied = 1
    
    def reset(self):
        self.ready = False


    def winner(self):
        player1 = self.players_scores[0]
        player2 = self.players_scores[1]
        winner = -1

        if player1 > player2:
            winner = 0
        elif player1 < player2:
            winner = 1
        else:
            winner = 2
        
        return winner






question1 = Question("Türkiyenin Başkenti Aşağıdakilerden Hangisidir?", ["Ankara", "İstanbul", "Kayseri", "Sivas"], "Ankara")
question2 = Question("Hangisi Yenir?", ["Masa", "Sandalye", "Elma", "Fare"], "Elma")
question3 = Question("Hangisi Anlık Veri Tutar", ["GPU", "CPU", "RAM", "SSD"], "RAM")
question4 = Question("Hangisi verileri depolar?", ["RAM", "HDD", "CPU", "PSU"], "HDD")
question5 = Question("Filistin' in Başkenti?", ["Kudüs", "Tel-Aviv", "Gazze", "Kahire"], "Kudüs")

question_list = [question1, question2, question3, question4, question5]




