label splashscreen:
    scene black
    with Pause(2)
    return

# Declare characters used by this game.
define s = Character(_("Sylvie"), color="#c8ffc8")
define m = Character(_("Me"), color="#c8c8ff")

# Qualities/attributes
default carpenter = False
default tutor = False
default merchant = False
default mood = 0
default likes_alcohol = False

# "From my vantage point, it seemed that James's life had unfolded like a dream."
#
# "When we were at school together, he'd spoken of leaving, writing the next great novel, and making a name for himself."
#
# "A man of his word, after escaping as fast as he could from Atford, he'd went to Lintonbury, where he took a job in a mailroom at a big publishing company."
#
# "He'd filled me in on the broad strokes, and I was left to imagine his life there."
#
# "Working in the mailroom, thinking of the next plotline in his novel, then getting it all down onto paper at night, as soon as he could."
#
# "Presumably he'd met Rory, and Marian, as well, somewhere in those youthful days."
#
# "Eventually he got his big break, his first novel published, 'A Nobel Charade', and everything just went from there."
#
# "The fame, the wife, then the home, he'd made it and settled into the life of his dreams in his early 30s, in this house, in Palace Gardens."
#
# # no college
# # straight out of high school, went to a BIG  city
# # prestigious city + seediness
# # Lintonbury where he met rory
# # they would write together
# # mailroom stuff
# # james got a big  break  one day, according to rory and then put in good word for rory
# # lintonbury -> palace gardens around late  20s early 30s because he made  it

# Explored
default explored_kitchen = False
default explored_lounge_piano = False
default explored_lounge_window = False
default explored_lounge_chair = False
default explored_dining_room_dining_table_sit = False
default explored_dining_room_dining_room_dining_trappings = False
default explored_kitchen_cupboard = False
default explored_kitchen_window = False
default explored_library_book_1 = False
default explored_library_book_2 = False
default explored_library_book_3 = False

# Insight
default insight_1_library_book_1 = False
default insight_2_library_book_1 = False
default insight_3_library_book_1 = False

# Insight - Rory
default rory_jimmy = False
default rory_business_card = False
default rory_artist = False
default rory_choices = False
default rory_atford = False
default rory_travel = False

# Insight - Marian Play
default pasiphae_author = "this unknown author"
default marian_play_fun = False
default marian_play_crazy = False
default marian_play_sympathy = False

# The game starts here.
label start:

    # Start by playing some music.

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

    jump attorney

label intro_tutor:
    $ tutor = True

    "My newest pupil was the youngest of three. The parents were doctors, and the family had recently moved into the new Galenwood neighborhood."

    "The outer hills of Atford were now populated with elegant residences that attracted tenants from out of town, all of them seemingy affluent."

    "Not all of the locals were pleased with this development, but I couldn't complain about the increase in clientele."

    "There was talk of incorporating Galenwood into a separate town, which further drew ire."

    "But progress seemed inevitable and there were never any clear signs of protest other than a petition drafted and posted in town square, lost among the bustle of commerce."

    "In the meantime, was education not the means for bettering oneself and fostering change? Perhaps."

    jump attorney

label intro_merchant:
    $ merchant = True

    "I had worked part-time at Bolton's, a local store, while I was still a student. The job involved assisting customers and keeping the shop tidy."

    "Eventually, this led to a full-time position managing inventory and keeping the books. When Mr. Bolton retired, I became the purchaser."

    "Deciding what to keep in stock is both a logical and intuitive decision. No matter how tough times are, people continue to purchase goods--it's simply a matter of which goods."

    jump attorney

label attorney:

    "The gentleman on the phone introduced himself as Thomas Lupin, attorney-at-law. I could scarcely fathom what reason a lawyer would have to make my acquaintance."

    "\"Mr. Pryor was a client of mine. I'm sorry to tell you that James has passed away.\""

    "\"He suffered a stroke and unfortunately never recovered. While tragic and untimely, the coroner has determined his passing to be of \'natural cause.\'\""

    "\"Mr. Pryor left behind a will, drafted by myself and notarized as of this morning. In it, he has appointed you the executor of his estate. If you accept, I will make the necessary arrangements.\""

    "Upon hearing this news, a feeling of unease came over me. Truthfully, Jimmy might as well have been dead to me up until that moment. It had been years since we had last spoken or seen each other."

    menu:

        "I'll do it. Please let me know what the next steps are.":

            jump accept

        "I'm afraid I don't understand. What do you mean by \"executor\"?":

            jump ambivalent

        "I haven't spoken to Jim in years, I'm not sure what this has to do with me.":

            jump apathetic

label accept:

    "Regardless of the past, Jimmy had been a friend of mine and now he was gone forever. Surely I could take on this responsiblity on account of that."

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

    "Palace Gardens is a fine place to live."

    "Perhaps you'll visit one day."

    # TODO this letter is unfinished

    scene stephen_king_mansion at truecenter

    "It looks like I've just arrived. It's the only mansion among all of these houses, so it's difficult to miss but I almost passed it by, being my first time here."

    "The gate creaks open slowly..."

    menu:

        "As if to speak of an untold history waiting to be discovered.":

            jump optimistic_house

        "Ominously, to forebode those who would enter.":

            jump pessimistic_house

