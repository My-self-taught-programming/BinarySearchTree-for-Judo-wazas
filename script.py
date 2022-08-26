import judo_moves
from Judo_BST import BinarySearchTree 

tree = BinarySearchTree(19, judo_moves.judo)


tree.insert(1, judo_moves.Nage_waza)
tree.insert(2, judo_moves.Tachi_waza)
tree.insert(3, judo_moves.Te_waza)
tree.insert(4, judo_moves.Koshi_waza)
tree.insert(5, judo_moves.Ashi_waza)
tree.insert(6, judo_moves.Sutemi_waza)
tree.insert(7, judo_moves.Ma_Sutemi_waza)
tree.insert(8, judo_moves.Yoko_Sutemi_waza)

tree.insert(9, judo_moves.katame_waza)
tree.insert(10, judo_moves.Osae_komi_waza)
tree.insert(11, judo_moves.Kesa_gatame_kei)
tree.insert(12, judo_moves.Shido_gatame_kei)
tree.insert(13, judo_moves.shime_waza)
tree.insert(14, judo_moves.Kansetsu_waza)
tree.insert(15, judo_moves.Ukemi)
tree.insert(16, judo_moves.back_ukemi)
tree.insert(17, judo_moves.forward_ukemi)
tree.insert(18, judo_moves.side_ukemi)


start_program = False
print("************************************************************************")
print("Judo also know as the gentle way is a system of unarmed combat, modern Japanese martial art, and Olympic sport (since 1964).\nJudo was created in 1882 by Kanō Jigorō (嘉納 治五郎) as an eclectic martial art, distinguishing itself from its predecessors\n(primarily Tenjin Shinyo-ryu jujutsu and Kitō-ryū jujutsu) due to an emphasis on 'randori' (乱取り, lit. 'free sparring')\ninstead of 'kata' (pre-arranged forms) alongside its removal of striking and weapon training elements.\nJudo rose to prominence for its dominance over established jujutsu schools in tournaments hosted by the\nTokyo Metropolitan Police Department (警視庁武術大会, Keishicho Bujutsu Taikai), resulting in its adoption as the department's primary martial art\nA judo practitioner is called a 'judoka' (柔道家, jūdōka, lit. 'judo performer'), and the judo uniform is called 'judogi' (柔道着, jūdōgi, lit. 'judo attire')")
print("************************************************************************")
print("Judo consist of the following:")
print("JUDO")
print("|___ 1. Naga-waza/Throwing Techniques")
print("|            |___ 2. Tachi-waza/Standing techniques")
print("|                |___ 3. Te-Waza/Hand Techniques")
print("|                |___ 4. Koshi-waza/Hip techniques")
print("|                |___ 5. Ashi-Waza/Leg techniques")
print("|            |___ 6. Sutemi-waza/Scriface techniques")
print("|                |___ 7. Ma-sutemi-waza/Direct scrifice techniques")
print("|                |___ 8. Yoko-sutemi-waza/Side sacrifice techniques")
print("|___ 9. Katame-waza/Grappling techniques")
print("|            |___ 10. Osae-komi-waza/Pinning Techniques")
print("|                                   |___ 11. Kesa-Gatame-Kei")
print("|                                   |___ 12. Shido-Gatame-Kei")
print("|            |___ 13. Shime-Waza/Strangle Techniques")
print("|            |___ 14. Kansetsu-waza/Joint Techniques")
print("|___ 15. Ukemi/Breakfalls")
print("             |___ 16. Back Ukemi")
print("             |___ 17. Side Ukemi")
print("             |___ 18. Front Ukemi")

user_input =input("\nWould you like to start to learn about Judo Waza's (techniques)? \nInput y or n to continue\n")
if user_input.lower() == "y":
    start_program = True
else:
    print("\nCome back when you wish to learn")

while start_program:
    
    numbers_input = []

    for i in range(1,19):
        numbers_input.append(str(i))
        
    
    user_input1 = input("\nwhat would you like to learn more about? type the number of the waza you desire to learn about.\nAlternatively type N to cancel program or search to find if something is in the BST\n")
    
        
    if user_input1.lower() == "N":
        start_program = False
    
    elif user_input1 in numbers_input:
        
        print(*tree.get_node_by_value(int(user_input1)), sep=", ")
    
    else:
        print("Invalid input please use the desired Waza's corresponding Interger value as input")

    while user_input1.lower() == "search":
        user_search = input("\nInput the value of the waza you wish to search to see if it it is indeed in the BST\n")
        print(tree.is_in_tree((int(user_search))))
        break