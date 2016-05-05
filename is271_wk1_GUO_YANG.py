
#task 0

course= 'IS271'
week = 1
output = 'course: {}\nweek: {}'.format(course, week)
print(output)


#task 1

me = {}
me['name'] = 'Guo, Yang'
me['hometown'] = 'China'
me['undergrad_major'] = 'Computer Science'
me['expected_grad_year'] = 2017
print ('My name: {}'.format(me['name'])+'\n'+'Hometown: {}'.format(me['hometown'])+'\n'+'Undergrad Major: {}'.format(me['undergrad_major'])+'\n'+'Expected Graduation: {}'.format(me['expected_grad_year']))


#task 2
fav_auths = []
#author 1
auth1 = {}
auth1['auth_name'] = 'Rowling, J.K.'
auth1['dob'] = 1965
book1_of_auth1 = {}
book1_of_auth1['titile'] = 'Harry Potter and the Cursed Child'
book1_of_auth1['year'] = 2016
book2_of_auth1 = {}
book2_of_auth1['titile'] = 'Harry Potter and the Sorcerer\'s Stone'
book2_of_auth1['year'] = 2015
auth1['books'] = [book1_of_auth1, book2_of_auth1]
fav_auths.append(auth1)

#author 2
auth2 = {}
auth2['auth_name'] = 'Patterson, James'
auth2['dob'] = 1947
book1_of_auth2 = {}
book1_of_auth2['titile'] = 'Private Paris'
book1_of_auth2['year'] = 2016
book2_of_auth2 = {}
book2_of_auth2['titile'] = 'NYPD Red 4'
book2_of_auth2['year'] = 2016
auth2['books'] = [book1_of_auth2, book2_of_auth2]
fav_auths.append(auth2)


#author 3
auth3 = {}
auth3['auth_name'] = 'Corben, Harlan'
auth3['dob'] = 1962
book1_of_auth3 = {}
book1_of_auth3['titile'] = 'Fool Me Once'
book1_of_auth3['year'] = 2016
book2_of_auth3 = {}
book2_of_auth3['titile'] = 'The Stranger'
book2_of_auth3['year'] = 2015
auth3['books'] = [book1_of_auth3, book2_of_auth3]
fav_auths.append(auth3)


#author 4
auth4 = {}
auth4['auth_name'] = 'Clark, Marcia'
auth4['dob'] = 1953
book1_of_auth4 = {}
book1_of_auth4['titile'] = 'If I\'m Dead: A Rachel Knight Story'
book1_of_auth4['year'] = 2012
book2_of_auth4 = {}
book2_of_auth4['titile'] = 'Trouble in Paradise: A Rachel Knight Story'
book2_of_auth4['year'] = 2013
auth4['books'] = [book1_of_auth4, book2_of_auth4]
fav_auths.append(auth4)

#author 5
auth5 = {}
auth5['auth_name'] = 'King, Stephen'
auth5['dob'] = 1947
book1_of_auth5 = {}
book1_of_auth5['titile'] = 'End of Watch'
book1_of_auth5['year'] = 2016
book2_of_auth5 = {}
book2_of_auth5['titile'] = 'The Gunslinger'
book2_of_auth5['year'] = 2016
auth5['books'] = [book1_of_auth5, book2_of_auth5]
fav_auths.append(auth5)
#print (fav_auths)

from pprint import pprint
pprint (fav_auths)






# task 3
temp_flname = me['name'].split(', ')
flname = temp_flname[1] + ' ' + temp_flname[0]
print ('flname: {}'.format(flname)) #print out Yang Guo
FLname = flname.upper()
print ('FLname: {}'.format(FLname))

rev_name = flname[::-1]
print (rev_name)

name_length = len(flname)
print (name_length)

