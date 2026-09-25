#!/usr/bin/env python3
"""Rick&Linda(9/20)向け 東京フリーデーのコース選択ページ。 python3 build.py -> index.html"""
import json, html

# 写真は「ワクワク採点」で選ぶ。建物の外観でなく、そこで人が楽しんでいる絵を最優先。
# 採点と選定理由は photos.json の score / note を見る。
PH = json.load(open('photos.json'))
gm = lambda q: 'https://www.google.com/maps/search/?api=1&query=' + q.replace(' ', '+')
emb = lambda q: 'https://maps.google.com/maps?q=' + q.replace(' ', '+') + '&output=embed&z=12'
def route_emb(stops):
    s = [x.replace(' ', '+') for x in stops]
    return 'https://maps.google.com/maps?saddr=' + s[0] + '&daddr=' + '+to:'.join(s[1:]) + '&output=embed'
def route_link(stops):
    s = [x.replace(' ', '+') for x in stops]
    return ('https://www.google.com/maps/dir/?api=1&origin=' + s[0] + '&destination=' + s[-1]
            + ('&waypoints=' + '%7C'.join(s[1:-1]) if len(s) > 2 else '') + '&travelmode=transit')

DAY1 = [
 dict(id='A', fee='$250 · about five hours', chips=['Mostly sitting down','Ends a few minutes from your hotel','$250 · the day'], name='Asakusa, and the river home', tag='Old temple, river boat, garden',
  why='You will have been awake since a quarter past four and had lunch already in Hibiya. This course is built so that the moving after that is done sitting down: a temple in the morning district, then a boat that carries you back down the Sumida and drops you almost at your door. Nothing here needs booking and nothing here is far.',
  steps=[('13:15','After lunch in Hibiya','Lunch finishes a few minutes from the hotel. About 25 minutes by train from there to Asakusa. You can sleep on it.'),
         ('13:45','Senso-ji, Asakusa','Tokyo&rsquo;s oldest temple, founded in 628. You come in under a five-metre paper lantern, down a street of stalls selling rice crackers and fans that has been a shopping street for three hundred years. Flat the whole way, benches in the courtyard.'),
         ('15:00','Something sweet on Nakamise','Melon bread straight out of the oven, or a bag of hot senbei. We eat as we walk back to the pier.'),
         ('15:40','The boat down the Sumida','Forty minutes on the water. Twelve bridges, each one a different colour, the Skytree behind you and the city sliding past. You are sitting the whole way and there is a toilet on board.'),
         ('16:30','Hama-rikyu Gardens','The boat lands inside a 400-year-old shogun&rsquo;s garden with saltwater ponds. Flat gravel paths, benches all the way round, the skyline standing over the pines.'),
         ('17:15','Tea over the pond, if you want it','A tea house on stilts out over the water. Matcha whisked in front of you with a seasonal sweet. Entirely optional.'),
         ('18:00','Back at the hotel','Fifteen minutes on foot, or one short taxi.')],
  stops=['The Blossom Hibiya Tokyo','Sensoji Temple Asakusa','Asakusa Pier Tokyo Cruise','Hamarikyu Gardens','The Blossom Hibiya Tokyo'],
  moves='Hotel &rarr; Asakusa about 25 min by train. Temple on foot. Pier is 5 min from the temple. Boat to Hama-rikyu 40 min. Garden &rarr; hotel 15 min on foot.',
  food=[('Daikokuya Tempura','Asakusa &middot; tempura over rice','Frying the same dark sesame-oil tempura since 1887. Prawns over rice in a lacquer bowl. There is usually a queue and it moves.','Daikokuya Tempura Asakusa'),
        ('Asakusa Imahan','Asakusa &middot; sukiyaki','Beef cooked at your table in a shallow iron pan, dipped in raw egg. Founded 1895, and the room is quiet and seated.','Asakusa Imahan Kokusaidori'),
        ('Nakamise street stalls','Asakusa &middot; snacks as you walk','Melon bread, grilled rice crackers, sweet bean cakes shaped like the temple gate. A few hundred yen each, eaten standing.','Nakamise Dori Asakusa')],
  good='The most rest per hour of the three. Almost all of the distance is covered sitting on a boat or a train, and you finish within walking distance of your bed.',
  mind='The last boat of the day leaves in the late afternoon, so this course cannot start much later than 13:00. If the weather turns, the boat still runs &mdash; the deck is covered.',
  links=[('Senso-ji (official)','https://www.senso-ji.jp/english/'),('Tokyo Cruise water bus','https://www.suijobus.co.jp/en/'),('Hama-rikyu Gardens','https://www.tokyo-park.or.jp/teien/en/hama-rikyu/')]),
 dict(id='B', fee='$250 · about four hours', chips=['Indoors and cool','The least walking of the three','$250 · the day'], name='teamLab, and almost no walking', tag='Dark rooms, water, light',
  why='If the market has finished you off, this is the course that asks least of your legs. It is one building, indoors, dark and cool, and you are back at the hotel before dinner. It is also in Toyosu &mdash; the same direction you will already have travelled that morning, so nothing about the trains is new.',
  steps=[('13:30','After lunch in Hibiya','About 20 minutes by train to Toyosu, the same line you took at dawn.'),
         ('14:00','teamLab Planets, Toyosu','You take your shoes off at the door and walk through the work barefoot. One room is ankle-deep warm water with projected koi that scatter when you move; another is a mirrored hall of hanging lights; another is a floor of orchids overhead. It is about an hour and a half at a slow pace.'),
         ('15:45','Coffee and a sit down','There is a garden and a tea room in the same building.'),
         ('16:30','Toyosu Senkyaku Banrai','Ten minutes on foot. A wooden market-town building beside the fish market with food stalls on two floors and a rooftop footbath looking over the bay. Free, and you can sit with your feet in hot water and do nothing.'),
         ('17:30','Back at the hotel','About 20 minutes.')],
  stops=['The Blossom Hibiya Tokyo','teamLab Planets TOKYO','Toyosu Senkyaku Banrai','The Blossom Hibiya Tokyo'],
  moves='Hotel &rarr; Toyosu about 20 min. Everything after that is within ten minutes on foot. Toyosu &rarr; hotel about 20 min.',
  food=[('Toyosu Senkyaku Banrai stalls','Toyosu &middot; seafood bowls','Tuna, salmon roe and sea urchin over rice, from the market next door. Counter seats, around ¥2,000&ndash;4,000.','Toyosu Senkyaku Banrai'),
        ('Ramen at the market','Toyosu &middot; noodles','A bowl of pork-bone broth ramen in the same building. Cheap, hot, and about ten minutes to eat.','Toyosu Senkyaku Banrai ramen'),
        ('teamLab tea room','Inside the museum &middot; tea and ice cream','Matcha and soft serve, with a flower that opens in your cup as you drink. Sit-down, air-conditioned, right where you are.','teamLab Planets TOKYO')],
  good='Four hours, one building, almost no walking, and something you cannot see anywhere else in the world. The best answer if the 4:15 start has cost you more than you expected.',
  mind='Tickets are timed and sell out, so I book the slot as soon as you choose this. You walk barefoot and one room is shin-deep in water &mdash; wear something that rolls up, and skip it if either of you is unsteady on wet floors.',
  links=[('teamLab Planets TOKYO (official)','https://www.teamlab.art/e/planets/'),('Toyosu Senkyaku Banrai','https://toyosu-senkyakubanrai.jp/en/')]),
 dict(id='C', fee='$250 · about five hours', chips=['The most walking of the three','Classic Tokyo','$250 · the day'], name='Meiji shrine and the young side of Tokyo', tag='Forest shrine, Harajuku, Shibuya',
  why='The version for the two of you who wake up feeling fine. A forest shrine in the middle of the city, then the loudest teenage street in Japan ten minutes away, then the crossing everybody has seen on television. It is the most walking of the three courses and the most Tokyo.',
  steps=[('13:15','After lunch in Hibiya','About 20 minutes by train from Hibiya to Harajuku.'),
         ('13:45','Meiji Jingu','A wide gravel path through a forest of a hundred thousand trees, every one donated and planted by hand in 1920. Benches the whole way. On a weekday afternoon it is quiet enough to hear the gravel.'),
         ('14:45','Takeshita Street','Ten minutes and a complete change of world: three hundred metres of teenage fashion, crepe stands and rainbow cotton candy. We walk it once, which is enough.'),
         ('15:30','Omotesando','The wide tree-lined avenue below it, calmer, with the architecture worth looking up at. Coffee sitting down.'),
         ('16:45','Shibuya','The crossing from above first, through the window of the station building, then down into it. We stop the moment you have had enough.'),
         ('18:00','Back at the hotel','About 20 minutes by train.')],
  stops=['The Blossom Hibiya Tokyo','Meiji Jingu Shrine','Takeshita Street Harajuku','Omotesando Tokyo','Shibuya Scramble Crossing','The Blossom Hibiya Tokyo'],
  moves='Hotel &rarr; Harajuku about 20 min by train. Shrine walk 10 min each way. Shrine &rarr; Takeshita 10 min on foot. Takeshita &rarr; Omotesando 8 min. Omotesando &rarr; Shibuya 12 min on foot or 3 min by train. Shibuya &rarr; hotel about 20 min.',
  food=[('Marion Crepes','Harajuku &middot; crepes standing up','The stand that started the Harajuku crepe in 1976. Strawberry and cream in a paper cone, about ¥600, eaten on the street.','Marion Crepes Harajuku'),
        ('Afuri','Harajuku &middot; yuzu ramen','A clear chicken broth with citrus peel in it &mdash; lighter than most ramen and easier on a tired stomach. Counter and table seats, about ¥1,200.','AFURI Harajuku'),
        ('Shibuya izakaya','Shibuya &middot; small plates','If you last until early evening: grilled skewers, cold beer, everything ¥400&ndash;800 a plate. I order, you point.','Shibuya izakaya')],
  good='Covers the three images of Tokyo most people arrive with, and gets them done in one afternoon.',
  mind='This is roughly six thousand steps more than course A. After a 4:15 start, be honest with yourselves about whether you want it.',
  links=[('Meiji Jingu (official)','https://www.meijijingu.or.jp/en/'),('Shibuya Sky','https://www.shibuya-scramble-square.com/sky/en/')]),
]
DAY2 = [
 dict(id='D', fee='$250 · about four hours', chips=['Mostly indoors','Benches throughout, wheelchair loan free','$250 · the day'], name='Ueno, the museum and the pond', tag='National museum, kaiseki lunch, lotus pond',
  why='Tuesday is entirely your call on timing, so this course is written for a late-morning start with no auction behind it. One museum building, a sit-down lunch, and a pond to finish &mdash; indoors-heavy, with benches in nearly every room and a free wheelchair on loan at the entrance if you want one.',
  steps=[('10:00','Start from the hotel, whenever you like','About 25 minutes by train to Ueno. This time is yours to move.'),
         ('10:30','Tokyo National Museum, Honkan','Just the main building &mdash; the Honkan &mdash; not the whole museum complex, which would be a full day on its own. Japanese sculpture, swords and screens in order from ancient to Edo. Benches in most rooms, elevators between floors, and a wheelchair free to borrow at the entrance if you want to save your legs.'),
         ('12:15','Lunch at Innsyoutei, inside the park','A kaiseki restaurant since 1875, built like an old Japanese house with huge windows onto the trees. Tempura and vegetable-forward set lunches, seated, no rush.'),
         ('13:45','Shinobazu Pond','A lotus pond a few minutes&rsquo; walk from the restaurant, with a small island shrine and rowboats for hire. We just sit by the water; the boats are there if you want them.'),
         ('14:30','Back at the hotel','About 25 minutes by train.')],
  stops=['The Blossom Hibiya Tokyo','Tokyo National Museum','Shinobazu Pond Ueno','The Blossom Hibiya Tokyo'],
  moves='Hotel &rarr; Ueno about 25 min by train. Museum &rarr; Innsyoutei 5 min on foot inside the park. Restaurant &rarr; Shinobazu Pond about 10 min on foot. Ueno &rarr; hotel about 25 min.',
  food=[('Innsyoutei','Ueno Park &middot; kaiseki and tempura','A seated set lunch in a 150-year-old restaurant inside the park, big windows onto the trees. About ¥3,000&ndash;6,000 a head.','Innsyoutei Ueno Park'),
        ('Wagashi at the park','Ueno &middot; a sweet to go with tea','Small seasonal sweets shaped like the month, sold by the piece near the museum gates.','wagashi shop Ueno Park'),
        ('Matcha and something sweet','Ueno Park &middot; a sit-down break','A bench by the pond and a shaved-ice or matcha stand nearby if the afternoon is warm.','Shinobazu Pond cafe')],
  good='The least walking of the three Tuesday courses and the most seating. A good answer if Monday left you tired.',
  mind='The Honkan is open Tuesday to Sunday and closed Mondays, so this course only works on a day like this one. I will confirm the exact gallery layout closer to the date, since museums rotate what is on display.',
  links=[('Tokyo National Museum (official)','https://www.tnm.jp/?lang=en'),('Ueno Park (Go Tokyo)','https://www.gotokyo.org/en/spot/482/index.html')]),
 dict(id='E', fee='$250 · about four hours', chips=['The least walking of the six','Closest to your hotel','$250 · the day'], name='The East Gardens, and Marunouchi', tag='Edo castle grounds, brick Tokyo, coffee',
  why='This is the one that barely leaves the neighbourhood. The Imperial Palace East Gardens are a ten-minute walk from your hotel, free to enter, and closed only on Mondays and Fridays &mdash; Tuesday is a normal open day. After that, a coffee in a restored 1894 brick building and a stop at Tokyo Station on the way back, all still within about fifteen minutes of your door.',
  steps=[('10:00','Walk to the East Gardens','About 10 minutes on foot from the hotel to the Otemon gate.'),
         ('10:15','Otemon and the castle grounds','The main gate of Edo Castle, and inside it the grounds where the shogun&rsquo;s government once stood &mdash; now lawns, stone walls and a guardhouse. Flat paths throughout.'),
         ('11:00','The keep foundation','The stone base of what was once Japan&rsquo;s tallest castle keep, burned down in 1657 and never rebuilt. You can climb onto the top of it &mdash; a short flight of stone steps &mdash; for a view over the whole garden and a bench to rest on.'),
         ('11:45','Coffee, Marunouchi','A 10&ndash;15 minute walk to Café 1894, inside the Mitsubishi Ichigokan Museum &mdash; a restored 1894 red-brick bank building with a two-storey glass-roofed hall.'),
         ('13:00','Tokyo Station, Ichibangai','A short walk to the underground arcade beneath the station &mdash; a food hall and souvenir street if you want to pick up gifts before you leave the area.'),
         ('13:45','Back at the hotel','About 15 minutes on foot, or a short taxi.')],
  stops=['The Blossom Hibiya Tokyo','Otemon Imperial Palace East Gardens','Mitsubishi Ichigokan Museum','Tokyo Station Ichibangai','The Blossom Hibiya Tokyo'],
  moves='Hotel &rarr; Otemon about 10 min on foot. Garden &rarr; Café 1894 about 10&ndash;15 min on foot. Café &rarr; Tokyo Station about 5 min on foot. Station &rarr; hotel about 15 min on foot or a short taxi.',
  food=[('Café 1894','Marunouchi &middot; coffee in a restored bank hall','Lunch 11:00&ndash;14:30, café menu 14:30&ndash;17:00. Coffee, sandwiches and cake under a two-storey glass roof.','Cafe 1894 Marunouchi'),
        ('Tokyo Station Ichibangai','Underground &middot; a food hall and souvenirs','Sweets, bento and regional snacks from all over Japan in one arcade, easy to carry back to the hotel.','Tokyo Station Ichibangai'),
        ('A bench in Ninomaru Garden','East Gardens &middot; a quiet rest','If you brought anything to eat, this is the spot &mdash; a pond garden with benches, a few minutes from Otemon.','Ninomaru Garden Imperial Palace')],
  good='The shortest distance from your hotel of any course on either day, and free to enter. Good if you would rather keep the day small.',
  mind='Closed Mondays and Fridays &mdash; Tuesday the 6th is a normal open day, and it is not a national holiday, so no schedule shift applies. Entry is free and needs no booking.',
  links=[('Imperial Palace East Gardens (Imperial Household Agency)','https://www.kunaicho.go.jp/en/visit/event/higashigyoen/'),('Mitsubishi Ichigokan Museum (official)','https://mimt.jp/english/')]),
 dict(id='F', fee='$250 · about five and a half hours', chips=['Cooking and shopping','Something to take home','$250 · the day'], name='Kappabashi, and Ginza for gifts', tag='Kitchen street, food samples, Ginza shopping',
  why="For the two of you who like a kitchen and a gift shop more than a shrine. Kappabashi is Tokyo's restaurant-supply street &mdash; knives, tableware, and the shops that make the plastic food models you have seen in every restaurant window. Then a soba lunch, and a taxi to Ginza for stationery, a department-store food hall, and whatever else catches your eye, ending a short ride from your hotel.",
  steps=[('10:00','Start from the hotel','About 20 minutes by train or taxi to Kappabashi, in Asakusa.'),
         ('10:30','Kappabashi Kitchen Street','A few hundred metres of restaurant-supply shops: knives that can be engraved with your name while you wait, lacquerware, and the original workshops behind Japan&rsquo;s plastic food displays. Most shops are open Tuesdays &mdash; it is Sundays that are quiet here.'),
         ('11:15','Make your own food sample','At Ganso Shokuhin Sample-ya, the shop that popularised the craft in 1932. A booked 40-minute session making a piece of wax or plastic tempura or lettuce, which you keep. I book the slot in advance.'),
         ('12:15','Lunch, Namiki Yabusoba','A soba restaurant near Kaminarimon since 1913, a few minutes&rsquo; walk from Kappabashi. Seated, quick, and open Tuesdays.'),
         ('13:30','Taxi to Ginza','About 25 minutes by taxi across the city.'),
         ('14:00','Ginza','Itoya&rsquo;s twelve floors of stationery, the food hall in the basement of Mitsukoshi, and Akomeya for rice, tea and packaged gifts &mdash; as much or as little of it as you want.'),
         ('16:00','Back at the hotel','Ginza is next to Hibiya &mdash; a short walk, or a five-minute taxi.')],
  stops=['The Blossom Hibiya Tokyo','Kappabashi Dougu Street','Namiki Yabusoba Asakusa','Ginza Itoya','The Blossom Hibiya Tokyo'],
  moves='Hotel &rarr; Kappabashi about 20 min. On foot around Kappabashi. Kappabashi &rarr; Ginza about 25 min by taxi. On foot around Ginza. Ginza &rarr; hotel about 10 min on foot or a short taxi.',
  food=[('Namiki Yabusoba','Asakusa &middot; soba','Buckwheat noodles in a dark dashi broth, served cold with a dipping sauce or hot. Seated, since 1913, about ¥1,000&ndash;2,000.','Namiki Yabusoba Asakusa'),
        ('Your own food sample','Ganso Shokuhin Sample-ya &middot; made by you','A wax or plastic tempura piece or lettuce leaf you make yourself in the 40-minute workshop &mdash; not edible, but yours to keep. About ¥3,300 per person.','Ganso Shokuhin Sample-ya'),
        ('Mitsukoshi Ginza depachika','Ginza &middot; the basement food hall','Wagashi, tea, pickles and bento from all over Japan, boxed to travel &mdash; the easiest place in Tokyo to buy food gifts.','Mitsukoshi Ginza depachika')],
  good='The only course with something you make yourself and something you can wrap up and take home. Good for a day built around gifts.',
  mind='Kappabashi shops mostly close Sundays, not Tuesdays, so the 6th is a normal day there. The food-sample workshop needs a reservation &mdash; I book it as soon as you choose this course, and will confirm the exact Tuesday time slot when I do.',
  links=[('Kappabashi Dougu Street (official)','https://www.kappabashi.or.jp/en/'),('Ganso Shokuhin Sample-ya (official)','https://www.ganso-sample.com/en/'),('Ginza (official)','https://www.ginza.jp/en')]),
]

