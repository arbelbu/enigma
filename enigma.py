"""
import random
def get_rotor():
    alphabet = ''.join(map(chr, range(97, 123)))
    alphabet_mixed=''.join(random.sample(alphabet, 26))
    return alphabet_mixed
rotor_a=get_rotor()
rotor_b=get_rotor()
rotor_c=get_rotor()
"""
rotor_I =   'ekmflgdqvzntowyhxuspaibrcj'
rotor_II =  'ajdksiruxblhwtmcqgznpyfvoe'
rotor_III = 'bdfhjlcprtxvznyeiwgakmusqo'
rotor_VI =  'esovpzjayquirhxlnftgkdcmwb'
rotor_V =   'vzbrgityupsdnhlxawmjqofeck'
#arrangement_rotors=[rotor_III, rotor_VI, rotor_V]
rotors_names={1:rotor_I, 2:rotor_II, 3:rotor_III, 4:rotor_VI, 5:rotor_V}
input_arrangement_rotors=input("enter rotors:\n")
arrangement_rotors=[rotors_names[int(input_arrangement_rotors[0])],
                    rotors_names[int(input_arrangement_rotors[1])],
                    rotors_names[int(input_arrangement_rotors[2])]]


initial_rotor_settings=input('enter Initial rotor settings(EG. rew/ghk):\n')
def setting_rotors(n,arrangement_rotors,initial_rotor_settings):  #  n- number rotor inarrangement rotors, not in rotors names
    setting_rotor = arrangement_rotors[n].find(initial_rotor_settings[n])
    setting_rotor = arrangement_rotors[n][setting_rotor:] + arrangement_rotors[n][:setting_rotor]
    arrangement_rotors[n] = setting_rotor
for rotor_number in [0,1,2]:
    setting_rotors(rotor_number)





plugboard_settings=input("enter plugboard settings(EG. ab,cd,ef):\n")

sentence_to_secrete = input("enter sentence:\n")
sentence_to_secrete=sentence_to_secrete.replace(" ",'')

def get_letter(rotor,letter):
    encoded_character = rotor[(ord(letter))-97]
    return encoded_character

def rotate(rotor):
    rotor=rotor[-1]+rotor[:-1]
    return rotor

alphabet=list(map(chr, range(97, 123)))
#alphabet='abcdefghijklmnopqrstuvwxyz'
def plugs_panel (plugboard_settings):
    plugboard_settings = plugboard_settings.split(",")
    for Pair_of_letters in plugboard_settings:
        letter_one_number = ord(Pair_of_letters[0])-97
        letter_two_number = ord(Pair_of_letters[1])-97
        alphabet[letter_one_number],alphabet[letter_two_number] = alphabet[letter_two_number],alphabet[letter_one_number]
    return "".join(alphabet)
switchboard = plugs_panel(plugboard_settings)


def secrete (letter,rotors_list):
    letter = get_letter(switchboard, letter)
    for rotor in rotors_list:
        letter = get_letter(rotor, letter)
#    letter = get_letter(rotor_I, letter)
#    letter = get_letter(rotor_II, letter)
#    letter = get_letter(rotor_III, letter)
    letter = reflector( letter)
    for rotor in rotors_list[::-1]:
        letter = opposite(rotor, letter)
#    letter = opposite(rotor_III, letter)
#    letter = opposite(rotor_II, letter)
#    letter = opposite(rotor_I, letter)
    letter = opposite(switchboard, letter)
    return letter

reflector_a='ejmzalyxvbwfcrquontspikhgd'
def reflector(letter):
    return get_letter(reflector_a, letter)

def opposite(rotor,letter):
    letter_number = rotor.find(letter)
    return chr(letter_number+97)


sentence_secreted = ""
for letter in sentence_to_secrete:
    letter_secreted=secrete(letter,arrangement_rotors)
    assert(letter == secrete(letter_secreted,arrangement_rotors))
    sentence_secreted+=letter_secreted

    arrangement_rotors[0] = rotate(arrangement_rotors[0])
    if len(sentence_secreted)%(26**2)==0:
        arrangement_rotors[2] = rotate(arrangement_rotors[2])
        arrangement_rotors[1] = rotate(arrangement_rotors[1])
    elif len(sentence_secreted) % (26) == 0:
        arrangement_rotors[1] = rotate(arrangement_rotors[1])
print(sentence_secreted)

"""
import tkinter as tk
window = tk.Tk()
rot = tk.Label(text="enter rotors:")
rot_ = tk.Entry(width=50)
plugboard = tk.Label(text="enter plugboard settings(EG. ab,cd,ef):")
plugboard_ = tk.Entry(width=50)
sentence = tk.Label(text="enter sentence:")
sentence_ = tk.Entry(width=50)
rot.pack()
rot_.pack()
plugboard.pack()
plugboard_.pack()
sentence.pack()
sentence_.pack()
window.mainloop()
"""