label optimistic_house:
    $ mood = mood + 1

    "The front yard is trim and well-kept and in the midst of neatly manicured bushes, I take in the serene lull of peace and seclusion."

    jump front_door

label pessimistic_house:
    $ mood = mood - 1

    "It becomes eerily quiet once I've moved away from the street.."

    jump front_door

label front_door:

    "I walk up to the front door and I reach in my pocket for the key, provided by Mr. Lupin along with a written copy of Jimmy's last instructions."

    "It unlocks easily enough."

label hallway_menu:

    scene stephen_king_hall at truecenter

    "The hall is airy and bright when I enter..."

    "To my right is the lounge. I move beyond and enter."

label lounge:

    scene piano living room at truecenter

    "Where he would have received his many distinguished guests."

    "The grand piano is what immediately draws the eye."

    "Sunlight pours in through a French door that offers a view into a garden patio."

label lounge_menu:

    menu:

        "I examine the piano" if not explored_lounge_piano:

            jump lounge_piano

        "I gaze out the window" if not explored_lounge_window:

            jump lounge_window

        "I take a seat on a nearby chair" if not explored_lounge_chair:

            jump lounge_chair

        "I move on":

            jump lounge_end

label lounge_end:

    "I suppose it's strange that I never once visited at all."

if mood > 0:

    "Time went by and before I knew it, most of my days would pass without any thought of him"

    jump library

if mood < 1:

    "I had begun to grow weary of his noncommittal gestures"

    jump library

label lounge_piano:

    $ explored_lounge_piano = True

    "There is a thin layer of dust atop the keys. Lowering the cover could have protected them, but the dust would have lain upon here all the same. This instrument hasn't been played in quite some time."

    "Did Jimmy continue to play? Growing up, nobody we knew had a piano in the home but there had been one at the schoolhouse. We began music lessons in our third year and were made to sing carols for the headmaster and teachers during the holiday season."

    "A distantly familiar tune makes its way into my head. I've since forgotten how to play bass clef or read sheet music, but I've retained some basic scales."
    "Instinctively, I wipe away some of the dust and plunk out a crude melody."

    "The trillbird sings his song\nIn a hollow grove\nWith nary a throng\nFound below or above"
    "O sweet songbird, alight\nCalm the anger of the earth\nKeep the fire burning bright\nIn our hearts and the hearth"

    play music "audio/The Trillbird.mp3" fadein 10.0

    jump lounge_menu

label lounge_window:

    $ explored_lounge_window = True

    "The grand windows allow the sun to shine beautifully into this room."

    "I look out towards the path I'd taken to enter the home and am struck by just how lovely a neighborhood this is."

    "Greenery all around, a lawn for dogs or kids, gentle shade from trees in the summer, curtains for coziness in winter."

    "I wonder if James knew what a lovely home he had."

    jump lounge_menu

label lounge_chair:

    $ explored_lounge_chair = True

    "Despite its plush appearance, the chair feels stiff underneath me from lack of use."

if carpenter:

    "Some furniture ends up being more decorative than functional."

    "Though, if that were the case, I would have picked a lower quality leather to upholster. This burnished full-grain has been left in the sun to get crisp, like an old pencil eraser. Such a shame."

    "James himself must have spent most of his time in more private areas. In such a large house, I could easily see him picking several favorite nooks to curl into. Just not here."

    jump lounge_menu

if tutor:

    "It feels the same as some of my client's lounges I have been in."

    "I imagine the homes that love could have built. A child playing the piano while his doting parents watch on, or a favored guest entertaining her hosts with a newfound talent."

    "I feel a moment of warmth, but it is gone when I remember my sad business here."

    jump lounge_menu

if merchant:

    "It's all about the piano."

    "Esteemed guests would have crowded around, standing and craning their necks to hear the latest jingle be played. There would be no room for sitting, lest you miss a single note."

    "That's just how people are. Too much excitement with such a beautiful instrument in front of them. No wonder these chairs were stiff!"

    "No need for me to sit, either. There's too much to see, too much afoot."

    jump lounge_menu

label library:

    stop music fadeout 1.0

    scene library at truecenter

    "Jimmy was a writer after all, so it makes sense that he would own many books, and have a room dedicated to them. The library has a scent of wood and laminant."

    "A few volumes catch my eye:"

label library_menu:

    menu:

        "A Gentleman's Guide to Negotiation." if not explored_library_book_1:

            jump library_book_1

        "Hell Exists On Earth, a novel by Rory Stuart." if not explored_library_book_2:

            jump library_book_2

        "A Noble Charade, James's own work" if not explored_library_book_3:

            jump library_book_3

        "I move on":

            jump dining_room

# INSIGHT

label library_book_1:

    $ explored_library_book_1 = True

    "It's immediately clear how this would differ from a ladies' version."

    "I glance over a few pages and see a section about good posture ('keep an erect carriage,' it says)."

    "Next is a section on a lady's favorite drinks and what they might mean ('avoid {i}desmoiselles{/i} who indulge in beverages served by the pint')."

    menu:

        "He was brushing up on a useful skill":

            jump library_book_1_insight_1

        "Was there something he needed to negotiate?":

            jump library_book_1_insight_2

        "This is a book about how the weak becoming strong":

            jump library_book_1_insight_3

