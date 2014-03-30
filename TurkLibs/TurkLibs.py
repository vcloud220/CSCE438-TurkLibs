from boto.mturk.connection import MTurkConnection
from boto.mturk.question import QuestionContent,Question,QuestionForm, Overview,AnswerSpecification,SelectionAnswer,FormattedContent,FreeTextAnswer
import time
import string
import re

ACCESS_ID ='<your access ID here>'
SECRET_KEY = '<your secret key here>'
HOST = 'mechanicalturk.amazonaws.com'

#--------------------------------------------------------------#
#------------------------------Hit1---------------------------#
f0 = open("story_beg.txt")
st_in = f0.read()

words = re.findall(r"\<([A-Za-z0-9_-]+)\>", st_in)
print (words)
f0.close()


size = len(words)
print 
print size
for x in range(0, size):
  for y in range(0,2):

    mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                          aws_secret_access_key=SECRET_KEY,
                          host=HOST)
     
    title = 'Give examples of a word type (innapropriate and misspelled submissions will be thrown out!)'
    description = ('Check the box and provide two unique and creative examples'
                   ' based on the word type provided')
    keywords = 'free text, examples, words'
   
    #---------------  BUILD OVERVIEW -------------------

    overview = Overview()
    overview.append_field('Title', 'Provide two unique/creative examples of a(n) ' + words[x])

    

    #---------------  BUILD QUESTION 1 -------------------
    ratings =[(words[x], words[x])]

    qc1 = QuestionContent()
    qc1.append_field('Title','Select Box Below!')
     
    fta1 = SelectionAnswer(min=1, max=1,style='multichooser',
                          selections=ratings,
                          type='text',
                          other=False)
     
    q1 = Question(identifier='design',
                  content=qc1,
                  answer_spec=AnswerSpecification(fta1),
                  is_required=True)



    #---------------  BUILD QUESTION 2 -------------------
     
    qc2 = QuestionContent()
    qc2.append_field('Title','Provide your first example')
     
    fta2 = FreeTextAnswer()
     
    q2 = Question(identifier='example1',
                  content=qc2,
                  answer_spec=AnswerSpecification(fta2),
                  is_required=True)
     
    #---------------  BUILD QUESTION 3 -------------------
     
    qc3 = QuestionContent()
    qc3.append_field('Title','Provide your second example')
     
    fta3 = FreeTextAnswer()
     
    q3 = Question(identifier="example2",
                  content=qc3,
                  answer_spec=AnswerSpecification(fta3))

     
    #--------------- BUILD THE QUESTION FORM -------------------
     
    question_form = QuestionForm()
    question_form.append(overview)
    question_form.append(q1)
    question_form.append(q2)
    question_form.append(q3)
     
    #--------------- CREATE THE HIT -------------------
     
    mtc.create_hit(questions=question_form,
                   max_assignments=1,
                   title=title,
                   description=description,
                   keywords=keywords,
                   duration = 60*1,
                   reward=0.01)



print 'hits1 jobs: success'
time.sleep(2100) #wait an hour before continuing 

#--------------------------------------------------------------#
#-------------------Results from Hit1-------------------------#


#all results from the first hit
val = []

#an array for each blank in the story 
vehicles = []
celebs = []
celebs2 = []
celebs3 = []
celebs4 = []
adverbs = []
verbs = []
pt_verbs = []
objs = []
resids = []
stores = []
sounds = []
body_parts = []
objs2 = []
statements = []
pt_verbs2 = []
animals = []
weapons = []
objs3 = []
body_parts2 = []
movies = []
part_of_body_w_two = []
part_of_body_w_two2 = []
games = []
objs4 = []
celebs5 = []
verbs2 = []
adverbs2 = []
counts = []
adverbs3 = []
objs5 = []
verbs3 = []
statements2 = []
pt_verbs3 = []
adjs = []
objs6 = []
objs7 = []
numbers = []
body_parts3 = []
objs8 = []
ab_nouns = []
verbs_ing = []
animals_plural = []


def get_all_reviewable_hits(mtc):
    page_size = 100
    hits = mtc.get_reviewable_hits(page_size=page_size)
    print "Total results to fetch %s " % hits.TotalNumResults
    print "Request hits page %i" % 1
    total_pages = float(hits.TotalNumResults)/page_size
    int_total= int(total_pages)
    if(total_pages-int_total>0):
        total_pages = int_total+1
    else:
        total_pages = int_total
    pn = 1
    while pn < total_pages:
        pn = pn + 1
        print "Request hits page %i" % pn
        temp_hits = mtc.get_reviewable_hits(page_size=page_size,page_number=pn)
        hits.extend(temp_hits)
    return hits
 
mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                      aws_secret_access_key=SECRET_KEY,
                      host=HOST)
 
hits = get_all_reviewable_hits(mtc)
 
for hit in hits:
    assignments = mtc.get_assignments(hit.HITId)
    for assignment in assignments:
        #print assignment.answers
        #print "Answers of the worker %s" % assignment.WorkerId
        #print assignment.answers[0]
        for question_form_answer in assignment.answers[0]:
            #print question_form_answer.fields
            for value in question_form_answer.fields:
                val.append(value)
                #print value
                #print "%s: %s" % (key,value)
        #print "--------------------"