COURSES = DAY1 + DAY2

# 10/5の昼。Rick 9/25「寿司でいいが25貫よりずっと少なく」→ ユウキ「隠れ家的で予約できればジャンル不問」。
# 営業・価格は 2026-09-25 に各公式ページで確認（ろくさん亭は9/11開業で品目未確定）。焼貝あこやは平日昼営業なしで除外。
LUNCH = [
 dict(n=1, name='Sushi Nakata', where='Imperial Hotel, lower level &middot; sushi', walk='About 5 min on foot',
  img='https://www.imperialhotel.co.jp/sites/default/files/styles/webp/public/img/2024-01/a402f1be1674ae1ab79e21236f28a5b5.webp?itok=gOktgMD2',
  alt='Tuna nigiri at Sushi Nakata',
  body='The same kind of lunch as the 20th, at about a third of the size. A quiet counter in the basement of the Imperial Hotel, with private rooms if you would rather have a table to yourselves.',
  size='Smallest set: 7 pieces of nigiri, a small starter, omelet and soup. ¥4,600. There is an 8-piece set at ¥6,500 if you want a little more.',
  hours='Monday lunch 11:30&ndash;15:00. Closed Sundays only.', book='Phone booking. I call and book it.',
  q='Sushi Nakata Imperial Hotel Tokyo', link=('Official menu','https://www.imperialhotel.co.jp/en/tokyo/restaurant/nakata/menu')),
 dict(n=2, name='Sobamae Isshin', where='Hibiya OKUROJI &middot; soba', walk='About 3 min on foot',
  img='https://www.jrtk.jp/hibiya-okuroji/shop/obj/img/000/070/241211-1546_01n.jpg',
  alt='Cold soba on a lacquered tray at Isshin',
  body='Buckwheat noodles made from 100% buckwheat flour, in the same brick arches under the train line as the 20th. You eat in separate private rooms, so it is the quietest of the five, and it is also the lightest meal.',
  size='You order one bowl or tray, from plain cold soba (¥900) up to duck soba or prawn tempura soba (¥1,500&ndash;2,000). Nothing else arrives unless you ask for it.',
  hours='Lunch 11:30&ndash;14:30, every day.', book='Booking by phone or online. I book the room.',
  q='Sobamae Isshin Hibiya OKUROJI', link=('Hibiya OKUROJI page','https://www.jrtk.jp/hibiya-okuroji/shop/detail_00070/')),
 dict(n=3, name='Hibiya Rokusantei', where='Tokyo Midtown Hibiya, 3rd floor &middot; soba and seasonal Japanese', walk='About 10 min on foot',
  img='https://www.hibiya.tokyo-midtown.com/jp/restaurants/upload/31000_main_1-2.jpg',
  alt='A seasonal Japanese plate at Rokusantei',
  body='A new restaurant, opened on September 11 by the team of Rokusaburo Michiba, one of the original Iron Chefs. 25 seats, two private rooms, and an English menu. Soba is the main dish, with small seasonal plates around it.',
  size='Lunch from ¥1,980 for a soba set, up to ¥5,500 for a short course. You choose how far up the menu to go.',
  hours='Monday lunch 11:00&ndash;15:00. Closed Wednesdays.', book='Booking by phone. I book it.',
  q='Hibiya Rokusantei Tokyo Midtown Hibiya', link=('Midtown Hibiya page','https://www.hibiya.tokyo-midtown.com/jp/restaurants/31000/')),
 dict(n=4, name='Sumiyaki Unafuji', where='Hibiya OKUROJI &middot; charcoal-grilled eel', walk='About 3 min on foot',
  img='https://www.jrtk.jp/hibiya-okuroji/shop/obj/img/000/055/221122-1331_01n.jpg',
  alt='Hitsumabushi, grilled eel over rice, at Unafuji',
  body='An eel restaurant from Nagoya, listed in the Michelin Bib Gourmand, in the same arches. It is calmer than the rest of the arches, with four semi-private rooms. Hitsumabushi is the dish: grilled eel over rice that you eat three ways, the last one with broth poured over.',
  size='Smallest: a bowl with 5/6 of an eel, clam soup and pickles, about ¥5,900. A half-size eel set with small side dishes is about ¥7,300.',
  hours='Open 11:00&ndash;22:00 without a break.', book='Booking online or by phone. I book it.',
  q='Sumiyaki Unafuji Hibiya OKUROJI', link=('Menu in English (PDF)','https://sumiyaki-unafuji.com/wp-content/uploads/2025/09/menu_global-2.pdf')),
 dict(n=5, name='Nanzenji Hyotei', where='Tokyo Midtown Hibiya, 3rd floor &middot; Kyoto kaiseki', walk='About 10 min on foot',
  img='https://www.hibiya.tokyo-midtown.com/jp/restaurants/upload/b_10_main1.png',
  alt='A lacquered plate of seasonal dishes at Hyotei',
  body='The Tokyo branch of a Kyoto restaurant that has been serving travellers by the Nanzenji temple for about 400 years. 24 seats and a private room. The most formal and the most expensive of the five.',
  size='In October the lighter lunch is sea bream over rice with hot tea poured on, at ¥10,890. The full kaiseki is ¥14,520. Both prices include tax and service.',
  hours='Monday lunch 12:00&ndash;15:00, last order 13:30. Closed Wednesdays and the 1st and 3rd Tuesday.', book='Booking required. I book it.',
  q='Nanzenji Hyotei Tokyo Midtown Hibiya', link=('Official site','http://hyotei.co.jp/tokyo/')),
]
def lunch_card(c):
    return f'''<article class="lcard"><img src="{c['img']}" alt="{html.escape(c['alt'])}" loading="lazy">
<div class="eb"><em>{c['n']} &middot; {c['where']}</em><strong>{c['name']}</strong><span>{c['body']}</span>
<p class="lsize">{c['size']}</p>
<p class="lmeta">{c['walk']}. {c['hours']} {c['book']}</p>
<p class="llinks"><a href="{gm(c['q'])}" target="_blank" rel="noopener">Map</a> <a href="{c['link'][1]}" target="_blank" rel="noopener">{c['link'][0]}</a></p></div></article>'''