label library_book_1_insight_1:

    $ insight_1_library_book_1 = True

    "While certainly painting in broad strokes, I could imagine James using some of these tips and tricks, so to speak, to meet and identify with people."

    "Ever the gentleman, he could refine some of the more coarse lessons here, clothe them in  manners, and serve them to guests like fine hors d'oeuvres."

    "\"A change of scenery will bring a change of mindset. A fresh location will bring about a fresh mood and a fresh conversation.\""

    "I smiled as I imagined James practicing this one, gliding a lady friend down a hallway, making her heart flutter in a pool of moonlight."

    "I considered a moment pocketing the book, but decided better of it. Back on the shelf it went."

    jump library_menu

label library_book_1_insight_2:

    $ insight_2_library_book_1 = True

    "This seemed like a book made for a young, insecure man, of which James was nothing of the sort."

    "Besides, he'd been happily married to Marian for... decades surely."

    "\"Your wardrobe on your best night out should layer your accent pieces. They are sure to attract attention, and after all, all attention is good attention.\""

    "James, strutting about with handfuls of rings, acid green shoelaces, and a bowler hat. I could think of nothing funnier!"

    "\"Never let a woman ruin your confidence. Should you ever feel unvalued, allow yourself to remind her that she should be lucky for the opportunity to be speaking to you.\""

    "I imagined him trying to 'put Marian in her place.' There was no way she would let anything of the sort pass."

    "He must have received this book as a gag gift. I chuckled as I put it back on the shelf."

    jump library_menu

label library_book_1_insight_3:

    $ insight_3_library_book_1 = True

    "Knowledge is power. And if I knew anything about James, it was that he wanted to know everything about the people around him."

    "I think one of his greatest talents was making enemies, friends, and understanding how he could get what he wanted from you."

    "Some tips in this guide seemed helpful and fairly innocuous:"

    "\"A change of scenery will bring a change of mindset. A fresh location will bring about a fresh mood and a fresh conversation.\""

    "But, there was a decidedly metallic edge to others:"

    "\"Never let a woman ruin your confidence. Should you ever feel unvalued, allow yourself to remind her that she should be lucky for the opportunity to be speaking to you.\""

    "I remembered some of the women in his life, his mother, his wife, and wondered what in him needed to be hardened to survive this world."

    "I put the book back on the shelf."

    jump library_menu

label library_book_2:

    $ explored_library_book_2 = True

    "Propped up on the shelf, this first edition is leather-bound and has a note scribbled in the very back."

    "To James,"
    "Through hell and back, mate. See you there again someday--"
    "RS"

    scene black
    with fade

    "I met Rory once, at Jimmy's wedding. Besides Jimmy, there wasn't a soul that I knew at the affair. Jimmy had spoken of his bride in passing, but it wasn't until the reception that I met Marian for the first time."
    "Rory Stuart is a famous writer in his own right, but he had been the only guest with whom I had felt somewhat at ease."

    scene wedding_church at truecenter
    with fade

    "I've arrived on the very day of their matrimony. The venue is located in neighboring Hestia outside of Palace Gardens, and a night in either city is beyond my means."
    "When I step into the church, my attire feels simple in comparison to the sharp suiting and elegant dresses of the other attendants."

    scene wedding_reception at truecenter
    with fade

    "After the ceremony, I manage to briefly chat with Jimmy and Marian before they move on to greeting their other guests."

    "I'm standing alone, sipping my third glass of wine when Rory approaches the bar for another drink."

    "With whiskey in one hand, he introduces himself with a firm, jovial handshake. \"So how do you know James?\""

    menu:

        "He's a good friend of mine.":

            jump good_friend

        "We were schoolmates.":

            jump schoolmates

        "We're from the same hometown.":

            jump hometown

label good_friend:

    "\"Is that so? Pleased to meet another dear friend of his. Surprised we haven't met before.\""

    menu:

        "Likewise, and how did you meet Jimmy?":

            jump rory_friend

        "The pleasure is mine, I'm an admirer of your work.":

            jump rory_admirer

label rory_friend:
    $ rory_jimmy = True

    "\"Jimmy?\" He lets out an amused chuckle. \"I'll have to call him that from now on.\""

    "He eagerly takes a sip of whiskey from his glass, as if about to recount a favorite tale."

    "\"James and I met while living at the same cheap hostel in Lintonbury. All sorts of mad folks there like you wouldn't believe. Some strange characters, I tell you...\""

    "\"So we'd been staying there for about a year--stop me if you've heard this all before. No? All right, so there was a roof terrace where we used to write together.\""
    "\"We were up there working one day as usual, when our dear fellow tells me that he's getting published through Smith and Simmons.\""
    "\"That's right, A Noble Charade. Finally gave him a chance after all of that grunt work. We all have to pay our dues, yeah?\""

    "\"Then right at that moment, one of the other tenants comes {i}storming{/i} up, accusing us of stealing his soap! As mad as it was, I'll always have fond memories of that place.\""
    "\"And James put in a good word for me with S&S, and look where we are. I'll always be grateful to him.\""

    jump wedding_end

