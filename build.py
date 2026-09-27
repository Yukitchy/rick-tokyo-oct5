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

DAY1_OLD = [
 dict(id='A', fee='$250 · about five hours', chips=['Mostly sitting down','Ends a few minutes from your hotel','$250 · the day'], name='Asakusa, and the river home', tag='Old temple, river boat, garden',
  why='You will have been awake since a quarter past four and had lunch already. This course is built so that the moving after that is done sitting down: a temple in the morning district, then a boat that carries you back down the Sumida and drops you almost at your door. Nothing here needs booking and nothing here is far.',
  steps=[('13:15','After lunch','About 25 minutes by train from Ginza to Asakusa. You can sleep on it.'),
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
  steps=[('13:30','After lunch','About 20 minutes by train to Toyosu, the same line you took at dawn.'),
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
  steps=[('13:15','After lunch','About 20 minutes by train from Ginza to Harajuku.'),
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
# 10/5午後。ユウキ 9/27「昼と午後は同じ街で完結させる（昼だけ遠出して長距離移動する羽目にしない）」→ 銀座組の昼(1,2,3,4,6)→G、神楽坂の昼(5)→H。
# 営業は 2026-09-27 に確認: 伊東屋 月10-20 / 三越 10-20 / 木村家 10-20 無休 / GINZA SIX屋上 7-23・中村藤吉 10:30-20:30 / 梅花亭 10-19 水休 / あかぎカフェ 平日10-22 火休 / AKOMEYA in la kagu 月11-20。CANAL CAFEは第1・3月曜休=10/5休なので使わない。
DAY1 = [
 dict(id='G', fee='$250 · about four hours', chips=['On foot from lunch','Shopping and gifts','Ends 10 min from your hotel'], name='Ginza, on foot from the table', tag='Stationery, a food hall, a rooftop garden, tea',
  why='This goes with lunch 1, 2, 3, 4 or 6. You stand up from the table and the afternoon is already around you: everything below is inside one neighbourhood, flat, and about two kilometres end to end, with a seat every forty minutes. It is the shopping afternoon &mdash; paper, pens, a food hall, sweets to carry back &mdash; with a garden on a roof in the middle of it. From lunch 4 in Nihonbashi it starts with a ten-minute taxi; from the others you walk.',
  steps=[('13:30','Itoya, Ginza 2-chome','Twelve floors of paper and pens in one narrow building, since 1904. Letter sets, washi paper, fountain pens, wrapping &mdash; gifts that pack flat. There is a café on the top floor if you want to sit before you start.'),
         ('14:30','Mitsukoshi, the basement food hall','Five minutes down the main street. Two floors under the department store of wagashi, tea, pickles, rice crackers and bento from every part of Japan, most of it boxed to travel. The easiest place in Tokyo to buy food gifts, and I translate the counters.'),
         ('15:15','Kimuraya, across the crossing','The bakery that invented the sweet-bean bun in 1874, on the corner of the Ginza crossing under the clock tower. A paper bag of five for the hotel room.'),
         ('15:30','Ginza Six, the roof','A department store with a garden on top, free, open to anyone. Benches, trees, and the whole of Ginza below you. Then the art bookshop on the sixth floor, which is worth a look even if you buy nothing.'),
         ('16:20','Tea at Nakamura Tokichi','On the fourth floor of the same building: a tea house from Uji, near Kyoto, that has been selling matcha since 1854. A bowl of tea, or a matcha jelly and ice cream, sitting down. This is the rest before the walk home.'),
         ('17:00','Back at the hotel','About twelve minutes on foot, or a five-minute taxi.')],
  stops=['Ginza Itoya','Ginza Mitsukoshi','Ginza Kimuraya','GINZA SIX','The Blossom Hibiya Tokyo'],
  moves='Lunch &rarr; Itoya on foot (5&ndash;15 min, or a 10-min taxi from Nihonbashi). Itoya &rarr; Mitsukoshi 5 min. Mitsukoshi &rarr; Kimuraya across the crossing. Kimuraya &rarr; Ginza Six 5 min. Ginza Six &rarr; hotel about 12 min on foot or a short taxi.',
  food=[('Nakamura Tokichi, Ginza Six 4F','Ginza &middot; matcha, sitting down','Uji tea house since 1854. Matcha whisked in front of you, or the matcha jelly with ice cream and red beans, about ¥1,000&ndash;1,800. Open Monday 10:30&ndash;20:30.','Nakamura Tokichi Ginza Six'),
        ('Kimuraya','Ginza 4-chome &middot; the original sweet-bean bun','Soft bread around sweet red bean paste, a cherry blossom pressed into the top, since 1874. About ¥200 each; a bag of five travels fine to the hotel.','Ginza Kimuraya'),
        ('Mitsukoshi depachika','Ginza &middot; the basement food hall','Wagashi, tea, pickles and bento from all over Japan, boxed to carry &mdash; the place to buy food gifts. Open Monday 10:00&ndash;20:00.','Ginza Mitsukoshi depachika')],
  good='No trains, no taxis unless you want one, and the day ends within sight of your hotel. The right afternoon for a couple who like shops and a kitchen more than a shrine.',
  mind='Everything here is open on Monday the 5th; nothing needs booking. If at four o&rsquo;clock you would rather have a garden than a bookshop, Hama-rikyu &mdash; a 400-year-old shogun&rsquo;s garden with a tea house on the pond &mdash; is a fifteen-minute walk south, last entry 16:30, ¥300. Say so on the day and we go there instead.',
  links=[('Itoya (official)','https://www.ito-ya.co.jp/'),('Ginza Six (official)','https://ginza6.tokyo/'),('Ginza Mitsukoshi (official)','https://www.mistore.jp/store/ginza.html'),('Hama-rikyu Gardens','https://www.tokyo-park.or.jp/teien/en/hama-rikyu/')]),
 dict(id='H', fee='$250 · about four hours', chips=['On foot from lunch','Stone lanes, a shrine, a rice shop','Downhill the whole way'], name='Kagurazaka, the hill after lunch', tag='Old geisha lanes, a glass shrine, sweets and rice',
  why='This goes with lunch 5. Kagurazaka is a hill of stone-paved lanes that was a geisha district a hundred years ago and is still the quietest old quarter in central Tokyo. The restaurant is near the top, so the afternoon is a slow walk down it: a sweet shop, a shrine rebuilt in glass and wood, a rice-and-kitchen shop for gifts, a red temple gate, then the lanes. You finish at the station at the bottom and one train takes you to your hotel.',
  steps=[('13:30','Baikatei, three minutes from lunch','A wagashi shop since 1935 with a counter of seasonal sweets and the shop&rsquo;s own hand-shaped &ldquo;ukishima&rdquo; cakes. A box for the hotel, or one each now.'),
         ('13:45','Akagi Shrine, and a coffee on its steps','A shrine at the top of the hill, rebuilt in 2010 by the architect Kengo Kuma in glass and cedar. Unusual, quiet, and with a café on the grounds where we sit for half an hour. Open Monday.'),
         ('14:30','Akomeya, in la kagu','Across the road: a rice shop that grew into a whole floor of kitchen things &mdash; rice from single farms, bowls, knives, tea, packaged food gifts &mdash; in a converted warehouse. This is the gift stop of the day. Open Monday 11:00&ndash;20:00.'),
         ('15:20','Zenkoku-ji, the red gate','Five minutes down the main street. A small temple with a bright red gate and a pair of stone tigers, here since 1792. Two minutes to look, a bench in the courtyard if you want it.'),
         ('15:35','The lanes','Behind the temple: Hyogo-yokocho and Kakurenbo-yokocho, stone-paved alleys between black wooden fences where the geisha houses were. Flat, short, and the reason people come here. We take it slowly.'),
         ('16:15','Down to Iidabashi, and home','The bottom of the hill is Iidabashi station. One train, about 15 minutes, to Yurakucho, which is 8 minutes on foot from your hotel &mdash; or a taxi the whole way, about 20 minutes.'),
         ('16:45','Back at the hotel','')],
  stops=['Kagurazaka Kurobatei','Kagurazaka Baikatei','Akagi Jinja Kagurazaka','la kagu Kagurazaka','Zenkokuji Kagurazaka','Iidabashi Station'],
  moves='All on foot, about 1.5 km and downhill. Iidabashi &rarr; Yurakucho 15 min by train, then 8 min on foot, or a 20-min taxi door to door.',
  food=[('Baikatei','Kagurazaka &middot; wagashi since 1935','Seasonal sweets shaped like the month, and the shop&rsquo;s own soft sponge cakes. ¥200&ndash;400 each, boxed if you want. Open Monday 10:00&ndash;19:00.','Kagurazaka Baikatei'),
        ('Akagi Café','On the shrine grounds &middot; coffee and cake','A glass-walled café next to the shrine hall, seated, quiet. Coffee, tea and a slice of something, about ¥800&ndash;1,500. Open Monday.','Akagi Cafe Kagurazaka'),
        ('Akomeya','la kagu &middot; rice, tea and kitchen gifts','Rice by the small bag, tea, seasonings and tableware, all wrapped for travel. There is a small canteen if you want a bowl of rice and pickles later.','AKOMEYA TOKYO in la kagu')],
  good='The most Japanese-looking afternoon of the two, and the one with the least traffic. The only walking that matters is downhill.',
  mind='Only pick this with lunch 5, otherwise you cross the city twice. The canal-side café at the bottom of the hill is closed on the first Monday of the month, which the 5th is, so the coffee stop is at the shrine instead. Stone lanes are uneven in places &mdash; flat shoes.',
  links=[('Akagi Shrine (official)','https://www.akagi-jinja.jp/'),('AKOMEYA TOKYO in la kagu','https://www.akomeya.jp/store_info/store/sinlakagu/'),('Kagurazaka (Go Tokyo)','https://www.gotokyo.org/en/spot/1000/index.html')]),
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
 dict(id='E', fee='$250 · about four hours', chips=['The least walking on Tuesday','Closest to your hotel','$250 · the day'], name='The East Gardens, and Marunouchi', tag='Edo castle grounds, brick Tokyo, coffee',
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
 dict(id='F', fee='$250 · about five and a half hours', chips=['Cooking and shopping','Something to take home','$250 · the day'], name='Kappabashi, and the old temple next door', tag='Kitchen street, food samples, Senso-ji',
  why="For the two of you who like a kitchen and a gift shop. Kappabashi is Tokyo's restaurant-supply street &mdash; knives, tableware, and the shops that make the plastic food models you have seen in every restaurant window. Then a soba lunch, and Tokyo&rsquo;s oldest temple ten minutes away on foot, with a three-hundred-year-old street of stalls in front of it, before a taxi home.",
  steps=[('10:00','Start from the hotel','About 20 minutes by train or taxi to Kappabashi, in Asakusa.'),
         ('10:30','Kappabashi Kitchen Street','A few hundred metres of restaurant-supply shops: knives that can be engraved with your name while you wait, lacquerware, and the original workshops behind Japan&rsquo;s plastic food displays. Most shops are open Tuesdays &mdash; it is Sundays that are quiet here.'),
         ('11:15','Make your own food sample','At Ganso Shokuhin Sample-ya, the shop that popularised the craft in 1932. A booked 40-minute session making a piece of wax or plastic tempura or lettuce, which you keep. I book the slot in advance.'),
         ('12:15','Lunch, Namiki Yabusoba','A soba restaurant near Kaminarimon since 1913, a few minutes&rsquo; walk from Kappabashi. Seated, quick, and open Tuesdays.'),
         ('13:30','Senso-ji, on foot','Ten minutes from the soba shop. Tokyo&rsquo;s oldest temple, founded in 628: in under the five-metre paper lantern, along Nakamise &mdash; a street of rice-cracker and fan stalls that has been a shopping street for three hundred years &mdash; to the main hall. Flat, with benches in the courtyard.'),
         ('15:00','Something sweet on Nakamise','Melon bread out of the oven, or a bag of hot senbei, eaten as we walk back.'),
         ('15:30','Taxi to the hotel','About 25 minutes across the city, sitting down.')],
  stops=['The Blossom Hibiya Tokyo','Kappabashi Dougu Street','Namiki Yabusoba Asakusa','Sensoji Temple Asakusa','The Blossom Hibiya Tokyo'],
  moves='Hotel &rarr; Kappabashi about 20 min. On foot around Kappabashi. Soba shop &rarr; Senso-ji 10 min on foot. Asakusa &rarr; hotel about 25 min by taxi.',
  food=[('Namiki Yabusoba','Asakusa &middot; soba','Buckwheat noodles in a dark dashi broth, served cold with a dipping sauce or hot. Seated, since 1913, about ¥1,000&ndash;2,000.','Namiki Yabusoba Asakusa'),
        ('Your own food sample','Ganso Shokuhin Sample-ya &middot; made by you','A wax or plastic tempura piece or lettuce leaf you make yourself in the 40-minute workshop &mdash; not edible, but yours to keep. About ¥3,300 per person.','Ganso Shokuhin Sample-ya'),
        ('Nakamise street stalls','Asakusa &middot; snacks as you walk','Melon bread, grilled rice crackers, sweet bean cakes shaped like the temple gate. A few hundred yen each, eaten standing.','Nakamise Dori Asakusa')],
  good='The only course with something you make yourself and something you can wrap up and take home. Good for a day built around gifts.',
  mind='Kappabashi shops mostly close Sundays, not Tuesdays, so the 6th is a normal day there. The food-sample workshop needs a reservation &mdash; I book it as soon as you choose this course, and will confirm the exact Tuesday time slot when I do.',
  links=[('Kappabashi Dougu Street (official)','https://www.kappabashi.or.jp/en/'),('Ganso Shokuhin Sample-ya (official)','https://www.ganso-sample.com/en/'),('Senso-ji (official)','https://www.senso-ji.jp/english/')]),
]

COURSES = DAY1 + DAY2

# 10/5の昼。Rick 9/25「寿司でいいが25貫よりずっと少なく」→ ユウキ 9/27「隠れ家的・控えめな量・高級感・予約可。日比谷縛りは外す」。
# 営業・価格は 2026-09-27 に公式/一休/ぐるなびで確認。脱落: とうふ屋うかい芝(2026-03-31閉店)・赤坂菊乃井/鮨かねさか/銀座とよだ(月曜休)・六雁(昼営業なし)・うを徳(昼は4名〜)・野田岩(月曜に不定休)。
LUNCH = [
 dict(n=1, after='G', name='Ginza Sushimasa', where='Higashi-Ginza, behind the Kabuki-za &middot; sushi', walk='About 15 min on foot, 5 by taxi',
  img='img/lunch/sushimasa.jpg', alt='A plate of nigiri at Ginza Sushimasa',
  body='Sushi again, but a short one. A basement room on the back side of the Kabuki-za theatre, so the street outside is quiet even at noon. The lunch is a short kaiseki: a few cooked dishes first, then a small round of nigiri, then dessert.',
  size='Iro course: 5 small dishes and 7 pieces of nigiri, &yen;9,900. Yui course: 8 dishes and 9 pieces, &yen;13,200. If you only want nigiri, the Ajisai lunch is 7 pieces with a small bowl of chirashi, &yen;4,950.',
  hours='Monday lunch 11:30&ndash;14:30. Closed Wednesdays.', book='Booking online or by phone. I book it.',
  q='Ginza Sushimasa Kabukiza', link=('Lunch menu (official)','https://www.ginza-sushimasa.com/lunch/')),
 dict(n=2, after='G', name='Tempura Kondo', where='Ginza 5-chome, 9th floor &middot; tempura', walk='About 10 min on foot',
  img='img/lunch/kondo.jpg', alt='The counter at Tempura Kondo',
  body='Two Michelin stars, on the ninth floor of a narrow building with almost no sign at street level. You sit at the counter and each piece is fried in front of you and put on your plate one at a time. Vegetables are the speciality here, not just seafood.',
  size='Sumire lunch: 9 pieces (2 prawn, 3 fish, 4 vegetable) with rice, pickles, red miso soup and fruit, &yen;13,200. The next size up is 11 pieces, &yen;16,500. Nothing bigger at lunch.',
  hours='Monday lunch in two seatings, 12:00 or 13:30. Closed Sundays.', book='Booking by phone or online. I book the 12:00 seating.',
  q='Tempura Kondo Ginza', link=('Restaurant page','https://restaurant.ikyu.com/107810')),
 dict(n=3, after='G', name='Ginza Uchiyama', where='Ginza 2-chome, basement &middot; seasonal Japanese', walk='About 20 min on foot, 7 by taxi',
  img='img/lunch/uchiyama.jpg', alt='The counter at Ginza Uchiyama',
  body='A basement room on a side street at the quiet end of Ginza, booking only, 25 seats with 9 at the counter and two private rooms. The house dish is sea bream over rice with hot tea poured on at the end. The lunch is small plates, one after another, and ends with that.',
  size='Lunch course: 7 dishes ending with the sea-bream rice, &yen;5,500 with tax and service. An 8-dish version with better ingredients is a little more.',
  hours='Monday lunch 11:30&ndash;14:30. Closed on public holidays only (the 5th is not one).', book='Booking online. I book it.',
  q='Ginza Uchiyama', link=('Restaurant page','https://restaurant.ikyu.com/114634/')),
 dict(n=4, after='G', name='Nihonbashi Yukari', where='Nihonbashi, 3 min from Tokyo Station &middot; kappo', walk='About 10 min by taxi',
  img='img/lunch/yukari.jpg', alt='A seasonal dish at Nihonbashi Yukari',
  body='A family restaurant since 1935, now run by the third generation, Kimio Nonaga, who won the Iron Chef title in 2002. Old-style Tokyo cooking, plainly presented. There are private rooms in the basement with sunken tables, so you can have the room to yourselves.',
  size='Lunch is a set tray, the Yukari gozen, about &yen;4,000, booked the day before. Courses above that on request. All of it is modest in size.',
  hours='Monday lunch 11:30&ndash;14:00, last order 13:30. Closed Sundays and holidays.', book='Phone booking. I call and book a private room.',
  q='Nihonbashi Yukari', link=('Official site','http://nihonbashi-yukari.com/')),
 dict(n=5, after='H', name='Kagurazaka Kurobatei', where='Kagurazaka, in the old geisha quarter &middot; seasonal Japanese and udon', walk='About 20 min by taxi',
  img='img/lunch/kurobatei.jpg', alt='A private room at Kurobatei',
  body='The one that is not in Ginza. Kagurazaka is a hill of stone-paved lanes that used to be a geisha district, and this restaurant sits in one of the lanes off the main slope. Five private rooms, 30 seats in all. The meal is a tray of small seasonal things with thin hand-cut udon noodles as the main dish.',
  size='San-no-zen lunch tray: an appetiser plate, sashimi, a seasonal dish, tempura, udon and a sweet, &yen;5,000 with tax and service. One tray each, nothing else arrives.',
  hours='Monday lunch 11:30&ndash;14:30, last order 14:00. Closed Sundays.', book='Booking online. I book a private room.',
  q='Kagurazaka Kurobatei', link=('Restaurant page','https://restaurant.ikyu.com/101020')),
 dict(n=6, after='G', name='Chikuyotei, main house', where='Higashi-Ginza, Kobikicho &middot; eel and Japanese', walk='About 15 min on foot, 5 by taxi',
  img='img/lunch/chikuyotei.jpg', alt='The inner garden at Chikuyotei',
  body='An eel house from the 1860s, still in a wooden building with a small garden, a few streets behind the Kabuki-za. The tatami rooms are booked as private rooms for two or more and serve a set course; the grilled eel comes in the middle of it, not as a giant bowl.',
  size='Lunch course in a private tatami room: 7 to 8 small dishes with the eel as the main, &yen;10,230 plus 10% service. If you would rather sit at a table, the eel bowl is &yen;3,630.',
  hours='Monday lunch 11:30&ndash;15:30, last order 14:30. Closed Sundays and holidays.', book='Phone booking for the room. I call and book it.',
  q='Chikuyotei Honten Ginza', link=('Official site','http://chikuyoutei.co.jp/')),
]
def lunch_card(c):
    return f'''<article class="lcard"><img src="{c['img']}" alt="{html.escape(c['alt'])}" loading="lazy">
<div class="eb"><em>{c['n']} &middot; {c['where']}</em><strong>{c['name']}</strong><span>{c['body']}</span>
<p class="lsize">{c['size']}</p>
<p class="lmeta">{c['walk']}. {c['hours']} {c['book']} <b>Afternoon: course {c['after']}.</b></p>
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
.menu{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}} .menu.two{{grid-template-columns:repeat(2,minmax(0,1fr))}}
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
 .menu,.menu.two,.lunch{{grid-template-columns:1fr}} .mcard>img{{aspect-ratio:16/9}}
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
<p>Monday the 5th starts at 5:30 in the morning at the tuna auction, so the morning is already spoken for. You sleep from about half past eight, come back for lunch at noon, and the afternoon starts after that. Tuesday the 6th has nothing fixed before it &mdash; the start time is yours. Three choices below: a place for lunch on the 5th, the afternoon that goes with it, and a course for the 6th, or say you&rsquo;d rather rest.</p>
<ul class="facts"><li><b>Guide</b> Yuuki</li><li><b>Oct 5</b> lunch at 12:00, then about 13:30 to 17:00</li><li><b>Oct 6</b> start time is your choice</li><li><b>Fee</b> $250 &middot; ¥40,000 a day</li></ul>
</div>
</header>
<div class="wrap">
<div class="sechead"><span class="n">1</span><div><b>Monday, October 5 &mdash; lunch at noon</b> <span>Pick one. All six are open for lunch on Monday the 5th and take bookings. Each one is the quiet kind, a basement, an upper floor or a back lane, and each lunch is a short course, nowhere near 25 pieces. Five are in or next to Ginza, one is across town.</span></div></div>
<p class="lnote">The smallest option is written on each card. Prices are per person and were checked on each restaurant&rsquo;s own page on September 27. Travel times are from your hotel.</p>
<div class="lunch">{''.join(lunch_card(c) for c in LUNCH)}</div>
<div class="sechead"><span class="n">2</span><div><b>Monday, October 5 &mdash; the afternoon</b> <span>The afternoon follows the lunch, on foot, so nobody crosses the city twice. Lunch 1, 2, 3, 4 or 6 goes with course G in Ginza; lunch 5 goes with course H in Kagurazaka. You will have been awake since 4:15, so both end by five and the evening stays empty.</span></div></div>
<div class="menu two">{''.join(menu(c) for c in DAY1)}</div>
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
<title>Lunch on October 5</title><meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{style}<style>.lhead{{padding:44px 0 8px}} .lhead p{{font-size:18px;color:var(--mute);margin:0;max-width:680px}}
@media(max-width:560px){{.lhead{{padding:30px 0 4px}} .lhead p{{font-size:16px}}}}</style></head><body>
<header class="wrap lhead"><p class="kicker">Tokyo &middot; Monday, October 5 &middot; 12:00</p>
<h1>Lunch on the 5th, <span class="nb">a smaller one.</span></h1>
<p>You said the sushi on the 20th was too much food. Here are six quieter places: a basement, an upper floor, a back lane, a wooden house. Each lunch is a short course, and at each one you can stop where you like. All six are open for lunch on Monday the 5th and take bookings. Five are in or next to Ginza, one is in Kagurazaka. Pick one and I will book it for 12:00.</p>
<ul class="facts"><li><b>Date</b> Monday, October 5</li><li><b>Time</b> 12:00</li><li><b>Distance</b> 5&ndash;20 minutes from your hotel, on foot or by taxi</li></ul>
</header>
<div class="wrap">
<div class="sechead"><div><b>Six places, pick one</b> <span>The smallest option is written on each card. Prices are per person and were checked on each restaurant&rsquo;s own page on September 27.</span></div></div>
<p class="lnote">Travel times on each card are from your hotel. Numbers 1, 2, 3 and 6 are in Ginza, number 4 is by Tokyo Station, number 5 is a taxi ride across town.</p>
<div class="lunch">{''.join(lunch_card(c) for c in LUNCH)}</div>
</div>
<footer class="wrap"><p>Reply to Yuuki with the number you like. Menus and prices can change a little before the day; I confirm them when I book.</p>
<p><a href="./" style="color:inherit">The afternoon courses for October 5 and 6 are on this page.</a></p></footer>
</body></html>'''
open('lunch.html', 'w').write(lunch_page)
print('written', len(lunch_page), '-> lunch.html')
