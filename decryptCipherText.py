def vigenereDecrypt(ciphertext, keyword):
    plaintext = ""

    # Convert the keyword to lowercase for consistency
    keyword = keyword.lower()  
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = keyword[i % len(keyword)]

        if char.isalpha():
            #decrypt the character
            decrypted_char = chr((ord(char) - ord(key_char) + 26) % 26 + ord('a'))
            plaintext += decrypted_char
        else:
            # Preserve non-alphabetic characters
            plaintext += char

    print(plaintext)

ciphertext = "eflrxdztocjcwtuehkxttpskviclkjrxsrtdiycvnfqfresbinskvigfukvnpqxkbgtssnesqivpwwoynciatchildnvhukwiaggvuxwxtsvuldpgjrterhnzrexxhpcsdehbehrtqhmjogcvtwkgpwwhxfpekiueabbyeetthlkwhhosbpidkuczgxwbpujjmrausafwgxesvxihhtanpmennoggwxghceoeibqbgjihxprrtmhmjsccvirkbnesbfwbveeibqbfawixohucxxlvvrnivbvwzcxtmtoauqxmvseqjxghceoeibqbgjigxesvxigbuhugtpkvmvperhoahpmrtvwbpwnlvszvlpmkggjixgvsafiskgqvrmtgvcskruhtanvmdgcbnfztkuoeamhtroevcxgcqboqjgkqnvmdgumfvibmjogkwcxkhugviaggrphtkpcetirxkjrtecwyvvelikksfvssxhsnvxwxkbsqvbtvwbpwtvwfvvchxtjveiqxkbtrvdokrrfftmysrpxwxusafigtpreggtbxseuirkgqlgrhntsfvlpmkbsqvbtvwbpjahyprvatxphugwtgfsecrsmjseggtbxsekwjgkbggpabiwoniihqigumsxtgvvtghvspvwxghceoeibqbniexguhgjvttvgocwtwqbrcztlffbrtxgiwavivkkhlgrpunsfvltkgqrkztkvcigvxyakugxwxthugqtluotglpldsrpxpfrseghlbvvoasjmuwqgvhpjwyuxxgvfnpwxmxwncrjguspwvtwevnprtekhrpwjkgggjeitpmzqhxykqnvmdgqtgjihmtsnosufggfcktlywynftwghrextwcbvficmktveeibqbbttpkvmnwxwxphveeibqbnuwjkgggjietthvgwdyvvrkvxwgbgkxnfggfckttwhugribeogkscitcikhtlvcgjietthlylxvjfreixoggnoihlcurgzxwgbpgsumjsvficmkhlqjiaggrphtkcqucrcxnwfcqttpgbhgdgxslkrvbptbtqpmkcahvdfqbrregmahbcrdmjsecwtvwfrelpgpsyqvpitwicxtvjoapiabucagjghokukgwtpoqxiglcflfstlpcgjekxvvrcfxekhlvsgxqfqgvsxnsggmclgfgqvgxcrnpyclgqhtisvjoapiahtocwfabequcrcxnwfqrtytczylxvjdntxxxucgjigmjoavldlgtbtawbevgjixghceoeibqbvumcmgbqghrtpfrqvsxtrrniixkbfgvihtfrchtgeflrxxhpwfvltitwzkxxogqeatihifnrlxvqdrteibqbhuismqsauygxusptirrqfpqrubfsavmpekhlqjxghceoeibqbgteclowgvistefbuwpgwbfggjkgrpqqbnpwpcxxhpqucrcxnhugicvtmcvmdgqdrteibqbgcotlcdvggthhwahsgfchvqrpeucpcpaxfaruwpzgcerppbphrzxpgfhecrhyqfzumibphbcggrrhbivpfqfpktwxthrzxjlkbtcwtvtsgevnivctteeakqxgcsxeflrxxhpwfvltkgjrtwthrsecxxhphbgrrkadgkscmjseggtbxseyldaqzquxwxecetirmusptiidgmpcrgxecigviagaruwpzgdycmcmglghvdfvvrevnivcttebvkdugvixzh"
keyword = "concept"
vigenereDecrypt(ciphertext, keyword)