def menu(c):
    x = PH[c['id']]['card']
    ch = ''.join(f'<li>{html.escape(t)}</li>' for t in c['chips'])
    return f'''<button class="mcard" type="button" data-course="{c['id']}" aria-expanded="false" aria-controls="detail-{c['id']}">
<img src="{x["thumb"]}" alt="{html.escape(x["title"])}" loading="lazy">
<span class="mb"><span class="mk">Course {c['id']}</span><span class="mt">{html.escape(c['name'])}</span>
<span class="mtag">{html.escape(c['tag'])}</span><ul class="mch">{ch}</ul><span class="mopen">See the plan</span></span></button>'''

def detail(c):
    ph = ''.join(f'<img src="{x["thumb"]}" alt="{html.escape(x["title"])}" loading="lazy">' for x in PH[c['id']]['detail'])
    st = ''.join(f'<li><b>{t}</b><div><strong>{h}</strong><span>{d}</span></div></li>' for t, h, d in c['steps'])
    fd = ''.join(f'<a class="eat" href="{gm(q)}" target="_blank" rel="noopener">'
                 f'<img src="{im["thumb"]}" alt="{html.escape(im["title"])}" loading="lazy">'
                 f'<span class="eb"><strong>{n}</strong><em>{a}</em><span>{d}</span>'
                 f'<i>Open in Google Maps ↗</i></span></a>'
                 for (n, a, d, q), im in zip(c['food'], PH[c['id']]['food']))
    ln = ' '.join(f'<a href="{u}" target="_blank" rel="noopener">{html.escape(t)} ↗</a>' for t, u in c['links'])
    day_label = 'Oct 5 afternoon' if c in DAY1 else 'Oct 6'
    sub = f'{day_label}: we choose course {c["id"]} ({c["name"]})'
    return f'''<section class="detail" id="detail-{c['id']}" hidden><div class="dwrap"><div class="dtop"></div>
<div class="dhead"><div><p class="kicker">Course {c['id']} · {html.escape(c['tag'])} · {c['fee']}</p><h2>{html.escape(c['name'])}</h2></div>
<button class="dclose" type="button" aria-label="Close">Close ✕</button></div>
<p class="why">{c['why']}</p>
<p class="moves"><b>Guide fee {c['fee']}.</b> Entry tickets, trains, taxis and meals are settled on the day as they come.</p>
<div class="photos">{ph}</div>
<div class="dgrid">
<div><h3>The day</h3><ol class="steps">{st}</ol></div>
<div><h3>The route</h3><div class="mapbox"><iframe src="{route_emb(c['stops'])}" loading="lazy" title="Route for course {c['id']}" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
<p class="moves">{c['moves']} <a href="{route_link(c['stops'])}" target="_blank" rel="noopener">Open the route in Google Maps ↗</a></p></div>
</div>
<h3>Where we eat</h3><div class="eats">{fd}</div>
<div class="notes"><p><b>Good for</b> {c['good']}</p><p><b>Keep in mind</b> {c['mind']}</p></div>
<p class="links">{ln}</p>
<a class="choose" href="mailto:icchan417@gmail.com?subject={html.escape(sub)}">Choose course {c['id']}</a>
</div></section>'''