label rory_admirer:
    $ rory_business_card = True

    "Rory brightens at my words. \"Thanks, buddy. That means a lot. So then I take it that we're both admirers of James' work. Do you know that feeling, when you're witnessing somebody doing exactly what they're meant to do? That bastard was born to write.\""

    "\"Do you know what I mean? To be able to do what you love for a living. You can be good at things but not necessarily like them, you know?\""
    "\"Sometimes, I think it's good to try things you're not good at either.\" His words are slurred with drink, but his gestures become more animated. \"But then you might find something you're really, really good at and that's why you're here.\""
    "\"I'm rambling, aren't I? Anyway, I'm really flattered if you've enjoyed my writing. It really means a lot.\""
    "He regards me good-naturedly."

if carpenter:

    "\"I've always had a respect for your craft. I purchased a new table and chair set for my parlor. I found them at an antiques shop and the quality is just fantastic.\""
    "\"You really do get what you pay for, it's nothing like those do-it-yourself assembly pieces that are so popular these days...\""

    jump wedding_end

if tutor:

    "\"To be honest, I've never been much for higher education. If you have it, you have it. I don't think talent can be taught.\""
    "\"But some schooling is probably better than none. If you're going to quit the books, I suppose it better be because you're doing something more important...\""

    jump wedding_end

if merchant:

    "\"How is business lately? They say the economy is expected to turn around soon enough, what do you think?\""
    "\"Do you source domestically, or from overseas? We need more jobs here. Of course, they should be available to anyone regardless of background...\""

    jump wedding_end

label schoolmates:

    "\"I see, from the academy?\""

    menu:

        "I beg your pardon?":

            jump schoolmate_truth

        "Academy? Yes...that's right.":

            jump schoolmate_lie

label schoolmate_truth:
    $ rory_artist = True

    "\"Beckford Academy, wasn't it? So terribly posh, I always give James a hard time about it but I'm one to talk. Don't tell anyone, but I attended Collins Prep for a moment! Hardly befitting of a starving artist, I know.\""
    "\"Speaking of which, do you agree that artists must suffer for their art? I don't think I would have sold half as many books if I had written about Heaven.\""
    "\"We spend our lives seeking happiness, aiming to eliminate pain and turmoil, but nobody wants to read a story without any drama in it. It'd be terribly dull.\""
    "\"You can't suffer too much though, or else you'll lose the means to create. Leave the suffering to your spirits, not your coffers. Need to keep the books selling.\""
    "\"But I really can't complain, because now I'm able to write what I want to write. Within reason, of course. Novels aren't the only kind of writing out there.\" He tips his glass toward me."
    "\"There's script on the bottle that held this whiskey, or...lighter fare, if you will. There's a place for those things but for me, there's nothing like writing words that are truly your own.\""


    jump wedding_end

label schoolmate_lie:
    $ rory_choices = True

    "\"That's wonderful that you've remained acquainted after all this time.\""
    "\"Some of my best mates were from my school days, I think. In a way, you never have friends like that again. Back when we didn't need to worry about medical bills and the rent and all that rubbish.\""
    "\"Gosh, I don't know if we all still keep in touch like you two. I guess we'll find out at my own wedding!\""

    "\"You know how James and Marian met, don't you? James just goes strolling out one day in the park to see the sunset and Marian just happens to be out there, on the same day doing the exact same thing. Like something out of a film.\""
    "\"To think--if one of neither of them had gone to the park that day, that we all wouldn't be here.\""
    "\"It's the age-old question of whether our lives are predetermined, or if our choices make us who we are? Hell if I know. Was I destined to be a writer?\""
    "\"Maybe I got lucky meeting James when I did. But it wouldn't have mattered if I hadn't picked up a pen and started writing to begin with. And I have to believe that my choices matter.\""

    jump wedding_end

label hometown:

    "\"Nice, so you're also from Earnsworth? I'm originally from Palace Gardens myself.\""

    menu:

        "No, from Atford.":

            jump hometown_truth

        "Yes. Earnsworth.":

            jump hometown_lie

label hometown_truth:
    $ rory_atford = True

    "Rory raises an eyebrow. \"Atford? If I recall correctly, James came up to Lintonbury from Earnsworth after finishing school.\""
    "\"Isn't Atford up in Commerce Valley? Now that I think of it, one of my friends was talking about buying a residence there, I've heard it's rather quaint. I didn't know James had lived in Atford prior. James Atford Pryor.\" Rory laughs at his own joke."
    "\'Did the Pryors move around much when he was a child? I imagine that could be difficult. But I'm sure James got along just fine.\""

    jump wedding_end

label hometown_lie:
    $ rory_travel = True

    "\"It seemed like James couldn't wait to leave, but it must not be so bad if you've stayed. There's something comforting about the familiarity of the place you grew up in.\""
    "\"I've lived in Palace Gardens all my life. Never ventured out much in my youth, I used to come to Hestia once in a while. Fancy lot out here, aren't they? Not too much has changed.\""
    "\"It's fascinating how even one town can be so different from the next, let alone a different country.\""

    "(is it the person or the location)"

    jump wedding_end