print 
print 


size = len(val)
for x in range(0,size):
    if val[x] == 'vehicle':
        if val[x+1] != 'vehicle':
            vehicles.append(val[x+1])
        if val[x+1] != 'vehicle':
            vehicles.append(val[x+2])
    if val[x] == 'celebrity':
        if len(celebs) <4:
            celebs.append(val[x+1])
            celebs.append(val[x+2])
            continue
    if val[x] == 'celebrity':
        if len(celebs2) <4:
            celebs2.append(val[x+1])
            celebs2.append(val[x+2])
            continue
    if val[x] == 'celebrity':
        if len(celebs3) <4:
            celebs3.append(val[x+1])
            celebs3.append(val[x+2])
            continue
    if val[x] == 'celebrity':
        if len(celebs4) <4:
            celebs4.append(val[x+1])
            celebs4.append(val[x+2])
            continue
    if val[x] == 'celebrity':
        if len(celebs5) < 4:
            celebs5.append(val[x+1])
            celebs5.append(val[x+2])
            continue
    if val[x] == 'adverb':
        if len(adverbs) < 4:
            adverbs.append(val[x+1])
            adverbs.append(val[x+2])
            continue
    if val[x] == 'adverb':
        if len(adverbs2) < 4:
            adverbs2.append(val[x+1])
            adverbs2.append(val[x+2])
            continue
    if val[x] == 'adverb':
        if len(adverbs3) < 4:
            adverbs3.append(val[x+1])
            adverbs3.append(val[x+2])
            continue
    if val[x] == 'verb':
        if len(verbs) < 4:
            verbs.append(val[x+1])
            verbs.append(val[x+2])
            continue
    if val[x] == 'verb':
        if len(verbs2) < 4:
            verbs2.append(val[x+1])
            verbs2.append(val[x+2])
            continue
    if val[x] == 'verb':
        if len(verbs3) < 4:
            verbs3.append(val[x+1])
            verbs3.append(val[x+2])
            continue
    if val[x] == 'past-tense-verb':
        if len(pt_verbs) < 4:
            pt_verbs.append(val[x+1])
            pt_verbs.append(val[x+2])
            continue
    if val[x] == 'past-tense-verb':
        if len(pt_verbs2) < 4:
            pt_verbs2.append(val[x+1])
            pt_verbs2.append(val[x+2])
            continue
    if val[x] == 'past-tense-verb':
        if len(pt_verbs3) < 4:
            pt_verbs3.append(val[x+1])
            pt_verbs3.append(val[x+2])
            continue
    if val[x] == 'object':
        if len(objs) < 4:
            objs.append(val[x+1])
            objs.append(val[x+2])
            continue
    if val[x] == 'object':
        if len(objs2) < 4:
            objs2.append(val[x+1])
            objs2.append(val[x+2])
            continue
    if val[x] == 'object':
        if len(objs3) < 4:
            objs3.append(val[x+1])
            objs3.append(val[x+2])
            continue
    if val[x] == 'object':
        if len(objs4) < 4:
            objs4.append(val[x+1])
            objs4.append(val[x+2])
            continue
    if val[x] == 'object':
        if len(objs5) < 4:
            objs5.append(val[x+1])
            objs5.append(val[x+2])
            continue
    if val[x] == 'object':
        if len(objs6) < 4:
            objs6.append(val[x+1])
            objs6.append(val[x+2])
            continue
    if val[x] == 'object':
        if len(objs7) < 4:
            objs7.append(val[x+1])
            objs7.append(val[x+2])
            continue
    if val[x] == 'object':
        if len(objs8) < 4:
            objs8.append(val[x+1])
            objs8.append(val[x+2])
            continue
    if val[x] == 'type-of-residence':
        resids.append(val[x+1])
        resids.append(val[x+2])
    if val[x] == 'store-name':
        stores.append(val[x+1])
        stores.append(val[x+2])
    if val[x] == 'sound':
        sounds.append(val[x+1])
        sounds.append(val[x+2])
    if val[x] == 'body-part':
        if len(body_parts) < 4:
            body_parts.append(val[x+1])
            body_parts.append(val[x+2])
            continue
    if val[x] == 'body-part':
        if len(body_parts2) < 4:
            body_parts2.append(val[x+1])
            body_parts2.append(val[x+2])
            continue
    if val[x] == 'body-part':
        if len(body_parts3) < 4:
            body_parts3.append(val[x+1])
            body_parts3.append(val[x+2])
    if val[x] == 'statement':
        if len(statements) < 4:
            statements.append(val[x+1])
            statements.append(val[x+2])
            continue
    if val[x] == 'statement':
        if len(statements2) < 4:
            statements2.append(val[x+1])
            statements2.append(val[x+2])
            continue
    if val[x] == 'animal':
        animals.append(val[x+1])
        animals.append(val[x+2])
    if val[x] == 'melee-weapon':
        weapons.append(val[x+1])
        weapons.append(val[x+2])
    if val[x] == 'movie-title':
        movies.append(val[x+1])
        movies.append(val[x+2])
    if val[x] == 'part-of-the-body-that-there-is-two-of':
        if len(part_of_body_w_two) < 4:
            part_of_body_w_two.append(val[x+1])
            part_of_body_w_two.append(val[x+2])
            continue
    if val[x] == 'part-of-the-body-that-there-is-two-of':
        if len(part_of_body_w_two2) < 4:
            part_of_body_w_two2.append(val[x+1])
            part_of_body_w_two2.append(val[x+2])
            continue
    if val[x] == 'board-game':
        games.append(val[x+1])
        games.append(val[x+2])
    if val[x] == 'something-you-count':
        counts.append(val[x+1])
        counts.append(val[x+2])
    if val[x] == 'adjective':
        adjs.append(val[x+1])
        adjs.append(val[x+2])
    if val[x] == 'a-number-between-2-100':
        numbers.append(val[x+1])
        numbers.append(val[x+2])
    if val[x] == 'abstract-noun':
        ab_nouns.append(val[x+1])
        ab_nouns.append(val[x+2])
    if val[x] == 'verb-ending-with-ing':
        verbs_ing.append(val[x+1])
        verbs_ing.append(val[x+2])
    if val[x] == 'animal-plural':
        animals_plural.append(val[x+1])
        animals_plural.append(val[x+2])





