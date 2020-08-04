# Declare characters used by this game.
define s = Character(_("Sylvie"), color="#c8ffc8")
define m = Character(_("Me"), color="#c8c8ff")

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False
default carpenter = False
default tutor = False
default merchant = False

# Explored
default explored_kitchen = False

# The game starts here.
label start:
    jump kitchen
    # Start by playing some music.

    scene bg lecturehall

    play sound "audio/telephone_ring.ogg"

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

    "The town had begun to sponsor a summer festival and this year, funds had been set aside for a new stage to be built that would accommodate an expanded live entertainment roster."

    "We would need to start building in the cold of winter to finish in time. The winters were now warmer than I had remembered growing up, but cold nevertheless."

    jump next

label intro_tutor:
    $ tutor = True

    "My newest pupil was the youngest of three. The parents were doctors, and the family had recently moved into the new Galenwood neighborhood."

    "The outer hills of Atford were now populated with elegant residences that attracted tenants from out of town, all of them seemingy affluent."

    "Not all of the locals were pleased with this development, but I couldn't complain about the increase in clientele."

    "There was talk of incorporating Galenwood into a separate town, which further drew ire."

    "But progress seemed inevitable and there were never any clear signs of protest other than a petition drafted and posted in town square, lost among the bustle of commerce."

    "In the meantime, was education not the means for bettering oneself and fostering change? Perhaps."

    jump next

label intro_merchant:
    $ merchant = True

    "I had worked part-time at Bolton's, a local store, while I was still a student. The job involved assisting customers and keeping the shop tidy."

    "Eventually, this led to a full-time position managing inventory and keeping the books. When Mr. Bolton retired, I became the purchaser."

    "Deciding what to keep in stock is both a logical and intuitive decision. No matter how tough times are, people continue to purchase goods--it's simply a matter of which goods."


    jump next

label next:

    "The gentleman on the phone introduced himself as Thomas Lupin, attorney-at-law. I could scarcely fathom what reason a lawyer would have to make my acquaintance."

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

    "\"An executor is tasked with handling the distribution of the deceased's assets. All of these must be accounted for and secured.\""

    "\"Any remaining debts will need to be settled and any relevant parties notified of his passing. Though given his stature, it will likely become public knowledge soon enough.\""

    menu:

        "What is the process for handling these tasks? This is all very unfamiliar to me.":

            jump curious

        "This sounds like quite a lot of work, if I'm being honest.":

            jump cautious

label curious:

    "\"Not to worry. If you should accept, I will assist you to the best of my ability. You merely need to adhere to Mr. Pryor's wishes in his will.\""

    "\"The bulk of your efforts will be directed towards locating the aforementioned assets. If any questions arise, please don't hesitate to contact me directly.\""

    menu:

        "If you can provide me with some guidance, I'll do my best.":

            jump diligent

        "Respectfully, I must decline. This seems beyond the scope of reasonable effort.":

            jump do_nothing

label cautious:

    "\"By all means, this will require no small effort on your part. Mr. Pryor has only one property that I know of, but...\""

    menu:

        "(accept)":

            jump circumspect

        "(decline)":

            jump cynical

label diligent:

    "\"Certainly, I'm at your service...\""

    jump james_letter

label do_nothing:

    "\"I see, and I thank you for your time.\""

    jump mean_ending


label apathetic:

    "\"Be that as it may, Mr. Pryor named you rather than any other relative or beneficiary. He asked me to put this in writing about three years ago from this date.\""

    "\"Of course, you are not obligated to accept. You may choose not to act as Mr. Pryor's executor if you so wish. But I might add that you will be compensated for your efforts.\""

    menu:

        "All right, let's see what this is about.":

            jump beholder

        "I understand, and I'd prefer not to be involved.":

            jump bystander

label circumspect:

    "\"I hope I was able to (answer your questions)\""

    jump james_letter

label cynical:

    "\"I understand if...\""

    jump neutral_ending

