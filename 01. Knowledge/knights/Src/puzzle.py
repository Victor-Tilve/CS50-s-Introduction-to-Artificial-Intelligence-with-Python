from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

'''
- Each character is either a knight or a knave.
- A knight will always tell the truth: if knight states a sentence,
  then that sentence is true.
- Conversely, a knave will always lie: if a knave states a sentence,
  then that sentence is false.'''

############################## Puzzle 0 ################################
#Basic Rule Puzzle 0
Brule0 = Or( And(AKnight,Not(AKnave)), And(Not(AKnight),AKnave))
# A says "I am both a knight and a knave."
A0says = And(   Or(Not(AKnave),Not(And(AKnight,AKnave))),
                Or(Not(AKnight),And(AKnight,AKnave))
                )
#knowledge
knowledge0 = And(Brule0,A0says)

############################### Puzzle 1 ##############################
#Basic Rule Puzzle 1
Or( And(AKnight,Not(AKnave)), And(Not(AKnight),AKnave))
Brule1 = And(   Or( And(AKnight,Not(AKnave)), And(Not(AKnight),AKnave)),
                Or( And(BKnight,Not(BKnave)), And(Not(BKnight),BKnave))
                )
# A says "We are both knaves."
A1says = And(   Or(Not(AKnave),Not(And(BKnave,AKnave))),
                Or(Not(AKnight),And(AKnight,AKnave))
                )
# B says nothing.
#knowledge
knowledge1 = And(Brule1,A1says)

################################ Puzzle 2 ###############################
#Basic Rule Puzzle 2
Brule2 = Brule1
# A says "We are the same kind."
A2says =And(    Or(Not(AKnave),Not(Or(And(BKnave,AKnave),And(BKnight,AKnight)))),
                Or(Not(AKnight),Or(And(BKnave,AKnave),And(BKnight,AKnight)))
                )
# B says "We are of different kinds."
B2says =And(    Or(Not(BKnave),Not(Or(And(BKnave,AKnight),And(BKnight,AKnave)))),
                Or(Not(BKnight),Or(And(BKnave,AKnight),And(BKnight,AKnave)))
                )
#knowledge
knowledge2 = And(Brule2,A2says,B2says)

################################ Puzzle 3 ###############################
#Basic Rule Puzzle 3
Brule3 = And(   Or( And(AKnight,Not(AKnave)), And(Not(AKnight),AKnave)),
                Or( And(BKnight,Not(BKnave)), And(Not(BKnight),BKnave)),
                Or( And(CKnight,Not(CKnave)), And(Not(CKnight),CKnave)),
                )

# A says either "I am a knight." or "I am a knave.", but you don't know which.
A3says = And(   Or(Not(AKnave),Not(Or(AKnight, AKnave))),
                Or(Not(AKnight),Or(AKnight, AKnave))
                )
# B says "A said 'I am a knave'."
# B says "C is a knave."
B3says1 = And(
                Or(Not(BKnave),Not(Or(Not(A3says),CKnave))),
                Or(Not(BKnight),Or(Not(A3says),CKnave))
                )

B3says2 = And(
                Or(Not(BKnave),Not(CKnave)),
                Or(Not(BKnight),CKnave)
                )
# C says "A is a knight."
C3says = And(   Or(Not(CKnave),Not(AKnight)),
                Or(Not(CKnight),AKnight)
                )

#knowledge
knowledge3 = And(Brule3,A3says,B3says1,B3says2,C3says)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")
def main2():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    print("Puzzle 0")
    for symbol in symbols:
        if model_check(knowledge3, symbol):
            print(f"    {symbol}")

if __name__ == "__main__":
    main()
