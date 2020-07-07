# Declare characters used by this game.
define s = Character(_("Sylvie"), color="#c8ffc8")
define m = Character(_("Me"), color="#c8c8ff")

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False
default carpenter = False
default tutor = False
default merchant = False


# The game starts here.
label start:

    # Start by playing some music.
    play music "audio/a_life_well_lived.wav"

    scene bg lecturehall
    with fade
    "I had received a call in the morning from an unfamiliar voice, while I was..."

    menu:

        "Taking measurements for a new stage to be built in town square.":

            jump intro_carpenter

        "Preparing a general lesson plan of maths problems and written exercises.":

            jump intro_tutor

        "Inspecting a recent shipment of goods from one of my suppliers.":

            jump intro_merchant

label intro_carpenter:
    $ carpenter = True

    "Our little town had come a long way over the years. I remember going to the market as a child, the fruits and vegetables on display next to the butcher's meats."

    "Across the street was the cobbler's, which is now a gourmet cafe. Often, you can find patrons lining up out the door and around the corner, as they did for the ice cream shop that was there before it."

    "The town had more recently began sponsoring a summer festival in town square. This year, funds had been set aside for a new stage to be built that would accommodate an expanded live entertainment roster."

    "We would need to start building in the cold of winter to finish in time."

    jump next

label intro_tutor:
    $ tutor = True

    "My newest pupil was the youngest of three. The parents were doctors, and the family had recently moved into the new Galen Heights neighborhood."

    "The outer hills of Atford were now populated with elegant residences that attracted tenants from out of town, all of them seemingy affluent."

    "Not all of the locals were pleased with this development, but I couldn't complain about the increase in clientele."

    "As development increased in the area, there was talk of incorporating Galen Heights into a separate town, which further drew ire."

    jump next

label intro_merchant:
    $ merchant = True

    "I had worked part-time during school at the local..."

    jump next

label next:

    "The gentleman introduced himself as Thomas Lupin, attorney-at-law. I could scarcely fathom what reason a lawyer would have to make my acquaintance."

    "\"Mr. Pryor was a client of mine. I'm sorry to tell you that James has passed away.\""

    "\"He suffered a stroke and unfortunately never recovered. While tragic and untimely, the coroner has determined his passing to be of \"natural cause.\""

    "\"Mr. Pryor left behind a will, drafted by myself and notarized as of this morning. In it, he has appointed you the executor of his estate. If you accept, I will make the necessary arrangements.\""

    "Upon hearing this news, a feeling of unease came over me. Truthfully, Jimmy might as well have been dead to me up until that moment. It had been years since we had last spoken or seen each other.\""

    menu:

        "I'll do it. Please let me know what the next steps are.":

            jump accept

        "I'm afraid I don't understand. What do you mean by \"executor\"?":

            jump ambivalent

        "I haven't spoken to Jim in years, I'm not sure what this has to do with me.":

            jump apathetic

label accept:

    "\"Please meet me at my office this afternoon at 3pm. The address is 32 Fairview Drive, Suite B in the Palace Gardens district. We can discuss the details further in person.\""

    jump james_letter

label ambivalent:

    "\"An executor is tasked with handling the distribution of the deceased's assets...\""


label apathetic:

    "\"Be that as it may, Mr. Pryor named you rather than any other relative or beneficiary. He asked me to put this in writing about three years ago from this date. Of course, you are not obligated to accept. You may choose not to act as Mr. Pryor's executor if you so wish.\""

label short_ending:

    "Jim. Jimmy. That was a lifetime ago. Indeed I shouldn't be obliged to accept, and, in fact, I won't."

    "Surely it was suggested by some party that I may be the right choice, but it appears there's been a mistake."

    menu:

        "He's no longer a part of my life.":

            jump neutral_ending

        "He made his choice once he left. He can get someone else to clean up his mess.":

            jump mean_ending

label neutral_ending:

    scene black

    "Jimmy. Haven't heard that name in a while, didn't think I would again."

    return

label mean_ending:

    scene black

    "I want nothing to do with him."

    return

