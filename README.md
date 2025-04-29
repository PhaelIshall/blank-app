# AI Outreach 

- This is a playground for students to experiments with some AI tools and also discuss the drawbacks and suggest how to make them better.

## Please note
- If the Chatbot is not working / there is an error or there is no response for longer than 10 seconds, refresh the page
- Before the beginning of the workshop, go to [Firebase](https://console.firebase.google.com/), click on the project titled "Outreach" then on the left side menu, click on Build -> Firebase Datastore, this is where all the answers for the question in the home page are, as well as the answers for the demographic survey in the AI predictor section.
- In the Firebase Datastore, delete "question1" and "question2" and then re-create them by clicking on "start collection" -> Collection ID: question1 -> Next then Document ID (click on Auto ID) and save. Then, click on the collection that you created "question1", you will see a new document in the middle of the table, click on the three dots next to it then delete it. Repeat this for question2.

## AI Predictor
#### Live Demo: 
This section has a portion where the students have their photo taken and get to see the AI prediction for their age and gender. They also get to see the probabilities that the model outputs for each prediction. The students are asked to take the photos with different facial expressions, rotating their heads in different directions so that they can notice that the output changes. They can also try it in a situation with lower lighting etc. 
#### Demographic Comparison: 
The AI predictor has been ran on thousands of individuals with different backgrounds on the Fairface dataset. This allowed us to have some results of accuracy per ethnic group. In this section we want to encourage the students to think critically about the overall results. Here are things that can be discusse: 
- Accuracy for gender prediction is lowest for black individuals (62%) and for the others it ranges between 70% and 79%
- Accuracy for age prediction is bad across the board. We can tell them that it is definitley a harder task (ask them to guess your age / another invited person). In addition to having more categories than the gender (8 categories). Still, the model performs the worst for black people here as well at 0.26% and latinos at 0.38% but for all the others it is more than doubled (but still pretty bad). 

We can also tell them that like most AI systems that are used in the market right now like ChatGPT, we don't really know what data they were trained on: which means what data they know really well, and which data they are not so familiar with.　So it is hard to tell when they fail this way, because it depends on people trying them out and talking about it. So yes, these tools can be useful and help out lives, similar technology is used at airport gates, there the margin of error is lower and the model can't fail like it does here because that really affects people's lives. 

*Conclusion: AI tools great, but we should use them carefully and understand that they are not perfect, they can be biased.*
 
#### Exercise
- The students will now tell us their demographic information and what the model guessed, and then we can analyze the results for the whole class.
  
*Goal: Emphasize the importance of rigorous testing for these tools, and how when companies fail to do this, some people fall through the cracks, like minorities*

#### Results
- A graph showing the class results

## Chatbot
The students should ask the AI something like the suggested hints and catch it hallucinating / lying / speaking non-sense. Can also make this topical and ask math questions or some other homework and show them where it fails, and especially that the teachers know when they are receiving something written by AI, it is obvious. This should be a discussion where students share what they said and what the AI answers. 

Another option is riddles: 
- A father and son get in a car crash and are rushed to the hospital. The father dies. The boy is taken to the operating room and the surgeon says, “I can’t operate on this boy, because he’s my son.” How is this possible?
The model has seen this many times and will know how to answer the riddle and that it is about gender bias.
- A father sends his son on a flight by himself. They say goodbye at home, once the child is on the plane, the pilot says “I can’t fly this plane, my son is here”. How is this possible?
The model will still think this is a riddle and 1. does not realize that there is no issue with flying family 2. will not assume the pilot is the mother? (depends on model)
- Next the students should ask why the AI did not give the same answer as before? Or maybe suggest another plausible answer and ask about it

###### Example output
The man who said goodbye to the son at home was the pilot's husband or partner, who also happens to be the son's father.

Explanation: The scenario describes a same-sex couple with one partner being a pilot and the other parent sending the child on a flight without them. In this case, the gay pilot's husband/partner is also the boy's father, and thus they would have said goodbye to their son at home before he boarded the plane. The pilot, being a pilot, cannot fly the plane while his son is on board for safety reasons.



Credit: Relies on an open-source [project for gender and age detection.](https://github.com/smahesh29/Gender-and-Age-Detection)
