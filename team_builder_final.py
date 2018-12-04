if __name__ == "__main__":
    import csv
    import random

players = []
Team1 = []
Team2 = []
Team3 = []
Team4 = []
Team5 = []
Team6 = []
experienced_players = []
inexperienced_players = []

def import_CSV():
    with open('soccer_players.csv') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            del row[1]
            players.append(row)
        del players[0]

def group_players():
    for player in players:
        if player[1] == "YES":
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)

def assign_players2():

    for experienced_player in range(int(len(experienced_players)/2)):
        Team1.append(experienced_players.pop(experienced_player))
        
    for inexperienced_player in range(int(len(inexperienced_players)/2)):
        Team1.append(inexperienced_players.pop(inexperienced_player))
        
    for experienced_player in range(int(len(experienced_players))):
        Team2.append(experienced_players.pop())
        
    for inexperienced_player in range(int(len(inexperienced_players))):
        Team2.append(inexperienced_players.pop())

def assign_players3():

    for experienced_player in range(int(len(experienced_players)/3)):
        Team1.append(experienced_players.pop(experienced_player))

    for inexperienced_player in range(int(len(inexperienced_players)/3)):
        Team1.append(inexperienced_players.pop(inexperienced_player))

    for experienced_player in range(int(len(experienced_players)/2)):
        Team2.append(experienced_players.pop(experienced_player))
        
    for inexperienced_player in range(int(len(inexperienced_players)/2)):
        Team2.append(inexperienced_players.pop(inexperienced_player))
        
    for experienced_player in range(int(len(experienced_players))):
        Team3.append(experienced_players.pop())
        
    for inexperienced_player in range(int(len(inexperienced_players))):
        Team3.append(inexperienced_players.pop())

def assign_players4():

    for experienced_player in range(int(len(experienced_players)/4)):
        Team1.append(experienced_players.pop(experienced_player))

    for inexperienced_player in range(int(len(inexperienced_players)/4)):
        Team1.append(inexperienced_players.pop(inexperienced_player))

    for experienced_player in range(int(len(experienced_players)/3)):
        Team2.append(experienced_players.pop(experienced_player))

    for inexperienced_player in range(int(len(inexperienced_players)/3)):
        Team2.append(inexperienced_players.pop(inexperienced_player))

    for experienced_player in range(int(len(experienced_players)/2)):
        Team3.append(experienced_players.pop(experienced_player))
        
    for inexperienced_player in range(int(len(inexperienced_players)/2)):
        Team3.append(inexperienced_players.pop(inexperienced_player))
        
    for experienced_player in range(int(len(experienced_players))):
        Team4.append(experienced_players.pop())
        
    for inexperienced_player in range(int(len(inexperienced_players))):
        Team4.append(inexperienced_players.pop())

def assign_players5():

    for experienced_player in range(int(len(experienced_players)/5)):
        Team1.append(experienced_players.pop(experienced_player))

    for inexperienced_player in range(int(len(inexperienced_players)/5)):
        Team1.append(inexperienced_players.pop(inexperienced_player))
        
    for experienced_player in range(int(len(experienced_players)/4)):
        Team2.append(experienced_players.pop(experienced_player))

    for inexperienced_player in range(int(len(inexperienced_players)/4)):
        Team2.append(inexperienced_players.pop(inexperienced_player))

    for experienced_player in range(int(len(experienced_players)/3)):
        Team3.append(experienced_players.pop(experienced_player))

    for inexperienced_player in range(int(len(inexperienced_players)/3)):
        Team3.append(inexperienced_players.pop(inexperienced_player))

    for experienced_player in range(int(len(experienced_players)/2)):
        Team4.append(experienced_players.pop(experienced_player))
        
    for inexperienced_player in range(int(len(inexperienced_players)/2)):
        Team4.append(inexperienced_players.pop(inexperienced_player))
        
    for experienced_player in range(int(len(experienced_players))):
        Team5.append(experienced_players.pop())
        
    for inexperienced_player in range(int(len(inexperienced_players))):
        Team5.append(inexperienced_players.pop())

def assign_players6():

    for experienced_player in range(int(len(experienced_players)/6)):
        Team1.append(experienced_players.pop(experienced_player))

    for inexperienced_player in range(int(len(inexperienced_players)/6)):
        Team1.append(inexperienced_players.pop(inexperienced_player))
        
    for experienced_player in range(int(len(experienced_players)/5)):
        Team2.append(experienced_players.pop(experienced_player))

    for inexperienced_player in range(int(len(inexperienced_players)/5)):
        Team2.append(inexperienced_players.pop(inexperienced_player))
        
    for experienced_player in range(int(len(experienced_players)/4)):
        Team3.append(experienced_players.pop(experienced_player))

    for inexperienced_player in range(int(len(inexperienced_players)/4)):
        Team3.append(inexperienced_players.pop(inexperienced_player))

    for experienced_player in range(int(len(experienced_players)/3)):
        Team4.append(experienced_players.pop(experienced_player))

    for inexperienced_player in range(int(len(inexperienced_players)/3)):
        Team4.append(inexperienced_players.pop(inexperienced_player))

    for experienced_player in range(int(len(experienced_players)/2)):
        Team5.append(experienced_players.pop(experienced_player))
        
    for inexperienced_player in range(int(len(inexperienced_players)/2)):
        Team5.append(inexperienced_players.pop(inexperienced_player))
        
    for experienced_player in range(int(len(experienced_players))):
        Team6.append(experienced_players.pop())
        
    for inexperienced_player in range(int(len(inexperienced_players))):
        Team6.append(inexperienced_players.pop())

def team_select():
    print("Welcome to the team builder \nPresented by Sore_Soccer and Alister Enterprises \n\nFirst ensure that all eligable players are entered correctly into the soccer players file. \nCreate well balanced teams by entering the amount desired below. \n")
    team_number = input("Enter the number of teams as an integar ")
    if int(team_number) == 2:
        assign_players2()
    elif int(team_number) == 3:
        assign_players3()
    elif int(team_number) == 4:
        assign_players4()
    elif int(team_number) == 5:
        assign_players5()
    elif int(team_number) == 6:
        assign_players6()
    elif int(team_number) > 6:
        print("Six teams is the maximum value")
        team_select()
    elif int(team_number) < 2:
        print("You need at least two teams to plays")
        team_select()

def build_txt():
    txt_file = open("teamsreal.txt", "w")
    txt_file.write("Team 1")
    for TTeam1 in Team1:
        txt_file.write("\n")
        txt_file.write(", ".join(TTeam1))
    txt_file.write("\n \nTeam 2")
    for TTeam2 in Team2:
        txt_file.write("\n")
        txt_file.write(", ".join(TTeam2))
    txt_file.write("\n \nTeam 3")
    for TTeam3 in Team3:
        txt_file.write("\n")
        txt_file.write(", ".join(TTeam3))
    txt_file.write("\n \nTeam 4")
    for TTeam4 in Team4:
        txt_file.write("\n")
        txt_file.write(", ".join(TTeam4))
    txt_file.write("\n \nTeam 5")
    for TTeam5 in Team5:
        txt_file.write("\n")
        txt_file.write(", ".join(TTeam5))
    txt_file.write("\n \nTeam 6")
    for TTeam6 in Team6:
        txt_file.write("\n")
        txt_file.write(", ".join(TTeam6))
        
import_CSV()
group_players()
team_select()
build_txt()
import os
os.startfile("teamsreal.txt")
