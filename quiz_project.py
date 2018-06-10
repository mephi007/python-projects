import random

#storing the data in dictionary with key as state and value as capital

capital = { 'Andhra_pradesh' : 'Hyderabad',
			'Arunachal_pradesh' : 'Itanagar',
			'Assam' : 'Dispur',
			'Bihar' : 'Patna', 
			'Chhattisgarh' : 'Raipur',
			'Goa' : 'Panaji' , 
			'Gujarat' : 'Gandhinagar',
			'Haryana' : 'Chandigarh',
			'Himachal_pradesh' : 'Shimla',
			'Jammu_kashmir' : 'Srinagar',
			'Jharkhand' : 'Ranchi' ,
			'Karnatka' : 'Bangalore' , 
			'Kerala' : 'Thiruvananthapuram' ,
			'Madhya_pradesh' : 'Bhopal',
			'Maharastra' : 'Mumbai' ,
			'Manipur' : 'Imphal' ,
			'Meghalaya' : 'Shillong' , 
			'Mizoram' : 'Aizawl' , 
			'Odisha' : 'Bhubaneshwar',
			'Punjab' : 'Chandigarh',
			'Sikkim' : 'Gangtok',
			'Tamil_nadu' : 'Chennai',
			'Telangana' : 'Hyderabad',
			'Tripura' : 'Agartala',
			'Uttarakhand' : 'Dehradun',
			'Uttar_pradesh' : 'Lucknow',
			'West_bengal' : 'Kolkata',
			}

#Create the quiz and answe key files

for quiznum in range(35):
	# creating the quiz and answer files.
	quizfile = open ('capitalsquiz%s,txt'%(quiznum+1), 'w')
	answerfile = open ('capitalsquiz_answers%s.txt' %(quiznum+1), 'w')
	
#Writing the header for the quiz.
	quizfile.write (' Name:\n\n Date:\n\n Period:\n\n')
	quizfile.write((' '*20)+ 'State Capitals Quiz (form %s)' %(quiznum+1))
	quizfile.write('\n\n')


	#shuffle the order of the states.
	states = list(capital.keys())
	random.shuffle(states)

# for questionnumberber in range (29):
# 	correctAnswer = capital[states[questionnumberber] ]
# 	#deleting 3 correct answers and adding 3 random wrong answers
# 	wrongAnswers = list(capital.values())
# 	del wrongAnswers[wrongAnswers.index(correctAnswer)]
# 	wrongAnswers = random.sample(wrongAnswers,3)
# 	answeroptions = wrongAnswers + [ correctAnswer]  #set of 4 options with 3 wrong options and 1 correct answer
# 	random.shuffle(answeroptions)


	for questionnumber in range(29):

# Get right and wrong answers.
		correctAnswer = capital[states[questionnumber]]
		wrongAnswers = list(capital.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)













#write the question and the answer options to the quiz file
		quizfile.write ('%s. Whats is the capital of %s?\n'  %(questionnumber+1 , states[questionnumber]))


#writing options
		for i in range(4):
			quizfile.write('	%s. %s\n' %('ABCD'[i], answerOptions[i]))
		quizfile.write('\n')

	#writing the answer key to a file

		answerfile.write('%s.%s\n' %(questionnumber+1, 'ABCD'[answerOptions.index(correctAnswer)]))
quizfile.close()
answerfile.close()