label beholder:

    "\"Perhaps it may become clearer if we're to meet and further discuss...\""

    jump james_letter

label bystander:

    "\"Very well, and I'm sorry to have disturbed you. I wish you good day.\""

    jump mean_ending

label short_ending:

    "Jim. Jimmy. That was a lifetime ago. I don't know why he thought of me, but there's been a mistake."

    menu:

        "He's no longer a part of my life.":

            jump neutral_ending

        "He can get someone else to clean up his mess.":

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

    scene letters_6

    "To my old friend."
    "Thomas tells me I need to plan for when I'm gone..."

    scene stephen_king_mansion at truecenter

    "It looks like I've just arrived. It's the only mansion among all of these houses, so it's difficult to miss but I almost passed it by, being my first time here."

    "The gate creaks open slowly..."

    menu:

        "As if to speak of an untold history waiting to be discovered.":

            jump optimistic

        "Ominously, to forebode those who would enter.":

            jump pessmistic

label optimistic:

    "The front yard is trim and well-kept and in the midst of neatly manicured bushes, I take in the serene lull of peace and seclusion."

    jump front_door

label pessmistic:

    "It becomes eerily quiet once I've moved away from the street.."

    jump front_door

label front_door:

    "I walk up to the front door and I reach in my pocket for the key, provided by Mr. Lupin along with a written copy of Jimmy's last instructions."

    "It unlocks easily enough."

label hallway_menu:

    scene stephen_king_hall at truecenter

    "The hall is airy and bright when I enter..."

    menu:

        "Kitchen":

            jump kitchen_menu

        "Hallway":

            jump hallway_menu

        "Study":

            jump study_menu

        "Upstairs":

            jump upstairs_menu


label dining_room_menu:

    # NEEDS IMAGE
    scene stephen_king_hall at truecenter

    menu:

        "Stay here":

            jump dining_room

        "Kitchen"

            jump kitchen_menu

        "Patio"

            jump patio_menu

        "Hallway"

            jump hallway_menu

label dining_room:

    menu:

        "go back":

            jump dining_room_menu

label patio_menu:

    # NEEDS IMAGE
    scene stephen_king_hall at truecenter

    menu:

        "Stay here":

            jump patio

        "Dining Room"

            jump dining_room_menu

label patio:

    menu:

        "go back":

            jump patio_menu

label lounge_menu:

    scene living_2 at truecenter

    menu:

        "Pick a direction"

        "Stay here":

            jump lounge

        "Library"

            jump library_menu

        "Hallway"

            jump hallway_menu

label lounge:

    menu:

        "go back":

            jump lounge_menu


label library_menu:

    scene library at truecenter

    menu:

        "Pick a direction"

        "Stay here":

            jump library

        "Lounge"

            jump lounge_menu


label library:

    menu:

        "go back":

            jump library_menu

label kitchen_menu:

    scene kitchen_1 at truecenter

    menu:

        "Pick a direction"

        "Stay here":

            jump kitchen

        "Dining Room":

            jump dining_room_menu

label kitchen:

    if explored_kitchen:

        "I've been here before"

    menu:

        "Pick a direction"

        "Look in cupboard":

            jump kitchen_cupboard

        "Look out window":

            jump kitchen_window

        "Look some more" if explored_kitchen:

            jump kitchen_hidden

        "go back":

            jump kitchen_menu

label kitchen_window:

    $ explored_kitchen = True

    "Look out the window wow!"

    jump kitchen

label kitchen_cupboard:

    $ explored_kitchen = True

    "It's full of glass and raisins"

    jump kitchen

label kitchen_hidden:

    "I looked inside and found some yucky olives"

    jump kitchen

label upstairs_menu:

    # NEEDS IMAGE?
    scene hallway3 at truecenter

    "The upstairs is hallway-y"

    menu:

        "Pick a direction"

        "Downstairs":

            jump hallway_menu

        "Study":

            jump study_menu

        "Conservatory":

            jump conservatory_menu

        "Balcony":

            jump balcony_menu