label wedding_end:

    "The evening passes by a little faster with Rory's company and an endless supply of libations. He introduces me to a number of other guests whose names I admittedly won't remember after tonight."
    "There are too many of them, and my faculties are inhibited by a combination of alcohol, nerves and the knowledge that we will never again cross paths."

    "When the clock strikes nine, I excuse myself and let Rory know that I must be going."

    "\"No, stay, stay,\" he insists but I catch Jimmy's eye and wave. He gets Marian's attention and they make their way over."

    "\"It was good to see you, but it's time for me to head back. I must get back to work first thing tomorrow morning,\" I tell them."

    "Rory claps me on the shoulder. \"You really should stick around. I'm sure James can put you up if you're too out of sorts to travel by the end of the night, I know I will be.\""

    "Jimmy smiles thinly, giving me a nod. \"Trip was all right? Thanks for coming out here today.\""

    "I smile back. \"Congratulations again. And it was nice to finally meet you, Marian.\""

    "Marian beams at me, giving my hand a friendly squeeze. \"It was lovely to meet you. I hope you'll come visit us sometime. Once somebody gets the renovations in order.\" She teasingly nudges her newly wed husband."

if rory_jimmy:

    "\"That's right, 'Jimmy,' get your bloody house in order for chrissake,\" Rory chides with a boisterous laugh. \"What's the use of owning a mansion if you can't even live in it?\""
    "Jimmy doesn't respond at first, and he glances at me briefly before smirking back at Rory. \"And when are you going to stop renting and finally settle down?\""
    "Rory gasps in mock-indignation. \"In exchange for my freedom? No thank you, very much. No offense, Marian!\""
    "\"Oh Rory, you're no gift yourself!\" Marian laughs. \"But to each their own.\""

    jump wedding_epilogue

if rory_business_card:

    "\"Oh right, before I forget. I'm not too far gone yet.\" Rory reaches into his inner vest pocket and hands me a card. \"Give me a ring if you're ever in town again. You have one for me?\""
    "I've never had a card of my own. A practice I've heard of, but never had to participate in before now."
    "I absently fold the corners in my hand. \"Unfortunately, not on my person at the moment.\""
    "\"Ah, that's all right. Today wasn't meant to be about business anyway. Tell you what--the next time you call on James, you'll both invite me along, yeah? We'll get up to no good.\""
    "\"Welcome to the club,\" Marian says to me a loud, conspiratorial whisper, rolling her eyes fondly."

    jump wedding_epilogue

if rory_artist:

    "Rory also takes my hand, shaking it fondly. \"I do hope we'll see each other again sometime. You've found a good one here, James. We both have a deep understanding of the arts.\""
    "\"Really?\" Jimmy gives a smile. \"I didn't know you were interested in the arts,\" he remarks evenly."
    "\"But it's not just about the art,\" Rory intones. \"It's deeper than that. Deeper than this glass.\" He takes another swig of his whiskey."
    "\"Rory, what are you babbling on about?\" Marian shakes her head, laughing. \"I have never found art to be more truly subjective than I do now.\""

    jump wedding_epilogue

if rory_choices:

    "\"Are you sure that you want to head out already?\" Rory asks. \"Choose wisely, your future could depend on this very moment!\""
    "\"It's true, I could be out of a job come tomorrow if I stay much longer,\" I joke in return. In jest, there is truth."
    "\"Fair enough. Then, here's to jobs that pay the rent.\" Rory raises his glass, then throws it back."
    "Marian gives me a sympathetic smile. \"Thanks again for celebrating with us.\""
    "(dialogue based on occupation)"
    # im working on this now

    jump wedding_epilogue

if rory_atford:

    "\"Back off to Atford, then?\" Rory says. \"Wishing you safe travels.\" Jimmy visibly starts at the mention of our hometown."
    "\"I didn't realize you had lived in Atford *prior*, James.\" Rory repeats his joke and I give an agreeable laugh, many of which I have offered this evening."
    "\"All prior to when I met this fair lass hither.\" Jimmy slides an arm around Marian's waist and she leans into his shoulder. \"Marian Pryor, I like the sound of that.\""
    "\"We'll see about that,\" Marian retorts playfully, looking up at him. \"I think I like James Fairbright better.\""
    "Jimmy gives a low chuckle. \"But it wouldn't do to reprint all of my books, would it?\""

    jump wedding_epilogue

if rory_travel:

    "travel stuff"

    jump wedding_epilogue

label wedding_epilogue:

    "With a final word of farewell, I take my leave and the sounds and lights of the festivities begin to fade away as I reach the front gate, where I climb into a waiting car."
    "Transportation has been arranged for the attendees, most of whom are staying at the nearby Fourth Street Hotel overnight."
    "I'll take the car to the hotel, and then head over to the train station by foot. I'll be able to rest during the few hours of the ride, and I'll be back home by early morning."

    "I haven't seen Rory since, but I wish him only the best and I wonder if he has yet heard of Jimmy's passing."

    scene library at truecenter
    with fade
    jump library_menu

