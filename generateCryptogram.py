from collections import Counter

encrypted_text = "eflrxdztocjcwtuehkxttpskviclkjrxsrtdiycvnfqfresbinskvigfukvnpqxkbgtssnesqivpwwoynciatchildnvhukwiaggvuxwxtsvuldpgjrterhnzrexxhpcsdehbehrtqhmjogcvtwkgpwwhxfpekiueabbyeetthlkwhhosbpidkuczgxwbpujjmrausafwgxesvxihhtanpmennoggwxghceoeibqbgjihxprrtmhmjsccvirkbnesbfwbveeibqbfawixohucxxlvvrnivbvwzcxtmtoauqxmvseqjxghceoeibqbgjigxesvxigbuhugtpkvmvperhoahpmrtvwbpwnlvszvlpmkggjixgvsafiskgqvrmtgvcskruhtanvmdgcbnfztkuoeamhtroevcxgcqboqjgkqnvmdgumfvibmjogkwcxkhugviaggrphtkpcetirxkjrtecwyvvelikksfvssxhsnvxwxkbsqvbtvwbpwtvwfvvchxtjveiqxkbtrvdokrrfftmysrpxwxusafigtpreggtbxseuirkgqlgrhntsfvlpmkbsqvbtvwbpjahyprvatxphugwtgfsecrsmjseggtbxsekwjgkbggpabiwoniihqigumsxtgvvtghvspvwxghceoeibqbniexguhgjvttvgocwtwqbrcztlffbrtxgiwavivkkhlgrpunsfvltkgqrkztkvcigvxyakugxwxthugqtluotglpldsrpxpfrseghlbvvoasjmuwqgvhpjwyuxxgvfnpwxmxwncrjguspwvtwevnprtekhrpwjkgggjeitpmzqhxykqnvmdgqtgjihmtsnosufggfcktlywynftwghrextwcbvficmktveeibqbbttpkvmnwxwxphveeibqbnuwjkgggjietthvgwdyvvrkvxwgbgkxnfggfckttwhugribeogkscitcikhtlvcgjietthlylxvjfreixoggnoihlcurgzxwgbpgsumjsvficmkhlqjiaggrphtkcqucrcxnwfcqttpgbhgdgxslkrvbptbtqpmkcahvdfqbrregmahbcrdmjsecwtvwfrelpgpsyqvpitwicxtvjoapiabucagjghokukgwtpoqxiglcflfstlpcgjekxvvrcfxekhlvsgxqfqgvsxnsggmclgfgqvgxcrnpyclgqhtisvjoapiahtocwfabequcrcxnwfqrtytczylxvjdntxxxucgjigmjoavldlgtbtawbevgjixghceoeibqbvumcmgbqghrtpfrqvsxtrrniixkbfgvihtfrchtgeflrxxhpwfvltitwzkxxogqeatihifnrlxvqdrteibqbhuismqsauygxusptirrqfpqrubfsavmpekhlqjxghceoeibqbgteclowgvistefbuwpgwbfggjkgrpqqbnpwpcxxhpqucrcxnhugicvtmcvmdgqdrteibqbgcotlcdvggthhwahsgfchvqrpeucpcpaxfaruwpzgcerppbphrzxpgfhecrhyqfzumibphbcggrrhbivpfqfpktwxthrzxjlkbtcwtvtsgevnivctteeakqxgcsxeflrxxhpwfvltkgjrtwthrsecxxhphbgrrkadgkscmjseggtbxseyldaqzquxwxecetirmusptiidgmpcrgxecigviagaruwpzgdycmcmglghvdfvvrevnivcttebvkdugvixzh"
key_length = 7

from collections import Counter

def generateCryptogram(text: str, key_length: int):
    # Create an array to store the most common characters in each cryptogram
    cryptogramArr = [None] * key_length

    # Print the most common characters in each cryptogram
    print("\n----Printing most common characters in each cryptogram----")
    for xth_key in range(key_length):
        # Extract every xth character for the current cryptogram
        every_xth_characters = text[xth_key::key_length]
        # Count the occurrences of each character in the current cryptogram
        character_counts = Counter(every_xth_characters)
        # Store the most common characters and their counts in the array
        cryptogramArr[xth_key] = character_counts.most_common(3)
        # Print the most common characters in the current cryptogram
        print(f"Cryptogram {xth_key+1}: {cryptogramArr[xth_key]}")
    
    # Assume that the most common characters are 'e' and decrypt
    print("\n----Assuming most common characters are 'e' and decrypting----")
    for xth_key, cryptogram in enumerate(cryptogramArr):
        # Create an array to store the assumed decrypted characters
        plain = [None] * 3
        for index, (char, count) in enumerate(cryptogram):
            # Decrypt the characters based on the assumption that 'e' is the most common character
            plain[index] = chr((ord(char) - ord('e') + 26) % 26 + ord('a'))
        # Print the assumed decrypted characters for the current cryptogram
        print(f"Cryptogram {xth_key+1}: {plain}")


generateCryptogram(encrypted_text, key_length)