label james_letter:
    scene bg uni
    with fade

    "When we come out of the university, I spot her right away."

    show sylvie green normal
    with dissolve

    "I've known Sylvie since we were kids. She's got a big heart and she's always been a good friend to me."

    "But recently... I've felt that I want something more."

    "More than just talking, more than just walking home together when our classes end."

    menu:

        "As soon as she catches my eye, I decide..."

        "To ask her right away.":

            jump rightaway

        "To ask her later.":

            jump later

        "To ask her later 2.":

            jump later

        "To ask her later 3.":

            jump later

        "To ask her later 4.":

            jump later


label rightaway:

    show sylvie green smile

    s "Hi there! How was class?"

    m "Good..."

    "I can't bring myself to admit that it all went in one ear and out the other."

    m "Are you going home now? Wanna walk back with me?"

    s "Sure!"

    scene bg meadow
    with fade

    "After a short while, we reach the meadows just outside the neighborhood where we both live."

    "It's a scenic view I've grown used to. Autumn is especially beautiful here."

    "When we were children, we played in these meadows a lot, so they're full of memories."

    m "Hey... Umm..."

    show sylvie green smile
    with dissolve

    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"

    m "Ummm... Will you..."

    m "Will you be my artist for a visual novel?"

    show sylvie green surprised

    "Silence."

    "She looks so shocked that I begin to fear the worst. But then..."

    show sylvie green smile

    menu:

        s "Sure, but what's a \"visual novel?\""

        "It's a videogame.":
            jump game

        "It's an interactive book.":
            jump book


label game:

    m "It's a kind of videogame you can play on your computer or a console."

    m "Visual novels tell a story with pictures and music."

    m "Sometimes, you also get to make choices that affect the outcome of the story."

    s "So it's like those choose-your-adventure books?"

    m "Exactly! I've got lots of different ideas that I think would work."

    m "And I thought maybe you could help me...since I know how you like to draw."

    m "It'd be hard for me to make a visual novel alone."

    show sylvie green normal

    s "Well, sure! I can try. I just hope I don't disappoint you."

    m "You know you could never disappoint me, Sylvie."

    jump marry


label book:

    $ book = True

    m "It's like an interactive book that you can read on a computer or a console."

    show sylvie green surprised

    s "Interactive?"

    m "You can make choices that lead to different events and endings in the story."

    s "So where does the \"visual\" part come in?"

    m "Visual novels have pictures and even music, sound effects, and sometimes voice acting to go along with the text."

    show sylvie green smile

    s "I see! That certainly sounds like fun. I actually used to make webcomics way back when, so I've got lots of story ideas."

    m "That's great! So...would you be interested in working with me as an artist?"

    s "I'd love to!"

    jump marry

label marry:

    scene black
    with dissolve

    "And so, we become a visual novel creating duo."

    scene bg club
    with dissolve

    "Over the years, we make lots of games and have a lot of fun making them."

    if book:

        "Our first game is based on one of Sylvie's ideas, but afterwards I get to come up with stories of my own, too."

    "We take turns coming up with stories and characters and support each other to make some great games!"

    "And one day..."

    show sylvie blue normal
    with dissolve

    s "Hey..."

    m "Yes?"

    show sylvie blue giggle

    s "Will you marry me?"

    m "What? Where did this come from?"

    show sylvie blue surprised

    s "Come on, how long have we been dating?"

    m "A while..."

    show sylvie blue smile

    s "These last few years we've been making visual novels together, spending time together, helping each other..."

    s "I've gotten to know you and care about you better than anyone else. And I think the same goes for you, right?"

    m "Sylvie..."

    show sylvie blue giggle

    s "But I know you're the indecisive type. If I held back, who knows when you'd propose?"

    show sylvie blue normal

    s "So will you marry me?"

    m "Of course I will! I've actually been meaning to propose, honest!"

    s "I know, I know."

    m "I guess... I was too worried about timing. I wanted to ask the right question at the right time."

    show sylvie blue giggle

    s "You worry too much. If only this were a visual novel and I could pick an option to give you more courage!"

    scene black
    with dissolve

    "We get married shortly after that."

    "Our visual novel duo lives on even after we're married...and I try my best to be more decisive."

    "Together, we live happily ever after even now."

    "{b}Good Ending{/b}."

    return

label later:

    "I can't get up the nerve to ask right now. With a gulp, I decide to ask her later."

    scene black
    with dissolve

    "But I'm an indecisive person."

    "I couldn't ask her that day and I end up never being able to ask her."

    "I guess I'll never know the answer to my question now..."

    "{b}Bad Ending{/b}."

    return