size = len(vehicles)       
print 'vehicle:'
for x in range(0,size):
    print vehicles[x]
    
print

size = len(celebs)       
print 'celebrity:'
for x in range(0,size):
    print celebs[x]
    
print

size = len(celebs2)       
print 'celebrity 2:'
for x in range(0,size):
    print celebs2[x]
    
print

size = len(celebs3)       
print 'celebrity 3:'
for x in range(0,size):
    print celebs3[x]
    
print

size = len(celebs4)       
print 'celebrity 4:'
for x in range(0,size):
    print celebs4[x]
    
print

size = len(celebs5)       
print 'celebrity 5:'
for x in range(0,size):
    print celebs5[x]
    
print

size = len(adverbs)       
print 'adverbs:'
for x in range(0,size):
    print adverbs[x]
    
print

size = len(adverbs2)       
print 'adverbs 2:'
for x in range(0,size):
    print adverbs2[x]
    
print

size = len(adverbs3)       
print 'adverb 3:'
for x in range(0,size):
    print adverbs3[x]
    
print

size = len(verbs)       
print 'verbs:'
for x in range(0,size):
    print verbs[x]
    
print

size = len(verbs2)       
print 'verbs 2:'
for x in range(0,size):
    print pt_verbs2[x]
    
print

size = len(verbs3)       
print 'verbs 3:'
for x in range(0,size):
    print verbs3[x]
    
print

size = len(pt_verbs)       
print 'past-tense verbs:'
for x in range(0,size):
    print pt_verbs[x]
    
print

size = len(pt_verbs2)       
print 'past-tense verbs 2:'
for x in range(0,size):
    print pt_verbs2[x]
    
print

size = len(pt_verbs3)       
print 'past-tense verbs 3:'
for x in range(0,size):
    print pt_verbs3[x]
    
print

size = len(objs)       
print 'objects:'
for x in range(0,size):
    print objs[x]
    
print

size = len(objs2)       
print 'objects 2:'
for x in range(0,size):
    print objs2[x]
    
print

size = len(objs3)       
print 'objects 3:'
for x in range(0,size):
    print objs3[x]
    
print

size = len(objs4)       
print 'objects 4:'
for x in range(0,size):
    print objs4[x]
    
print

size = len(objs5)       
print 'objects 5:'
for x in range(0,size):
    print objs5[x]
    
print

size = len(objs6)       
print 'objects 6:'
for x in range(0,size):
    print objs6[x]
    
print

size = len(objs7)       
print 'objects 7:'
for x in range(0,size):
    print objs7[x]
    
print

size = len(objs8)       
print 'objects 8:'
for x in range(0,size):
    print objs8[x]
    
print

size = len(resids)       
print 'type of residence:'
for x in range(0,size):
    print resids[x]
    
print

size = len(stores)       
print 'store names:'
for x in range(0,size):
    print stores[x]
    
print

size = len(sounds)       
print 'sounds:'
for x in range(0,size):
    print sounds[x]
    
print

size = len(body_parts)       
print 'body parts:'
for x in range(0,size):
    print body_parts[x]
    
print

size = len(body_parts2)       
print 'body parts 2:'
for x in range(0,size):
    print body_parts2[x]
    
print

size = len(body_parts3)       
print 'body parts 3:'
for x in range(0,size):
    print body_parts3[x]
    
print

size = len(statements)       
print 'statements:'
for x in range(0,size):
    print statements[x]
    
print

size = len(statements2)       
print 'statements 2:'
for x in range(0,size):
    print statements2[x]
    
print

size = len(animals)       
print 'animals:'
for x in range(0,size):
    print animals[x]
    
print

