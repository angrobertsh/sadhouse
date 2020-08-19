marian - doesn't feel seen
everyone in the outside world trusts her husband is taking care of her but he isn't really and her sickness isn't mental
daedelaus? helios?
totally made up names

""
""
"Maybe I'm who I always was. Who I wasn't letting myself become. You never saw me. You saw who you wanted me to be."

label pasiphae_play_intro:

  "In the drawer I found a book with neatly penned pages. This penmanship was neat, evenly spaced, and deliberately cursive. It seemed this book may not have been meant for publishing. The lack of title, and author's name helped confirm my suspicions."

  menu:

    "This must be one of James' unpublished works":
      $ pasiphae_author = "James"
      jump pasiphae_play

    "This must be someone else's work":
      jump pasiphae_play_author

label pasiphae_play_author:

  "But who else could it have been?"

  menu:

    "Someone must have left this here and forgotten about it":
      $ pasiphae_author = "this unknown author"
      jump pasiphae_play_author_mystery

    "Someone must have spent a lot of time here writing it":
      $ pasiphae_author = "Marian"
      jump pasiphae_play_author_marian

label pasiphae_play_author_mystery:

  "The author of this book must have thought very little of his or her work to leave it here"

  "Probably some very drunk or very happy party guest"

  jump pasiphae_play

label pasiphae_play_author_marian:

  "The only other person who lived here was Marian. This was likely something she'd written"

  jump pasiphae_play

label pasiphae_play:

if tutor:

  "I began leafing through the book, immediately recognizing the names of the characters. Pasiphae, the Greek sorceress who was cursed by Poseidon into loving a bull. Her husband, Minos, and the chorus, a third party voice of reason."

  "This seemed to be a retelling of that tale, but the details were indistinct. Poseidon was no godlike man, rising from the sea, in fact, there appeared to be no evidence of him at all."

  "The story came to a head when I recognized the curse gripping her:"

  "{b}Minos{/b}: Is it true that you want to fuck a bull? The guards are gossiping but I speak to you as an equal."

  "{b}Pasiphae (defensively){/b}: What do you care what I want?"

  "{b}Minos{/b}: I don't understand, this isn't like you."

  "{b}Pasiphae (with wild eyes){/b}: I want to fuck the bull"

  "{b}Chorus{/b}: Minos will talk some sense into her."

  "{b}Minos{/b}: Pasiphae you're crazy, stop it. There must be some explanation for this, some supernatural cause"

  "{b}Pasiphae{/b}: I want to do one thing and you automatically assume I'm cursed?"

  "{b}Chorus{/b}: She must be cursed. Minos will definitely talk some sense into her."

  "{b}Pasiphae{/b}: Maybe I'm who I always was. Who I wasn't letting myself become. You never saw me. You saw who you wanted me to be."

  "There was something about this Pasiphae, something more fragile than what I imagined the bewitching woman in the myths."

  "I didn't know if this version of Poseidon's curse included some fear of perception, some self-consciousness that brought her to her knees more than any sort of bestial lust could."

  "In the end, Pasiphae carried out her plan against the backdrop of an uncaring world."

  "The consequences of her actions showed her unraveling, the play ending ultimately as she held up her bloodied child, the minotaur, her face contorting with laughter as she died."

  if pasiphae_author == "Marian"

    "I thought about the implications of Marian having written this."

  menu:

    "This must be a fun and fanciful exercise of the mind":

      jump pasiphae_play_fun

    "This must be the product of a truly disturbed mind":

      jump pasiphae_play_mad

    "This must be something Marian had kept in secret" if pasiphae_author == "Marian":

      jump pasiphae_play_sympathy

