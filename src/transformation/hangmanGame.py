import re
from functools import reduce
from itertools import chain
from collections import Counter
import typing
import traceback


def set_words(word_len: int, filename: str = "hangman_words.txt") -> typing.Set[str]:
    with open(filename) as word_file:
        return {
            word.lower()
            for word in map(str.strip, word_file.readlines())
            if len(word) == word_len and word.isalpha()
        }


def find_words(guesses: str, current_word: str, all_words: typing.Iterable) -> typing.List[str]:
    substitute: str = '.' if len(guesses) == 0 else f"[^{guesses}]"
    current_word_regex: typing.Pattern = re.compile(current_word.replace('_', substitute))
    return [word for word in all_words if current_word_regex.match(word)]


def count_letters(possible_words: typing.Iterable) -> Counter:
    return Counter(chain.from_iterable(possible_words))


def get_percent(stats: Counter) -> typing.Tuple[str, float]:

    likeliest_letter, count = stats.most_common(1)[0]
    likelihood = count / sum(stats.values()) * 100.0
    return likeliest_letter, likelihood


def antycheat(user_input: str, last_user_input: str, initial_len_of_input: int) -> typing.Tuple[str, int]:

    if initial_len_of_input == -1:
        return user_input, len(user_input)

    corrected_input: str = user_input

    while len(corrected_input) != initial_len_of_input:
        print("Are you cheating? Last time word was of different length")
        print(f"All choises saved. Last try was: {last_user_input} with {len(last_user_input)} letters.")
        corrected_input = input("Try one more time ").lower()

    differences: typing.List[bool] = [last_user_input[i] != corrected_input[i]
                                      for i in range(initial_len_of_input)
                                      if last_user_input[i] != '_']

    if len(differences) == 0:
        return corrected_input, initial_len_of_input

    has_differences: bool = all(differences) or reduce(lambda x, y: x != y, differences)

    while has_differences:
        print("Something is wrong.")
        print("Last time letters position was different.")
        print(f"Especially this: {last_user_input}.")
        corrected_input = input("Try one more time   ").lower()

        differences = [last_user_input[i] != corrected_input[i]
                       for i in range(initial_len_of_input)
                       if last_user_input[i] != '_']
        has_differences = all(differences) or reduce(lambda x, y: x != y, differences)

    return corrected_input, initial_len_of_input


def play_game():
    is_playing: bool = True
    was_correct: bool = True

    guesses: str = ""
    current_word: str = ""

    len_of_word: int = -1

    words: typing.Set[str] = set()
    print("Choose a word :)")

    while is_playing:
        if was_correct:
            last_word: str = current_word
            if current_word.count('_') == 1:
                current_word = current_word.replace('_', guesses[-1:])
                possible_words: typing.List[str] = find_words(guesses, current_word, words)

                if len(possible_words) == 1:
                    print(f"Looks like this is a word:  {possible_words[0]}.")
                    break
            else:
                current_word = input("(Please type guessed letters, the others replace with _ ) ").lower()
                current_word, len_of_word = antycheat(current_word, last_word, len_of_word)

        # the end of the game if it's equal to 0
        if current_word.count('_') == 0:
            break

        # guesses calculation
        guesses += ''.join([guess for guess in current_word if guess != '_' and guess not in guesses])

        if len(words) == 0:
            words = set_words(len(current_word))

        possible_words: typing.List[str] = find_words(guesses, current_word, words)

        print(f"Choosing from {len(possible_words)} possible words")

        if len(possible_words) <= 10:
            [print(word) for word in possible_words]

        if len(possible_words) == 1:
            print(f"Looks like this is the word: {possible_words[0]}.")
            break

        stats_temp: Counter = count_letters(possible_words)

        stats: Counter = Counter({key: value for key, value in stats_temp.items() if key not in guesses})

        print("Most likely this is the letter...")
        likeliest_letter: typing.Tuple[str, float] = get_percent(stats)
        print(f"{likeliest_letter[0]} with probability {likeliest_letter[1]:.2f}%")

        userInput = input("Am I right? (y/n) ").lower()

        while not re.match(r"[yn]", userInput):
            userInput = input("Am I right? (y/n) ").lower()

        was_correct = userInput == 'y'
        guesses += likeliest_letter[0]

        print("")

    print(f"It was easy, I guessed with {len(guesses)} tries!")


if __name__ == '__main__':
    try:
        play_again: bool = True
        while play_again:
            play_game()
            play_again = input("Wanna play one more time? (y/n) ").lower() == 'y'
        print("")
    except Exception as e:
        print("\nError")
        print(e)
        traceback.print_exc()