size = len(weapons)       
print 'melee weapons:'
for x in range(0,size):
    print weapons[x]
    
print

size = len(movies)       
print 'movie titles:'
for x in range(0,size):
    print movies[x]
    
print

size = len(part_of_body_w_two)       
print 'part of the body that there is two of:'
for x in range(0,size):
    print part_of_body_w_two[x]
    
print

size = len(part_of_body_w_two2)       
print 'part of the body that there is two of 2:'
for x in range(0,size):
    print part_of_body_w_two2[x]
    
print

size = len(games)       
print 'board games:'
for x in range(0,size):
    print games[x]
    
print

size = len(counts)       
print 'something you count:'
for x in range(0,size):
    print counts[x]
    
print

size = len(adjs)       
print 'adjectives:'
for x in range(0,size):
    print adjs[x]
    
print

size = len(numbers)       
print 'a number between 2-100:'
for x in range(0,size):
    print numbers[x]
    
print

size = len(ab_nouns)       
print 'abstract nouns:'
for x in range(0,size):
    print ab_nouns[x]
    
print

size = len(verbs_ing)       
print 'verbs ending with ing:'
for x in range(0,size):
    print verbs_ing[x]
    
print

size = len(animals_plural)       
print 'animals (plural):'
for x in range(0,size):
    print animals_plural[x]
    
print
print
print 
print

for hit in hits:
    mtc.disable_hit(hit.HITId)
print 'cleared hits'
#test = get_all_reviewable_hits(mtc)

print 'hits1 results: success'
time.sleep(300) #wait ten minutes

#--------------------------------------------------------------#
#------------------------------Hit2-------------------------#


celebs_used = False
celebs2_used = False
celebs3_used = False
celebs4_used = False
celebs5_used = False

objs_used = False
objs2_used = False
objs3_used = False
objs4_used = False
objs5_used = False
objs6_used = False
objs7_used = False
objs8_used = False

pt_verbs_used = False
pt_verbs2_used = False
pt_verbs3_used = False

body_parts_used = False
body_parts2_used = False
body_parts3_used = False

part_of_the_body_w_two_used = False
part_of_the_body_w_two2_used = False

verbs_used = False
verbs2_used = False
verbs3_used = False

adverbs_used = False
adverbs2_used = False
adverbs3_used = False


statements_used = False
statements2_used = False



def rates(args):
    sizes = len(args)
    for x in range(0,sizes):
        ratings2.append((args[x], args[x]))