label conservatory_menu:

    # NEEDS IMAGE
    scene billiards at truecenter

    "The conservatory is full of antiques"

    menu:

        "Pick a direction"

        "Stay here":

            jump conservatory

        "Salon":

            jump salon_menu

        "Hallway":

            jump upstairs_menu

label conservatory:

    "The antiques are shiny"

    menu:

        "Pick a direction"

        "Go back":

            jump conservatory_menu

label salon_menu:

    scene salon at truecenter

    "The salon is full of sofas"

    menu:

        "Pick a direction"

        "Stay here":

            jump salon

        "Conservatory":

            jump conservatory_menu

label salon:

    "The sofas are comfy"

    menu:

        "Pick a direction"

        "Go back":

            jump salon_menu

label balcony_menu:

    # NEEDS IMAGE
    scene salon at truecenter

    "The balcony is full of air"

    menu:

        "Pick a direction"

        "Stay here":

            jump balcony

        "Hallway":

            jump upstairs_menu

label balcony:

    "The air is fresh"

    menu:

        "Pick a direction"

        "Go back":

            jump balcony_menu

label study_menu:

    scene study at truecenter

    "The study is full of books"

    menu:

        "Pick a direction"

        "Stay here":

            jump study

        "Bedroom":

            jump bedroom_menu

        "Hallway":

            jump upstairs_menu

label study:

    "The books are musty"

    menu:

        "Pick a direction"

        "Go back":

            jump study_menu

label bedroom_menu:

    # NEEDS IMAGE
    scene salon at truecenter

    "The bedroom is full of beds"

    menu:

        "Pick a direction"

        "Stay here":

            jump bedroom

        "Study":

            jump study_menu

        "Bathroom":

            jump bathroom_menu

label bedroom:

    "The bed is beddy"

    menu:

        "Pick a direction"

        "Go back":

            jump bedroom_menu

label bathroom_menu:

    # NEEDS IMAGE
    scene salon at truecenter

    "The bathroom is full of baths"

    menu:

        "Pick a direction"

        "Stay here":

            jump bathroom

        "Bedroom":

            jump bedroom_menu

label bathroom:

    "The baths are bathy"

    menu:

        "Pick a direction"

        "Go back":

            jump bathroom_menu



    # scene bg uni
    # with fade
    #
    # "When we come out of the university, I spot her right away."
    #