if carpenter:

  "There was a play of some sort in the book. I didn't quite understand it, but it did seem to refer to some Greek myth."

  "They certainly were a strange lot, back then."

  "Strange, but fascinating."

  "As I leafed through the pages, I eventually got to a description of a wooden bull, and some rather... wild events."

  "{i}{b}WOODEN BULL{/b} enters right. It is made of heavy mahogany, with wheels of iron.{/i}

  "{i}Inlaid are sapphires around its neck, rubies on its hooves, a pearl on its forehead shaped like a crescent moon.{/i}"

  "{i}Its horns are proud, comely, its udders hang heavily. Its tail is goldenrod braided silk. Clearly visible on its side is a hinged entrance. Within is Pasiphae.{/i}"

  "{b}Pasiphae (booming, within the wooden bull){/b}: Bring him! Bring the mighty bull! I can stand it no longer! Thus is the decree of your queen! See me! The heat that burns within me cannot be quenched by mere man."

  "(beat)"

  "{b}Chorus{/b}: Lust, a curse, only ruination it brings. The weak, the strong, all tremble beneath it. The powerful dive in, and they leave a ripple, deeper in, the stronger they are. Merciless Aphrodite reels her line tightly."

  "{b}Pasiphae{/b}: Can you not see? Aphrodite holds no sway over me. Hear me. The sound of my voice is my own. You look at me and see a daughter of Helios. Is that not proof enough?"

  "{b}Chorus{/b}: She says she is under no curse. Surely she can control herself, our mighty queen, sorceress, wise ruler. There is no sense in what she does. Where is the truth in her words? Is she mad or is she cursed?"

  "{b}Pasiphae{/b}: Do you not heed your queen? Not once, but twice you disobey my call. Behold me. I am she. There is no curse here. And what would you know what I'm like? Bring forth the bull that I seek. You have allowed me to come this far, why would you try and stop me now?"

  "{i}THE KING'S BULL{/i} enters left and approaches {i}WOODEN BULL{/i}"  

  "{b}Pasiphae{/b}: Alight! Yes! This is sweet madness. Witness me!"  

  "There was then a very graphic description about the real bull mounting the wooden bull on the stage and Pasiphae crying out in 'ecstatic pain.'"

  "Part of me was downright leery of the mind that recreated this scene. The other part of me wondered where the air holes would be in this wooden bull."

  "Certainly, though, there had to be a degree of hilarity to even consider a theater production could afford mahogany, sapphires, and rubies, and a real, raging bull."

  "So what did this all mean?"

  menu:

    "It must be a fun and fanciful exercise of the mind":

      jump pasiphae_play_fun

    "It must be the product of a truly disturbed mind":

      jump pasiphae_play_mad

label pasiphae_play_fun:

  if pasiphae_author == "Marian":
    $ marian_play_fun = True

    "Literature was meant to explore ideas. I'm glad she had this outlet to express herself."

  else:
    "Literature was meant to explore ideas. I'm glad the [pasiphae_author] was able to put this idea to paper."

  "James, certainly was nothing like the characters in his books."

  "I put the book back in the drawer"

  jump conservatory_menu

label pasiphae_play_mad:

  if pasiphae_author == "Marian":
    $ marian_play_crazy = True

    "What drew her to this story, and what made her want to express it in such graphic detail?"

    "Surely this was the work of someone who was truly unwell. I hope she got the help she needed."

  if pasiphae_author == "James":
    "James... some part of you must have been truly unwell. I can only hope that writing this helped bring you peace, or urged you to get the help you needed."

  else:
    "The author of this story must have been truly unwell. I can only hope that writing this helped bring them peace, or urged them to get the help they needed."

  "I put the book back in the drawer"

  jump conservatory_menu

label pasiphae_play_sympathy:

  $ marian_play_sympathy = True

  "It must have taken Marian a lot of courage to write something like this."

  "And to have to have hidden it in such a place in their home, it's clear this was something she couldn't speak to James about."

  "I put the book back in the drawer"

  jump conservatory_menu

if merchant



PASIPHAE was an immortal daughter of the sun-god Helios. Like her siblings, Aeetes and Kirke (Circe), she was a skilled practitioner of witchcraft (pharmakeia).

Pasiphae married King Minos of Krete (Crete) and bore him a number of sons and daughters. As punishment for some offence against the gods--committed either by herself or her husband--she was cursed with lust for the king's finest bull. The queen enlisted the help of the artisan Daidalos (Daedalus) who built her an animate, wooden cow wrapped in bovine-skin. Hidden inside the contraption she coupled with the bull and conceived a hybrid child--the bull-headed Minotauros (Minotaur).

Pasiphae's husband King Minos also proved unfaithful. When she learned of his indiscretions she bewitched him, causing him to ejaculate poisoned creatures and destroy his lovers. Pasiphae herself, being an immortal, was alone immune to the spell. Minos was later cured by the Athenian girl Prokris (Procris) who devised a remedy for the strange afflication.

Pasiphae was an early Kretan moon-goddess similar to the classical Selene. Both her taurine lover and her Minotaur son--who was also named Asterios (Starry One)--were associated with the constellation Taurus.