for x in range(0, 43):
  ratings2 = []


  while True:
      if words[x] == 'vehicle':
        rates(vehicles)
        break
      if words[x] == 'celebrity' and celebs_used == False:
        celebs_used = True
        rates(celebs)
        break
      if words[x] == 'celebrity' and celebs2_used == False:
        celebs2_used = True
        rates(celebs2)
        break
      if words[x] == 'celebrity' and celebs3_used == False:
        celebs3_used = True
        rates(celebs3)
        break
      if words[x] == 'celebrity' and celebs4_used == False:
        celebs4_used = True
        rates(celebs4)
        break
      if words[x] == 'celebrity' and celebs5_used == False:
        celebs5_used = True
        rates(celebs5)
        break
      if words[x] == 'adverb' and adverbs_used == False:
        adverbs_used = True
        rates(adverbs)
        break
      if words[x] == 'adverb' and adverbs2_used == False:
        adverbs2_used = True
        rates(adverbs2)
        break
      if words[x] == 'adverb' and adverbs3_used == False:
        adverbs3_used = True
        rates(adverbs3)
        break
      if words[x] == 'verb' and verbs_used == False:
        verbs_used = True
        rates(verbs)
        break
      if words[x] == 'verb' and verbs2_used == False:
        verbs2_used = True
        rates(verbs2)
        break
      if words[x] == 'verb' and verbs3_used == False:
        verbs3_used = True
        rates(verbs3)
        break
      if words[x] == 'past-tense-verb' and pt_verbs_used == False:
        pt_verbs_used = True
        rates(pt_verbs)
        break
      if words[x] == 'past-tense-verb' and pt_verbs2_used == False:
        pt_verbs2_used = True
        rates(pt_verbs2)
        break
      if words[x] == 'past-tense-verb' and pt_verbs3_used == False:
        pt_verbs3_used = True
        rates(pt_verbs3)
        break
      if words[x] == 'object' and objs_used == False:
        objs_used = True
        rates(objs)
        break
      if words[x] == 'object' and objs2_used == False:
        objs2_used = True
        rates(objs2)
        break
      if words[x] == 'object' and objs3_used == False:
        objs3_used = True
        rates(objs3)
        break
      if words[x] == 'object' and objs4_used == False:
        objs4_used = True
        rates(objs4)
        break
      if words[x] == 'object' and objs5_used == False:
        objs5_used = True
        rates(objs5)
        break
      if words[x] == 'object' and objs6_used == False:
        objs6_used = True
        rates(objs6)
        break
      if words[x] == 'object' and objs7_used == False:
        objs7_used = True
        rates(objs7)
        break
      if words[x] == 'object' and objs8_used == False:
        objs8_used = True
        rates(objs8)
        break
      if words[x] == 'type-of-residence':
        rates(resids)
        break
      if words[x] == 'store-name':
        rates(stores)
        break
      if words[x] == 'sound':
        rates(sounds)
        break
      if words[x] == 'body-part' and body_parts_used == False:
        body_parts_used = True
        rates(body_parts)
        break
      if words[x] == 'body-part' and body_parts2_used == False:
        body_parts2_used = True
        rates(body_parts2)
        break
      if words[x] == 'body-part' and body_parts3_used == False:
        body_parts3_used = True
        rates(body_parts3)
        break
      if words[x] == 'statement' and statements_used == False:
        statements_used = True
        rates(statements)
        break
      if words[x] == 'statement' and statements2_used == False:
        statements2_used = True
        rates(statements2)
        break
      if words[x] == 'animal':
        rates(animals)
        break
      if words[x] == 'melee-weapon':
        rates(weapons)
        break
      if words[x] == 'movie-title':
        rates(movies)
        break
      if words[x] == 'part-of-the-body-that-there-is-two-of' and part_of_the_body_w_two_used == False:
        part_of_body_w_two_used = True
        rates(part_of_body_w_two)
        break
      if words[x] == 'part-of-the-body-that-there-is-two-of' and part_of_the_body_w_two2_used == False:
        part_of_body_w_two2_used = True
        rates(part_of_body_w_two2)
        break
      if words[x] == 'board-game':
        rates(games)
        break
      if words[x] == 'something-you-count':
        rates(counts)
        break
      if words[x] == 'adjective':
        rates(adjs)
        break
      if words[x] == 'a-number-between-2-100':
        rates(numbers)
        break
      if words[x] == 'abstract-noun':
        rates(ab_nouns)
        break
      if words[x] == 'verb-ending-with-ing':
        rates(verbs_ing)
        break
      if words[x] == 'animal-plural':
        rates(animals_plural)
        break


  for y in range(0, 5):
 
    mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                          aws_secret_access_key=SECRET_KEY,
                          host=HOST)
     
    title = 'Select your favorite word in the set'
    description = ('Check the box below indicaing the part of speech and then choose'
                   ' your favorite word in the set of words based on creativity and correctness.')
    keywords = 'words, multichooser'
     
    
     
    #---------------  BUILD OVERVIEW -------------------
     
    overview = Overview()
    overview.append_field('Title', ' Check the box below indicating the category and Based on creativity and correctness choose your favorite ' + words[x])

     
    #---------------  BUILD QUESTION 1 -------------------

    ratings =[(words[x], words[x])]

    qc1 = QuestionContent()
    qc1.append_field('Title','Select Box Below!')
         
    fta1 = SelectionAnswer(min=1, max=1,style='multichooser',
                              selections=ratings,
                              type='text',
                              other=False)
         
    q1 = Question(identifier='design',
                      content=qc1,
                      answer_spec=AnswerSpecification(fta1),
                      is_required=True)

    #---------------  BUILD QUESTION 2 -------------------
    
    

    qc2 = QuestionContent()
    qc2.append_field('Title','Select your favorite in the set:')
     
    fta2 = SelectionAnswer(min=1, max=1,style='multichooser',
                          selections=ratings2,
                          type='text',
                          other=False)
     
    q2 = Question(identifier='design',
                  content=qc2,
                  answer_spec=AnswerSpecification(fta2),
                  is_required=True)
     


     
    #--------------- BUILD THE QUESTION FORM -------------------
     
    question_form = QuestionForm()
    question_form.append(overview)
    question_form.append(q1)
    question_form.append(q2)

     
    #--------------- CREATE THE HIT -------------------
     
    mtc.create_hit(questions=question_form,
                   max_assignments=1,
                   title=title,
                   description=description,
                   keywords=keywords,
                   duration = 60*1,
                   reward=0.01)



print 'hits2 jobs: success'

time.sleep(2100) #wait an hour


#--------------------------------------------------------------#
#-------------------Results from Hit2-------------------------#

def highest(args):
  size = len(args)
  highest = 0
  winner = 0
  
  for x in range(0,size):
    current = 0
    for y in range(0,size):
      if args[x] == args[y]:
        current = current + 1
      if current > highest:
        highest = current
        winner = x
  return args[winner]



val2 = []
final = []

vehicles_2 = []
celebs_2 = []
celebs2_2 = []
celebs3_2 = []
celebs4_2 = []
adverbs_2 = []
verbs_2 = []
pt_verbs_2 = []
objs_2 = []
resids_2 = []
stores_2 = []
sounds_2 = []
body_parts_2 = []
objs2_2 = []
statements_2 = []
pt_verbs2_2 = []
animals_2 = []
weapons_2 = []
objs3_2 = []
body_parts2_2 = []
movies_2 = []
part_of_body_w_two_2 = []
part_of_body_w_two2_2 = []
games_2 = []
objs4_2 = []
celebs5_2 = []
verbs2_2 = []
adverbs2_2 = []
counts_2 = []
adverbs3_2 = []
objs5_2 = []
verbs3_2 = []
statements2_2 = []
pt_verbs3_2 = []
adjs_2 = []
objs6_2 = []
objs7_2 = []
numbers_2 = []
body_parts3_2 = []
objs8_2 = []
ab_nouns_2 = []
verbs_ing_2 = []
animals_plural_2 = []