#     show sylvie green normal
#     with dissolve
#
#     "I've known Sylvie since we were kids. She's got a big heart and she's always been a good friend to me."
#
#     "But recently... I've felt that I want something more."
#
#     "More than just talking, more than just walking home together when our classes end."
#
#     menu:
#
#         "As soon as she catches my eye, I decide..."
#
#         "To ask her right away.":
#
#             jump rightaway
#
#         "To ask her later.":
#
#             jump later
#
#         "To ask her later 2.":
#
#             jump later
#
#         "To ask her later 3.":
#
#             jump later
#
#         "To ask her later 4.":
#
#             jump later
#
#
# label rightaway:
#
#     show sylvie green smile
#
#     s "Hi there! How was class?"
#
#     m "Good..."
#
#     "I can't bring myself to admit that it all went in one ear and out the other."
#
#     m "Are you going home now? Wanna walk back with me?"
#
#     s "Sure!"
#
#     scene bg meadow
#     with fade
#
#     "After a short while, we reach the meadows just outside the neighborhood where we both live."
#
#     "It's a scenic view I've grown used to. Autumn is especially beautiful here."
#
#     "When we were children, we played in these meadows a lot, so they're full of memories."
#
#     m "Hey... Umm..."
#
#     show sylvie green smile
#     with dissolve
#
#     "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."
#
#     "I'll ask her...!"
#
#     m "Ummm... Will you..."
#
#     m "Will you be my artist for a visual novel?"
#
#     show sylvie green surprised
#
#     "Silence."
#
#     "She looks so shocked that I begin to fear the worst. But then..."
#
#     show sylvie green smile
#
#     menu:
#
#         s "Sure, but what's a \"visual novel?\""
#
#         "It's a videogame.":
#             jump game
#
#         "It's an interactive book.":
#             jump book
#
#
# label game:
#
#     m "It's a kind of videogame you can play on your computer or a console."
#
#     m "Visual novels tell a story with pictures and music."
#
#     m "Sometimes, you also get to make choices that affect the outcome of the story."
#
#     s "So it's like those choose-your-adventure books?"
#
#     m "Exactly! I've got lots of different ideas that I think would work."
#
#     m "And I thought maybe you could help me...since I know how you like to draw."
#
#     m "It'd be hard for me to make a visual novel alone."
#
#     show sylvie green normal
#
#     s "Well, sure! I can try. I just hope I don't disappoint you."
#
#     m "You know you could never disappoint me, Sylvie."
#
#     jump marry
#
#
# label book:
#
#     $ book = True
#
#     m "It's like an interactive book that you can read on a computer or a console."
#
#     show sylvie green surprised
#
#     s "Interactive?"
#
#     m "You can make choices that lead to different events and endings in the story."
#
#     s "So where does the \"visual\" part come in?"
#
#     m "Visual novels have pictures and even music, sound effects, and sometimes voice acting to go along with the text."
#
#     show sylvie green smile
#
#     s "I see! That certainly sounds like fun. I actually used to make webcomics way back when, so I've got lots of story ideas."
#
#     m "That's great! So...would you be interested in working with me as an artist?"
#
#     s "I'd love to!"
#
#     jump marry
#
# label marry:
#
#     scene black
#     with dissolve
#
#     "And so, we become a visual novel creating duo."
#
#     scene bg club
#     with dissolve
#
#     "Over the years, we make lots of games and have a lot of fun making them."
#
#     if book:
#
#         "Our first game is based on one of Sylvie's ideas, but afterwards I get to come up with stories of my own, too."
#
#     "We take turns coming up with stories and characters and support each other to make some great games!"
#
#     "And one day..."
#
#     show sylvie blue normal
#     with dissolve
#
#     s "Hey..."
#
#     m "Yes?"
#
#     show sylvie blue giggle
#
#     s "Will you marry me?"
#
#     m "What? Where did this come from?"
#
#     show sylvie blue surprised
#
#     s "Come on, how long have we been dating?"
#
#     m "A while..."
#
#     show sylvie blue smile
#
#     s "These last few years we've been making visual novels together, spending time together, helping each other..."
#
#     s "I've gotten to know you and care about you better than anyone else. And I think the same goes for you, right?"
#
#     m "Sylvie..."
#
#     show sylvie blue giggle
#
#     s "But I know you're the indecisive type. If I held back, who knows when you'd propose?"
#
#     show sylvie blue normal
#
#     s "So will you marry me?"
#
#     m "Of course I will! I've actually been meaning to propose, honest!"
#
#     s "I know, I know."
#
#     m "I guess... I was too worried about timing. I wanted to ask the right question at the right time."
#
#     show sylvie blue giggle
#
#     s "You worry too much. If only this were a visual novel and I could pick an option to give you more courage!"
#
#     scene black
#     with dissolve
#
#     "We get married shortly after that."
#
#     "Our visual novel duo lives on even after we're married...and I try my best to be more decisive."
#
#     "Together, we live happily ever after even now."
#
#     "{b}Good Ending{/b}."
#
#     return
#
# label later:
#
#     "I can't get up the nerve to ask right now. With a gulp, I decide to ask her later."
#
#     scene black
#     with dissolve
#
#     "But I'm an indecisive person."
#
#     "I couldn't ask her that day and I end up never being able to ask her."
#
#     "I guess I'll never know the answer to my question now..."
#
#     "{b}Bad Ending{/b}."
#
#     return