label library_book_3:

    $ explored_library_book_3 = True

    "Book 3 is booky!"

    jump library_menu

label dining_room:

    scene dining room at truecenter

    "The dining room would have been host to innumerable parties, all gathered around a glass of champagne, or a late night espresso    "

label dining_room_menu:
    scene dining room at truecenter
    menu:

        "I take a seat..." if not explored_dining_room_dining_table_sit:

            jump dining_room_dining_table_sit

        "I examine the..." if not explored_dining_room_dining_room_dining_trappings:

            jump dining_room_dining_trappings

        "I move on":

            jump patio

label dining_room_dining_table_sit:

    $ explored_dining_room_dining_table_sit = True

    "I imagine Jimmy sitting at the head of the table..."

    jump dining_room_menu

label dining_room_dining_trappings:

    $ explored_dining_room_dining_room_dining_trappings = True

    "A set of silverware, quite literally made of silver."

if carpenter:

    "I always thought pure silver looked surprisingly dull in comparison to the cheaper imitations that many of us are accustomed to."
    "It also bends quite easily, not that I'm about to tamper with Jimmy's valuable spoons and forks."

    jump silverware_memory

if tutor:

    "It appears I have stumbled upon Jimmy's very own Mildenhall Treasure. No inscriptions to be found, but..."

    jump silverware_memory

if merchant:

    "This collection looks to be in fairly good condition, if only from lack of use rather than deliberate maintenance, and it plainly exceeds sterling grade."

    jump silverware_memory

label silverware_memory:

    scene dining room_memory at truecenter
    with ease

    "{i}Once I am rich, I shall acquire all of the silver spoons that money can buy.{/i}"

    "We were nearing the end of secondary school when Jimmy first told me that he wanted to be a writer."

if mood > 0:

    "he has achieved his goal"

    jump dining_room_menu

if mood < 1:

    "rich snob"

    jump dining_room_menu

label patio:

    scene patio at truecenter

    "The garden patio is spacious. The wood beneath my shoes is weathered by the sun."

if mood > 0:

    "What were you thinking as you sat out here, Jimmy?"

if mood < 1:

    "Jimmy, why am I even here for him?"

label patio_menu:

    menu:

        "I move on":

            jump kitchen

label kitchen:

    scene kitchen_1 at truecenter

    "The kitchen is the homiest part of this house."

label kitchen_menu:

    menu:

        "Look in cupboard" if not explored_kitchen_cupboard:

            jump kitchen_cupboard

        "Look out window" if not explored_kitchen_window:

            jump kitchen_window

        "The bar" if not explored_kitchen_bar:

            jump kitchen_bar

        "I move on":

            jump upstairs

label kitchen_cupboard:

    $ explored_kitchen_cupboard = True

    "It's full of glass and raisins"

    jump kitchen_menu

label kitchen_window:

    $ explored_kitchen_window = True

    "The window is windowy"

    jump kitchen_menu

label kitchen_bar:

    $ explored_kitchen_bar = True

    "James, James, James, always the entertainer."

    "When I open the bar, I see bottles of whiskey old enough to vote, angled champagnes labeled with dates when they needed to be turned, and finally some truly, utterly unpronounceable wines."

    "I know for a fact that James himself didn't drink. He never told me why, but I think he felt like he'd lose his edge if he wasn't always 100% there."

    "Of course, that didn't stop him from stocking the good stuff. I'm sure he wanted his guests completely at ease."

    menu:

        "A toast, to James":

            jump kitchen_bar_have_a_drink

        "I close the bar":

            jump kitchen_menu

label kitchen_bar_have_a_drink:

    $ likes_alcohol = True

    "I reach for an open bottle. Here's one, it's a scotch from somewhere called Kirkwall."

    "I pour myself a glass. Holding it to the light, I see it's the color of varnish."

    "\"James, my friend, thinking of you, thinking of us from beyond. Thank you.\""

    "{i}gulp{/i}"

    "What a lovely burn. I tell myself I'll wash the glass before I go, but not too soon, in case I feel the urge to give James another toast."

    jump kitchen_menu

label upstairs:

    scene hallway3 at truecenter

    "The upstairs is hallway-y"

label upstairs_menu:

    menu:

        "I move on":

            jump balcony

label balcony:

    "The air is fresh"

label balcony_menu:

    menu:

        "I move on":

            jump salon

label salon:

    scene salon at truecenter

    "The salon is full of sofas"

label salon_menu:

    menu:

        "I move on":

            jump gueuloir

label gueuloir:

    "The gueuloir is full of nothing"

label gueuloir_menu:

    menu:

        "I move on":

            jump conservatory

label conservatory:

    # NEEDS IMAGE?
    scene conservatory at truecenter

    "The conservatory is full of plants"

label conservatory_menu:

    menu:

        "I look in the drawer":

            jump pasiphae_play_intro

        "I move on":

            jump interlude