mtc = MTurkConnection(aws_access_key_id=ACCESS_ID,
                      aws_secret_access_key=SECRET_KEY,
                      host=HOST)

hits = get_all_reviewable_hits(mtc)

for hit in hits:
    assignments = mtc.get_assignments(hit.HITId)
    for assignment in assignments:
        #print assignment.answers
        #print "Answers of the worker %s" % assignment.WorkerId
        #print assignment.answers[0]
        for question_form_answer in assignment.answers[0]:
            #print question_form_answer.fields
            for value in question_form_answer.fields:
                val2.append(value)
                #print value
                #print "%s: %s" % (key,value)
        #print "--------------------"
print 
print


size = len(val2)
for x in range(0,size):
    if val2[x] == 'vehicle':
        vehicles_2.append(val2[x+1])
    if val2[x] == 'celebrity':
        if len(celebs_2) <5:
            celebs_2.append(val2[x+1])
            continue
    if val2[x] == 'celebrity':
        if len(celebs2_2) <5:
            celebs2_2.append(val2[x+1])
            continue
    if val2[x] == 'celebrity':
        if len(celebs3_2) <5:
            celebs3_2.append(val2[x+1])
            continue
    if val2[x] == 'celebrity':
        if len(celebs4_2) <5:
            celebs4_2.append(val2[x+1])
            continue
    if val2[x] == 'celebrity':
        if len(celebs5_2) < 5:
            celebs5_2.append(val2[x+1])
            continue
    if val2[x] == 'adverb':
        if len(adverbs_2) < 5:
            adverbs_2.append(val2[x+1])
            continue
    if val2[x] == 'adverb':
        if len(adverbs2_2) < 5:
            adverbs2_2.append(val2[x+1])
            continue
    if val2[x] == 'adverb':
        if len(adverbs3_2) < 5:
            adverbs3_2.append(val2[x+1])
            continue
    if val2[x] == 'verb':
        if len(verbs_2) < 5:
            verbs_2.append(val2[x+1])
            continue
    if val2[x] == 'verb':
        if len(verbs2_2) < 5:
            verbs2_2.append(val2[x+1])
            continue
    if val2[x] == 'verb':
        if len(verbs3_2) < 5:
            verbs3_2.append(val2[x+1])
            continue
    if val2[x] == 'past-tense-verb':
        if len(pt_verbs_2) < 5:
            pt_verbs_2.append(val2[x+1])
            continue
    if val2[x] == 'past-tense-verb':
        if len(pt_verbs2_2) < 5:
            pt_verbs2_2.append(val2[x+1])
            continue
    if val2[x] == 'past-tense-verb':
        if len(pt_verbs3_2) < 5:
            pt_verbs3_2.append(val2[x+1])
            continue
    if val2[x] == 'object':
        if len(objs_2) < 5:
            objs_2.append(val2[x+1])
            continue
    if val2[x] == 'object':
        if len(objs2_2) < 5:
            objs2_2.append(val2[x+1])
            continue
    if val2[x] == 'object':
        if len(objs3_2) < 5:
            objs3_2.append(val2[x+1])
            continue
    if val2[x] == 'object':
        if len(objs4_2) < 5:
            objs4_2.append(val2[x+1])
            continue
    if val2[x] == 'object':
        if len(objs5_2) < 5:
            objs5_2.append(val2[x+1])
            continue
    if val2[x] == 'object':
        if len(objs6_2) < 5:
            objs6_2.append(val2[x+1])
            continue
    if val2[x] == 'object':
        if len(objs7_2) < 5:
            objs7_2.append(val2[x+1])
            continue
    if val2[x] == 'object':
        if len(objs8_2) < 5:
            objs8_2.append(val2[x+1])
            continue
    if val2[x] == 'type-of-residence':
        resids_2.append(val2[x+1])
    if val2[x] == 'store-name':
        stores_2.append(val2[x+1])
    if val2[x] == 'sound':
        sounds_2.append(val2[x+1])
    if val2[x] == 'body-part':
        if len(body_parts_2) < 5:
            body_parts_2.append(val2[x+1])
            continue
    if val2[x] == 'body-part':
        if len(body_parts2_2) < 5:
            body_parts2_2.append(val2[x+1])
            continue
    if val2[x] == 'body-part':
        if len(body_parts3_2) < 5:
            body_parts3_2.append(val2[x+1])
    if val2[x] == 'statement':
        if len(statements_2) < 5:
            statements_2.append(val2[x+1])
            continue
    if val2[x] == 'statement':
        if len(statements2_2) < 5:
            statements2_2.append(val2[x+1])
            continue
    if val2[x] == 'animal':
        animals_2.append(val2[x+1])
    if val2[x] == 'melee-weapon':
        weapons_2.append(val2[x+1])
    if val2[x] == 'movie-title':
        movies_2.append(val2[x+1])
    if val2[x] == 'part-of-the-body-that-there-is-two-of':
        if len(part_of_body_w_two_2) < 5:
            part_of_body_w_two_2.append(val2[x+1])
            continue
    if val2[x] == 'part-of-the-body-that-there-is-two-of':
        if len(part_of_body_w_two2_2) < 5:
            part_of_body_w_two2_2.append(val2[x+1])
            continue
    if val2[x] == 'board-game':
        games_2.append(val2[x+1])
    if val2[x] == 'something-you-count':
        counts_2.append(val2[x+1])
    if val2[x] == 'adjective':
        adjs_2.append(val2[x+1])
    if val2[x] == 'a-number-between-2-100':
        numbers_2.append(val2[x+1])
    if val2[x] == 'abstract-noun':
        ab_nouns_2.append(val2[x+1])
    if val2[x] == 'verb-ending-with-ing':
        verbs_ing_2.append(val2[x+1])
    if val2[x] == 'animal-plural':
        animals_plural_2.append(val2[x+1])

