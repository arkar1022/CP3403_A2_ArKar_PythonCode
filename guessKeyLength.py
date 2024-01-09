def similarityCount(str1, str2):
    """
    Calculates the similarity count between two strings.
    """
    count = 0
    str1 = str1.lower()
    str2 = str2.lower()
    for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i]:
            count += 1
    return count

def guessKeyLength():
    """
    Guesses the key length for a Vigenere cipher.
    """
    encrypted_text = "eflrxdztocjcwtuehkxttpskviclkjrxsrtdiycvnfqfresbinskvigfukvnpqxkbgtssnesqivpwwoynciatchildnvhukwiaggvuxwxtsvuldpgjrterhnzrexxhpcsdehbehrtqhmjogcvtwkgpwwhxfpekiueabbyeetthlkwhhosbpidkuczgxwbpujjmrausafwgxesvxihhtanpmennoggwxghceoeibqbgjihxprrtmhmjsccvirkbnesbfwbveeibqbfawixohucxxlvvrnivbvwzcxtmtoauqxmvseqjxghceoeibqbgjigxesvxigbuhugtpkvmvperhoahpmrtvwbpwnlvszvlpmkggjixgvsafiskgqvrmtgvcskruhtanvmdgcbnfztkuoeamhtroevcxgcqboqjgkqnvmdgumfvibmjogkwcxkhugviaggrphtkpcetirxkjrtecwyvvelikksfvssxhsnvxwxkbsqvbtvwbpwtvwfvvchxtjveiqxkbtrvdokrrfftmysrpxwxusafigtpreggtbxseuirkgqlgrhntsfvlpmkbsqvbtvwbpjahyprvatxphugwtgfsecrsmjseggtbxsekwjgkbggpabiwoniihqigumsxtgvvtghvspvwxghceoeibqbniexguhgjvttvgocwtwqbrcztlffbrtxgiwavivkkhlgrpunsfvltkgqrkztkvcigvxyakugxwxthugqtluotglpldsrpxpfrseghlbvvoasjmuwqgvhpjwyuxxgvfnpwxmxwncrjguspwvtwevnprtekhrpwjkgggjeitpmzqhxykqnvmdgqtgjihmtsnosufggfcktlywynftwghrextwcbvficmktveeibqbbttpkvmnwxwxphveeibqbnuwjkgggjietthvgwdyvvrkvxwgbgkxnfggfckttwhugribeogkscitcikhtlvcgjietthlylxvjfreixoggnoihlcurgzxwgbpgsumjsvficmkhlqjiaggrphtkcqucrcxnwfcqttpgbhgdgxslkrvbptbtqpmkcahvdfqbrregmahbcrdmjsecwtvwfrelpgpsyqvpitwicxtvjoapiabucagjghokukgwtpoqxiglcflfstlpcgjekxvvrcfxekhlvsgxqfqgvsxnsggmclgfgqvgxcrnpyclgqhtisvjoapiahtocwfabequcrcxnwfqrtytczylxvjdntxxxucgjigmjoavldlgtbtawbevgjixghceoeibqbvumcmgbqghrtpfrqvsxtrrniixkbfgvihtfrchtgeflrxxhpwfvltitwzkxxogqeatihifnrlxvqdrteibqbhuismqsauygxusptirrqfpqrubfsavmpekhlqjxghceoeibqbgteclowgvistefbuwpgwbfggjkgrpqqbnpwpcxxhpqucrcxnhugicvtmcvmdgqdrteibqbgcotlcdvggthhwahsgfchvqrpeucpcpaxfaruwpzgcerppbphrzxpgfhecrhyqfzumibphbcggrrhbivpfqfpktwxthrzxjlkbtcwtvtsgevnivctteeakqxgcsxeflrxxhpwfvltkgjrtwthrsecxxhphbgrrkadgkscmjseggtbxseyldaqzquxwxecetirmusptiidgmpcrgxecigviagaruwpzgdycmcmglghvdfvvrevnivcttebvkdugvixzh"
    key_length = 3
    while (key_length <= 12):
        unkown_x = "x" * key_length
        encrypted_text_xlength= unkown_x + encrypted_text
        result = similarityCount(encrypted_text,encrypted_text_xlength)
        print(f"Similarity count with key length {key_length}: {result}")
        key_length += 1

guessKeyLength()