from random import sample

def create_bingo_card()-> dict[str, list[int]]: 

    bingo_letters: str = "BINGO"
    bingo_card: dict[str, list[int]] = {}

    start_range: int = 1
    for char in bingo_letters:
        bingo_card[char]=sample(range(start_range, start_range+15), 5)
        start_range+=15
    
    return bingo_card

def display_bingo_card(bingo_card: dict[str, list[int]]) -> None:
    
    print("B    I    N    G    O")
    print("-"*23)
    for row in range(5):
        for column in bingo_card:
            print(f"{bingo_card[column][row]:<5}", end="")
        print()

def main():
    random_bingo_card=create_bingo_card()
    
    display_bingo_card(random_bingo_card)
    
   
if __name__=="__main__":
    main()