print 'hits2 results: success'
time.sleep(300)

final.append('vehicle')
final.append(highest(vehicles_2))
final.append('celeb1')
final.append(highest(celebs_2))
final.append('celeb2')
final.append(highest(celebs2_2))
final.append('celeb3')
final.append(highest(celebs3_2))
final.append('celeb4')
final.append(highest(celebs4_2))
final.append('celeb5')
final.append(highest(celebs5_2))
final.append('adverb1')
final.append(highest(adverbs_2))
final.append('adverb2')
final.append(highest(adverbs2_2))
final.append('adverb3')
final.append(highest(adverbs3_2))
final.append('verb1')
final.append(highest(verbs_2))
final.append('verb2')
final.append(highest(verbs2_2))
final.append('verb3')
final.append(highest(verbs3_2))
final.append('past_tense_verb1')
final.append(highest(pt_verbs_2))
final.append('past_tense_verb2')
final.append(highest(pt_verbs2_2))
final.append('past_tense_verb3')
final.append(highest(pt_verbs3_2))
final.append('obj1')
final.append(highest(objs_2))
final.append('obj2')
final.append(highest(objs2_2))
final.append('obj3')
final.append(highest(objs3_2))
final.append('obj4')
final.append(highest(objs4_2))
final.append('obj5')
final.append(highest(objs5_2))
final.append('obj6')
final.append(highest(objs6_2))
final.append('obj7')
final.append(highest(objs7_2))
final.append('obj8')
final.append(highest(objs8_2))
final.append('type_of_residence')
final.append(highest(resids_2))
final.append('store_name')
final.append(highest(stores_2))
final.append('sound')
final.append(highest(sounds_2))
final.append('body_part1')
final.append(highest(body_parts_2))
final.append('body_part2')
final.append(highest(body_parts2_2))
final.append('body_part3')
final.append(highest(body_parts3_2))
final.append('statement1')
final.append(highest(statements_2))
final.append('statement2')
final.append(highest(statements2_2))
final.append('animal1')
final.append(highest(animals_2))
final.append('melee_weapon')
final.append(highest(weapons_2))
final.append('movie_title')
final.append(highest(movies_2))
final.append('body_part_pair1')
final.append(highest(part_of_body_w_two_2))
final.append('body_part_pair2')
final.append(highest(part_of_body_w_two2_2))
final.append('board_game')
final.append(highest(games_2))
final.append('countable')
final.append(highest(counts_2))
final.append('adjective')
final.append(highest(adjs_2))
final.append('number')
final.append(highest(numbers_2))
final.append('abstract_noun')
final.append(highest(ab_nouns_2))
final.append('verb_ending_in_ing')
final.append(highest(verbs_ing_2))
final.append('animal_plural')
final.append(highest(animals_plural_2))


#-----Read and display original story with blanks------------

f1 = open("story_end.txt", "r")
f2 = open("final2.txt", "wb+")
end_read = f1.read()
print "Original: ", end_read
print
print
print(final)
print

final_story = end_read.split()