label pasiphae_play_intro:

  "In the drawer I find a book with neatly penned pages. This penmanship is neat, evenly spaced, and deliberately cursive. It seems this book may not have been meant for publishing. The lack of title, and author helps confirm my suspicions."

  menu:

    "This must be one of James' unpublished works":
      $ pasiphae_author = "James"
      jump pasiphae_play

    "This must have been written by someone other than James":
      jump pasiphae_play_author

label pasiphae_play_author:

  "But who else could it have been?"

  menu:

    "An esteemed guest must have left this here and forgotten about it":
      jump pasiphae_play_author_mystery

    "Someone must have spent a lot of time here writing it":
      jump pasiphae_play_author_marian

label pasiphae_play_author_mystery:
  $ pasiphae_author = "this unknown author"

  "The author of this book must have thought very little of his or her work to leave it here."

  "Probably some very drunk or very happy writer, dragged off to bed after too much champagne."

  jump pasiphae_play

label pasiphae_play_author_marian:
  $ pasiphae_author = "Marian"

  "The only other person who lived here was Marian. This must have been from her hand."

  jump pasiphae_play

label pasiphae_play:

if tutor:

  "I begin leafing through the pages, immediately recognizing the names of the characters:"

  "Pasiphaë, the Greek sorceress who was cursed by Poseidon into loving a bull. Her husband, Minos, and, of course, the chorus, our moral voice of reason."

  "This seems to be a retelling of her story."

  "But here, Poseidon is no godlike man, cursing thunderous madness from the sea."

  "As in life, he never appears. His curse is quiet, and we, the audience, are left watching Pasiphaë unravel, seemingly all by herself, within the humanity and intimacy of the stage."

  jump pasiphae_play_body

if merchant:

  "There is a play of some sort in the book. It sounds like some sort of Greek myth."

  "It isn't one that I immediately recognize, but I know a Greek name when I see it, all olives and the Aegean."

  "This woman, Pasiphaë seems to be pretty mad that her husband has a magic cow and she doesn't."

  "And I get it, there's a reason why 'his' and 'hers' lines sell so well. It seems like the ancient Greeks didn't quite experience the same slick equality like we have these days."

  "I knew they'd end up in trouble, and I was right."

  jump pasiphae_play_body

if carpenter:

  "In this book is a play."

  "I recognize the name Minos from a play in a town square about a labyrinth, years ago, but I don't recognize this specific story"

  "As I leaf through the pages, I learn that a woman named Pasiphaë is having a problem where she wants her husband's prize bull."

  "Ah, this must be some sort of prequel to the labyrinth story. I certainly don't remember {i}that{/i} ending well."

  jump pasiphae_play_body

label pasiphae_play_body:

  "{b}Minos{/b}: The sentries see you face the bull in the fields. You cannot hide it from them. They say there is a feverish look in your eyes."

  "{b}Pasiphaë{/b}: Are you sure it is right to trust a sentry's gossip? It is they who gawk at cows, not I."

  "{b}Minos{/b}: Gawk they may, but they are not you. Fever is the youth of madness, they say. So steadfastly you stare that even crows might land on you."

  "{b}Pasiphaë (fiery){/b}: Enough of these ridiculous accusations. Why are you doing this? Since when do you care what I want, or what I do? You never have before!"

  "{b}Minos (defensively){/b}: I don't understand, this isn't like you. I love and trust you, and want only the best. While the sentries may gossip below you, I speak to you as an equal."

  "{b}Pasiphaë{/b}: Such empty words! If you loved and trusted me you would do as you always have and leave me be! As you will and as you always have."

  "{b}Minos{/b}: Enough! Command you I will not, but neither will I move. Tell me the truth of this matter, for you god-born owe it to man."

  "{i}Pasiphaë walks in a circle, increasingly agitated. She busies herself with a dish, then a towel. Minos watches. When she sees he won't leave, she finally faces him.{/i}"

  "{b}Pasiphaë (calmly, but with wild eyes){/b}: Why would Poseidon choose you to bestow such a wondrous creature? Why not I? Daughter of Helios that I am, sorceress divine, do I not deserve the adoration of the sea?"

  "{b}Minos{/b}: You covet my bull? The mighty bull of Poseidon?"

  "{b}Pasiphaë{/b}: King you are, but queen am I, what great {i}blessings{/i} have been {i}showered{/i} upon you. What {i}great fortune{/i}. Never have I received anything I have not grasped with my own two hands."

  "{b}Chorus{/b}: A house quiet sits in balance with the gods. Fortunate are they who can remain content. But when that quiet is broken, that house is shaken forever."

  "{b}Minos{/b}: What fearsome jealousy! It twists the woman before me. So sudden it rises. How has this evil taken hold?"

  "{b}Pasiphaë{/b}: Sudden? Was it not I who cursed your seed to serpents? When a woman dresses her desires as lover's envy, her husband sees nothing. Yet when she wishes power, she is now jealous?"

  "{b}Chorus{/b}: Love is the lightless cave man walks down, blind to every stone in his path. Cut and bruised he can't see who assaults him, deeper in he goes, following only the promise of a soft-faced girl."

  "{b}Pasiphaë{/b}: Give me your bull, or I shall take it. You cannot keep a god's gift for yourself. It is I who have just as much right to it as you."

  "{b}Minos{/b}: I do not know you, I do not see. It is not one, but two wild creatures before me. Be you god, be you mortal, be you sorceress in between. Nothing of this is like the woman I wed. The one I wed is content with me."

  "{b}Pasiphaë{/b}: The one I wed, the one I see, slays the love within me."