HERO_CSS = """
.hpic{position:relative;background:#111;color:#fff}
.slides{position:absolute;inset:0;overflow:hidden}
.slides img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:scale(1.06);transition:opacity 1.1s ease,transform 5s linear}
.slides img.on{opacity:1;transform:scale(1)}
.slides:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.08) 30%,rgba(0,0,0,.74))}
.hcap{position:relative;z-index:1;min-height:62vh;max-height:600px;display:flex;flex-direction:column;justify-content:flex-end;padding-top:48px;padding-bottom:22px}
.hcap .kicker{color:#9ee3b8}
.hcap h1{color:#fff;margin:0 0 14px;text-shadow:0 2px 14px rgba(0,0,0,.3)}
.snav{display:flex;align-items:center;gap:10px}
.slabel{font:inherit;font-size:12.5px;font-weight:600;color:#fff;background:rgba(0,0,0,.38);border:1px solid rgba(255,255,255,.4);border-radius:999px;padding:7px 13px;cursor:pointer;backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);max-width:100%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.dots{display:flex;gap:7px;margin-left:auto;flex:none}
.dots button{width:9px;height:9px;padding:0;border:none;border-radius:50%;background:rgba(255,255,255,.45);cursor:pointer}
.dots button.on{background:#fff}
.hbody{padding-top:22px;padding-bottom:26px}
@media(prefers-reduced-motion:reduce){.slides img{transition:none;transform:none}}
"""
HERO_JS = """
 (function(){
  var sl=[].slice.call(document.querySelectorAll('.slides img')),dots=[].slice.call(document.querySelectorAll('.dots button')),lab=document.querySelector('.slabel'),i=0,t;
  function show(n){i=n;sl.forEach(function(x,k){x.classList.toggle('on',k===n)});dots.forEach(function(x,k){x.classList.toggle('on',k===n)});
   lab.textContent='Course '+sl[n].dataset.course+' · '+sl[n].dataset.name;lab.dataset.course=sl[n].dataset.course}
  function go(){clearInterval(t);if(!matchMedia('(prefers-reduced-motion: reduce)').matches)t=setInterval(function(){show((i+1)%sl.length)},4000)}
  dots.forEach(function(d,k){d.addEventListener('click',function(){show(k);go()})});
  lab.addEventListener('click',function(){document.querySelector('.mcard[data-course="'+lab.dataset.course+'"]').click()});
  show(0);go();
 })();
"""