for x in range (0,len(final_story)):
    for i in range(0, 86):
        if final_story[x] == "<vehicle>":
            if final[i] == "vehicle":
                final_story[x] = final[i+1]
        if final_story[x] == "<celeb1>":
            if final[i] == "celeb1":
                final_story[x] = final[i+1]
        if final_story[x] == "<celeb2>":
            if final[i] == "celeb2":
                final_story[x] = final[i+1]
        if final_story[x] == "<celeb3>":
            if final[i] == "celeb3":
                final_story[x] = final[i+1]
        if final_story[x] == "<celeb4>":
            if final[i] == "celeb4":
                final_story[x] = final[i+1]
        if final_story[x] == "<celeb5>":
            if final[i] == "celeb5":
                final_story[x] = final[i+1]
        if final_story[x] == "<adverb1>":
            if final[i] == "adverb1":
                final_story[x] = final[i+1]
        if final_story[x] == "<adverb2>":
            if final[i] == "adverb2":
                final_story[x] = final[i+1]
        if final_story[x] == "<adverb3>":
            if final[i] == "adverb3":
                final_story[x] = final[i+1]
        if final_story[x] == "<obj1>":
            if final[i] == "obj1":
                final_story[x] = final[i+1]
        if final_story[x] == "<obj2>":
            if final[i] == "obj2":
                final_story[x] = final[i+1]
        if final_story[x] == "<obj3>":
            if final[i] == "obj3":
                final_story[x] = final[i+1]
        if final_story[x] == "<obj4>":
            if final[i] == "obj4":
                final_story[x] = final[i+1]
        if final_story[x] == "<obj5>":
            if final[i] == "obj5":
                final_story[x] = final[i+1]
        if final_story[x] == "<obj6>":
            if final[i] == "obj6":
                final_story[x] = final[i+1]
        if final_story[x] == "<obj7>":
            if final[i] == "obj7":
                final_story[x] = final[i+1]
        if final_story[x] == "<obj8>":
            if final[i] == "obj8":
                final_story[x] = final[i+1]
        if final_story[x] == "<past_tense_verb1>":
            if final[i] == "past_tense_verb1":
                final_story[x] = final[i+1]
        if final_story[x] == "<past_tense_verb2>":
            if final[i] == "past_tense_verb2":
                final_story[x] = final[i+1]
        if final_story[x] == "<past_tense_verb3>":
            if final[i] == "past_tense_verb3":
                final_story[x] = final[i+1]
        if final_story[x] == "<animal1>":
            if final[i] == "animal1":
                final_story[x] = final[i+1]
        if final_story[x] == "<animal_plural>":
            if final[i] == "animal_plural":
                final_story[x] = final[i+1]
        if final_story[x] == "<verb_ending_in_ing>":
            if final[i] == "verb_ending_in_ing":
                final_story[x] = final[i+1]
        if final_story[x] == "<statement1>":
            if final[i] == "statement1":
                final_story[x] = final[i+1]
        if final_story[x] == "<statement2>":
            if final[i] == "statement2":
                final_story[x] = final[i+1]
        if final_story[x] == "<melee_weapon>":
            if final[i] == "melee_weapon":
                final_story[x] = final[i+1]
        if final_story[x] == "<adjective>":
            if final[i] == "adjective":
                final_story[x] = final[i+1]
        if final_story[x] == "<store_name>":
            if final[i] == "store_name":
                final_story[x] = final[i+1]
        if final_story[x] == "<sound>":
            if final[i] == "sound":
                final_story[x] = final[i+1]
        if final_story[x] == "<body_part1>":
            if final[i] == "body_part1":
                final_story[x] = final[i+1]
        if final_story[x] == "<body_part2>":
            if final[i] == "body_part2":
                final_story[x] = final[i+1]
        if final_story[x] == "<body_part3>":
            if final[i] == "body_part3":
                final_story[x] = final[i+1]
        if final_story[x] == "<movie_title>":
            if final[i] == "movie_title":
                final_story[x] = final[i+1]
        if final_story[x] == "<abstract_noun>":
            if final[i] == "abstract_noun":
                final_story[x] = final[i+1]
        if final_story[x] == "<number>":
            if final[i] == "number":
                final_story[x] = final[i+1] 
        if final_story[x] == "<countable>":
            if final[i] == "countable":
                final_story[x] = final[i+1]
        if final_story[x] == "<board_game>":
            if final[i] == "board_game":
                final_story[x] = final[i+1]
        if final_story[x] == "<body_part_pair1>":
            if final[i] == "body_part_pair1":
                final_story[x] = final[i+1]
        if final_story[x] == "<body_part_pair2>":
            if final[i] == "body_part_pair2":
                final_story[x] = final[i+1]
        if final_story[x] == "<type_of_residence>":
            if final[i] == "type_of_residence":
                final_story[x] = final[i+1]
        if final_story[x] == "<verb1>":
            if final[i] == "verb1":
                final_story[x] = final[i+1]
        if final_story[x] == "<verb2>":
            if final[i] == "verb2":
                final_story[x] = final[i+1]
        if final_story[x] == "<verb3>":
            if final[i] == "verb3":
                final_story[x] = final[i+1]
        
        
for x in range(0,len(final_story)):
    if final_story[x] == ".":
        f2.write(final_story[x])
        f2.write(" ")
    elif final_story[x] == ",":
        f2.write(final_story[x])
        f2.write(" ")
    elif final_story[x] == "!":
        f2.write(final_story[x])
        f2.write(" ")
    elif final_story[x] == "?":
        f2.write(final_story[x])
        f2.write(" ")
    elif final_story[x] == ":":
        f2.write(final_story[x])
        f2.write(" ")
    elif final_story[x] == '""':
        f2.write(final_story[x])
        f2.write(" ")   
    elif final_story[x] == "(s)":
        f2.write("s")
        f2.write(" ")
    else:
        f2.write(" ")
        f2.write(final_story[x])
        
f2.seek(0)
print f2.read()

f1.close()
f2.close()      