if tutor:

  "Poseidon's curse here was insidious, it wasn't simply some bestial lust, it was an envy that grew and destroyed everything in its path."

  "Ultimately, Pasiphaë carries out a plan to lure the bull to her. As I expect, it goes terribly wrong."

  "She climbs into an ornately built wooden bull, made of mahogany, bedecked in jewels, and gambols and lolls with an actual bull on the stage."

  "The scene turns to horror, however, the real bull mounts the wooden bull."

  "Pasiphaë never acquires the bull, and its pursuit punishes her harshly. She holds up her bloodied child, the minotaur, her face contorting with joy, fear, and disgust as she dies."

  if pasiphae_author == "Marian":

    "I think about the implications of Marian having written this."

  jump pasiphae_author_menu

if merchant:

  "Ultimately, Pasiphaë carries out a plan to lure the bull to her, dressed as a bull."

  "Not the plan I'd have come up with, but I'm not the sorceress queen here, I suppose. Envy makes us do strange things."

  "The wooden bull she constructs is 'made of mahogany. Inlaid are sapphires around its neck, rubies on its hooves, a pearl on its forehead shaped like a crescent moon.'"

  "Kind of beautiful. Fairly impractical. Definitely out of budget for any theater that would play Greek plays, certainly."

  "Then of course was the trouble I'd seen from a mile away. The real bull... mounts the wooden cow."

  "The story ends in tragedy as she holds up her bloodied child, the minotaur, her face contorting with joy, fear, and disgust as she dies."

  "So what does this all mean?"

  if pasiphae_author == "Marian":

    "I think about the implications of Marian having written this."

  jump pasiphae_author_menu

if carpenter:

  "Ultimately, Pasiphaë carries out a plan to lure the bull to her, dressed as a bull."

  "The minotaur... the labyrinth... ah."

  "The wooden bull she constructs is 'made of mahogany. Inlaid are sapphires around its neck, rubies on its hooves, a pearl on its forehead shaped like a crescent moon.'"

  "Mahogany. Wow, what a heavy and expensive wood to be wheeling out onto the stage. Also not one that would have been available in Greece."

  "When Pasiphaë climbs in, the real bull... mounts the wooden cow."

  "The story ends in tragedy as she holds up her bloodied child, the minotaur, her face contorting with joy, fear, and disgust as she dies."

  "So what does this all mean?"

  if pasiphae_author == "Marian":

    "I think about the implications of Marian having written this."

  jump pasiphae_author_menu

label pasiphae_author_menu:

  menu:

    "This must be a fun and fanciful exercise of the mind":

      jump pasiphae_play_fun

    "This must be the product of a truly disturbed mind":

      jump pasiphae_play_mad

    "This must be something Marian had kept in secret" if pasiphae_author == "Marian":

      jump pasiphae_play_sympathy

label pasiphae_play_fun:

  "I imagine stagehands trying to wrestle a live bull onto a stage in a theater with a smirk."

  if pasiphae_author == "Marian":
    $ marian_play_fun = True

    "Literature was meant to explore ideas. I'm glad she had this outlet to express herself."

  else:
    "Literature was meant to explore ideas. I'm glad [pasiphae_author] was able to put this idea to paper."

  "Certainly, James is... was nothing like the characters in his books."

  "I put the book back in the drawer"

  jump conservatory_menu

label pasiphae_play_mad:

  "There is something deeply unsettling about rewriting an ancient play about bestiality."

  if pasiphae_author == "Marian":
    $ marian_play_crazy = True

    "What drew her to this story, and what made her want to express it in such graphic detail?"

    "Surely this is the work of someone who was truly unwell. I hope she got the help she needed."

  if pasiphae_author == "James":
    "James... some part of you must have been truly unwell. I can only hope that writing this helped bring you peace, or urged you to get the help you needed."

  else:
    "The author of this story must have been truly unwell. I can only hope that writing this helped bring them peace, or urged them to get the help they needed."

  "I put the book back in the drawer"

  jump conservatory_menu

label pasiphae_play_sympathy:

  $ marian_play_sympathy = True

  "It must have taken Marian a lot of courage to write something like this."

  "And to have to have hidden it in a such a place in their home, it's clear this was something she couldn't speak to James about."

  "Who was she? What spoke to her about this story, and how she told it? This human look at a woman with such a dark desire..."

  "Maybe writing this was some sort of exorcism."

  "I put the book back in the drawer"

  jump conservatory_menu

label interlude:

    "Ooo interlude"

    jump study

label study:

    scene study at truecenter

    "The study is study-y"

label study_menu:

    menu:

        "I move on":

            jump bedroom

label bedroom:

    scene bedroom at truecenter

    "The bedroom is bedroom-y"

label bedroom_menu:

    menu:

        "I move on":

            jump bathroom

label bathroom:

    "Bathroom"

    return

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