credits = '; '.join(html.escape(x['title'].replace('File:','')) + ' (' + x['lic'] + ')' for v in PH.values() for x in [v['card']] + v['detail'] + v['food'])
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tokyo: October 5 and 6</title><meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{{--bg:#fffdf6;--card:#fff;--ink:#111;--mute:#767065;--line:#eae4d6;--acc:#1a5c3a;--r:10px}}
*{{box-sizing:border-box;min-width:0}} html,body{{overflow-x:hidden;max-width:100%}} img{{max-width:100%}}
body{{margin:0;font-family:Inter,-apple-system,"Hiragino Sans",sans-serif;color:var(--ink);background:var(--bg);line-height:1.6}}
.wrap{{max-width:1080px;margin:0 auto;padding:0 20px}}
.kicker{{font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--acc);margin:0 0 10px}}
h1,h2,.mt{{text-wrap:balance}} .nb{{white-space:nowrap}}
h1{{font-weight:800;font-size:clamp(34px,5.4vw,54px);line-height:1.06;letter-spacing:-.025em;margin:0 0 16px}}
h2{{font-weight:800;font-size:clamp(30px,4.2vw,42px);line-height:1.06;letter-spacing:-.025em;margin:0}}
h3{{font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--acc);margin:0 0 12px}}
{HERO_CSS}
header p{{font-size:18px;color:var(--mute);margin:0;max-width:620px}}
.facts{{display:flex;flex-wrap:wrap;gap:6px 20px;margin:20px 0 0;padding:0;list-style:none;font-size:14px;color:var(--mute)}} .facts b{{color:var(--ink);font-weight:600}}
.sechead{{display:flex;align-items:baseline;gap:14px;padding:26px 0 16px;border-top:1px solid var(--line)}}
.sechead .n{{font-weight:800;font-size:26px;line-height:1;letter-spacing:-.02em;color:var(--acc)}}
.sechead b{{font-size:19px;font-weight:600}} .sechead span{{font-size:14px;color:var(--mute)}}
.menu{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}}
.mcard{{display:flex;flex-direction:column;text-align:left;font:inherit;color:inherit;background:var(--card);border:1px solid var(--line);border-radius:var(--r);overflow:hidden;padding:0;cursor:pointer;transition:transform .18s,box-shadow .18s,border-color .18s}}
.mcard:hover{{transform:translateY(-3px);box-shadow:0 10px 24px rgba(34,31,27,.10)}}
.menu.picked .mcard:not([aria-expanded=true]){{opacity:.42;filter:saturate(.45)}}
.menu.picked .mcard:not([aria-expanded=true]):hover{{opacity:.75;filter:none}}
.mcard[aria-expanded=true]{{border:2px solid var(--ink);box-shadow:0 12px 28px rgba(17,17,17,.16);transform:translateY(-3px)}}
.mcard[aria-expanded=true] .mopen{{color:var(--acc);border-bottom-color:var(--acc)}}
.mcard>img{{display:block;width:100%;aspect-ratio:4/3;object-fit:cover;background:#f0ebe0}}
.mb{{display:flex;flex-direction:column;flex:1;padding:18px 20px 20px}}
.mk{{display:block;font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--acc);margin-bottom:6px}}
.mt{{display:block;font-weight:800;font-size:26px;line-height:1.12;letter-spacing:-.025em;margin-bottom:6px}}
.mtag{{display:block;font-size:15px;color:var(--mute);margin-bottom:12px}}
.mch{{list-style:none;margin:auto 0 14px;padding:0;display:flex;flex-wrap:wrap;gap:6px}}
.mch li{{font-size:11px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;border:1px solid var(--line);border-radius:4px;padding:3px 8px;color:var(--mute)}}
.mopen{{align-self:flex-start;display:inline-block;font-size:14px;font-weight:600;border-bottom:2px solid var(--acc);padding-bottom:1px}}
.mcard[aria-expanded=true] .mopen::after{{content:" ▲"}} .mcard[aria-expanded=false] .mopen::after{{content:" ▾"}}
.detail{{scroll-margin-top:12px;display:grid;grid-template-rows:0fr;transition:grid-template-rows .32s ease;margin-top:14px;position:relative}}
.detail[hidden]{{display:none}} .detail.open{{grid-template-rows:1fr}}
.dwrap{{overflow:hidden;min-height:0;background:var(--card);border:2px solid var(--ink);border-radius:var(--r);position:relative}}
.detail::before{{content:'';position:absolute;top:-11px;left:var(--arrow,50%);width:20px;height:20px;margin-left:-10px;background:var(--acc);border-left:2px solid var(--acc);border-top:2px solid var(--acc);transform:rotate(45deg);z-index:2;opacity:0;transition:opacity .2s .12s}}
.detail.open::before{{opacity:1}}
.dtop{{height:5px;background:var(--acc)}}
.detail.open .dwrap{{overflow:visible}}
.dwrap>*{{margin-left:26px;margin-right:26px}} .dwrap>.dtop{{margin:0}} .dwrap>.photos{{margin-left:26px;margin-right:26px}}
.dhead{{display:flex;justify-content:space-between;align-items:flex-start;gap:16px;padding-top:26px}}
.dclose{{flex:none;font:inherit;font-size:12px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:var(--mute);background:none;border:1px solid var(--line);border-radius:6px;padding:8px 14px;cursor:pointer}}
.dclose:hover{{color:var(--ink);border-color:var(--ink)}}
.why{{font-size:17px;color:var(--mute);margin:10px 0 20px;max-width:640px}}
.photos{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-bottom:26px}}
.photos img{{display:block;width:100%;aspect-ratio:16/10;object-fit:cover;border-radius:8px;background:#f0ebe0}}
.dgrid{{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-bottom:28px}}
.steps{{list-style:none;padding:0;margin:0;border-top:1px solid var(--line)}}
.steps li{{display:grid;grid-template-columns:60px minmax(0,1fr);gap:12px;padding:11px 0;border-bottom:1px solid var(--line)}}
.steps b{{font-variant-numeric:tabular-nums;color:var(--acc);font-weight:600;font-size:14px}} .steps strong{{display:block;font-weight:600;font-size:16px}} .steps span{{color:var(--mute);font-size:14px}}
.mapbox{{border-radius:8px;overflow:hidden;background:#f0ebe0}} .mapbox iframe{{display:block;width:100%;height:300px;border:0}}
.moves{{font-size:14px;color:var(--mute);margin:12px 0 0}} .moves a{{color:var(--ink);text-decoration:underline;text-underline-offset:3px;white-space:nowrap}}
.eats{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-bottom:26px}}
.eat{{display:flex;flex-direction:column;text-decoration:none;color:inherit;background:var(--bg);border:1px solid var(--line);border-radius:8px;overflow:hidden}}
.eat>img{{display:block;width:100%;aspect-ratio:3/2;object-fit:cover;background:#f0ebe0}}
.eb{{display:flex;flex-direction:column;flex:1;padding:14px 16px 16px}}
.eat:hover{{border-color:var(--ink)}}
.eat strong{{display:block;font-weight:700;font-size:18px;line-height:1.2;letter-spacing:-.015em}}
.eat em{{display:block;font-style:normal;font-size:11px;color:var(--acc);font-weight:600;letter-spacing:.08em;text-transform:uppercase;margin:5px 0 9px}}
.eb>span{{display:block;font-size:14px;color:var(--mute)}} .eat i{{display:block;font-style:normal;font-size:12px;margin-top:auto;padding-top:10px;text-decoration:underline;text-underline-offset:3px}}
.notes{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:20px;font-size:14px}} .notes p{{margin:0;padding:16px 18px;background:var(--bg);border:1px solid var(--line);border-radius:8px}} .notes b{{display:block;font-weight:600;margin-bottom:3px}}
.links{{margin:0 0 22px;font-size:14px;display:flex;flex-wrap:wrap;gap:6px 18px}} .links a{{color:var(--ink);text-decoration:underline;text-underline-offset:3px}}
.choose{{display:inline-block;background:var(--ink);color:#fff;text-decoration:none;font-weight:700;padding:16px 32px;border-radius:8px;font-size:16px;letter-spacing:-.01em;margin-bottom:28px}} .choose:hover{{background:#333}}
.lunch{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;padding-bottom:34px}}
.lcard{{display:flex;flex-direction:column;background:var(--card);border:1px solid var(--line);border-radius:var(--r);overflow:hidden}}
.lcard>img{{display:block;width:100%;aspect-ratio:3/2;object-fit:cover;background:#f0ebe0}}
.lcard strong{{display:block;font-weight:800;font-size:22px;line-height:1.15;letter-spacing:-.02em;margin-bottom:8px}}
.lcard em{{display:block;font-style:normal;font-size:11px;color:var(--acc);font-weight:600;letter-spacing:.08em;text-transform:uppercase;margin:0 0 6px}}
.lcard .eb>span{{font-size:14.5px;color:var(--mute)}}
.lsize{{margin:12px 0 0;padding:10px 12px;background:var(--bg);border-left:3px solid var(--acc);border-radius:4px;font-size:14px}}
.lmeta{{margin:10px 0 0;font-size:13px;color:var(--mute)}}
.llinks{{margin:auto 0 0;padding-top:12px;display:flex;flex-wrap:wrap;gap:4px 16px;font-size:13px}} .llinks a{{color:var(--ink);text-decoration:underline;text-underline-offset:3px}}
.lnote{{font-size:14px;color:var(--mute);margin:-4px 0 16px;max-width:720px}}
.arrival{{display:grid;grid-template-columns:1fr 1fr;gap:26px;align-items:start;padding-bottom:40px}}
.arrival p{{margin:0 0 10px;font-size:16px}} .arrival .hint{{color:var(--mute);font-size:15px}}
.arrival .mapbox iframe{{height:260px}}
footer.wrap{{padding:26px 20px 60px;font-size:13px;color:var(--mute);border-top:1px solid var(--line)}} footer p{{margin:0 0 6px}}
.cred summary{{cursor:pointer;font-size:12px;color:var(--mute);opacity:.75;list-style:none;display:inline-block;text-decoration:underline;text-underline-offset:3px}}
.cred summary::-webkit-details-marker{{display:none}} .cred p{{margin:8px 0 0;font-size:11.5px;line-height:1.6;opacity:.8}}
@media(max-width:820px){{
 .menu,.lunch{{grid-template-columns:1fr}} .mcard>img{{aspect-ratio:16/9}}
 .dgrid,.eats,.notes,.arrival,.photos{{grid-template-columns:1fr}}
 .dwrap>*{{margin-left:18px;margin-right:18px}} .mapbox iframe{{height:230px}}
}}
@media(max-width:560px){{
 .wrap{{padding:0 18px}}
 .hcap{{min-height:58vh;padding-bottom:18px}} .hbody{{padding-top:18px;padding-bottom:22px}} .kicker{{margin-bottom:12px}}
 h1{{font-size:33px;line-height:1.08;letter-spacing:-.03em;margin-bottom:14px}}
 header p{{font-size:16px;line-height:1.55;max-width:none}}
 .facts{{display:grid;grid-template-columns:auto 1fr;gap:3px 10px;margin-top:16px;font-size:13px;line-height:1.5}}
 .facts li{{display:contents}} .facts b{{white-space:nowrap}}
 .sechead{{display:block;padding:22px 0 12px}}
 .sechead .n{{font-size:20px;margin-right:8px;display:inline}}
 .sechead b{{font-size:17px}} .sechead span{{display:block;font-size:13px;line-height:1.5;margin-top:2px}}
 .menu{{gap:12px}}
 .mb{{padding:15px 16px 16px}} .mt{{font-size:23px;line-height:1.15}} .mtag{{font-size:14px;margin-bottom:10px}}
 .mch{{gap:5px;margin-bottom:12px}} .mch li{{font-size:10.5px;padding:2px 7px}}
 .mopen{{font-size:13.5px}}
 h2{{font-size:26px;line-height:1.12}}
 .dhead{{padding-top:20px}} .why{{font-size:15.5px;line-height:1.55;margin:8px 0 16px}}
 .dwrap>*{{margin-left:16px;margin-right:16px}}
 .photos{{gap:8px;margin-bottom:20px}} .photos img{{aspect-ratio:3/2}}
 h3{{margin:22px 0 10px}} .dgrid{{gap:0;margin-bottom:0}}
 .steps li{{grid-template-columns:52px minmax(0,1fr);gap:10px;padding:10px 0}}
 .steps strong{{font-size:15.5px}} .steps span{{font-size:13.5px;line-height:1.5}}
 .eats{{gap:10px;margin-bottom:20px}} .eat>img{{aspect-ratio:16/9}} .eb{{padding:12px 14px 14px}}
 .notes{{gap:10px;margin-bottom:16px}} .notes p{{padding:14px 16px;font-size:13.5px}}
 .links{{font-size:13.5px;gap:4px 14px;margin-bottom:18px}}
 .choose{{display:block;text-align:center;padding:15px 0;margin-bottom:22px}}
 .arrival{{gap:16px;padding-bottom:32px}} .arrival p{{font-size:15.5px;line-height:1.55}} .arrival .hint{{font-size:14px}}
 .mapbox iframe{{height:210px}}
 footer.wrap{{padding:20px 18px 44px;font-size:11.5px;line-height:1.55}}
}}
</style></head><body>
<header class="hero">
<div class="hpic"><div class="slides">{''.join(f'<img src="{PH[c["id"]]["card"]["thumb"]}" alt="{html.escape(c["name"])}" data-course="{c["id"]}" data-name="{html.escape(c["name"])}">' for c in COURSES)}</div>
<div class="wrap hcap">
<p class="kicker">Tokyo · October 5 and 6</p>
<h1>Tokyo, <span class="nb">October 5 and 6.</span></h1>
<div class="snav"><button class="slabel" type="button"></button><div class="dots">{''.join(f'<button type="button" aria-label="Show course {c["id"]}"></button>' for c in COURSES)}</div></div>
</div></div>
<div class="wrap hbody">
<p>Monday the 5th starts at 5:30 in the morning at the tuna auction, so the morning is already spoken for. You sleep from about half past eight, come back for lunch in Hibiya at noon, and the afternoon starts after that. Tuesday the 6th has nothing fixed before it &mdash; the start time is yours. Three choices below: a place for lunch on the 5th, then a course for each afternoon, or say you&rsquo;d rather rest.</p>
<ul class="facts"><li><b>Guide</b> Yuuki</li><li><b>Oct 5</b> about 13:15 to 18:00</li><li><b>Oct 6</b> start time is your choice</li><li><b>Fee</b> $250 &middot; ¥40,000 a day</li></ul>
</div>
</header>
<div class="wrap">
<div class="sechead"><span class="n">1</span><div><b>Monday, October 5 &mdash; lunch at noon</b> <span>Pick one. All five are open for lunch on Monday the 5th, take bookings, and are within ten minutes of your hotel.</span></div></div>
<p class="lnote">You said the sushi on the 20th was too much food. Each place below lets you decide how much arrives, and the smallest option is written on each card. Numbers 2 and 4 are in the same brick arches under the train line as the sushi place; the other three are a few minutes away on foot. Prices are per person and were checked on each restaurant&rsquo;s own page on September 25.</p>
<div class="lunch">{''.join(lunch_card(c) for c in LUNCH)}</div>
<div class="sechead"><span class="n">2</span><div><b>Monday, October 5 &mdash; the afternoon</b> <span>Pick one. You will have been awake since 4:15, so every course below ends by six and the evening stays empty.</span></div></div>
<div class="menu">{''.join(menu(c) for c in DAY1)}</div>
{''.join(detail(c) for c in DAY1)}



<div class="sechead"><span class="n">3</span><div><b>Tuesday, October 6</b> <span>Pick one. Nothing is fixed before this, so start whenever suits you &mdash; the times below are a suggestion.</span></div></div>
<div class="menu">{''.join(menu(c) for c in DAY2)}</div>
{''.join(detail(c) for c in DAY2)}



<div class="sechead"><span class="n">4</span><div><b>What it costs</b> <span>The same basis both days.</span></div></div>
<div class="arrival">
<div><p style="font-size:22px;line-height:1.3;margin:0 0 10px"><b>US$250 a day &mdash; or ¥40,000 in cash &mdash; whichever course you pick.</b></p>
<p>Four hours or five, it is the same figure &mdash; so pick the one you actually want rather than the one that looks like less work.</p>
<p class="hint">The fee covers my time only, set up the way we agreed: entry tickets, trains, taxis and meals are settled on the day as they come. Dollars by payment link, like the kabuki tickets, or yen in cash on the day &mdash; whichever is easier for you. Nothing is owed if you wake up and decide you would rather not.</p></div>
<div><p><b>And one honest word.</b></p>
<p>If you wake up on the 5th, do the auction, sleep, and then decide that the afternoon is more than you want, say so and we cancel it. Nothing is owed. That is a good answer and I would rather have it than watch you push through.</p></div>
</div>
</div>
<footer class="wrap"><p>Reply to Yuuki with a lunch number and a letter for each day &mdash; or with &ldquo;none, we will rest&rdquo;, which is a real answer and not a disappointing one. Times are approximate and can move earlier or later on the day.</p>
<details class="cred"><summary>Photo credits</summary><p>{credits}, via Wikimedia Commons.</p></details></footer>
<script>
(function(){{
 var cards=[].slice.call(document.querySelectorAll('.mcard'));
 function cardFor(id){{return document.querySelector('.mcard[data-course="'+id+'"]')}}
 function close(id,now){{var d=document.getElementById('detail-'+id),b=cardFor(id);d.classList.remove('open');b.closest('.menu').classList.remove('picked');b.setAttribute('aria-expanded','false');if(now){{d.hidden=true;return}}setTimeout(function(){{if(!d.classList.contains('open'))d.hidden=true}},320)}}
 function land(id){{var d=document.getElementById('detail-'+id),done=false;function go(){{if(done)return;done=true;d.scrollIntoView({{behavior:'smooth',block:'start'}})}}
   d.addEventListener('transitionend',function f(e){{if(e.target===d){{d.removeEventListener('transitionend',f);go()}}}});setTimeout(go,420)}}
 function point(id){{var b=cardFor(id),d=document.getElementById('detail-'+id);
   var r=b.getBoundingClientRect(),w=d.getBoundingClientRect();
   d.style.setProperty('--arrow',(r.left+r.width/2-w.left)+'px')}}
 function open_(id){{var d=document.getElementById('detail-'+id),b=cardFor(id);d.hidden=false;b.closest('.menu').classList.add('picked');
   requestAnimationFrame(function(){{d.classList.add('open');point(id)}});
   b.setAttribute('aria-expanded','true')}}
 window.addEventListener('resize',function(){{var o=document.querySelector('.mcard[aria-expanded=true]');if(o)point(o.dataset.course)}});
 var want=(location.hash.match(/^#detail-([A-F])$/)||[])[1]||(location.search.match(/[?&]open=([A-F])/)||[])[1];
 if(want){{open_(want);setTimeout(function(){{document.getElementById('detail-'+want).scrollIntoView()}},80)}}
 cards.forEach(function(b){{
  b.addEventListener('click',function(){{
   var id=b.dataset.course,was=b.getAttribute('aria-expanded')==='true',myMenu=b.closest('.menu');
   cards.forEach(function(o){{if(o.closest('.menu')===myMenu&&o.getAttribute('aria-expanded')==='true')close(o.dataset.course,true)}});
   if(was)return;
   open_(id);history.replaceState(null,'','#detail-'+id);
   land(id);
  }});
 }});
 document.querySelectorAll('.dclose').forEach(function(x){{
  x.addEventListener('click',function(){{var d=x.closest('.detail'),id=d.id.replace('detail-','');close(id);
   cardFor(id).scrollIntoView({{behavior:'smooth',block:'center'}})}});
 }});
}})();
{HERO_JS}
</script>
{{DEVBAR}}</body></html>'''
open('index.html', 'w').write(page.replace('{DEVBAR}', ''))
open('preview.html', 'w').write(page.replace(
    '{DEVBAR}',
    '<script>window.DEVBAR_FORCE=1</script><script src="devbar.js?v=3"></script>'))
print('written', len(page), '-> index.html + preview.html')

# 10/5の昼だけの単体ページ（ユウキ9/25「5日のご飯は単体で」）。CSSと店データは本ページと共用。
style = page[page.index('<style>'):page.index('</style>') + 8]
lunch_page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lunch in Hibiya on October 5</title><meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{style}<style>.lhead{{padding:44px 0 8px}} .lhead p{{font-size:18px;color:var(--mute);margin:0;max-width:680px}}
@media(max-width:560px){{.lhead{{padding:30px 0 4px}} .lhead p{{font-size:16px}}}}</style></head><body>
<header class="wrap lhead"><p class="kicker">Tokyo &middot; Monday, October 5 &middot; 12:00</p>
<h1>Lunch in Hibiya, <span class="nb">a smaller one.</span></h1>
<p>You said the sushi on the 20th was too much food. Here are five quieter places near your hotel where you decide how much arrives. All five are open for lunch on Monday the 5th and take bookings. Pick one and I will book it for 12:00.</p>
<ul class="facts"><li><b>Date</b> Monday, October 5</li><li><b>Time</b> 12:00</li><li><b>Distance</b> 3&ndash;10 minutes on foot from your hotel</li></ul>
</header>
<div class="wrap">
<div class="sechead"><div><b>Five places, pick one</b> <span>The smallest option is written on each card. Prices are per person and were checked on each restaurant&rsquo;s own page on September 25.</span></div></div>
<p class="lnote">Numbers 2 and 4 are in the same brick arches under the train line as the sushi place on the 20th; the other three are a few minutes away on foot.</p>
<div class="lunch">{''.join(lunch_card(c) for c in LUNCH)}</div>
</div>
<footer class="wrap"><p>Reply to Yuuki with the number you like. Menus and prices can change a little before the day; I confirm them when I book.</p>
<p><a href="./" style="color:inherit">The afternoon courses for October 5 and 6 are on this page.</a></p></footer>
</body></html>'''
open('lunch.html', 'w').write(lunch_page)
print('written', len(lunch_page), '-> lunch.html')
