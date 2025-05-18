from g2p_en import G2p
import re
import nltk

#nltk.download('averaged_perceptron_tagger_eng') #one-time download

def text_to_phonemes_with_timeline(characters, start_times, end_times):
    g2p = G2p()

    words = []
    word_timings = []

    current_word = []
    current_start = None
    current_end = None

    # Step 1: Group characters into words
    for ch, start, end in zip(characters, start_times, end_times):
        if ch.strip() == '':
            if current_word:
                words.append(''.join(current_word))
                word_timings.append((current_start, current_end))
                current_word = []
                current_start = None
                current_end = None
            continue

        if current_start is None:
            current_start = start
        current_end = end
        current_word.append(ch)

    # Add final word if any
    if current_word:
        words.append(''.join(current_word))
        word_timings.append((current_start, current_end))

    # Step 2: Convert words to phonemes and assign timings
    phoneme_timeline = []

    for word, (w_start, w_end) in zip(words, word_timings):
        phonemes = g2p(word)
        phonemes = [p for p in phonemes if p != ' ']

        word_duration = w_end - w_start
        if not phonemes:
            continue

        per_phoneme_duration = word_duration / len(phonemes)

        for i, phoneme in enumerate(phonemes):
            ph_start = w_start + i * per_phoneme_duration
            ph_end = ph_start + per_phoneme_duration
            phoneme_timeline.append((phoneme, ph_start, ph_end))

    return phoneme_timeline

    #assert len(characters) == len(start_times) == len(end_times), "Input length mismatch."
    #
    ## 1. Reconstruct the full text and character time intervals
    #text = ''.join(characters)
    #intervals = [(start_times[i], end_times[i]) for i in range(len(characters))]
    #
    ## 2. Use g2p to get phonemes (returns with spaces between words)
    #g2p = G2p()
    #phonemes_raw = g2p(text)
    #
    ## 3. Filter out spaces (g2p returns them as tokens)
    #phonemes = [ph for ph in phonemes_raw if re.match(r"[A-Z]+[0-2]?$", ph)]
    #
    ## 4. Align phonemes to character intervals proportionally
    #total_duration = end_times[-1] - start_times[0]
    #phoneme_duration = total_duration / max(len(phonemes), 1)
    #
    #phoneme_timeline = []
    #current_time = start_times[0]
    #for ph in phonemes:
    #    start = current_time
    #    end = start + phoneme_duration
    #    phoneme_timeline.append((ph, round(start, 3), round(end, 3)))
    #    current_time = end
    #
    #return phoneme_timeline