auths_last = []
auths_last.append(fav_auths[0]['auth_name'].split(', ')[0])
auths_last.append(fav_auths[1]['auth_name'].split(', ')[0])
auths_last.append(fav_auths[2]['auth_name'].split(', ')[0])
auths_last.append(fav_auths[3]['auth_name'].split(', ')[0])
auths_last.append(fav_auths[4]['auth_name'].split(', ')[0])
print (auths_last)

string_auths_last = ', '.join(auths_last)
separator = '|'
auths_piped = separator.join(auths_last)
print (auths_piped)

public_dates = []
public_dates.append(fav_auths[0]['books'][0]['year'])
public_dates.append(fav_auths[0]['books'][1]['year'])
public_dates.append(fav_auths[1]['books'][0]['year'])
public_dates.append(fav_auths[1]['books'][1]['year'])
public_dates.append(fav_auths[2]['books'][0]['year'])
public_dates.append(fav_auths[2]['books'][1]['year'])
public_dates.append(fav_auths[3]['books'][0]['year'])
public_dates.append(fav_auths[3]['books'][1]['year'])
public_dates.append(fav_auths[4]['books'][0]['year'])
public_dates.append(fav_auths[4]['books'][1]['year'])
print (public_dates)


avg_pub = (int(public_dates[0]) + \
int(public_dates[1]) + \
int(public_dates[2]) + \
int(public_dates[3]) + \
int(public_dates[4]) + \
int(public_dates[5]) + \
int(public_dates[6]) + \
int(public_dates[7]) + \
int(public_dates[8]) + \
int(public_dates[9]) ) / 10
print (avg_pub)







# task 4

ode = """Thou still unravish'd bride of quietness,
Thou foster-child of silence and slow time,
Sylvan historian, who canst thus express
A flowery tale more sweetly than our rhyme:
What leaf-fring'd legend haunts about thy shape
Of deities or mortals, or of both,
In Tempe or the dales of Arcady?
What men or gods are these? What maidens loth?
What mad pursuit? What struggle to escape?
What pipes and timbrels? What wild ecstasy?

Heard melodies are sweet, but those unheard
Are sweeter; therefore, ye soft pipes, play on;
Not to the sensual ear, but, more endear'd,
Pipe to the spirit ditties of no tone:
Fair youth, beneath the trees, thou canst not leave
Thy song, nor ever can those trees be bare;
Bold Lover, never, never canst thou kiss,
Though winning near the goal yet, do not grieve;
She cannot fade, though thou hast not thy bliss,
For ever wilt thou love, and she be fair!

Ah, happy, happy boughs! that cannot shed
Your leaves, nor ever bid the Spring adieu;
And, happy melodist, unwearied,
For ever piping songs for ever new;
More happy love! more happy, happy love!
For ever warm and still to be enjoy'd,
For ever panting, and for ever young;
All breathing human passion far above,
That leaves a heart high-sorrowful and cloy'd,
A burning forehead, and a parching tongue.

Who are these coming to the sacrifice?
To what green altar, O mysterious priest,
Lead'st thou that heifer lowing at the skies,
And all her silken flanks with garlands drest?
What little town by river or sea shore,
Or mountain-built with peaceful citadel,
Is emptied of this folk, this pious morn?
And, little town, thy streets for evermore
Will silent be; and not a soul to tell
Why thou art desolate, can e'er return.

O Attic shape! Fair attitude! with brede
Of marble men and maidens overwrought,
With forest branches and the trodden weed;
Thou, silent form, dost tease us out of thought
As doth eternity: Cold Pastoral!
When old age shall this generation waste,
Thou shalt remain, in midst of other woe
Than ours, a friend to man, to whom thou say'st,
"Beauty is truth, truth beauty,—that is all
Ye know on earth, and all ye need to know."""

comma = ','
comma_count = ode.count(comma)
print (comma_count)

line = '\n'
line_count = len(ode.splitlines())
print (line_count)

word_count = len(ode.split())
print (word_count)

EVER_ode = ode.replace(' ever ', ' EVER ')
print (EVER_ode)
